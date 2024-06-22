"""FractionMeasurementBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.utility.units_and_measurements import _1652
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_FRACTION_MEASUREMENT_BASE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "FractionMeasurementBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.units_and_measurements.measurements import (
        _1675,
        _1736,
    )

    Self = TypeVar("Self", bound="FractionMeasurementBase")
    CastSelf = TypeVar(
        "CastSelf", bound="FractionMeasurementBase._Cast_FractionMeasurementBase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("FractionMeasurementBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FractionMeasurementBase:
    """Special nested class for casting FractionMeasurementBase to subclasses."""

    __parent__: "FractionMeasurementBase"

    @property
    def measurement_base(self: "CastSelf") -> "_1652.MeasurementBase":
        return self.__parent__._cast(_1652.MeasurementBase)

    @property
    def damage(self: "CastSelf") -> "_1675.Damage":
        from mastapy._private.utility.units_and_measurements.measurements import _1675

        return self.__parent__._cast(_1675.Damage)

    @property
    def percentage(self: "CastSelf") -> "_1736.Percentage":
        from mastapy._private.utility.units_and_measurements.measurements import _1736

        return self.__parent__._cast(_1736.Percentage)

    @property
    def fraction_measurement_base(self: "CastSelf") -> "FractionMeasurementBase":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class FractionMeasurementBase(_1652.MeasurementBase):
    """FractionMeasurementBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FRACTION_MEASUREMENT_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_FractionMeasurementBase":
        """Cast to another type.

        Returns:
            _Cast_FractionMeasurementBase
        """
        return _Cast_FractionMeasurementBase(self)
