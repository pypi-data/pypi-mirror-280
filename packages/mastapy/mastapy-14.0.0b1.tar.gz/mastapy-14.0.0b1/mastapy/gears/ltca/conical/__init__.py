"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.ltca.conical._886 import ConicalGearBendingStiffness
    from mastapy._private.gears.ltca.conical._887 import ConicalGearBendingStiffnessNode
    from mastapy._private.gears.ltca.conical._888 import ConicalGearContactStiffness
    from mastapy._private.gears.ltca.conical._889 import ConicalGearContactStiffnessNode
    from mastapy._private.gears.ltca.conical._890 import (
        ConicalGearLoadDistributionAnalysis,
    )
    from mastapy._private.gears.ltca.conical._891 import (
        ConicalGearSetLoadDistributionAnalysis,
    )
    from mastapy._private.gears.ltca.conical._892 import (
        ConicalMeshedGearLoadDistributionAnalysis,
    )
    from mastapy._private.gears.ltca.conical._893 import (
        ConicalMeshLoadDistributionAnalysis,
    )
    from mastapy._private.gears.ltca.conical._894 import (
        ConicalMeshLoadDistributionAtRotation,
    )
    from mastapy._private.gears.ltca.conical._895 import ConicalMeshLoadedContactLine
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.ltca.conical._886": ["ConicalGearBendingStiffness"],
        "_private.gears.ltca.conical._887": ["ConicalGearBendingStiffnessNode"],
        "_private.gears.ltca.conical._888": ["ConicalGearContactStiffness"],
        "_private.gears.ltca.conical._889": ["ConicalGearContactStiffnessNode"],
        "_private.gears.ltca.conical._890": ["ConicalGearLoadDistributionAnalysis"],
        "_private.gears.ltca.conical._891": ["ConicalGearSetLoadDistributionAnalysis"],
        "_private.gears.ltca.conical._892": [
            "ConicalMeshedGearLoadDistributionAnalysis"
        ],
        "_private.gears.ltca.conical._893": ["ConicalMeshLoadDistributionAnalysis"],
        "_private.gears.ltca.conical._894": ["ConicalMeshLoadDistributionAtRotation"],
        "_private.gears.ltca.conical._895": ["ConicalMeshLoadedContactLine"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConicalGearBendingStiffness",
    "ConicalGearBendingStiffnessNode",
    "ConicalGearContactStiffness",
    "ConicalGearContactStiffnessNode",
    "ConicalGearLoadDistributionAnalysis",
    "ConicalGearSetLoadDistributionAnalysis",
    "ConicalMeshedGearLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAtRotation",
    "ConicalMeshLoadedContactLine",
)
