"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.materials._594 import AGMACylindricalGearMaterial
    from mastapy._private.gears.materials._595 import (
        BenedictAndKelleyCoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._596 import BevelGearAbstractMaterialDatabase
    from mastapy._private.gears.materials._597 import BevelGearISOMaterial
    from mastapy._private.gears.materials._598 import BevelGearISOMaterialDatabase
    from mastapy._private.gears.materials._599 import BevelGearMaterial
    from mastapy._private.gears.materials._600 import BevelGearMaterialDatabase
    from mastapy._private.gears.materials._601 import CoefficientOfFrictionCalculator
    from mastapy._private.gears.materials._602 import (
        CylindricalGearAGMAMaterialDatabase,
    )
    from mastapy._private.gears.materials._603 import CylindricalGearISOMaterialDatabase
    from mastapy._private.gears.materials._604 import CylindricalGearMaterial
    from mastapy._private.gears.materials._605 import CylindricalGearMaterialDatabase
    from mastapy._private.gears.materials._606 import (
        CylindricalGearPlasticMaterialDatabase,
    )
    from mastapy._private.gears.materials._607 import (
        DrozdovAndGavrikovCoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._608 import GearMaterial
    from mastapy._private.gears.materials._609 import GearMaterialDatabase
    from mastapy._private.gears.materials._610 import (
        GearMaterialExpertSystemFactorSettings,
    )
    from mastapy._private.gears.materials._611 import (
        InstantaneousCoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._612 import (
        ISO14179Part1CoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._613 import (
        ISO14179Part2CoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._614 import (
        ISO14179Part2CoefficientOfFrictionCalculatorBase,
    )
    from mastapy._private.gears.materials._615 import (
        ISO14179Part2CoefficientOfFrictionCalculatorWithMartinsModification,
    )
    from mastapy._private.gears.materials._616 import ISOCylindricalGearMaterial
    from mastapy._private.gears.materials._617 import (
        ISOTC60CoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._618 import (
        ISOTR1417912001CoefficientOfFrictionConstants,
    )
    from mastapy._private.gears.materials._619 import (
        ISOTR1417912001CoefficientOfFrictionConstantsDatabase,
    )
    from mastapy._private.gears.materials._620 import (
        KlingelnbergConicalGearMaterialDatabase,
    )
    from mastapy._private.gears.materials._621 import (
        KlingelnbergCycloPalloidConicalGearMaterial,
    )
    from mastapy._private.gears.materials._622 import ManufactureRating
    from mastapy._private.gears.materials._623 import (
        MisharinCoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._624 import (
        ODonoghueAndCameronCoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._625 import PlasticCylindricalGearMaterial
    from mastapy._private.gears.materials._626 import PlasticSNCurve
    from mastapy._private.gears.materials._627 import RatingMethods
    from mastapy._private.gears.materials._628 import RawMaterial
    from mastapy._private.gears.materials._629 import RawMaterialDatabase
    from mastapy._private.gears.materials._630 import (
        ScriptCoefficientOfFrictionCalculator,
    )
    from mastapy._private.gears.materials._631 import SNCurveDefinition
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.materials._594": ["AGMACylindricalGearMaterial"],
        "_private.gears.materials._595": [
            "BenedictAndKelleyCoefficientOfFrictionCalculator"
        ],
        "_private.gears.materials._596": ["BevelGearAbstractMaterialDatabase"],
        "_private.gears.materials._597": ["BevelGearISOMaterial"],
        "_private.gears.materials._598": ["BevelGearISOMaterialDatabase"],
        "_private.gears.materials._599": ["BevelGearMaterial"],
        "_private.gears.materials._600": ["BevelGearMaterialDatabase"],
        "_private.gears.materials._601": ["CoefficientOfFrictionCalculator"],
        "_private.gears.materials._602": ["CylindricalGearAGMAMaterialDatabase"],
        "_private.gears.materials._603": ["CylindricalGearISOMaterialDatabase"],
        "_private.gears.materials._604": ["CylindricalGearMaterial"],
        "_private.gears.materials._605": ["CylindricalGearMaterialDatabase"],
        "_private.gears.materials._606": ["CylindricalGearPlasticMaterialDatabase"],
        "_private.gears.materials._607": [
            "DrozdovAndGavrikovCoefficientOfFrictionCalculator"
        ],
        "_private.gears.materials._608": ["GearMaterial"],
        "_private.gears.materials._609": ["GearMaterialDatabase"],
        "_private.gears.materials._610": ["GearMaterialExpertSystemFactorSettings"],
        "_private.gears.materials._611": [
            "InstantaneousCoefficientOfFrictionCalculator"
        ],
        "_private.gears.materials._612": [
            "ISO14179Part1CoefficientOfFrictionCalculator"
        ],
        "_private.gears.materials._613": [
            "ISO14179Part2CoefficientOfFrictionCalculator"
        ],
        "_private.gears.materials._614": [
            "ISO14179Part2CoefficientOfFrictionCalculatorBase"
        ],
        "_private.gears.materials._615": [
            "ISO14179Part2CoefficientOfFrictionCalculatorWithMartinsModification"
        ],
        "_private.gears.materials._616": ["ISOCylindricalGearMaterial"],
        "_private.gears.materials._617": ["ISOTC60CoefficientOfFrictionCalculator"],
        "_private.gears.materials._618": [
            "ISOTR1417912001CoefficientOfFrictionConstants"
        ],
        "_private.gears.materials._619": [
            "ISOTR1417912001CoefficientOfFrictionConstantsDatabase"
        ],
        "_private.gears.materials._620": ["KlingelnbergConicalGearMaterialDatabase"],
        "_private.gears.materials._621": [
            "KlingelnbergCycloPalloidConicalGearMaterial"
        ],
        "_private.gears.materials._622": ["ManufactureRating"],
        "_private.gears.materials._623": ["MisharinCoefficientOfFrictionCalculator"],
        "_private.gears.materials._624": [
            "ODonoghueAndCameronCoefficientOfFrictionCalculator"
        ],
        "_private.gears.materials._625": ["PlasticCylindricalGearMaterial"],
        "_private.gears.materials._626": ["PlasticSNCurve"],
        "_private.gears.materials._627": ["RatingMethods"],
        "_private.gears.materials._628": ["RawMaterial"],
        "_private.gears.materials._629": ["RawMaterialDatabase"],
        "_private.gears.materials._630": ["ScriptCoefficientOfFrictionCalculator"],
        "_private.gears.materials._631": ["SNCurveDefinition"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AGMACylindricalGearMaterial",
    "BenedictAndKelleyCoefficientOfFrictionCalculator",
    "BevelGearAbstractMaterialDatabase",
    "BevelGearISOMaterial",
    "BevelGearISOMaterialDatabase",
    "BevelGearMaterial",
    "BevelGearMaterialDatabase",
    "CoefficientOfFrictionCalculator",
    "CylindricalGearAGMAMaterialDatabase",
    "CylindricalGearISOMaterialDatabase",
    "CylindricalGearMaterial",
    "CylindricalGearMaterialDatabase",
    "CylindricalGearPlasticMaterialDatabase",
    "DrozdovAndGavrikovCoefficientOfFrictionCalculator",
    "GearMaterial",
    "GearMaterialDatabase",
    "GearMaterialExpertSystemFactorSettings",
    "InstantaneousCoefficientOfFrictionCalculator",
    "ISO14179Part1CoefficientOfFrictionCalculator",
    "ISO14179Part2CoefficientOfFrictionCalculator",
    "ISO14179Part2CoefficientOfFrictionCalculatorBase",
    "ISO14179Part2CoefficientOfFrictionCalculatorWithMartinsModification",
    "ISOCylindricalGearMaterial",
    "ISOTC60CoefficientOfFrictionCalculator",
    "ISOTR1417912001CoefficientOfFrictionConstants",
    "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
    "KlingelnbergConicalGearMaterialDatabase",
    "KlingelnbergCycloPalloidConicalGearMaterial",
    "ManufactureRating",
    "MisharinCoefficientOfFrictionCalculator",
    "ODonoghueAndCameronCoefficientOfFrictionCalculator",
    "PlasticCylindricalGearMaterial",
    "PlasticSNCurve",
    "RatingMethods",
    "RawMaterial",
    "RawMaterialDatabase",
    "ScriptCoefficientOfFrictionCalculator",
    "SNCurveDefinition",
)
