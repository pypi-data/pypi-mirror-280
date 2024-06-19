from enum import Enum


class MetricType(str, Enum):
    CALCULATED = "Calculated"
    MANUAL = "Manual"
    RAW = "Raw"
    SYSTEM = "System"

    def __str__(self) -> str:
        return str(self.value)
