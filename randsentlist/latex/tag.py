from enum import Enum, auto


class Tag(Enum):
    DOCUMENTCLASS = auto()
    BEGIN_DOCUMENT = auto()
    END_DOCUMENT = auto()
    BEGIN_ENUM = auto()
    END_ENUM = auto()
    PACKAGE = auto()
    COMPOSITE_PACKAGE = auto()
    ITEM = auto()
