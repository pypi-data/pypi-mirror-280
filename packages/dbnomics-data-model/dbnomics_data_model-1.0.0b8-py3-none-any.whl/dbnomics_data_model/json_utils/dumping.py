from typing import Any, cast

from jsonalias import Json
from typedload.datadumper import Dumper
from typedload.exceptions import TypedloadException

from dbnomics_data_model.json_utils.serializing import serialize_json

from .errors import JsonDumpError

__all__ = ["dump_as_json_bytes", "dump_as_json_data"]


def dump_as_json_bytes(value: Any, *, dumper: Dumper) -> bytes:
    data = dump_as_json_data(value, dumper=dumper)
    return serialize_json(data)


def dump_as_json_data(value: Any, *, dumper: Dumper) -> Json:
    try:
        data = dumper.dump(value)
    except TypedloadException as exc:
        raise JsonDumpError(value=value) from exc

    return cast(Json, data)
