"""TorqueConverterLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5636
from mastapy._private.system_model.analyses_and_results.static_loads import _7000
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_TORQUE_CONVERTER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TorqueConverterLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.math_utility import _1581
    from mastapy._private.system_model.part_model.couplings import _2669
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7101,
        _6953,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="TorqueConverterLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="TorqueConverterLoadCase._Cast_TorqueConverterLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_TorqueConverterLoadCase:
    """Special nested class for casting TorqueConverterLoadCase to subclasses."""

    __parent__: "TorqueConverterLoadCase"

    @property
    def coupling_load_case(self: "CastSelf") -> "_7000.CouplingLoadCase":
        return self.__parent__._cast(_7000.CouplingLoadCase)

    @property
    def specialised_assembly_load_case(
        self: "CastSelf",
    ) -> "_7101.SpecialisedAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7101,
        )

        return self.__parent__._cast(_7101.SpecialisedAssemblyLoadCase)

    @property
    def abstract_assembly_load_case(
        self: "CastSelf",
    ) -> "_6953.AbstractAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6953,
        )

        return self.__parent__._cast(_6953.AbstractAssemblyLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7077.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7077,
        )

        return self.__parent__._cast(_7077.PartLoadCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def torque_converter_load_case(self: "CastSelf") -> "TorqueConverterLoadCase":
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
class TorqueConverterLoadCase(_7000.CouplingLoadCase):
    """TorqueConverterLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _TORQUE_CONVERTER_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def initial_lock_up_clutch_temperature(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.InitialLockUpClutchTemperature

        if temp is None:
            return 0.0

        return temp

    @initial_lock_up_clutch_temperature.setter
    @enforce_parameter_types
    def initial_lock_up_clutch_temperature(self: "Self", value: "float") -> None:
        self.wrapped.InitialLockUpClutchTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def initially_locked(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.InitiallyLocked

        if temp is None:
            return False

        return temp

    @initially_locked.setter
    @enforce_parameter_types
    def initially_locked(self: "Self", value: "bool") -> None:
        self.wrapped.InitiallyLocked = bool(value) if value is not None else False

    @property
    def lock_up_clutch_pressure_for_no_torque_converter_operation(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.LockUpClutchPressureForNoTorqueConverterOperation

        if temp is None:
            return 0.0

        return temp

    @lock_up_clutch_pressure_for_no_torque_converter_operation.setter
    @enforce_parameter_types
    def lock_up_clutch_pressure_for_no_torque_converter_operation(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.LockUpClutchPressureForNoTorqueConverterOperation = (
            float(value) if value is not None else 0.0
        )

    @property
    def lock_up_clutch_pressure_time_profile(
        self: "Self",
    ) -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.LockUpClutchPressureTimeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @lock_up_clutch_pressure_time_profile.setter
    @enforce_parameter_types
    def lock_up_clutch_pressure_time_profile(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.LockUpClutchPressureTimeProfile = value.wrapped

    @property
    def lock_up_clutch_rule(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_TorqueConverterLockupRule":
        """EnumWithSelectedValue[mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterLockupRule]"""
        temp = self.wrapped.LockUpClutchRule

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueConverterLockupRule.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lock_up_clutch_rule.setter
    @enforce_parameter_types
    def lock_up_clutch_rule(
        self: "Self", value: "_5636.TorqueConverterLockupRule"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueConverterLockupRule.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LockUpClutchRule = value

    @property
    def locking_speed_ratio_threshold(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LockingSpeedRatioThreshold

        if temp is None:
            return 0.0

        return temp

    @locking_speed_ratio_threshold.setter
    @enforce_parameter_types
    def locking_speed_ratio_threshold(self: "Self", value: "float") -> None:
        self.wrapped.LockingSpeedRatioThreshold = (
            float(value) if value is not None else 0.0
        )

    @property
    def time_for_full_clutch_pressure(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TimeForFullClutchPressure

        if temp is None:
            return 0.0

        return temp

    @time_for_full_clutch_pressure.setter
    @enforce_parameter_types
    def time_for_full_clutch_pressure(self: "Self", value: "float") -> None:
        self.wrapped.TimeForFullClutchPressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def time_to_change_locking_state(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TimeToChangeLockingState

        if temp is None:
            return 0.0

        return temp

    @time_to_change_locking_state.setter
    @enforce_parameter_types
    def time_to_change_locking_state(self: "Self", value: "float") -> None:
        self.wrapped.TimeToChangeLockingState = (
            float(value) if value is not None else 0.0
        )

    @property
    def transient_time_to_change_locking_status(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TransientTimeToChangeLockingStatus

        if temp is None:
            return 0.0

        return temp

    @transient_time_to_change_locking_status.setter
    @enforce_parameter_types
    def transient_time_to_change_locking_status(self: "Self", value: "float") -> None:
        self.wrapped.TransientTimeToChangeLockingStatus = (
            float(value) if value is not None else 0.0
        )

    @property
    def vehicle_speed_to_unlock(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.VehicleSpeedToUnlock

        if temp is None:
            return 0.0

        return temp

    @vehicle_speed_to_unlock.setter
    @enforce_parameter_types
    def vehicle_speed_to_unlock(self: "Self", value: "float") -> None:
        self.wrapped.VehicleSpeedToUnlock = float(value) if value is not None else 0.0

    @property
    def assembly_design(self: "Self") -> "_2669.TorqueConverter":
        """mastapy._private.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_TorqueConverterLoadCase":
        """Cast to another type.

        Returns:
            _Cast_TorqueConverterLoadCase
        """
        return _Cast_TorqueConverterLoadCase(self)
