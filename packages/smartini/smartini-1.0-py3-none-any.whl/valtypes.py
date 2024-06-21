from typing import Callable, Union
from re import split


class CustomType:

    def __new__(cls, processor: Callable) -> type:
        cls._smartini_processor = processor
        return cls


class ListType(CustomType):

    def __new__(cls, delimiter: str = ",", ignore_whitespace: bool = True) -> type:
        if ignore_whitespace:
            delimiter = rf"\s*{delimiter}\s*"
        return super().__new__(cls, lambda x: split(pattern=delimiter, string=x))


class NumericType(CustomType):

    def __new__(cls, decimal_sep: str = ".", thousands_sep: str = ",") -> type:
        return super().__new__(
            cls, lambda x: cls._str_to_num(x, decimal_sep, thousands_sep)
        )

    @classmethod
    def _str_to_num(
        cls, string: str, decimal_sep, thousands_sep
    ) -> int | float | complex:
        string = string.replace(decimal_sep, ".").replace(thousands_sep, "")
        error = None
        for converter in (int, float, complex):
            try:
                return converter(string)
            except ValueError as e:
                error = e
                continue
        raise ValueError("ini input does not match smartini valtype!") from error


class BoolType(CustomType):

    def __new__(
        cls,
        true_aliases: tuple[str, ...] = ("1", "true", "yes"),
        false_aliases: tuple[str, ...] = ("0", "false", "no"),
    ) -> type:
        true_aliases = tuple(i.lower() for i in true_aliases)
        false_aliases = tuple(i.lower() for i in false_aliases)
        return super().__new__(
            cls, lambda x: cls._str_to_bool(x, true_aliases, false_aliases)
        )

    @classmethod
    def _str_to_bool(
        cls, string: str, true_aliases: tuple[str, ...], false_aliases: tuple[str, ...]
    ) -> int | float | complex:
        string = string.lower()
        if string in true_aliases:
            return True
        if string in false_aliases:
            return False
        raise ValueError("ini input does not match smartini valtype!")


COMMALIST = Union[str, ListType(ignore_whitespace=True)]
NEWLINELIST = Union[str, ListType(delimiter="\n", ignore_whitespace=True)]
NUMERIC = Union[str, NumericType()]
BOOLEAN = Union[str, bool, BoolType()]
