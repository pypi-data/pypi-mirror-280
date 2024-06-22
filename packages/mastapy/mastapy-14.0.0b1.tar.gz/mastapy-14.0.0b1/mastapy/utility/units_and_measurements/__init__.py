"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.utility.units_and_measurements._1649 import (
        DegreesMinutesSeconds,
    )
    from mastapy._private.utility.units_and_measurements._1650 import EnumUnit
    from mastapy._private.utility.units_and_measurements._1651 import InverseUnit
    from mastapy._private.utility.units_and_measurements._1652 import MeasurementBase
    from mastapy._private.utility.units_and_measurements._1653 import (
        MeasurementSettings,
    )
    from mastapy._private.utility.units_and_measurements._1654 import MeasurementSystem
    from mastapy._private.utility.units_and_measurements._1655 import SafetyFactorUnit
    from mastapy._private.utility.units_and_measurements._1656 import TimeUnit
    from mastapy._private.utility.units_and_measurements._1657 import Unit
    from mastapy._private.utility.units_and_measurements._1658 import UnitGradient
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.units_and_measurements._1649": ["DegreesMinutesSeconds"],
        "_private.utility.units_and_measurements._1650": ["EnumUnit"],
        "_private.utility.units_and_measurements._1651": ["InverseUnit"],
        "_private.utility.units_and_measurements._1652": ["MeasurementBase"],
        "_private.utility.units_and_measurements._1653": ["MeasurementSettings"],
        "_private.utility.units_and_measurements._1654": ["MeasurementSystem"],
        "_private.utility.units_and_measurements._1655": ["SafetyFactorUnit"],
        "_private.utility.units_and_measurements._1656": ["TimeUnit"],
        "_private.utility.units_and_measurements._1657": ["Unit"],
        "_private.utility.units_and_measurements._1658": ["UnitGradient"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)
