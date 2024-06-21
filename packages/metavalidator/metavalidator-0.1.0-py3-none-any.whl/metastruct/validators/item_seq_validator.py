from typing import Type

from metastruct.basetypes import ErrEnum
from metastruct.validators.item_constructor import contruct_item_from_text


def is_valid_item_seq(rawtext: str, constructor: Type) -> bool:
    """Check for a list of items of valid structure as per constructor.

    Parameters
    ----------
    rawtext : str
    constructor : Type
        Any class constructor

    Example
    -------
    >>> class Person:
    >>>     def __init__(self, name, age):
    >>>         self.name = name
    >>>         self.age = age
    >>>         print("Person created")
    >>> is_valid_item_seq('[{"name": "John", "age": 30}]', Person)

    Returns
    -------
    bool
        True if the raw text is _both_ a valid json _and_ a valid structure for
        the constructor, False otherwise
    """
    status = contruct_item_from_text(rawtext, constructor)
    return status == ErrEnum.NO_ERR
