import random
import string
from collections.abc import Sequence
from typing import Any, Optional, Union, get_args, get_origin

from pydantic import BaseModel, create_model

from dvcx.lib.feature import (
    DVCX_TO_TYPE,
    TYPE_TO_DVCX,
    Feature,
    FeatureType,
    FeatureTypeNames,
    ShallowFeature,
    convert_type_to_dvcx,
)
from dvcx.lib.file import FileInfo
from dvcx.lib.reader import FeatureReader
from dvcx.lib.utils import DvcxParamsError
from dvcx.query.schema import Column
from dvcx.sql.types import NullType, SQLType

FeatureLike = Union[type["Feature"], FeatureReader, Column, str]

AUTO_FEATURE_PREFIX = "_auto_fr"
SUFFIX_SYMBOLS = string.digits + string.ascii_lowercase


class DvcxFeatureTypeError(DvcxParamsError):
    def __init__(self, ds_name, msg):
        if ds_name:
            ds_name = f"' {ds_name}'"
        super().__init__(f"Cannot build dataset{ds_name} from features: {msg}")


class FeatureToTupleError(DvcxParamsError):
    def __init__(self, ds_name, msg):
        if ds_name:
            ds_name = f"' {ds_name}'"
        super().__init__(f"Cannot convert features for dataset{ds_name}: {msg}")


class ColumnFeature(Feature):
    def _get_column_value(self):
        raise NotImplementedError("value is not defined for class ColumnFeature")


feature_cache: dict[type[BaseModel], type[Feature]] = {}


def pydantic_to_feature(data_cls: type[BaseModel]) -> type[Feature]:
    if data_cls in feature_cache:
        return feature_cache[data_cls]

    fields = {}
    for name, field_info in data_cls.model_fields.items():
        anno = field_info.annotation
        if anno not in TYPE_TO_DVCX:
            orig = get_origin(anno)
            if orig == list:
                anno = get_args(anno)  # type: ignore[assignment]
                if isinstance(anno, Sequence):
                    anno = anno[0]  # type: ignore[unreachable]
                is_list = True
            else:
                is_list = False

            try:
                convert_type_to_dvcx(anno)
            except TypeError:
                if not Feature.is_feature(anno):  # type: ignore[arg-type]
                    anno = pydantic_to_feature(anno)  # type: ignore[arg-type]

            if is_list:
                anno = list[anno]  # type: ignore[valid-type]
        fields[name] = (anno, field_info.default)

    cls = create_model(
        data_cls.__name__,
        __base__=(data_cls, Feature),  # type: ignore[call-overload]
        **fields,
    )
    feature_cache[data_cls] = cls
    return cls


