"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.utility.enums._1869 import BearingForceArrowOption
    from mastapy._private.utility.enums._1870 import TableAndChartOptions
    from mastapy._private.utility.enums._1871 import ThreeDViewContourOption
    from mastapy._private.utility.enums._1872 import (
        ThreeDViewContourOptionFirstSelection,
    )
    from mastapy._private.utility.enums._1873 import (
        ThreeDViewContourOptionSecondSelection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.enums._1869": ["BearingForceArrowOption"],
        "_private.utility.enums._1870": ["TableAndChartOptions"],
        "_private.utility.enums._1871": ["ThreeDViewContourOption"],
        "_private.utility.enums._1872": ["ThreeDViewContourOptionFirstSelection"],
        "_private.utility.enums._1873": ["ThreeDViewContourOptionSecondSelection"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
