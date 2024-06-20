import json
from typing import get_args, get_origin

import pytest

from dvcx.lib.feature_types import FeatureTypes
from dvcx.lib.file import File, FileInfo
from dvcx.lib.signal_schema import FeatureMapError, SignalSchema
from dvcx.sql.types import Float, Int64, String


def test_feature_to_tuple():
    fib = [1, 1, 2, 3, 5, 8]
    values = ["odd" if num % 2 else "even" for num in fib]

    typ, partition_by, vals = FeatureTypes.features_to_tuples(fib=fib, odds=values)

    assert get_origin(typ) is tuple
    assert get_args(typ) == (FileInfo, int, str)
    assert len(vals) == len(fib)
    assert type(vals[0]) is tuple
    assert len(vals[0]) == 3
    assert type(vals[0][0]) == FileInfo
    assert vals[0][1:] == (1, "odd")
    assert vals[-1][1:] == (fib[-1], values[-1])


def test_feature_schema_deserialize_basic():
    stored = {"name": "str", "count": "int", "file": "File@1"}
    signals = SignalSchema.deserialize(stored)

    assert len(signals.values) == 3
    assert signals.values.keys() == stored.keys()
    assert list(signals.values.values()) == [str, int, File]


def test_feature_schema_deserialize_error():
    SignalSchema.deserialize({})

    with pytest.raises(FeatureMapError):
        SignalSchema.deserialize(json.dumps({"name": "str"}))

    with pytest.raises(FeatureMapError):
        SignalSchema.deserialize({"name": [1, 2, 3]})

    with pytest.raises(FeatureMapError):
        SignalSchema.deserialize({"name": "unknown"})


def test_feature_schema_serialize_basic():
    schema = {
        "name": str,
        "age": float,
        "f": File,
    }
    signals = SignalSchema(schema).serialize()

    assert len(signals) == 3
    assert signals["name"] == "str"
    assert signals["age"] == "float"
    assert signals["f"] == "File@1"


def test_feature_schema_serialize_from_column():
    signals = SignalSchema.from_column_types({"age": Float, "name": String}).values

    assert len(signals) == 2
    assert signals["name"] == str
    assert signals["age"] == float


def test_feature_schema_serialize_from_column_error():
    with pytest.raises(FeatureMapError):
        SignalSchema.from_column_types({"age": Float, "wrong_type": File})


def test_feature_map_to_udf_spec():
    signals = SignalSchema.deserialize(
        {
            "age": "float",
            "address": "str",
            "f": "FileEx@1",
        }
    )

    spec = SignalSchema.to_udf_spec(signals)

    assert len(spec) == 2 + len(File.model_fields)

    assert "age" in spec
    assert spec["age"] == Float

    assert "address" in spec
    assert spec["address"] == String

    assert "f__name" in spec
    assert spec["f__name"] == String

    assert "f__size" in spec
    assert spec["f__size"] == Int64


def test_feature_map_to_udf_spec_shallow():
    signals = SignalSchema.deserialize(
        {
            "age": "float",
            "address": "str",
            "f": "File@1",
        }
    )

    spec = SignalSchema.to_udf_spec(signals)

    assert len(spec) == 2 + len(File.model_fields)

    assert "age" in spec
    assert spec["age"] == Float

    assert "address" in spec
    assert spec["address"] == String

    assert "name" in spec
    assert spec["name"] == String

    assert "size" in spec
    assert spec["size"] == Int64