class FeatureTypes:
    @classmethod
    def column_class(
        cls,
        name: Union[str, Column],
        typ=Any,
        default=None,
        value_func=None,
    ):
        """Creating a column feature dynamically.
        :param fields:
            **name: <name> is string or a Column. For Column, a type can be specified.
            **typ: type of a column. Default is `Any`.
            **default: an optional default value
            **value_func: an optional function for get_value()
        """

        new_class = ColumnFeature

        if isinstance(name, Column):
            if typ is Any and not isinstance(name.type, NullType):
                if isinstance(name.type, SQLType):
                    typ = DVCX_TO_TYPE.get(type(name.type), Any)  # type: ignore[arg-type]
                else:
                    typ = type(name.type)
            name = name.name

        fields = {name: (typ, default)}
        new_class_name = (
            f"{new_class.__name__}_{name}_{FeatureTypes.get_random_suffix()}"
        )

        obj = create_model(
            new_class_name,
            __base__=new_class,  # type: ignore[call-overload]
            **fields,
        )

        obj._get_column_value = lambda self: getattr(self, name)

        if value_func:
            obj.get_value = lambda self: value_func(obj._get_column_value(self))
        else:
            obj.get_value = obj._get_column_value

        return obj

    @classmethod
    def column_classes(
        cls, fields: dict[Union[str, Column], tuple[type, Any]], value_func=None
    ) -> type:
        """Creating columns dynamically.
        :param fields:
            **fields: Attributes of the new model. They should be passed in the format:
            `<name>=(<type>, <default value>)` or `<name>=(<type>, <FieldInfo>)`
            where <name> is string or a Column
        """
        fields_text_keys = {
            key.name if isinstance(key, Column) else key: value
            for key, value in fields.items()
        }

        cls_suffix = "_".join(fields_text_keys.keys())
        new_class = Feature

        obj = create_model(
            f"{new_class.__name__}_{cls_suffix}",
            __base__=new_class,  # type: ignore[call-overload]
            **fields_text_keys,
        )

        obj._get_column_value = lambda self: tuple(
            [getattr(self, name) for name in fields_text_keys]
        )

        if value_func:
            obj.get_value = lambda self: value_func(self)
        else:
            obj.get_value = obj._get_column_value

        return obj

    @classmethod
    def to_features(cls, *fr_classes: FeatureLike) -> Sequence[type["Feature"]]:
        features = []
        for fr in fr_classes:
            if isinstance(fr, (str, Column)):
                features.append(cls.column_class(fr))
            elif isinstance(fr, FeatureReader):
                features += cls.to_features(fr.fr_class)
            else:
                features.append(fr)
        return features

    @staticmethod
    def create_from_column_types(col_types: dict[str, Any]) -> type[Feature]:
        fields = {}
        for field, typ in col_types.items():
            if not isinstance(typ, Feature):
                typ = DVCX_TO_TYPE[typ]
            fields[field] = (Optional[typ], None)
        return FeatureTypes.create_auto_feature("col_type", fields)

    @staticmethod
    def get_random_suffix():
        return "".join(random.choice(SUFFIX_SYMBOLS) for _ in range(5))  # noqa: S311

    @staticmethod
    def create_auto_feature(
        name: str, fields: dict[str, Any], is_shallow: bool = True
    ) -> type[Feature]:
        name_suffix = name + "_" if name else ""
        random_suffix = FeatureTypes.get_random_suffix()

        return create_model(
            f"{AUTO_FEATURE_PREFIX}_{name_suffix}{random_suffix}",
            __base__=ShallowFeature if is_shallow else Feature,  # type: ignore[call-overload]
            **fields,
        )

    @staticmethod
    def features_to_tuples(
        ds_name: str = "",
        output: Union[None, FeatureType, Sequence[str], dict[str, FeatureType]] = None,
        **fr_map,
    ) -> tuple[Any, Any, Any]:
        types_map = {}
        length = -1
        for k, v in fr_map.items():
            if not isinstance(v, Sequence) or isinstance(v, str):
                raise FeatureToTupleError(ds_name, f"features '{k}' is not a sequence")
            len_ = len(v)
            if length < 0:
                length = len_
            elif length == 0:
                raise FeatureToTupleError(ds_name, f"feature '{k}' is empty list")
            elif length != len_:
                raise FeatureToTupleError(
                    ds_name,
                    f"feature '{k}' should have length {length} while {len_} is given",
                )
            typ = type(v[0])
            if not Feature.is_feature_type(typ):
                raise FeatureToTupleError(
                    ds_name,
                    f"feature '{k}' has unsupported type '{typ.__name__}'."
                    f" Please use Feature types: {FeatureTypeNames}",
                )
            types_map[k] = typ
        if output:
            if not isinstance(output, Sequence) and not isinstance(output, str):
                if len(fr_map) != 1:
                    raise FeatureToTupleError(
                        ds_name,
                        f"only one output type was specified, {len(fr_map)} expected",
                    )
                key: str = next(iter(fr_map.keys()))
                output = {key: output}  # type: ignore[dict-item]

            if len(output) != len(fr_map):
                raise FeatureToTupleError(
                    ds_name,
                    f"number of outputs '{len(output)}' should match"
                    f" number of features '{len(fr_map)}'",
                )
            if isinstance(output, dict):
                raise FeatureToTupleError(
                    ds_name,
                    f"output type must be dict[str, FeatureType] while "
                    f"'{type(output).__name__}' is given",
                )
        else:
            output = types_map
        if "file" not in output:
            values = [FileInfo(name="")] * length
            # Add to the beginning of the map:
            fr_map = dict([("file", values), *list(fr_map.items())])
            output = dict([("file", FileInfo), *list(output.items())])  # type: ignore[union-attr]

        output_types: list[type] = list(output.values())  # type: ignore[union-attr,arg-type]
        if len(output) > 1:
            tuple_type = tuple(output_types)
            res_type = tuple[tuple_type]  # type: ignore[valid-type]
            res_values = list(zip(*fr_map.values()))
        else:
            res_type = output_types[0]  # type: ignore[misc]
            res_values = next(iter(fr_map.values()))

        return res_type, output, res_values
