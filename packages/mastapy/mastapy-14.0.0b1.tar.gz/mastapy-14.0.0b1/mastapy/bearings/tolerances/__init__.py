"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.bearings.tolerances._1953 import BearingConnectionComponent
    from mastapy._private.bearings.tolerances._1954 import InternalClearanceClass
    from mastapy._private.bearings.tolerances._1955 import BearingToleranceClass
    from mastapy._private.bearings.tolerances._1956 import (
        BearingToleranceDefinitionOptions,
    )
    from mastapy._private.bearings.tolerances._1957 import FitType
    from mastapy._private.bearings.tolerances._1958 import InnerRingTolerance
    from mastapy._private.bearings.tolerances._1959 import InnerSupportTolerance
    from mastapy._private.bearings.tolerances._1960 import InterferenceDetail
    from mastapy._private.bearings.tolerances._1961 import InterferenceTolerance
    from mastapy._private.bearings.tolerances._1962 import ITDesignation
    from mastapy._private.bearings.tolerances._1963 import MountingSleeveDiameterDetail
    from mastapy._private.bearings.tolerances._1964 import OuterRingTolerance
    from mastapy._private.bearings.tolerances._1965 import OuterSupportTolerance
    from mastapy._private.bearings.tolerances._1966 import RaceDetail
    from mastapy._private.bearings.tolerances._1967 import RaceRoundnessAtAngle
    from mastapy._private.bearings.tolerances._1968 import RadialSpecificationMethod
    from mastapy._private.bearings.tolerances._1969 import RingTolerance
    from mastapy._private.bearings.tolerances._1970 import RoundnessSpecification
    from mastapy._private.bearings.tolerances._1971 import RoundnessSpecificationType
    from mastapy._private.bearings.tolerances._1972 import SupportDetail
    from mastapy._private.bearings.tolerances._1973 import SupportMaterialSource
    from mastapy._private.bearings.tolerances._1974 import SupportTolerance
    from mastapy._private.bearings.tolerances._1975 import (
        SupportToleranceLocationDesignation,
    )
    from mastapy._private.bearings.tolerances._1976 import ToleranceCombination
    from mastapy._private.bearings.tolerances._1977 import TypeOfFit
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bearings.tolerances._1953": ["BearingConnectionComponent"],
        "_private.bearings.tolerances._1954": ["InternalClearanceClass"],
        "_private.bearings.tolerances._1955": ["BearingToleranceClass"],
        "_private.bearings.tolerances._1956": ["BearingToleranceDefinitionOptions"],
        "_private.bearings.tolerances._1957": ["FitType"],
        "_private.bearings.tolerances._1958": ["InnerRingTolerance"],
        "_private.bearings.tolerances._1959": ["InnerSupportTolerance"],
        "_private.bearings.tolerances._1960": ["InterferenceDetail"],
        "_private.bearings.tolerances._1961": ["InterferenceTolerance"],
        "_private.bearings.tolerances._1962": ["ITDesignation"],
        "_private.bearings.tolerances._1963": ["MountingSleeveDiameterDetail"],
        "_private.bearings.tolerances._1964": ["OuterRingTolerance"],
        "_private.bearings.tolerances._1965": ["OuterSupportTolerance"],
        "_private.bearings.tolerances._1966": ["RaceDetail"],
        "_private.bearings.tolerances._1967": ["RaceRoundnessAtAngle"],
        "_private.bearings.tolerances._1968": ["RadialSpecificationMethod"],
        "_private.bearings.tolerances._1969": ["RingTolerance"],
        "_private.bearings.tolerances._1970": ["RoundnessSpecification"],
        "_private.bearings.tolerances._1971": ["RoundnessSpecificationType"],
        "_private.bearings.tolerances._1972": ["SupportDetail"],
        "_private.bearings.tolerances._1973": ["SupportMaterialSource"],
        "_private.bearings.tolerances._1974": ["SupportTolerance"],
        "_private.bearings.tolerances._1975": ["SupportToleranceLocationDesignation"],
        "_private.bearings.tolerances._1976": ["ToleranceCombination"],
        "_private.bearings.tolerances._1977": ["TypeOfFit"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
