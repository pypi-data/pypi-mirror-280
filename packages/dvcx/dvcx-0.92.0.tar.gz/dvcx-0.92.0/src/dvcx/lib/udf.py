import inspect
import sys
import traceback
from typing import TYPE_CHECKING, Callable, Optional

from dvcx.lib.feature import Feature
from dvcx.lib.signal_schema import SignalSchema
from dvcx.lib.utils import DvcxError, DvcxParamsError
from dvcx.query import Stream, udf

if TYPE_CHECKING:
    from dvxc.query.udf import UDFWrapper


class UdfError(DvcxParamsError):
    def __init__(self, msg):
        super().__init__(f"UDF error: {msg}")


class UDFBase:
    is_input_batched = False
    is_output_batched = False
    is_input_grouped = False
    is_output_single = False

    def __init__(
        self,
        params: SignalSchema,
        output: SignalSchema,
        func: Optional[Callable] = None,
    ):
        self.params = params
        self.output = output
        self._func = func

        params_spec = params.to_udf_spec()
        self.params_spec = list(params_spec.keys())
        self._contains_stream = False
        if params.contains_file():
            self.params_spec.insert(0, Stream())  # type: ignore[arg-type]
            self._contains_stream = True

        self.output_spec = output.to_udf_spec()

        self._catalog = None

    @property
    def name(self):
        return self.__class__.__name__

    def set_catalog(self, catalog):
        self._catalog = catalog.copy(db=False)

    @property
    def catalog(self):
        return self._catalog

    def to_udf_wrapper(self, batch=1) -> "UDFWrapper":
        udf_wrapper = udf(self.params_spec, self.output_spec, batch=batch)
        return udf_wrapper(self)

    def bootstrap(self):
        """Initialization process executed on each worker before processing begins.
        This is needed for tasks like pre-loading ML models prior to scoring.
        """

    def teardown(self):
        """Teardown process executed on each process/worker after processing ends.
        This is needed for tasks like closing connections to end-points.
        """

    def process(self, *args, **kwargs):
        if not self._func:
            raise NotImplementedError("UDF processing is not implemented")
        return self._func(*args, **kwargs)

    def validate_results(self, results, *args, **kwargs):
        return results

    def __call__(self, *rows, **kwargs):
        if self.is_input_grouped:
            objs = self._parse_grouped_rows(rows)
        else:
            objs = self._parse_rows(rows)

        if not self.is_input_batched:
            objs = objs[0]

        result_objs = self.process_safe(objs)

        if not self.is_output_batched:
            result_objs = [result_objs]

        if self.is_output_single:
            result_objs = [[x] for x in result_objs]

        if len(self.output.values) > 1:
            res = []
            for tuple_ in result_objs:
                flat = []
                for obj in tuple_:
                    if isinstance(obj, Feature):
                        flat.extend(Feature._flatten(obj))
                    else:
                        flat.append(obj)
                res.append(flat)
        else:
            res = [
                Feature._flatten(obj) if isinstance(obj, Feature) else obj
                for obj in result_objs
            ]

        if not self.is_output_batched:
            assert len(res) == 1, (
                f"{self.name} returns {len(res)} " f"rows while it's not batched"
            )
            if not isinstance(res[0], (str, int, float, bool)):
                res = res[0]

        return res

    def _parse_rows(self, rows):
        if not self.is_input_batched:
            rows = [rows]
        objs = []
        for row in rows:
            if self._contains_stream:
                stream, *row = row
            else:
                stream = None

            obj_row = self.params.row_to_objs(row)

            if self._contains_stream:
                for obj in obj_row:
                    if isinstance(obj, Feature):
                        obj._set_stream(self._catalog, stream, True)

            objs.append(obj_row)
        return objs

    def _parse_grouped_rows(self, rows):
        group = rows[0]
        spec_map = {}
        output_map = {}
        for name, anno in self.params.values.items():
            if inspect.isclass(anno) and issubclass(anno, Feature):
                length = len(anno._to_udf_spec())
            else:
                length = 1
            spec_map[name] = anno, length
            output_map[name] = []

        for flat_obj in group:
            if self._contains_stream:
                position = 1
                stream = flat_obj[0]
            else:
                position = 0
                stream = None

            for signal, (cls, length) in spec_map.items():
                slice = flat_obj[position : position + length]
                position += length

                if Feature.is_feature(cls):
                    obj = cls(**cls._unflatten_to_json(slice))
                else:
                    obj = slice[0]

                if isinstance(obj, Feature):
                    obj._set_stream(self._catalog, stream)
                output_map[signal].append(obj)

        return list(output_map.values())

    def process_safe(self, obj_rows):
        try:
            result_objs = self.process(*obj_rows)
            # if inspect.isgeneratorfunction(self.process):
            if inspect.isgenerator(result_objs):
                result_objs = list(result_objs)
        except Exception as e:  # noqa: BLE001
            msg = f"============== Error in user code: '{self.name}' =============="
            print(msg)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback.tb_next)
            print("=" * len(msg))
            raise DvcxError(
                f"Error in user code in class '{self.name}': {e!s}"
            ) from None
        return result_objs


class Mapper(UDFBase):
    pass


class BatchMapper(Mapper):
    is_input_batched = True
    is_output_batched = True


class Generator(UDFBase):
    is_output_batched = True


class Aggregator(UDFBase):
    is_input_batched = True
    is_output_batched = True
    is_input_grouped = True


class GroupMapper(UDFBase):
    is_input_batched = True
    is_output_batched = True
