import datetime
import math
from collections.abc import Generator, Iterator

import pandas as pd
import pytest

from dvcx.lib.datachain import C, DataChain
from dvcx.lib.feature import Feature, ShallowFeature
from dvcx.lib.file import FileInfo
from dvcx.lib.signal_schema import SignalSchema
from dvcx.lib.udf_signature import UdfSignatureError
from dvcx.lib.utils import DvcxParamsError
from dvcx.query import DatasetRow

FILE_NAMES = ["f1.jpg", "f1.json", "f1.txt", "f2.jpg", "f2.json"]
FILE_SIZES = [1, 2, 3, 4, 5]
FILES = [FileInfo(name=name, size=size) for name, size in zip(FILE_NAMES, FILE_SIZES)]

DF_DATA = {
    "first_name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 45],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
}


class MyFr(Feature):
    nnn: str
    count: int


features = [MyFr(nnn="n1", count=3), MyFr(nnn="n2", count=5), MyFr(nnn="n1", count=1)]


def test_pandas_conversion(catalog):
    df = pd.DataFrame(DF_DATA)
    df1 = DataChain.from_pandas(df)
    df1 = df1.select("first_name", "age", "city").to_pandas()
    assert df1.equals(df)


def test_pandas_file_columns(catalog):
    ds = DataChain.from_pandas(pd.DataFrame(DF_DATA))
    df = ds.to_pandas()
    assert all(col in df.columns for col in DatasetRow.schema)


def test_pandas_file_column_conflict(catalog):
    file_records = {"name": ["aa.txt", "bb.txt", "ccc.jpg", "dd", "e.txt"]}
    with pytest.raises(DvcxParamsError):
        DataChain.from_pandas(pd.DataFrame(DF_DATA | file_records))

    file_records = {"etag": [1, 2, 3, 4, 5]}
    with pytest.raises(DvcxParamsError):
        DataChain.from_pandas(pd.DataFrame(DF_DATA | file_records))


