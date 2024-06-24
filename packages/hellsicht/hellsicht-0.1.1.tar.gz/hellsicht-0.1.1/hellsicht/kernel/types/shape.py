from dataclasses import dataclass, field
from typing import NewType

from hellsicht.types import FieldName


ColumnType = NewType('ColumnType', str)


def parse_field_type(typename: str) -> ColumnType:
    return ColumnType(typename)


@dataclass(frozen=True)
class DataShape:
    columns: dict[FieldName, ColumnType] = field(default_factory=dict)