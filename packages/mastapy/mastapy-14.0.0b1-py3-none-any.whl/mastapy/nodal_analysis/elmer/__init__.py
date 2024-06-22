"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.nodal_analysis.elmer._175 import ContactType
    from mastapy._private.nodal_analysis.elmer._176 import ElectricMachineAnalysisPeriod
    from mastapy._private.nodal_analysis.elmer._177 import ElmerResultEntityType
    from mastapy._private.nodal_analysis.elmer._178 import ElmerResults
    from mastapy._private.nodal_analysis.elmer._179 import (
        ElmerResultsFromElectromagneticAnalysis,
    )
    from mastapy._private.nodal_analysis.elmer._180 import (
        ElmerResultsFromMechanicalAnalysis,
    )
    from mastapy._private.nodal_analysis.elmer._181 import ElmerResultsViewable
    from mastapy._private.nodal_analysis.elmer._182 import ElmerResultType
    from mastapy._private.nodal_analysis.elmer._183 import (
        MechanicalContactSpecification,
    )
    from mastapy._private.nodal_analysis.elmer._184 import NodalAverageType
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.nodal_analysis.elmer._175": ["ContactType"],
        "_private.nodal_analysis.elmer._176": ["ElectricMachineAnalysisPeriod"],
        "_private.nodal_analysis.elmer._177": ["ElmerResultEntityType"],
        "_private.nodal_analysis.elmer._178": ["ElmerResults"],
        "_private.nodal_analysis.elmer._179": [
            "ElmerResultsFromElectromagneticAnalysis"
        ],
        "_private.nodal_analysis.elmer._180": ["ElmerResultsFromMechanicalAnalysis"],
        "_private.nodal_analysis.elmer._181": ["ElmerResultsViewable"],
        "_private.nodal_analysis.elmer._182": ["ElmerResultType"],
        "_private.nodal_analysis.elmer._183": ["MechanicalContactSpecification"],
        "_private.nodal_analysis.elmer._184": ["NodalAverageType"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ContactType",
    "ElectricMachineAnalysisPeriod",
    "ElmerResultEntityType",
    "ElmerResults",
    "ElmerResultsFromElectromagneticAnalysis",
    "ElmerResultsFromMechanicalAnalysis",
    "ElmerResultsViewable",
    "ElmerResultType",
    "MechanicalContactSpecification",
    "NodalAverageType",
)