def test_pandas_uppercase_columns(catalog):
    data = {
        "FirstName": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Age": [25, 30, 35, 40, 45],
        "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    }
    df = DataChain.from_pandas(pd.DataFrame(data)).to_pandas()
    assert all(col not in df.columns for col in data)
    assert all(col.lower() in df.columns for col in data)


def test_pandas_incorrect_column_names(catalog):
    with pytest.raises(DvcxParamsError):
        DataChain.from_pandas(
            pd.DataFrame({"First Name": ["Alice", "Bob", "Charlie", "David", "Eva"]})
        )

    with pytest.raises(DvcxParamsError):
        DataChain.from_pandas(
            pd.DataFrame({"": ["Alice", "Bob", "Charlie", "David", "Eva"]})
        )

    with pytest.raises(DvcxParamsError):
        DataChain.from_pandas(
            pd.DataFrame({"First@Name": ["Alice", "Bob", "Charlie", "David", "Eva"]})
        )


def test_from_features_basic(catalog):
    ds = DataChain.create_empty(DataChain.DEFAULT_FILE_RECORD)
    ds = ds.gen(
        lambda prm: [FileInfo(name="")] * 5, params="parent", output={"file": FileInfo}
    )

    ds_name = "my_ds"
    ds.save(ds_name)
    ds = DataChain(name=ds_name)

    assert isinstance(ds.feature_schema, dict)
    assert isinstance(ds.signals_schema, SignalSchema)
    assert ds.signals_schema.values.keys() == {"file"}
    assert set(ds.signals_schema.values.values()) == {FileInfo}


def test_from_features(catalog):
    ds = DataChain.create_empty(DataChain.DEFAULT_FILE_RECORD)
    ds = ds.gen(
        lambda prm: list(zip([FileInfo(name="")] * len(features), features)),
        params="parent",
        output={"file": FileInfo, "t1": MyFr},
    )
    df1 = ds.to_pandas()

    assert df1[["t1__nnn", "t1__count"]].equals(
        pd.DataFrame({"t1__nnn": ["n1", "n2", "n1"], "t1__count": [3, 5, 1]})
    )


def test_preserve_feature_schema(catalog):
    ds = DataChain.create_empty(DataChain.DEFAULT_FILE_RECORD)
    ds = ds.gen(
        lambda prm: list(zip([FileInfo(name="")] * len(features), features, features)),
        params="parent",
        output={"file": FileInfo, "t1": MyFr, "t2": MyFr},
    )

    ds_name = "my_ds1"
    ds.save(ds_name)
    ds = DataChain(name=ds_name)

    assert isinstance(ds.feature_schema, dict)
    assert isinstance(ds.signals_schema, SignalSchema)
    assert ds.signals_schema.values.keys() == {"t1", "t2", "file"}
    assert set(ds.signals_schema.values.values()) == {MyFr, FileInfo}


def test_from_features_simple_types(catalog):
    fib = [1, 1, 2, 3, 5, 8]
    values = ["odd" if num % 2 else "even" for num in fib]

    ds = DataChain.from_features(fib=fib, odds=values)

    df = ds.to_pandas()
    assert len(df) == len(fib)
    assert df["fib"].tolist() == fib
    assert df["odds"].tolist() == values


def test_from_features_more_simple_types(catalog):
    ds_name = "my_ds_type"
    DataChain.from_features(
        t1=features,
        num=range(len(features)),
        bb=[True, True, False],
        dd=[{}, {"ee": 3}, {"ww": 1, "qq": 2}],
        time=[
            datetime.datetime.now(),
            datetime.datetime.today(),
            datetime.datetime.today(),
        ],
        f=[3.14, 2.72, 1.62],
    ).save(ds_name)

    ds = DataChain(name=ds_name)
    signals = ds.signals_schema.values
    assert signals.keys() == {
        "t1",
        "num",
        "file",
        "bb",
        "dd",
        "time",
        "f",
    }
    assert set(signals.values()) == {
        MyFr,
        FileInfo,
        int,
        bool,
        dict,
        datetime.datetime,
        float,
    }


def test_file_list(catalog):
    df = DataChain.from_features(file=FILES).to_pandas()

    assert len(df) == len(FILES)
    assert df["name"].tolist() == FILE_NAMES
    assert df["size"].tolist() == FILE_SIZES


def test_gen(catalog):
    class _TestFr(ShallowFeature):
        file_info: FileInfo
        sqrt: float
        my_name: str

    ds = DataChain.from_features(t1=features)
    ds = ds.gen(
        x=lambda m_fr: [
            _TestFr(
                file_info=FileInfo(name=""),
                sqrt=math.sqrt(m_fr.count),
                my_name=m_fr.nnn,
            )
        ],
        params="t1",
        output={"x": _TestFr},
    )

    df = ds.to_pandas()

    assert df["my_name"].tolist() == ["n1", "n2", "n1"]
    for actual_sqrt, expected in zip(df["sqrt"], [3, 5, 1]):
        assert math.isclose(actual_sqrt, math.sqrt(expected), rel_tol=1e-7)
    with pytest.raises(KeyError):
        df["t1__nnn"]


def test_map(catalog):
    class _TestFr(ShallowFeature):
        sqrt: float
        my_name: str

    ds = DataChain.from_features(t1=features)

    df = ds.map(
        x=lambda m_fr: _TestFr(
            sqrt=math.sqrt(m_fr.count),
            my_name=m_fr.nnn + "_suf",
        ),
        params="t1",
        output={"x": _TestFr},
    ).to_pandas()

    assert df["my_name"].tolist() == ["n1_suf", "n2_suf", "n1_suf"]
    for actual_sqrt, expected in zip(df["sqrt"], [3, 5, 1]):
        assert math.isclose(actual_sqrt, math.sqrt(expected), rel_tol=1e-7)


def test_agg(catalog):
    class _TestFr(ShallowFeature):
        f: FileInfo
        cnt: int
        my_name: str

    df = (
        DataChain.from_features(t1=features)
        .agg(
            x=lambda frs: [
                _TestFr(
                    f=FileInfo(name=""),
                    cnt=sum([f.count for f in frs]),
                    my_name="-".join([fr.nnn for fr in frs]),
                )
            ],
            partition_by=C.t1__nnn,
            params="t1",
            output={"x": _TestFr},
        )
        .to_pandas()
    )

    assert len(df) == 2
    assert df["my_name"].tolist() == ["n1-n1", "n2"]
    assert df["cnt"].tolist() == [4, 5]


def test_agg_two_params(catalog):
    class _TestFr(ShallowFeature):
        f: FileInfo
        cnt: int
        my_name: str

    features2 = [
        MyFr(nnn="n1", count=6),
        MyFr(nnn="n2", count=10),
        MyFr(nnn="n1", count=2),
    ]

    ds = DataChain.from_features(t1=features, t2=features2).agg(
        x=lambda frs1, frs2: [
            _TestFr(
                f=FileInfo(name=""),
                cnt=sum([f1.count + f2.count for f1, f2 in zip(frs1, frs2)]),
                my_name="-".join([fr.nnn for fr in frs1]),
            )
        ],
        partition_by=C.t1__nnn,
        params=("t1", "t2"),
        output={"x": _TestFr},
    )

    df = ds.to_pandas()
    assert len(df) == 2
    assert df["my_name"].tolist() == ["n1-n1", "n2"]
    assert df["cnt"].tolist() == [12, 15]


def test_agg_simple_iterator(catalog):
    def func(key, val) -> Iterator[tuple[FileInfo, str]]:
        for i in range(val):
            yield FileInfo(name=""), f"{key}_{i}"

    keys = ["a", "b", "c"]
    values = [3, 1, 2]
    ds = DataChain.from_features(key=keys, val=values).gen(res=func)

    df = ds.to_pandas()
    res = df["res_1"].tolist()
    assert res == ["a_0", "a_1", "a_2", "b_0", "c_0", "c_1"]


def test_agg_simple_iterator_error(catalog):
    chain = DataChain.from_features(key=["a", "b", "c"])

    with pytest.raises(UdfSignatureError):

        def func(key) -> int:
            return 1

        chain.gen(res=func)

    with pytest.raises(UdfSignatureError):

        class _MyCls(Feature):
            x: int

        def func(key) -> _MyCls:  # type: ignore[misc]
            return _MyCls(x=2)

        chain.gen(res=func)

    with pytest.raises(UdfSignatureError):

        def func(key) -> tuple[FileInfo, str]:  # type: ignore[misc]
            yield None, "qq"

        chain.gen(res=func)


def test_agg_tuple_result_iterator(catalog):
    class _ImageGroup(Feature):
        name: str
        size: int

    def func(key, val) -> Iterator[tuple[FileInfo, _ImageGroup]]:
        n = "-".join(key)
        v = sum(val)
        yield FileInfo(name=n), _ImageGroup(name=n, size=v)

    keys = ["n1", "n2", "n1"]
    values = [1, 5, 9]
    ds = DataChain.from_features(key=keys, val=values).agg(
        x=func, partition_by=C("key")
    )

    df = ds.to_pandas()
    assert len(df) == 2
    assert df["x_1__name"].tolist() == ["n1-n1", "n2"]
    assert df["x_1__size"].tolist() == [10, 5]


def test_agg_tuple_result_generator(catalog):
    class _ImageGroup(Feature):
        name: str
        size: int

    def func(key, val) -> Generator[tuple[FileInfo, _ImageGroup], None, None]:
        n = "-".join(key)
        v = sum(val)
        yield FileInfo(name=n), _ImageGroup(name=n, size=v)

    keys = ["n1", "n2", "n1"]
    values = [1, 5, 9]
    ds = DataChain.from_features(key=keys, val=values).agg(
        x=func, partition_by=C("key")
    )

    df = ds.to_pandas()
    assert len(df) == 2
    assert df["x_1__name"].tolist() == ["n1-n1", "n2"]
    assert df["x_1__size"].tolist() == [10, 5]
