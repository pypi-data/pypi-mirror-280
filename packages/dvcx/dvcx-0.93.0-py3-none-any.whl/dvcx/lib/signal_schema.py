from collections.abc import Sequence
from typing import Any

from dvcx.lib.feature import (
    DEFAULT_DELIMITER,
    DVCX_TO_TYPE,
    NAMES_TO_TYPES,
    TYPE_TO_DVCX,
    Feature,
    FeatureType,
)
from dvcx.lib.feature_registry import Registry
from dvcx.lib.utils import DvcxParamsError


class FeatureMapError(DvcxParamsError):
    pass


class SignalSchema:
    def __init__(self, values: dict[str, FeatureType]):
        self.values = values

    @staticmethod
    def from_column_types(col_types: dict[str, Any]) -> "SignalSchema":
        signals: dict[str, FeatureType] = {}
        for field, type_ in col_types.items():
            type_ = DVCX_TO_TYPE.get(type_, None)
            if type_ is None:
                raise FeatureMapError(
                    f"feature map cannot be obtained for column '{field}':"
                    f" unsupported type '{type_}'"
                )
            signals[field] = type_
        return SignalSchema(signals)

    def serialize(self) -> dict[str, str]:
        return {
            name: fr_type._name() if Feature.is_feature(fr_type) else fr_type.__name__  # type: ignore[union-attr]
            for name, fr_type in self.values.items()
        }

    @staticmethod
    def deserialize(schema: dict[str, str]) -> "SignalSchema":
        if not isinstance(schema, dict):
            raise FeatureMapError(f"cannot deserialize feature schema: {schema}")

        signals: dict[str, FeatureType] = {}
        for signal, type_name in schema.items():
            try:
                fr = NAMES_TO_TYPES.get(type_name, None)
                if not fr:
                    type_name, version = Registry.parse_name_version(type_name)
                    fr = Registry.get(type_name, version)
            except TypeError as err:
                raise FeatureMapError(f"cannot deserialize '{signal}': {err}") from err

            if not fr:
                raise FeatureMapError(
                    f"cannot deserialize '{signal}': unsupported type '{type_name}'"
                )
            signals[signal] = fr

        return SignalSchema(signals)

    def to_udf_spec(self) -> dict[str, Any]:
        res = {}
        for signal, fr_type in self.values.items():
            signal_path = signal.split(".")

            if Feature.is_feature(fr_type):
                delimiter = fr_type._delimiter  # type: ignore[union-attr]
                if fr_type._is_shallow:  # type: ignore[union-attr]
                    signal_path = []
                spec = fr_type._to_udf_spec()  # type: ignore[union-attr]
                for attr, value in spec:
                    name_path = [*signal_path, attr]
                    res[delimiter.join(name_path)] = value
            else:
                delimiter = DEFAULT_DELIMITER
                res[delimiter.join(signal_path)] = TYPE_TO_DVCX.get(fr_type, None)
        return res

    def row_to_objs(self, row: Sequence[Any]) -> list[FeatureType]:
        objs = []
        pos = 0
        for fr_type in self.values.values():
            if Feature.is_feature(fr_type):
                j, pos = fr_type._unflatten_to_json_pos(row, pos)  # type: ignore[union-attr]
                objs.append(fr_type(**j))
            else:
                objs.append(row[pos])
                pos += 1
        return objs  # type: ignore[return-value]

    def contains_file(self) -> bool:
        return any(
            fr._is_file  # type: ignore[union-attr]
            for fr in self.values.values()
            if Feature.is_feature(fr)
        )

    def slice(self, keys: Sequence[str]) -> "SignalSchema":
        return SignalSchema({k: v for k, v in self.values.items() if k in keys})
