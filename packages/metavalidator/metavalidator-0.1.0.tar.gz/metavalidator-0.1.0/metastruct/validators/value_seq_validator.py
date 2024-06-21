"""Enum Sequence
"""
import re
from typing import Set


def is_value_seq(seq: str, allowed: Set, sep: str = "") -> bool:
    """Check a sequence contains only legal `values`."""
    if not sep:
        vals = re.split("", seq)[1:-1]
    else:
        vals = re.split(sep, seq)
    return all([item in allowed for item in vals])


def is_enum_seq(seq: str, allowed: Set, sep: str = "") -> bool:
    return is_value_seq(seq=seq, allowed=allowed, sep=sep)


class SetItemSequence:
    """A sequence of enums.

    Init and check that a sequence contains only specified enums.

    Example
    -------
    >>> EnumSequence(**{
        "seq": ["0", "1", "2"]
    })
    """

    def __init__(self, seq: str):
        self.seq = seq
