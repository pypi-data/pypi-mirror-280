from enum import auto

from strenum import LowercaseStrEnum


TD_VERSION = "v0.0.2"
TSR_VERSION = "v0.0.1"

MODEL_URLS = {
    "table_detection": {
        "v0.0.1": {
            "url": "https://drive.google.com/uc?id=1_owQ6JvJkEVCS4nhkmaTE8sIBDj6aQwF",
            "file": "td_v0.0.1.pt",
        },
        "v0.0.2": {
            "url": "https://drive.google.com/uc?id=1FdAAw9CqV9popKyqbXcslqn7tYyJLmn8",
            "file": "td_v0.0.2.pt",
        },
    },
    "table_structure_recognition": {
        "v0.0.1": {
            "url": "https://drive.google.com/uc?id=14sXs0Z6zKDeu41uKStl44hxfM1ghhg0d",
            "file": "tsr_v0.0.1.pt",
        }
    },
}


class Task(LowercaseStrEnum):
    TABLE_DETECTION = auto()
    TABLE_STRUCTURE_RECOGNITION = auto()


class OutputFormat(LowercaseStrEnum):
    HTML = auto()
    LATEX = auto()
    CSV = auto()


class BorderFormat(LowercaseStrEnum):
    FULL_BORDER = auto()
    NO_BORDER = auto()
    HOR_BORDER = auto()
    VER_BORDER = auto()
    INNER_BORDER = auto()
    OUTER_BORDER = auto()


class VerticalAlign(LowercaseStrEnum):
    TOP = auto()
    MIDDLE = auto()
    BOTTOM = auto()


class HorizontalAlign(LowercaseStrEnum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()
