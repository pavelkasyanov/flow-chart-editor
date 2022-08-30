from enum import Enum


class ElementType(str, Enum):
    UNKNOWN = "UNKNOWN"
    START = "START"
    END = "END"
    PRINT = "PRINT"
    INPUT = "INPUT"
