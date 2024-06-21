from typing import Type

from metastruct.basetypes import ErrEnum
from metastruct.utils import JSONTool


def contruct_item_from_text(rawtext: str, constructor: Type) -> ErrEnum:
    """Validate the raw text."""
    try:
        data = JSONTool.from_raw(rawtext)
    except Exception as _:
        return ErrEnum.BAD_RESP

    try:
        if isinstance(data, list):
            for item in data:
                constructor(**item)
        else:
            constructor(**data)
    except Exception as _:
        return ErrEnum.BAD_SCHEMA
    return ErrEnum.NO_ERR
