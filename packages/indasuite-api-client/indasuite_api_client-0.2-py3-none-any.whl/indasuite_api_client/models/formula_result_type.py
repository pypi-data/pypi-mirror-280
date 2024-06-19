from enum import Enum


class FormulaResultType(str, Enum):
    BOOL = "BOOL"
    INT = "INT"
    REAL = "REAL"

    def __str__(self) -> str:
        return str(self.value)
