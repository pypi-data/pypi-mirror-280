"""PointLoadLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar
from enum import Enum

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import overridable, enum_with_selected_value
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.system_model.analyses_and_results.static_loads import _7130
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_POINT_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PointLoadLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.nodal_analysis.varying_input_components import _98, _99
    from mastapy._private.system_model.part_model import _2527
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7086,
        _7073,
        _6984,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="PointLoadLoadCase")
    CastSelf = TypeVar("CastSelf", bound="PointLoadLoadCase._Cast_PointLoadLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PointLoadLoadCase:
    """Special nested class for casting PointLoadLoadCase to subclasses."""

    __parent__: "PointLoadLoadCase"

    @property
    def virtual_component_load_case(
        self: "CastSelf",
    ) -> "_7130.VirtualComponentLoadCase":
        return self.__parent__._cast(_7130.VirtualComponentLoadCase)

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7073.MountableComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7073,
        )

        return self.__parent__._cast(_7073.MountableComponentLoadCase)

    @property
    def component_load_case(self: "CastSelf") -> "_6984.ComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6984,
        )

        return self.__parent__._cast(_6984.ComponentLoadCase)

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
    def point_load_load_case(self: "CastSelf") -> "PointLoadLoadCase":
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
class PointLoadLoadCase(_7130.VirtualComponentLoadCase):
    """PointLoadLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _POINT_LOAD_LOAD_CASE

    class ForceSpecification(Enum):
        """ForceSpecification is a nested enum."""

        @classmethod
        def type_(cls) -> "Type":
            return _POINT_LOAD_LOAD_CASE.ForceSpecification

        RADIAL_TANGENTIAL = 0
        FORCE_X_FORCE_Y = 1

    def __enum_setattr(self: "Self", attr: str, value: "Any") -> None:
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: "Self", attr: str) -> None:
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    ForceSpecification.__setattr__ = __enum_setattr
    ForceSpecification.__delattr__ = __enum_delattr

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle_of_radial_force(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AngleOfRadialForce

        if temp is None:
            return 0.0

        return temp

    @angle_of_radial_force.setter
    @enforce_parameter_types
    def angle_of_radial_force(self: "Self", value: "float") -> None:
        self.wrapped.AngleOfRadialForce = float(value) if value is not None else 0.0

    @property
    def displacement_x(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DisplacementX

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement_x.setter
    @enforce_parameter_types
    def displacement_x(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DisplacementX = value

    @property
    def displacement_y(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DisplacementY

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement_y.setter
    @enforce_parameter_types
    def displacement_y(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DisplacementY = value

    @property
    def displacement_z(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DisplacementZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement_z.setter
    @enforce_parameter_types
    def displacement_z(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DisplacementZ = value

    @property
    def force_specification_options(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification":
        """EnumWithSelectedValue[mastapy._private.system_model.analyses_and_results.static_loads.PointLoadLoadCase.ForceSpecification]"""
        temp = self.wrapped.ForceSpecificationOptions

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @force_specification_options.setter
    @enforce_parameter_types
    def force_specification_options(
        self: "Self", value: "PointLoadLoadCase.ForceSpecification"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ForceSpecificationOptions = value

    @property
    def magnitude_radial_force(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MagnitudeRadialForce

        if temp is None:
            return 0.0

        return temp

    @magnitude_radial_force.setter
    @enforce_parameter_types
    def magnitude_radial_force(self: "Self", value: "float") -> None:
        self.wrapped.MagnitudeRadialForce = float(value) if value is not None else 0.0

    @property
    def radial_load(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RadialLoad

        if temp is None:
            return 0.0

        return temp

    @radial_load.setter
    @enforce_parameter_types
    def radial_load(self: "Self", value: "float") -> None:
        self.wrapped.RadialLoad = float(value) if value is not None else 0.0

    @property
    def tangential_load(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TangentialLoad

        if temp is None:
            return 0.0

        return temp

    @tangential_load.setter
    @enforce_parameter_types
    def tangential_load(self: "Self", value: "float") -> None:
        self.wrapped.TangentialLoad = float(value) if value is not None else 0.0

    @property
    def twist_theta_x(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwistThetaX

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @twist_theta_x.setter
    @enforce_parameter_types
    def twist_theta_x(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwistThetaX = value

    @property
    def twist_theta_y(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwistThetaY

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @twist_theta_y.setter
    @enforce_parameter_types
    def twist_theta_y(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwistThetaY = value

    @property
    def twist_theta_z(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwistThetaZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @twist_theta_z.setter
    @enforce_parameter_types
    def twist_theta_z(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwistThetaZ = value

    @property
    def axial_load(self: "Self") -> "_98.ForceInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: "Self") -> "_2527.PointLoad":
        """mastapy._private.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_x(self: "Self") -> "_98.ForceInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceX

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_y(self: "Self") -> "_98.ForceInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def moment_x(self: "Self") -> "_99.MomentInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.MomentInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentX

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def moment_y(self: "Self") -> "_99.MomentInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.MomentInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def moment_z(self: "Self") -> "_99.MomentInputComponent":
        """mastapy._private.nodal_analysis.varying_input_components.MomentInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentZ

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: "Self",
    ) -> "_7086.PointLoadHarmonicLoadData":
        """mastapy._private.system_model.analyses_and_results.static_loads.PointLoadHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_PointLoadLoadCase":
        """Cast to another type.

        Returns:
            _Cast_PointLoadLoadCase
        """
        return _Cast_PointLoadLoadCase(self)
