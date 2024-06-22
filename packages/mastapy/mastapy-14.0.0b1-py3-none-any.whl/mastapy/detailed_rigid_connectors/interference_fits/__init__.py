"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.detailed_rigid_connectors.interference_fits._1489 import (
        AssemblyMethods,
    )
    from mastapy._private.detailed_rigid_connectors.interference_fits._1490 import (
        CalculationMethods,
    )
    from mastapy._private.detailed_rigid_connectors.interference_fits._1491 import (
        InterferenceFitDesign,
    )
    from mastapy._private.detailed_rigid_connectors.interference_fits._1492 import (
        InterferenceFitHalfDesign,
    )
    from mastapy._private.detailed_rigid_connectors.interference_fits._1493 import (
        StressRegions,
    )
    from mastapy._private.detailed_rigid_connectors.interference_fits._1494 import (
        Table4JointInterfaceTypes,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.detailed_rigid_connectors.interference_fits._1489": [
            "AssemblyMethods"
        ],
        "_private.detailed_rigid_connectors.interference_fits._1490": [
            "CalculationMethods"
        ],
        "_private.detailed_rigid_connectors.interference_fits._1491": [
            "InterferenceFitDesign"
        ],
        "_private.detailed_rigid_connectors.interference_fits._1492": [
            "InterferenceFitHalfDesign"
        ],
        "_private.detailed_rigid_connectors.interference_fits._1493": ["StressRegions"],
        "_private.detailed_rigid_connectors.interference_fits._1494": [
            "Table4JointInterfaceTypes"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)
