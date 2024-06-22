"""SpeedTorqueCurveLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.electric_machines.load_cases_and_analyses import _1413
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPEED_TORQUE_CURVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SpeedTorqueCurveLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.electric_machines import _1308
    from mastapy._private.electric_machines.load_cases_and_analyses import _1420, _1405

    Self = TypeVar("Self", bound="SpeedTorqueCurveLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpeedTorqueCurveLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpeedTorqueCurveLoadCase:
    """Special nested class for casting SpeedTorqueCurveLoadCase to subclasses."""

    __parent__: "SpeedTorqueCurveLoadCase"

    @property
    def non_linear_dq_model_multiple_operating_points_load_case(
        self: "CastSelf",
    ) -> "_1413.NonLinearDQModelMultipleOperatingPointsLoadCase":
        return self.__parent__._cast(
            _1413.NonLinearDQModelMultipleOperatingPointsLoadCase
        )

    @property
    def electric_machine_load_case_base(
        self: "CastSelf",
    ) -> "_1405.ElectricMachineLoadCaseBase":
        from mastapy._private.electric_machines.load_cases_and_analyses import _1405

        return self.__parent__._cast(_1405.ElectricMachineLoadCaseBase)

    @property
    def speed_torque_curve_load_case(self: "CastSelf") -> "SpeedTorqueCurveLoadCase":
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
class SpeedTorqueCurveLoadCase(_1413.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """SpeedTorqueCurveLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPEED_TORQUE_CURVE_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def maximum_speed(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_speed.setter
    @enforce_parameter_types
    def maximum_speed(self: "Self", value: "float") -> None:
        self.wrapped.MaximumSpeed = float(value) if value is not None else 0.0

    @property
    def minimum_speed(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @minimum_speed.setter
    @enforce_parameter_types
    def minimum_speed(self: "Self", value: "float") -> None:
        self.wrapped.MinimumSpeed = float(value) if value is not None else 0.0

    @property
    def number_of_speed_values(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfSpeedValues

        if temp is None:
            return 0

        return temp

    @number_of_speed_values.setter
    @enforce_parameter_types
    def number_of_speed_values(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfSpeedValues = int(value) if value is not None else 0

    @enforce_parameter_types
    def analysis_for(
        self: "Self", setup: "_1308.ElectricMachineSetup"
    ) -> "_1420.SpeedTorqueCurveAnalysis":
        """mastapy._private.electric_machines.load_cases_and_analyses.SpeedTorqueCurveAnalysis

        Args:
            setup (mastapy._private.electric_machines.ElectricMachineSetup)
        """
        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_SpeedTorqueCurveLoadCase":
        """Cast to another type.

        Returns:
            _Cast_SpeedTorqueCurveLoadCase
        """
        return _Cast_SpeedTorqueCurveLoadCase(self)
