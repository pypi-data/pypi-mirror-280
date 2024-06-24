# -*- coding: utf-8 -*-

import typing as T
from ordered_set import OrderedSet


def get_values(enum_class) -> OrderedSet:
    """
    Get all values from an enum class.

    Example::

        >>> class Color:
        ...     RED = 1
        ...     GREEN = 2
        ...     BLUE = 3
        >>> get_values(Color)
        OrderedSet([1, 2, 3])
    """
    return OrderedSet(
        [v for k, v in enum_class.__dict__.items() if not k.startswith("_")]
    )


KT = T.TypeVar("KT")
VT = T.TypeVar("VT")


def group_by(
    iterable: T.Iterable[VT],
    get_key: T.Callable[[VT], KT],
) -> T.Dict[KT, T.List[VT]]:
    """
    Group items by it's key, with type hint.

    Example::

        >>> class Record:
        ...     def __init__(self, product: str, date: str, sale: int):
        ...         self.product = product
        ...         self.date = date
        ...         self.sale = sale

        >>> records = [
        ...     Record("apple", "2020-01-01", 10),
        ...     Record("apple", "2020-01-02", 20),
        ...     Record("apple", "2020-01-03", 30),
        ...     Record("banana", "2020-01-01", 10),
        ...     Record("banana", "2020-01-02", 20),
        ...     Record("banana", "2020-01-03", 30),
        ... ]

        >>> group_by(records, lambda x: x.product)
        {
            "apple": [
                Record("apple", "2020-01-01", 10),
                Record("apple", "2020-01-02", 20),
                Record("apple", "2020-01-03", 30),
            ],
            "banana": [
                Record("banana", "2020-01-01", 10),
                Record("banana", "2020-01-02", 20),
                Record("banana", "2020-01-03", 30),
            ],
        }
    """
    grouped = dict()
    for item in iterable:
        key = get_key(item)
        try:
            grouped[key].append(item)
        except KeyError:
            grouped[key] = [item]
    return grouped
