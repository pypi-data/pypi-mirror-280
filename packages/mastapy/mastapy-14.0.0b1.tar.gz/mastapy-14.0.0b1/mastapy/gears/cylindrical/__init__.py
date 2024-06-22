"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.cylindrical._1246 import (
        CylindricalGearLTCAContactChartDataAsTextFile,
    )
    from mastapy._private.gears.cylindrical._1247 import (
        CylindricalGearLTCAContactCharts,
    )
    from mastapy._private.gears.cylindrical._1248 import (
        CylindricalGearWorstLTCAContactChartDataAsTextFile,
    )
    from mastapy._private.gears.cylindrical._1249 import (
        CylindricalGearWorstLTCAContactCharts,
    )
    from mastapy._private.gears.cylindrical._1250 import (
        GearLTCAContactChartDataAsTextFile,
    )
    from mastapy._private.gears.cylindrical._1251 import GearLTCAContactCharts
    from mastapy._private.gears.cylindrical._1252 import PointsWithWorstResults
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.cylindrical._1246": [
            "CylindricalGearLTCAContactChartDataAsTextFile"
        ],
        "_private.gears.cylindrical._1247": ["CylindricalGearLTCAContactCharts"],
        "_private.gears.cylindrical._1248": [
            "CylindricalGearWorstLTCAContactChartDataAsTextFile"
        ],
        "_private.gears.cylindrical._1249": ["CylindricalGearWorstLTCAContactCharts"],
        "_private.gears.cylindrical._1250": ["GearLTCAContactChartDataAsTextFile"],
        "_private.gears.cylindrical._1251": ["GearLTCAContactCharts"],
        "_private.gears.cylindrical._1252": ["PointsWithWorstResults"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)
