"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_two_d_fe_analysis._917 import (
        CylindricalGearMeshTIFFAnalysis,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._918 import (
        CylindricalGearMeshTIFFAnalysisDutyCycle,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._919 import (
        CylindricalGearSetTIFFAnalysis,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._920 import (
        CylindricalGearSetTIFFAnalysisDutyCycle,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._921 import (
        CylindricalGearTIFFAnalysis,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._922 import (
        CylindricalGearTIFFAnalysisDutyCycle,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._923 import (
        CylindricalGearTwoDimensionalFEAnalysis,
    )
    from mastapy._private.gears.gear_two_d_fe_analysis._924 import (
        FindleyCriticalPlaneAnalysis,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_two_d_fe_analysis._917": [
            "CylindricalGearMeshTIFFAnalysis"
        ],
        "_private.gears.gear_two_d_fe_analysis._918": [
            "CylindricalGearMeshTIFFAnalysisDutyCycle"
        ],
        "_private.gears.gear_two_d_fe_analysis._919": [
            "CylindricalGearSetTIFFAnalysis"
        ],
        "_private.gears.gear_two_d_fe_analysis._920": [
            "CylindricalGearSetTIFFAnalysisDutyCycle"
        ],
        "_private.gears.gear_two_d_fe_analysis._921": ["CylindricalGearTIFFAnalysis"],
        "_private.gears.gear_two_d_fe_analysis._922": [
            "CylindricalGearTIFFAnalysisDutyCycle"
        ],
        "_private.gears.gear_two_d_fe_analysis._923": [
            "CylindricalGearTwoDimensionalFEAnalysis"
        ],
        "_private.gears.gear_two_d_fe_analysis._924": ["FindleyCriticalPlaneAnalysis"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CylindricalGearMeshTIFFAnalysis",
    "CylindricalGearMeshTIFFAnalysisDutyCycle",
    "CylindricalGearSetTIFFAnalysis",
    "CylindricalGearSetTIFFAnalysisDutyCycle",
    "CylindricalGearTIFFAnalysis",
    "CylindricalGearTIFFAnalysisDutyCycle",
    "CylindricalGearTwoDimensionalFEAnalysis",
    "FindleyCriticalPlaneAnalysis",
)
