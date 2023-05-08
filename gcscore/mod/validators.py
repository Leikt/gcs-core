import re
from typing import Any

Undefined = object()


def validate_required(header: str, obj: Any):
    if obj is Undefined:
        raise ValueError(f'{header}: is required.')


def validate_type(header: str, obj: Any, accepted_types: list[type]):
    if type(obj) not in accepted_types:
        types = ", ".join([t.__name__ for t in accepted_types])
        raise ValueError(f'{header}: expect type {types}. Got {type(obj).__name__}')


def validate_string_pattern(header: str, string: str, pattern: re.Pattern):
    if pattern.match(string) is None:
        raise ValueError(f'{header}: "{string}" does not match the validation pattern "{pattern.pattern}"')