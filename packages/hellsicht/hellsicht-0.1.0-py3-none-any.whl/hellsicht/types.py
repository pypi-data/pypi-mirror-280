from dataclasses import dataclass
from typing import TypeAlias, NewType

JSONType: TypeAlias = int | str | float | bool | None | list['JSONType'] | dict[str, 'JSONType']
FieldName = NewType('FieldName', str)
RegularExpression = NewType('RegularExpression', str)


def parse_field_name(name: str) -> FieldName:
    """
    Parse the given field name and return a FieldName object.

    Args:
        name (str): The name of the field.

    Returns:
        FieldName: A FieldName object representing the parsed field name.

    """
    return FieldName(name)

def parse_regular_expression(pattern: str) -> RegularExpression:
    """
    Args:
        pattern: A string representing the regular expression pattern.

    Returns:
        A RegularExpression object initialized with the given pattern.
    """
    return RegularExpression(pattern)


@dataclass(frozen=True)
class DataClass:
    pass



