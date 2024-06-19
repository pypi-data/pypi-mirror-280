from enum import Enum


class AccessType(str, Enum):
    READ = "Read"
    READWRITE = "ReadWrite"
    WRITE = "Write"

    def __str__(self) -> str:
        return str(self.value)
