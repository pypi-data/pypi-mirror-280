"""DutyCyclePropertySummaryPercentage"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.utility.property import _1889
from mastapy._private.utility.units_and_measurements.measurements import _1736
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_PERCENTAGE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummaryPercentage"
)

if TYPE_CHECKING:
    from typing import Any, Type

    Self = TypeVar("Self", bound="DutyCyclePropertySummaryPercentage")
    CastSelf = TypeVar(
        "CastSelf",
        bound="DutyCyclePropertySummaryPercentage._Cast_DutyCyclePropertySummaryPercentage",
    )

T = TypeVar("T")

__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummaryPercentage",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DutyCyclePropertySummaryPercentage:
    """Special nested class for casting DutyCyclePropertySummaryPercentage to subclasses."""

    __parent__: "DutyCyclePropertySummaryPercentage"

    @property
    def duty_cycle_property_summary(
        self: "CastSelf",
    ) -> "_1889.DutyCyclePropertySummary":
        return self.__parent__._cast(_1889.DutyCyclePropertySummary)

    @property
    def duty_cycle_property_summary_percentage(
        self: "CastSelf",
    ) -> "DutyCyclePropertySummaryPercentage":
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
class DutyCyclePropertySummaryPercentage(
    _1889.DutyCyclePropertySummary[_1736.Percentage, T]
):
    """DutyCyclePropertySummaryPercentage

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _DUTY_CYCLE_PROPERTY_SUMMARY_PERCENTAGE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def average_value(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageValue

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_absolute_value(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAbsoluteValue

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_value(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumValue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_value(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_DutyCyclePropertySummaryPercentage":
        """Cast to another type.

        Returns:
            _Cast_DutyCyclePropertySummaryPercentage
        """
        return _Cast_DutyCyclePropertySummaryPercentage(self)
