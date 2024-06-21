"""Meta-structure for the QAgent class."""

from typing import Any, Dict, List

from pydantic import BaseModel


class NamedScore(BaseModel):
    """Class representing the named score."""

    name: str
    score: float


class NamedNumericalList(BaseModel):
    """A named list of items."""

    name: str
    items: List[float]


class NamedAnyList(BaseModel):
    """A named list of items of _any_ type."""

    name: str
    items: List[Any]


class RespWithNamedScore(BaseModel):
    """A response of named scores.

    Example
    -------
    >>> RespWithNamedScore(**{
        "resp": {
            "name": "John",
            "score": 0.9
        }
    })

    >>> RespWithNamedScore(
        resp={"name": 0.9, "age": 0.8}
    )
    """

    resp: Dict[str, float]
