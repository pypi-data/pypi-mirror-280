"""HobbingProcessTotalModificationCalculation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _689,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HOBBING_PROCESS_TOTAL_MODIFICATION_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessTotalModificationCalculation",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility_gui.charts import _1917
    from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _703,
    )

    Self = TypeVar("Self", bound="HobbingProcessTotalModificationCalculation")
    CastSelf = TypeVar(
        "CastSelf",
        bound="HobbingProcessTotalModificationCalculation._Cast_HobbingProcessTotalModificationCalculation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessTotalModificationCalculation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HobbingProcessTotalModificationCalculation:
    """Special nested class for casting HobbingProcessTotalModificationCalculation to subclasses."""

    __parent__: "HobbingProcessTotalModificationCalculation"

    @property
    def hobbing_process_calculation(
        self: "CastSelf",
    ) -> "_689.HobbingProcessCalculation":
        return self.__parent__._cast(_689.HobbingProcessCalculation)

    @property
    def process_calculation(self: "CastSelf") -> "_703.ProcessCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _703,
        )

        return self.__parent__._cast(_703.ProcessCalculation)

    @property
    def hobbing_process_total_modification_calculation(
        self: "CastSelf",
    ) -> "HobbingProcessTotalModificationCalculation":
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
class HobbingProcessTotalModificationCalculation(_689.HobbingProcessCalculation):
    """HobbingProcessTotalModificationCalculation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HOBBING_PROCESS_TOTAL_MODIFICATION_CALCULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def lead_range_max(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LeadRangeMax

        if temp is None:
            return 0.0

        return temp

    @lead_range_max.setter
    @enforce_parameter_types
    def lead_range_max(self: "Self", value: "float") -> None:
        self.wrapped.LeadRangeMax = float(value) if value is not None else 0.0

    @property
    def lead_range_min(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LeadRangeMin

        if temp is None:
            return 0.0

        return temp

    @lead_range_min.setter
    @enforce_parameter_types
    def lead_range_min(self: "Self", value: "float") -> None:
        self.wrapped.LeadRangeMin = float(value) if value is not None else 0.0

    @property
    def number_of_lead_bands(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfLeadBands

        if temp is None:
            return 0

        return temp

    @number_of_lead_bands.setter
    @enforce_parameter_types
    def number_of_lead_bands(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfLeadBands = int(value) if value is not None else 0

    @property
    def number_of_profile_bands(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    @enforce_parameter_types
    def number_of_profile_bands(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def total_errors_chart_left_flank(self: "Self") -> "_1917.ThreeDChartDefinition":
        """mastapy._private.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalErrorsChartLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_errors_chart_right_flank(self: "Self") -> "_1917.ThreeDChartDefinition":
        """mastapy._private.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalErrorsChartRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_HobbingProcessTotalModificationCalculation":
        """Cast to another type.

        Returns:
            _Cast_HobbingProcessTotalModificationCalculation
        """
        return _Cast_HobbingProcessTotalModificationCalculation(self)
