"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.cylindrical._462 import AGMAScuffingResultsRow
    from mastapy._private.gears.rating.cylindrical._463 import (
        CylindricalGearDesignAndRatingSettings,
    )
    from mastapy._private.gears.rating.cylindrical._464 import (
        CylindricalGearDesignAndRatingSettingsDatabase,
    )
    from mastapy._private.gears.rating.cylindrical._465 import (
        CylindricalGearDesignAndRatingSettingsItem,
    )
    from mastapy._private.gears.rating.cylindrical._466 import (
        CylindricalGearDutyCycleRating,
    )
    from mastapy._private.gears.rating.cylindrical._467 import (
        CylindricalGearFlankDutyCycleRating,
    )
    from mastapy._private.gears.rating.cylindrical._468 import (
        CylindricalGearFlankRating,
    )
    from mastapy._private.gears.rating.cylindrical._469 import CylindricalGearMeshRating
    from mastapy._private.gears.rating.cylindrical._470 import (
        CylindricalGearMicroPittingResults,
    )
    from mastapy._private.gears.rating.cylindrical._471 import CylindricalGearRating
    from mastapy._private.gears.rating.cylindrical._472 import (
        CylindricalGearRatingGeometryDataSource,
    )
    from mastapy._private.gears.rating.cylindrical._473 import (
        CylindricalGearScuffingResults,
    )
    from mastapy._private.gears.rating.cylindrical._474 import (
        CylindricalGearSetDutyCycleRating,
    )
    from mastapy._private.gears.rating.cylindrical._475 import CylindricalGearSetRating
    from mastapy._private.gears.rating.cylindrical._476 import (
        CylindricalGearSingleFlankRating,
    )
    from mastapy._private.gears.rating.cylindrical._477 import (
        CylindricalMeshDutyCycleRating,
    )
    from mastapy._private.gears.rating.cylindrical._478 import (
        CylindricalMeshSingleFlankRating,
    )
    from mastapy._private.gears.rating.cylindrical._479 import (
        CylindricalPlasticGearRatingSettings,
    )
    from mastapy._private.gears.rating.cylindrical._480 import (
        CylindricalPlasticGearRatingSettingsDatabase,
    )
    from mastapy._private.gears.rating.cylindrical._481 import (
        CylindricalPlasticGearRatingSettingsItem,
    )
    from mastapy._private.gears.rating.cylindrical._482 import CylindricalRateableMesh
    from mastapy._private.gears.rating.cylindrical._483 import DynamicFactorMethods
    from mastapy._private.gears.rating.cylindrical._484 import (
        GearBlankFactorCalculationOptions,
    )
    from mastapy._private.gears.rating.cylindrical._485 import ISOScuffingResultsRow
    from mastapy._private.gears.rating.cylindrical._486 import MeshRatingForReports
    from mastapy._private.gears.rating.cylindrical._487 import MicropittingRatingMethod
    from mastapy._private.gears.rating.cylindrical._488 import MicroPittingResultsRow
    from mastapy._private.gears.rating.cylindrical._489 import (
        MisalignmentContactPatternEnhancements,
    )
    from mastapy._private.gears.rating.cylindrical._490 import RatingMethod
    from mastapy._private.gears.rating.cylindrical._491 import (
        ReducedCylindricalGearSetDutyCycleRating,
    )
    from mastapy._private.gears.rating.cylindrical._492 import (
        ScuffingFlashTemperatureRatingMethod,
    )
    from mastapy._private.gears.rating.cylindrical._493 import (
        ScuffingIntegralTemperatureRatingMethod,
    )
    from mastapy._private.gears.rating.cylindrical._494 import ScuffingMethods
    from mastapy._private.gears.rating.cylindrical._495 import ScuffingResultsRow
    from mastapy._private.gears.rating.cylindrical._496 import ScuffingResultsRowGear
    from mastapy._private.gears.rating.cylindrical._497 import TipReliefScuffingOptions
    from mastapy._private.gears.rating.cylindrical._498 import ToothThicknesses
    from mastapy._private.gears.rating.cylindrical._499 import (
        VDI2737SafetyFactorReportingObject,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.cylindrical._462": ["AGMAScuffingResultsRow"],
        "_private.gears.rating.cylindrical._463": [
            "CylindricalGearDesignAndRatingSettings"
        ],
        "_private.gears.rating.cylindrical._464": [
            "CylindricalGearDesignAndRatingSettingsDatabase"
        ],
        "_private.gears.rating.cylindrical._465": [
            "CylindricalGearDesignAndRatingSettingsItem"
        ],
        "_private.gears.rating.cylindrical._466": ["CylindricalGearDutyCycleRating"],
        "_private.gears.rating.cylindrical._467": [
            "CylindricalGearFlankDutyCycleRating"
        ],
        "_private.gears.rating.cylindrical._468": ["CylindricalGearFlankRating"],
        "_private.gears.rating.cylindrical._469": ["CylindricalGearMeshRating"],
        "_private.gears.rating.cylindrical._470": [
            "CylindricalGearMicroPittingResults"
        ],
        "_private.gears.rating.cylindrical._471": ["CylindricalGearRating"],
        "_private.gears.rating.cylindrical._472": [
            "CylindricalGearRatingGeometryDataSource"
        ],
        "_private.gears.rating.cylindrical._473": ["CylindricalGearScuffingResults"],
        "_private.gears.rating.cylindrical._474": ["CylindricalGearSetDutyCycleRating"],
        "_private.gears.rating.cylindrical._475": ["CylindricalGearSetRating"],
        "_private.gears.rating.cylindrical._476": ["CylindricalGearSingleFlankRating"],
        "_private.gears.rating.cylindrical._477": ["CylindricalMeshDutyCycleRating"],
        "_private.gears.rating.cylindrical._478": ["CylindricalMeshSingleFlankRating"],
        "_private.gears.rating.cylindrical._479": [
            "CylindricalPlasticGearRatingSettings"
        ],
        "_private.gears.rating.cylindrical._480": [
            "CylindricalPlasticGearRatingSettingsDatabase"
        ],
        "_private.gears.rating.cylindrical._481": [
            "CylindricalPlasticGearRatingSettingsItem"
        ],
        "_private.gears.rating.cylindrical._482": ["CylindricalRateableMesh"],
        "_private.gears.rating.cylindrical._483": ["DynamicFactorMethods"],
        "_private.gears.rating.cylindrical._484": ["GearBlankFactorCalculationOptions"],
        "_private.gears.rating.cylindrical._485": ["ISOScuffingResultsRow"],
        "_private.gears.rating.cylindrical._486": ["MeshRatingForReports"],
        "_private.gears.rating.cylindrical._487": ["MicropittingRatingMethod"],
        "_private.gears.rating.cylindrical._488": ["MicroPittingResultsRow"],
        "_private.gears.rating.cylindrical._489": [
            "MisalignmentContactPatternEnhancements"
        ],
        "_private.gears.rating.cylindrical._490": ["RatingMethod"],
        "_private.gears.rating.cylindrical._491": [
            "ReducedCylindricalGearSetDutyCycleRating"
        ],
        "_private.gears.rating.cylindrical._492": [
            "ScuffingFlashTemperatureRatingMethod"
        ],
        "_private.gears.rating.cylindrical._493": [
            "ScuffingIntegralTemperatureRatingMethod"
        ],
        "_private.gears.rating.cylindrical._494": ["ScuffingMethods"],
        "_private.gears.rating.cylindrical._495": ["ScuffingResultsRow"],
        "_private.gears.rating.cylindrical._496": ["ScuffingResultsRowGear"],
        "_private.gears.rating.cylindrical._497": ["TipReliefScuffingOptions"],
        "_private.gears.rating.cylindrical._498": ["ToothThicknesses"],
        "_private.gears.rating.cylindrical._499": [
            "VDI2737SafetyFactorReportingObject"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AGMAScuffingResultsRow",
    "CylindricalGearDesignAndRatingSettings",
    "CylindricalGearDesignAndRatingSettingsDatabase",
    "CylindricalGearDesignAndRatingSettingsItem",
    "CylindricalGearDutyCycleRating",
    "CylindricalGearFlankDutyCycleRating",
    "CylindricalGearFlankRating",
    "CylindricalGearMeshRating",
    "CylindricalGearMicroPittingResults",
    "CylindricalGearRating",
    "CylindricalGearRatingGeometryDataSource",
    "CylindricalGearScuffingResults",
    "CylindricalGearSetDutyCycleRating",
    "CylindricalGearSetRating",
    "CylindricalGearSingleFlankRating",
    "CylindricalMeshDutyCycleRating",
    "CylindricalMeshSingleFlankRating",
    "CylindricalPlasticGearRatingSettings",
    "CylindricalPlasticGearRatingSettingsDatabase",
    "CylindricalPlasticGearRatingSettingsItem",
    "CylindricalRateableMesh",
    "DynamicFactorMethods",
    "GearBlankFactorCalculationOptions",
    "ISOScuffingResultsRow",
    "MeshRatingForReports",
    "MicropittingRatingMethod",
    "MicroPittingResultsRow",
    "MisalignmentContactPatternEnhancements",
    "RatingMethod",
    "ReducedCylindricalGearSetDutyCycleRating",
    "ScuffingFlashTemperatureRatingMethod",
    "ScuffingIntegralTemperatureRatingMethod",
    "ScuffingMethods",
    "ScuffingResultsRow",
    "ScuffingResultsRowGear",
    "TipReliefScuffingOptions",
    "ToothThicknesses",
    "VDI2737SafetyFactorReportingObject",
)
