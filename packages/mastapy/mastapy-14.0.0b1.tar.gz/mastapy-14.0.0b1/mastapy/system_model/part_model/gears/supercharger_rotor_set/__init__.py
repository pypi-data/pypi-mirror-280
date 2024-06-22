"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2611 import (
        BoostPressureInputOptions,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2612 import (
        InputPowerInputOptions,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2613 import (
        PressureRatioInputOptions,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2614 import (
        RotorSetDataInputFileOptions,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2615 import (
        RotorSetMeasuredPoint,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2616 import (
        RotorSpeedInputOptions,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2617 import (
        SuperchargerMap,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2618 import (
        SuperchargerMaps,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2619 import (
        SuperchargerRotorSet,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2620 import (
        SuperchargerRotorSetDatabase,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set._2621 import (
        YVariableForImportedData,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.gears.supercharger_rotor_set._2611": [
            "BoostPressureInputOptions"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2612": [
            "InputPowerInputOptions"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2613": [
            "PressureRatioInputOptions"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2614": [
            "RotorSetDataInputFileOptions"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2615": [
            "RotorSetMeasuredPoint"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2616": [
            "RotorSpeedInputOptions"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2617": [
            "SuperchargerMap"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2618": [
            "SuperchargerMaps"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2619": [
            "SuperchargerRotorSet"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2620": [
            "SuperchargerRotorSetDatabase"
        ],
        "_private.system_model.part_model.gears.supercharger_rotor_set._2621": [
            "YVariableForImportedData"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)
