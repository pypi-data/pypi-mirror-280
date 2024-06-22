"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_designs.bevel._1217 import (
        AGMAGleasonConicalGearGeometryMethods,
    )
    from mastapy._private.gears.gear_designs.bevel._1218 import BevelGearDesign
    from mastapy._private.gears.gear_designs.bevel._1219 import BevelGearMeshDesign
    from mastapy._private.gears.gear_designs.bevel._1220 import BevelGearSetDesign
    from mastapy._private.gears.gear_designs.bevel._1221 import BevelMeshedGearDesign
    from mastapy._private.gears.gear_designs.bevel._1222 import (
        DrivenMachineCharacteristicGleason,
    )
    from mastapy._private.gears.gear_designs.bevel._1223 import EdgeRadiusType
    from mastapy._private.gears.gear_designs.bevel._1224 import FinishingMethods
    from mastapy._private.gears.gear_designs.bevel._1225 import (
        MachineCharacteristicAGMAKlingelnberg,
    )
    from mastapy._private.gears.gear_designs.bevel._1226 import (
        PrimeMoverCharacteristicGleason,
    )
    from mastapy._private.gears.gear_designs.bevel._1227 import (
        ToothProportionsInputMethod,
    )
    from mastapy._private.gears.gear_designs.bevel._1228 import (
        ToothThicknessSpecificationMethod,
    )
    from mastapy._private.gears.gear_designs.bevel._1229 import (
        WheelFinishCutterPointWidthRestrictionMethod,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_designs.bevel._1217": [
            "AGMAGleasonConicalGearGeometryMethods"
        ],
        "_private.gears.gear_designs.bevel._1218": ["BevelGearDesign"],
        "_private.gears.gear_designs.bevel._1219": ["BevelGearMeshDesign"],
        "_private.gears.gear_designs.bevel._1220": ["BevelGearSetDesign"],
        "_private.gears.gear_designs.bevel._1221": ["BevelMeshedGearDesign"],
        "_private.gears.gear_designs.bevel._1222": [
            "DrivenMachineCharacteristicGleason"
        ],
        "_private.gears.gear_designs.bevel._1223": ["EdgeRadiusType"],
        "_private.gears.gear_designs.bevel._1224": ["FinishingMethods"],
        "_private.gears.gear_designs.bevel._1225": [
            "MachineCharacteristicAGMAKlingelnberg"
        ],
        "_private.gears.gear_designs.bevel._1226": ["PrimeMoverCharacteristicGleason"],
        "_private.gears.gear_designs.bevel._1227": ["ToothProportionsInputMethod"],
        "_private.gears.gear_designs.bevel._1228": [
            "ToothThicknessSpecificationMethod"
        ],
        "_private.gears.gear_designs.bevel._1229": [
            "WheelFinishCutterPointWidthRestrictionMethod"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)
