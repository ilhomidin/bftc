from abc import ABC, abstractproperty
from dataclasses import dataclass
from typing import Union


class NonValueToken(ABC):
    @abstractproperty
    def tag(self) -> str:
        ...


class ValueToken(NonValueToken, ABC):
    @abstractproperty
    def value(self) -> int:
        ...


@dataclass(frozen=True)
class MutateCellValueToken(ValueToken):
    value: int

    @property
    def tag(self) -> str:
        return "MutateCellValue"


class LoopStartToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "LoopStart"


class LoopEndToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "LoopEnd"


class NextCellToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "NextCell"


class PreviousCellToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "PreviousCell"


class PutCellValueToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "PutCellValue"


class GetCellValueToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "GetCellValue"


class InvalidSyntaxToken(NonValueToken):
    @property
    def tag(self) -> str:
        return "InvalidSyntax"


Token = Union[NonValueToken, ValueToken]


__all__ = [
    "Token",
    "NonValueToken",
    "ValueToken",
    "MutateCellValueToken",
    "LoopStartToken",
    "LoopEndToken",
    "NextCellToken",
    "PreviousCellToken",
    "PutCellValueToken",
    "GetCellValueToken",
    "InvalidSyntax",
]
