import pandas as pd

from dvcx.lib.datachain import C, DataChain
from dvcx.lib.parquet import process_parquet
from dvcx.lib.webdataset import process_webdataset
from dvcx.lib.webdataset_laion import LaionParquet, WDSLaion, process_laion_meta

wds = (
    DataChain.from_storage("gs://dvcx-datacomp-small/shards")
    .filter(C.name.glob("00000000.tar"))
    .settings(cache=True)
    .gen(laion=process_webdataset(spec=WDSLaion), params="file")
)

meta_emd = (
    DataChain.from_storage("gs://dvcx-datacomp-small/metadata")
    .filter(C.name.glob("0020f*.npz"))
    .gen(emd=process_laion_meta)
)

meta_pq = (
    DataChain.from_storage("gs://dvcx-datacomp-small/metadata")
    .filter(C.name.glob("0020f*.parquet"))
    .gen(pq=process_parquet(spec=LaionParquet))
)

meta = meta_emd.merge(
    meta_pq, on=(C.name, C.emd__index), right_on=(C.name, C.pq__index)
)

res = wds.merge(meta, on=C.laion__json__uid, right_on=C.pq__uid)

df = res.limit(10).to_pandas()
with pd.option_context("display.max_columns", None):
    print(df)
