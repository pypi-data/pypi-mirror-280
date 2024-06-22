"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.manufacturing.cylindrical._632 import (
        CutterFlankSections,
    )
    from mastapy._private.gears.manufacturing.cylindrical._633 import (
        CylindricalCutterDatabase,
    )
    from mastapy._private.gears.manufacturing.cylindrical._634 import (
        CylindricalGearBlank,
    )
    from mastapy._private.gears.manufacturing.cylindrical._635 import (
        CylindricalGearManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.cylindrical._636 import (
        CylindricalGearSpecifiedMicroGeometry,
    )
    from mastapy._private.gears.manufacturing.cylindrical._637 import (
        CylindricalGearSpecifiedProfile,
    )
    from mastapy._private.gears.manufacturing.cylindrical._638 import (
        CylindricalHobDatabase,
    )
    from mastapy._private.gears.manufacturing.cylindrical._639 import (
        CylindricalManufacturedGearDutyCycle,
    )
    from mastapy._private.gears.manufacturing.cylindrical._640 import (
        CylindricalManufacturedGearLoadCase,
    )
    from mastapy._private.gears.manufacturing.cylindrical._641 import (
        CylindricalManufacturedGearMeshDutyCycle,
    )
    from mastapy._private.gears.manufacturing.cylindrical._642 import (
        CylindricalManufacturedGearMeshLoadCase,
    )
    from mastapy._private.gears.manufacturing.cylindrical._643 import (
        CylindricalManufacturedGearSetDutyCycle,
    )
    from mastapy._private.gears.manufacturing.cylindrical._644 import (
        CylindricalManufacturedGearSetLoadCase,
    )
    from mastapy._private.gears.manufacturing.cylindrical._645 import (
        CylindricalMeshManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.cylindrical._646 import (
        CylindricalMftFinishingMethods,
    )
    from mastapy._private.gears.manufacturing.cylindrical._647 import (
        CylindricalMftRoughingMethods,
    )
    from mastapy._private.gears.manufacturing.cylindrical._648 import (
        CylindricalSetManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.cylindrical._649 import (
        CylindricalShaperDatabase,
    )
    from mastapy._private.gears.manufacturing.cylindrical._650 import Flank
    from mastapy._private.gears.manufacturing.cylindrical._651 import (
        GearManufacturingConfigurationViewModel,
    )
    from mastapy._private.gears.manufacturing.cylindrical._652 import (
        GearManufacturingConfigurationViewModelPlaceholder,
    )
    from mastapy._private.gears.manufacturing.cylindrical._653 import (
        GearSetConfigViewModel,
    )
    from mastapy._private.gears.manufacturing.cylindrical._654 import HobEdgeTypes
    from mastapy._private.gears.manufacturing.cylindrical._655 import (
        LeadModificationSegment,
    )
    from mastapy._private.gears.manufacturing.cylindrical._656 import (
        MicroGeometryInputs,
    )
    from mastapy._private.gears.manufacturing.cylindrical._657 import (
        MicroGeometryInputsLead,
    )
    from mastapy._private.gears.manufacturing.cylindrical._658 import (
        MicroGeometryInputsProfile,
    )
    from mastapy._private.gears.manufacturing.cylindrical._659 import (
        ModificationSegment,
    )
    from mastapy._private.gears.manufacturing.cylindrical._660 import (
        ProfileModificationSegment,
    )
    from mastapy._private.gears.manufacturing.cylindrical._661 import (
        SuitableCutterSetup,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.manufacturing.cylindrical._632": ["CutterFlankSections"],
        "_private.gears.manufacturing.cylindrical._633": ["CylindricalCutterDatabase"],
        "_private.gears.manufacturing.cylindrical._634": ["CylindricalGearBlank"],
        "_private.gears.manufacturing.cylindrical._635": [
            "CylindricalGearManufacturingConfig"
        ],
        "_private.gears.manufacturing.cylindrical._636": [
            "CylindricalGearSpecifiedMicroGeometry"
        ],
        "_private.gears.manufacturing.cylindrical._637": [
            "CylindricalGearSpecifiedProfile"
        ],
        "_private.gears.manufacturing.cylindrical._638": ["CylindricalHobDatabase"],
        "_private.gears.manufacturing.cylindrical._639": [
            "CylindricalManufacturedGearDutyCycle"
        ],
        "_private.gears.manufacturing.cylindrical._640": [
            "CylindricalManufacturedGearLoadCase"
        ],
        "_private.gears.manufacturing.cylindrical._641": [
            "CylindricalManufacturedGearMeshDutyCycle"
        ],
        "_private.gears.manufacturing.cylindrical._642": [
            "CylindricalManufacturedGearMeshLoadCase"
        ],
        "_private.gears.manufacturing.cylindrical._643": [
            "CylindricalManufacturedGearSetDutyCycle"
        ],
        "_private.gears.manufacturing.cylindrical._644": [
            "CylindricalManufacturedGearSetLoadCase"
        ],
        "_private.gears.manufacturing.cylindrical._645": [
            "CylindricalMeshManufacturingConfig"
        ],
        "_private.gears.manufacturing.cylindrical._646": [
            "CylindricalMftFinishingMethods"
        ],
        "_private.gears.manufacturing.cylindrical._647": [
            "CylindricalMftRoughingMethods"
        ],
        "_private.gears.manufacturing.cylindrical._648": [
            "CylindricalSetManufacturingConfig"
        ],
        "_private.gears.manufacturing.cylindrical._649": ["CylindricalShaperDatabase"],
        "_private.gears.manufacturing.cylindrical._650": ["Flank"],
        "_private.gears.manufacturing.cylindrical._651": [
            "GearManufacturingConfigurationViewModel"
        ],
        "_private.gears.manufacturing.cylindrical._652": [
            "GearManufacturingConfigurationViewModelPlaceholder"
        ],
        "_private.gears.manufacturing.cylindrical._653": ["GearSetConfigViewModel"],
        "_private.gears.manufacturing.cylindrical._654": ["HobEdgeTypes"],
        "_private.gears.manufacturing.cylindrical._655": ["LeadModificationSegment"],
        "_private.gears.manufacturing.cylindrical._656": ["MicroGeometryInputs"],
        "_private.gears.manufacturing.cylindrical._657": ["MicroGeometryInputsLead"],
        "_private.gears.manufacturing.cylindrical._658": ["MicroGeometryInputsProfile"],
        "_private.gears.manufacturing.cylindrical._659": ["ModificationSegment"],
        "_private.gears.manufacturing.cylindrical._660": ["ProfileModificationSegment"],
        "_private.gears.manufacturing.cylindrical._661": ["SuitableCutterSetup"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CutterFlankSections",
    "CylindricalCutterDatabase",
    "CylindricalGearBlank",
    "CylindricalGearManufacturingConfig",
    "CylindricalGearSpecifiedMicroGeometry",
    "CylindricalGearSpecifiedProfile",
    "CylindricalHobDatabase",
    "CylindricalManufacturedGearDutyCycle",
    "CylindricalManufacturedGearLoadCase",
    "CylindricalManufacturedGearMeshDutyCycle",
    "CylindricalManufacturedGearMeshLoadCase",
    "CylindricalManufacturedGearSetDutyCycle",
    "CylindricalManufacturedGearSetLoadCase",
    "CylindricalMeshManufacturingConfig",
    "CylindricalMftFinishingMethods",
    "CylindricalMftRoughingMethods",
    "CylindricalSetManufacturingConfig",
    "CylindricalShaperDatabase",
    "Flank",
    "GearManufacturingConfigurationViewModel",
    "GearManufacturingConfigurationViewModelPlaceholder",
    "GearSetConfigViewModel",
    "HobEdgeTypes",
    "LeadModificationSegment",
    "MicroGeometryInputs",
    "MicroGeometryInputsLead",
    "MicroGeometryInputsProfile",
    "ModificationSegment",
    "ProfileModificationSegment",
    "SuitableCutterSetup",
)
