"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears._324 import AccuracyGrades
    from mastapy._private.gears._325 import AGMAToleranceStandard
    from mastapy._private.gears._326 import BevelHypoidGearDesignSettings
    from mastapy._private.gears._327 import BevelHypoidGearRatingSettings
    from mastapy._private.gears._328 import CentreDistanceChangeMethod
    from mastapy._private.gears._329 import CoefficientOfFrictionCalculationMethod
    from mastapy._private.gears._330 import ConicalGearToothSurface
    from mastapy._private.gears._331 import ContactRatioDataSource
    from mastapy._private.gears._332 import ContactRatioRequirements
    from mastapy._private.gears._333 import CylindricalFlanks
    from mastapy._private.gears._334 import CylindricalMisalignmentDataSource
    from mastapy._private.gears._335 import DeflectionFromBendingOption
    from mastapy._private.gears._336 import GearFlanks
    from mastapy._private.gears._337 import GearNURBSSurface
    from mastapy._private.gears._338 import GearSetDesignGroup
    from mastapy._private.gears._339 import GearSetModes
    from mastapy._private.gears._340 import GearSetOptimisationResult
    from mastapy._private.gears._341 import GearSetOptimisationResults
    from mastapy._private.gears._342 import GearSetOptimiser
    from mastapy._private.gears._343 import Hand
    from mastapy._private.gears._344 import ISOToleranceStandard
    from mastapy._private.gears._345 import LubricationMethods
    from mastapy._private.gears._346 import MicroGeometryInputTypes
    from mastapy._private.gears._347 import MicroGeometryModel
    from mastapy._private.gears._348 import (
        MicropittingCoefficientOfFrictionCalculationMethod,
    )
    from mastapy._private.gears._349 import NamedPlanetAngle
    from mastapy._private.gears._350 import PlanetaryDetail
    from mastapy._private.gears._351 import PlanetaryRatingLoadSharingOption
    from mastapy._private.gears._352 import PocketingPowerLossCoefficients
    from mastapy._private.gears._353 import PocketingPowerLossCoefficientsDatabase
    from mastapy._private.gears._354 import QualityGradeTypes
    from mastapy._private.gears._355 import SafetyRequirementsAGMA
    from mastapy._private.gears._356 import (
        SpecificationForTheEffectOfOilKinematicViscosity,
    )
    from mastapy._private.gears._357 import SpiralBevelRootLineTilt
    from mastapy._private.gears._358 import SpiralBevelToothTaper
    from mastapy._private.gears._359 import TESpecificationType
    from mastapy._private.gears._360 import WormAddendumFactor
    from mastapy._private.gears._361 import WormType
    from mastapy._private.gears._362 import ZerolBevelGleasonToothTaperOption
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears._324": ["AccuracyGrades"],
        "_private.gears._325": ["AGMAToleranceStandard"],
        "_private.gears._326": ["BevelHypoidGearDesignSettings"],
        "_private.gears._327": ["BevelHypoidGearRatingSettings"],
        "_private.gears._328": ["CentreDistanceChangeMethod"],
        "_private.gears._329": ["CoefficientOfFrictionCalculationMethod"],
        "_private.gears._330": ["ConicalGearToothSurface"],
        "_private.gears._331": ["ContactRatioDataSource"],
        "_private.gears._332": ["ContactRatioRequirements"],
        "_private.gears._333": ["CylindricalFlanks"],
        "_private.gears._334": ["CylindricalMisalignmentDataSource"],
        "_private.gears._335": ["DeflectionFromBendingOption"],
        "_private.gears._336": ["GearFlanks"],
        "_private.gears._337": ["GearNURBSSurface"],
        "_private.gears._338": ["GearSetDesignGroup"],
        "_private.gears._339": ["GearSetModes"],
        "_private.gears._340": ["GearSetOptimisationResult"],
        "_private.gears._341": ["GearSetOptimisationResults"],
        "_private.gears._342": ["GearSetOptimiser"],
        "_private.gears._343": ["Hand"],
        "_private.gears._344": ["ISOToleranceStandard"],
        "_private.gears._345": ["LubricationMethods"],
        "_private.gears._346": ["MicroGeometryInputTypes"],
        "_private.gears._347": ["MicroGeometryModel"],
        "_private.gears._348": ["MicropittingCoefficientOfFrictionCalculationMethod"],
        "_private.gears._349": ["NamedPlanetAngle"],
        "_private.gears._350": ["PlanetaryDetail"],
        "_private.gears._351": ["PlanetaryRatingLoadSharingOption"],
        "_private.gears._352": ["PocketingPowerLossCoefficients"],
        "_private.gears._353": ["PocketingPowerLossCoefficientsDatabase"],
        "_private.gears._354": ["QualityGradeTypes"],
        "_private.gears._355": ["SafetyRequirementsAGMA"],
        "_private.gears._356": ["SpecificationForTheEffectOfOilKinematicViscosity"],
        "_private.gears._357": ["SpiralBevelRootLineTilt"],
        "_private.gears._358": ["SpiralBevelToothTaper"],
        "_private.gears._359": ["TESpecificationType"],
        "_private.gears._360": ["WormAddendumFactor"],
        "_private.gears._361": ["WormType"],
        "_private.gears._362": ["ZerolBevelGleasonToothTaperOption"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AccuracyGrades",
    "AGMAToleranceStandard",
    "BevelHypoidGearDesignSettings",
    "BevelHypoidGearRatingSettings",
    "CentreDistanceChangeMethod",
    "CoefficientOfFrictionCalculationMethod",
    "ConicalGearToothSurface",
    "ContactRatioDataSource",
    "ContactRatioRequirements",
    "CylindricalFlanks",
    "CylindricalMisalignmentDataSource",
    "DeflectionFromBendingOption",
    "GearFlanks",
    "GearNURBSSurface",
    "GearSetDesignGroup",
    "GearSetModes",
    "GearSetOptimisationResult",
    "GearSetOptimisationResults",
    "GearSetOptimiser",
    "Hand",
    "ISOToleranceStandard",
    "LubricationMethods",
    "MicroGeometryInputTypes",
    "MicroGeometryModel",
    "MicropittingCoefficientOfFrictionCalculationMethod",
    "NamedPlanetAngle",
    "PlanetaryDetail",
    "PlanetaryRatingLoadSharingOption",
    "PocketingPowerLossCoefficients",
    "PocketingPowerLossCoefficientsDatabase",
    "QualityGradeTypes",
    "SafetyRequirementsAGMA",
    "SpecificationForTheEffectOfOilKinematicViscosity",
    "SpiralBevelRootLineTilt",
    "SpiralBevelToothTaper",
    "TESpecificationType",
    "WormAddendumFactor",
    "WormType",
    "ZerolBevelGleasonToothTaperOption",
)
