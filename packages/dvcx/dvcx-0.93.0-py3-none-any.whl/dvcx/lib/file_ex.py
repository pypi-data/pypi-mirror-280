from typing import Optional, Union

from dvcx.lib.file import File, TextFile


class FileEx(File):
    _is_shallow = False


class TextFileEx(TextFile):
    _is_shallow = False


def get_file(
    source: str,
    parent: str,
    name: str,
    version: str,
    etag: str,
    size: int,
    vtype: str,
    location: Optional[Union[dict, list[dict]]],
) -> FileEx:
    return FileEx(
        source=source,
        parent=parent,
        name=name,
        version=version,
        etag=etag,
        size=size,
        vtype=vtype,
        location=location,
    )


def get_text_file(
    source: str,
    parent: str,
    name: str,
    version: str,
    etag: str,
    size: int,
    vtype: str,
    location: Optional[Union[dict, list[dict]]],
) -> TextFileEx:
    return TextFileEx(
        source=source,
        parent=parent,
        name=name,
        version=version,
        etag=etag,
        size=size,
        vtype=vtype,
        location=location,
    )
