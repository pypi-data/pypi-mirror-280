from enum import Enum


class InstantQueryDirection(str, Enum):
    AFTER_MOMENT = "After_moment"
    BEFORE_MOMENT = "Before_moment"

    def __str__(self) -> str:
        return str(self.value)
