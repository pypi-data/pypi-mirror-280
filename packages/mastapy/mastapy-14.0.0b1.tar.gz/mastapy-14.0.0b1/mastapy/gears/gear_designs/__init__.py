"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_designs._964 import (
        BevelHypoidGearDesignSettingsDatabase,
    )
    from mastapy._private.gears.gear_designs._965 import (
        BevelHypoidGearDesignSettingsItem,
    )
    from mastapy._private.gears.gear_designs._966 import (
        BevelHypoidGearRatingSettingsDatabase,
    )
    from mastapy._private.gears.gear_designs._967 import (
        BevelHypoidGearRatingSettingsItem,
    )
    from mastapy._private.gears.gear_designs._968 import DesignConstraint
    from mastapy._private.gears.gear_designs._969 import (
        DesignConstraintCollectionDatabase,
    )
    from mastapy._private.gears.gear_designs._970 import DesignConstraintsCollection
    from mastapy._private.gears.gear_designs._971 import GearDesign
    from mastapy._private.gears.gear_designs._972 import GearDesignComponent
    from mastapy._private.gears.gear_designs._973 import GearMeshDesign
    from mastapy._private.gears.gear_designs._974 import GearSetDesign
    from mastapy._private.gears.gear_designs._975 import (
        SelectedDesignConstraintsCollection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_designs._964": ["BevelHypoidGearDesignSettingsDatabase"],
        "_private.gears.gear_designs._965": ["BevelHypoidGearDesignSettingsItem"],
        "_private.gears.gear_designs._966": ["BevelHypoidGearRatingSettingsDatabase"],
        "_private.gears.gear_designs._967": ["BevelHypoidGearRatingSettingsItem"],
        "_private.gears.gear_designs._968": ["DesignConstraint"],
        "_private.gears.gear_designs._969": ["DesignConstraintCollectionDatabase"],
        "_private.gears.gear_designs._970": ["DesignConstraintsCollection"],
        "_private.gears.gear_designs._971": ["GearDesign"],
        "_private.gears.gear_designs._972": ["GearDesignComponent"],
        "_private.gears.gear_designs._973": ["GearMeshDesign"],
        "_private.gears.gear_designs._974": ["GearSetDesign"],
        "_private.gears.gear_designs._975": ["SelectedDesignConstraintsCollection"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BevelHypoidGearDesignSettingsDatabase",
    "BevelHypoidGearDesignSettingsItem",
    "BevelHypoidGearRatingSettingsDatabase",
    "BevelHypoidGearRatingSettingsItem",
    "DesignConstraint",
    "DesignConstraintCollectionDatabase",
    "DesignConstraintsCollection",
    "GearDesign",
    "GearDesignComponent",
    "GearMeshDesign",
    "GearSetDesign",
    "SelectedDesignConstraintsCollection",
)
