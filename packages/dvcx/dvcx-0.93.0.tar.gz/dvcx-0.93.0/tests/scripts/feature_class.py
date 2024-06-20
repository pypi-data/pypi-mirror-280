from dvcx.lib.datachain import C, DataChain
from dvcx.lib.feature import Feature


class Embedding(Feature):
    value: float


ds_name = "feature_class"
ds = (
    DataChain.from_storage("gs://dvcx-datalakes/dogs-and-cats/")
    .filter(C.name.glob("*cat*.jpg"))  # type: ignore [attr-defined]
    .limit(5)
    .map(emd=lambda file: Embedding(value=512), output=Embedding)
)

ds.save(ds_name)
