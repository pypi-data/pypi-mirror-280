import io
from collections.abc import Sequence
from typing import Optional, Union

from dvcx.catalog import Catalog
from dvcx.lib.feature import Feature
from dvcx.lib.feature_types import FeatureLike, FeatureTypes
from dvcx.lib.file import File
from dvcx.lib.utils import DvcxError
from dvcx.query import Stream


class ValidationError(DvcxError):
    pass


class SchemaError(ValidationError):
    def __init__(self, udf_name: str, context: str, message: str):
        super().__init__(f"'{udf_name}' {context} schema validation error: {message}")


class OutputError(ValidationError):
    def __init__(self, udf_name: str, message: str, num: Optional[int] = None):
        num_str = "" if num is None else f"#{num + 1} "
        super().__init__(f"Output {num_str}of '{udf_name}' error: {message}")


class UserCodeError(DvcxError):
    def __init__(self, class_name: str, message: str):
        super().__init__(f"Error in user code in class '{class_name}': {message}")


class FeatureConverter:
    @property
    def udf_params_list(self):
        return self._udf_params_list

    @property
    def udf_output_spec(self):
        return self._udf_output_spec

    @staticmethod
    def has_feature_stream(fr_classes: Sequence[type[Feature]]):
        return any(
            f._is_file  # type: ignore[attr-defined]
            for f in fr_classes
        )

    @staticmethod
    def has_row_stream(row):
        if len(row) == 0:
            return False
        return isinstance(row[0], (Stream, io.IOBase))

    @staticmethod
    def get_flattened_params(fr_classes: Sequence[type[Feature]]):
        udf_params_spec = Feature._features_to_udf_spec(fr_classes)
        stream_prm = (
            [Stream()] if FeatureConverter.has_feature_stream(fr_classes) else []
        )
        return stream_prm + list(udf_params_spec.keys())

    @staticmethod
    def _convert_to_sequence(
        arg: Union[FeatureLike, Sequence[FeatureLike]],
    ) -> tuple[Sequence[type[Feature]], bool]:
        if not isinstance(arg, Sequence):
            return FeatureTypes.to_features(*[arg]), True
        return FeatureTypes.to_features(*arg), False

    @staticmethod
    def deserialize(
        rows: Sequence[Sequence],
        params: Sequence[str],
        fr_classes: Sequence[type[Feature]],
        catalog: Catalog,
        caching_enabled: bool,
    ) -> Sequence[Sequence[Feature]]:
        clean_rows, streams = FeatureConverter._separate_streams_from_rows(
            rows, fr_classes
        )

        feature_rows = [
            FeatureConverter._row_with_params_to_features(row, fr_classes, params)
            for row in clean_rows
        ]

        for features, stream in zip(feature_rows, streams):
            for feature in features:
                if isinstance(feature, File):
                    feature._set_stream(catalog, stream)  # type: ignore [attr-defined]

        return feature_rows

    @staticmethod
    def _separate_streams_from_rows(
        rows, fr_classes: Sequence[type[Feature]]
    ) -> tuple[Sequence, Sequence]:
        streams = []
        res_rows = []
        if FeatureConverter.has_feature_stream(fr_classes):
            for row in rows:
                if FeatureConverter.has_row_stream(row):
                    streams.append(row[0])
                    res_rows.append(row[1:])
                else:
                    streams.append(None)  # type: ignore [arg-type]
                    res_rows.append(row)
        else:
            res_rows = rows
        return res_rows, streams

    @staticmethod
    def _row_with_params_to_features(
        row: Sequence, fr_classes: Sequence[type[Feature]], params: Sequence[str]
    ) -> Sequence[Feature]:
        new_params = (
            params
            if not FeatureConverter.has_feature_stream(fr_classes)
            else params[1:]
        )
        return [cls._unflatten(dict(zip(new_params, row))) for cls in fr_classes]
