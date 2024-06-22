"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.utility.file_access_helpers._1867 import ColumnTitle
    from mastapy._private.utility.file_access_helpers._1868 import (
        TextFileDelimiterOptions,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.file_access_helpers._1867": ["ColumnTitle"],
        "_private.utility.file_access_helpers._1868": ["TextFileDelimiterOptions"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ColumnTitle",
    "TextFileDelimiterOptions",
)
