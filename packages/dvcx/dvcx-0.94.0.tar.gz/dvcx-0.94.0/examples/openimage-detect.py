import json

import pandas as pd
from PIL import Image

from dvcx.lib.datachain import DataChain
from dvcx.lib.feature import ShallowFeature
from dvcx.lib.feature_udf import FeatureAggregator
from dvcx.lib.file import File, FileInfo
from dvcx.query.schema import C
from dvcx.sql.functions import path


class BBox(ShallowFeature):
    x_min: int
    x_max: int
    y_min: int
    y_max: int


class OpenImageDetect(FeatureAggregator):
    def __init__(self):
        super().__init__(File, [FileInfo, BBox])

    def process(self, args):
        if len(args) != 2:
            raise ValueError("Group jpg-json mismatch")

        stream_jpg = args[0]
        stream_json = args[1]
        if args[0].get_file_ext() != "jpg":
            stream_jpg, stream_json = stream_json, stream_jpg

        with stream_jpg.open() as fd:
            img = Image.open(fd)

        with stream_json.open() as stream_json:
            detections = json.load(stream_json).get("detections", [])

        for i, detect in enumerate(detections):
            bbox = BBox(
                x_min=int(detect["XMin"] * img.width),
                x_max=int(detect["XMax"] * img.width),
                y_min=int(detect["YMin"] * img.height),
                y_max=int(detect["YMax"] * img.height),
            )

            fstream = FileInfo(
                name=f"detect_{i}",
                source=source,
                parent=f"{stream_jpg.parent}/{stream_jpg.name}",
                version=stream_jpg.version,
                etag=f"{stream_jpg.etag}_{stream_jpg.etag}",
            )

            yield fstream, bbox


source = "s3://ldb-public/remote/data-lakes/open-images-v6-test-200"

ds = (
    DataChain(source, anon=True)
    .filter(C.name.glob("*.jpg") | C.name.glob("*.json"))
    .aggregate(
        OpenImageDetect(),
        partition_by=path.file_stem(C.name),
    )
)

with pd.option_context("display.max_columns", None):
    df = ds.limit(10).to_pandas()
    print(df)
