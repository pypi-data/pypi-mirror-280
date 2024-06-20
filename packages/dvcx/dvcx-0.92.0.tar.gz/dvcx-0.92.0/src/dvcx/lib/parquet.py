from collections.abc import Iterator
from typing import Callable

import pandas as pd
from pydantic import Field

from dvcx.lib.feature import Feature
from dvcx.lib.file import File, FileInfo


class BasicParquet(Feature):
    file_info: FileInfo
    index: int = Field(default=None)


def process_parquet(spec: type[BasicParquet]) -> Callable:
    def process(file: File) -> Iterator[spec]:  # type: ignore[valid-type]
        with file.open() as fd:
            df = pd.read_parquet(fd)
            df["index"] = df.index

            for pq_dict in df.to_dict("records"):
                pq_dict["file_info"] = FileInfo(
                    name=str(pq_dict["index"]),
                    source=file.source,
                    parent=file.get_full_name(),
                    version=file.version,
                    etag=file.etag,
                )
                yield spec(**pq_dict)

    return process
