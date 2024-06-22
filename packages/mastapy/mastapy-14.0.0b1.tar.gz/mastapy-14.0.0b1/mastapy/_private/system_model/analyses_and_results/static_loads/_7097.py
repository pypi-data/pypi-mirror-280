"""RootAssemblyLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.system_model.analyses_and_results.static_loads import _6965
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ROOT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RootAssemblyLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.system_model.part_model import _2530
    from mastapy._private.nodal_analysis.varying_input_components import _98, _97, _102
    from mastapy._private.math_utility.control import _1623
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _6951,
        _7012,
        _6953,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="RootAssemblyLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="RootAssemblyLoadCase._Cast_RootAssemblyLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_RootAssemblyLoadCase:
    """Special nested class for casting RootAssemblyLoadCase to subclasses."""

    __parent__: "RootAssemblyLoadCase"

    @property
    def assembly_load_case(self: "CastSelf") -> "_6965.AssemblyLoadCase":
        return self.__parent__._cast(_6965.AssemblyLoadCase)

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
    def root_assembly_load_case(self: "CastSelf") -> "RootAssemblyLoadCase":
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
class RootAssemblyLoadCase(_6965.AssemblyLoadCase):
    """RootAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ROOT_ASSEMBLY_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def brake_force_gain(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BrakeForceGain

        if temp is None:
            return 0.0

        return temp

    @brake_force_gain.setter
    @enforce_parameter_types
    def brake_force_gain(self: "Self", value: "float") -> None:
        self.wrapped.BrakeForceGain = float(value) if value is not None else 0.0

    @property
    def max_brake_force(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaxBrakeForce

        if temp is None:
            return 0.0

        return temp

    @max_brake_force.setter
    @enforce_parameter_types
    def max_brake_force(self: "Self", value: "float") -> None:
        self.wrapped.MaxBrakeForce = float(value) if value is not None else 0.0

    @property
    def oil_initial_temperature(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OilInitialTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_initial_temperature.setter
    @enforce_parameter_types
    def oil_initial_temperature(self: "Self", value: "float") -> None:
        self.wrapped.OilInitialTemperature = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_alpha(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingAlpha

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_alpha.setter
    @enforce_parameter_types
    def rayleigh_damping_alpha(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingAlpha = value

    @property
    def assembly_design(self: "Self") -> "_2530.RootAssembly":
        """mastapy._private.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def brake_force_input_values(self: "Self") -> "_98.ForceInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BrakeForceInputValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def drive_cycle_pid_control_settings(self: "Self") -> "_1623.PIDControlSettings":
        """mastapy._private.math_utility.control.PIDControlSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DriveCyclePIDControlSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case(self: "Self") -> "_6951.StaticLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def road_incline_input_values(self: "Self") -> "_97.AngleInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.AngleInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoadInclineInputValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def target_vehicle_speed(self: "Self") -> "_102.VelocityInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.VelocityInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TargetVehicleSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def supercharger_rotor_sets(
        self: "Self",
    ) -> "List[_7012.CylindricalGearSetLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerRotorSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_RootAssemblyLoadCase":
        """Cast to another type.

        Returns:
            _Cast_RootAssemblyLoadCase
        """
        return _Cast_RootAssemblyLoadCase(self)
