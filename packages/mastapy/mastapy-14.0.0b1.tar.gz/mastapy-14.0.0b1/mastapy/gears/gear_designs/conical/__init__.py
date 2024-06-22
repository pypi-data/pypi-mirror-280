"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_designs.conical._1188 import ActiveConicalFlank
    from mastapy._private.gears.gear_designs.conical._1189 import (
        BacklashDistributionRule,
    )
    from mastapy._private.gears.gear_designs.conical._1190 import ConicalFlanks
    from mastapy._private.gears.gear_designs.conical._1191 import ConicalGearCutter
    from mastapy._private.gears.gear_designs.conical._1192 import ConicalGearDesign
    from mastapy._private.gears.gear_designs.conical._1193 import ConicalGearMeshDesign
    from mastapy._private.gears.gear_designs.conical._1194 import ConicalGearSetDesign
    from mastapy._private.gears.gear_designs.conical._1195 import (
        ConicalMachineSettingCalculationMethods,
    )
    from mastapy._private.gears.gear_designs.conical._1196 import (
        ConicalManufactureMethods,
    )
    from mastapy._private.gears.gear_designs.conical._1197 import (
        ConicalMeshedGearDesign,
    )
    from mastapy._private.gears.gear_designs.conical._1198 import (
        ConicalMeshMisalignments,
    )
    from mastapy._private.gears.gear_designs.conical._1199 import CutterBladeType
    from mastapy._private.gears.gear_designs.conical._1200 import CutterGaugeLengths
    from mastapy._private.gears.gear_designs.conical._1201 import DummyConicalGearCutter
    from mastapy._private.gears.gear_designs.conical._1202 import FrontEndTypes
    from mastapy._private.gears.gear_designs.conical._1203 import (
        GleasonSafetyRequirements,
    )
    from mastapy._private.gears.gear_designs.conical._1204 import (
        KIMoSBevelHypoidSingleLoadCaseResultsData,
    )
    from mastapy._private.gears.gear_designs.conical._1205 import (
        KIMoSBevelHypoidSingleRotationAngleResult,
    )
    from mastapy._private.gears.gear_designs.conical._1206 import (
        KlingelnbergFinishingMethods,
    )
    from mastapy._private.gears.gear_designs.conical._1207 import (
        LoadDistributionFactorMethods,
    )
    from mastapy._private.gears.gear_designs.conical._1208 import TopremEntryType
    from mastapy._private.gears.gear_designs.conical._1209 import TopremLetter
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_designs.conical._1188": ["ActiveConicalFlank"],
        "_private.gears.gear_designs.conical._1189": ["BacklashDistributionRule"],
        "_private.gears.gear_designs.conical._1190": ["ConicalFlanks"],
        "_private.gears.gear_designs.conical._1191": ["ConicalGearCutter"],
        "_private.gears.gear_designs.conical._1192": ["ConicalGearDesign"],
        "_private.gears.gear_designs.conical._1193": ["ConicalGearMeshDesign"],
        "_private.gears.gear_designs.conical._1194": ["ConicalGearSetDesign"],
        "_private.gears.gear_designs.conical._1195": [
            "ConicalMachineSettingCalculationMethods"
        ],
        "_private.gears.gear_designs.conical._1196": ["ConicalManufactureMethods"],
        "_private.gears.gear_designs.conical._1197": ["ConicalMeshedGearDesign"],
        "_private.gears.gear_designs.conical._1198": ["ConicalMeshMisalignments"],
        "_private.gears.gear_designs.conical._1199": ["CutterBladeType"],
        "_private.gears.gear_designs.conical._1200": ["CutterGaugeLengths"],
        "_private.gears.gear_designs.conical._1201": ["DummyConicalGearCutter"],
        "_private.gears.gear_designs.conical._1202": ["FrontEndTypes"],
        "_private.gears.gear_designs.conical._1203": ["GleasonSafetyRequirements"],
        "_private.gears.gear_designs.conical._1204": [
            "KIMoSBevelHypoidSingleLoadCaseResultsData"
        ],
        "_private.gears.gear_designs.conical._1205": [
            "KIMoSBevelHypoidSingleRotationAngleResult"
        ],
        "_private.gears.gear_designs.conical._1206": ["KlingelnbergFinishingMethods"],
        "_private.gears.gear_designs.conical._1207": ["LoadDistributionFactorMethods"],
        "_private.gears.gear_designs.conical._1208": ["TopremEntryType"],
        "_private.gears.gear_designs.conical._1209": ["TopremLetter"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)
