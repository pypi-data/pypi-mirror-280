"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.ltca._848 import ConicalGearFilletStressResults
    from mastapy._private.gears.ltca._849 import ConicalGearRootFilletStressResults
    from mastapy._private.gears.ltca._850 import ContactResultType
    from mastapy._private.gears.ltca._851 import CylindricalGearFilletNodeStressResults
    from mastapy._private.gears.ltca._852 import (
        CylindricalGearFilletNodeStressResultsColumn,
    )
    from mastapy._private.gears.ltca._853 import (
        CylindricalGearFilletNodeStressResultsRow,
    )
    from mastapy._private.gears.ltca._854 import CylindricalGearRootFilletStressResults
    from mastapy._private.gears.ltca._855 import (
        CylindricalMeshedGearLoadDistributionAnalysis,
    )
    from mastapy._private.gears.ltca._856 import GearBendingStiffness
    from mastapy._private.gears.ltca._857 import GearBendingStiffnessNode
    from mastapy._private.gears.ltca._858 import GearContactStiffness
    from mastapy._private.gears.ltca._859 import GearContactStiffnessNode
    from mastapy._private.gears.ltca._860 import GearFilletNodeStressResults
    from mastapy._private.gears.ltca._861 import GearFilletNodeStressResultsColumn
    from mastapy._private.gears.ltca._862 import GearFilletNodeStressResultsRow
    from mastapy._private.gears.ltca._863 import GearLoadDistributionAnalysis
    from mastapy._private.gears.ltca._864 import GearMeshLoadDistributionAnalysis
    from mastapy._private.gears.ltca._865 import GearMeshLoadDistributionAtRotation
    from mastapy._private.gears.ltca._866 import GearMeshLoadedContactLine
    from mastapy._private.gears.ltca._867 import GearMeshLoadedContactPoint
    from mastapy._private.gears.ltca._868 import GearRootFilletStressResults
    from mastapy._private.gears.ltca._869 import GearSetLoadDistributionAnalysis
    from mastapy._private.gears.ltca._870 import GearStiffness
    from mastapy._private.gears.ltca._871 import GearStiffnessNode
    from mastapy._private.gears.ltca._872 import (
        MeshedGearLoadDistributionAnalysisAtRotation,
    )
    from mastapy._private.gears.ltca._873 import UseAdvancedLTCAOptions
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.ltca._848": ["ConicalGearFilletStressResults"],
        "_private.gears.ltca._849": ["ConicalGearRootFilletStressResults"],
        "_private.gears.ltca._850": ["ContactResultType"],
        "_private.gears.ltca._851": ["CylindricalGearFilletNodeStressResults"],
        "_private.gears.ltca._852": ["CylindricalGearFilletNodeStressResultsColumn"],
        "_private.gears.ltca._853": ["CylindricalGearFilletNodeStressResultsRow"],
        "_private.gears.ltca._854": ["CylindricalGearRootFilletStressResults"],
        "_private.gears.ltca._855": ["CylindricalMeshedGearLoadDistributionAnalysis"],
        "_private.gears.ltca._856": ["GearBendingStiffness"],
        "_private.gears.ltca._857": ["GearBendingStiffnessNode"],
        "_private.gears.ltca._858": ["GearContactStiffness"],
        "_private.gears.ltca._859": ["GearContactStiffnessNode"],
        "_private.gears.ltca._860": ["GearFilletNodeStressResults"],
        "_private.gears.ltca._861": ["GearFilletNodeStressResultsColumn"],
        "_private.gears.ltca._862": ["GearFilletNodeStressResultsRow"],
        "_private.gears.ltca._863": ["GearLoadDistributionAnalysis"],
        "_private.gears.ltca._864": ["GearMeshLoadDistributionAnalysis"],
        "_private.gears.ltca._865": ["GearMeshLoadDistributionAtRotation"],
        "_private.gears.ltca._866": ["GearMeshLoadedContactLine"],
        "_private.gears.ltca._867": ["GearMeshLoadedContactPoint"],
        "_private.gears.ltca._868": ["GearRootFilletStressResults"],
        "_private.gears.ltca._869": ["GearSetLoadDistributionAnalysis"],
        "_private.gears.ltca._870": ["GearStiffness"],
        "_private.gears.ltca._871": ["GearStiffnessNode"],
        "_private.gears.ltca._872": ["MeshedGearLoadDistributionAnalysisAtRotation"],
        "_private.gears.ltca._873": ["UseAdvancedLTCAOptions"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConicalGearFilletStressResults",
    "ConicalGearRootFilletStressResults",
    "ContactResultType",
    "CylindricalGearFilletNodeStressResults",
    "CylindricalGearFilletNodeStressResultsColumn",
    "CylindricalGearFilletNodeStressResultsRow",
    "CylindricalGearRootFilletStressResults",
    "CylindricalMeshedGearLoadDistributionAnalysis",
    "GearBendingStiffness",
    "GearBendingStiffnessNode",
    "GearContactStiffness",
    "GearContactStiffnessNode",
    "GearFilletNodeStressResults",
    "GearFilletNodeStressResultsColumn",
    "GearFilletNodeStressResultsRow",
    "GearLoadDistributionAnalysis",
    "GearMeshLoadDistributionAnalysis",
    "GearMeshLoadDistributionAtRotation",
    "GearMeshLoadedContactLine",
    "GearMeshLoadedContactPoint",
    "GearRootFilletStressResults",
    "GearSetLoadDistributionAnalysis",
    "GearStiffness",
    "GearStiffnessNode",
    "MeshedGearLoadDistributionAnalysisAtRotation",
    "UseAdvancedLTCAOptions",
)
