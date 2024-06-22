"""SplineJointDesign"""
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
from mastapy._private._internal.implicit import enum_with_selected_value, overridable
from mastapy._private.detailed_rigid_connectors.splines import _1440, _1463
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.detailed_rigid_connectors import _1433
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SplineJointDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines import (
        _1452,
        _1451,
        _1459,
        _1455,
        _1460,
        _1436,
        _1439,
        _1443,
        _1446,
        _1447,
        _1454,
        _1466,
    )

    Self = TypeVar("Self", bound="SplineJointDesign")
    CastSelf = TypeVar("CastSelf", bound="SplineJointDesign._Cast_SplineJointDesign")


__docformat__ = "restructuredtext en"
__all__ = ("SplineJointDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SplineJointDesign:
    """Special nested class for casting SplineJointDesign to subclasses."""

    __parent__: "SplineJointDesign"

    @property
    def detailed_rigid_connector_design(
        self: "CastSelf",
    ) -> "_1433.DetailedRigidConnectorDesign":
        return self.__parent__._cast(_1433.DetailedRigidConnectorDesign)

    @property
    def custom_spline_joint_design(self: "CastSelf") -> "_1436.CustomSplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1436

        return self.__parent__._cast(_1436.CustomSplineJointDesign)

    @property
    def din5480_spline_joint_design(
        self: "CastSelf",
    ) -> "_1439.DIN5480SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1439

        return self.__parent__._cast(_1439.DIN5480SplineJointDesign)

    @property
    def gbt3478_spline_joint_design(
        self: "CastSelf",
    ) -> "_1443.GBT3478SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1443

        return self.__parent__._cast(_1443.GBT3478SplineJointDesign)

    @property
    def iso4156_spline_joint_design(
        self: "CastSelf",
    ) -> "_1446.ISO4156SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1446

        return self.__parent__._cast(_1446.ISO4156SplineJointDesign)

    @property
    def jisb1603_spline_joint_design(
        self: "CastSelf",
    ) -> "_1447.JISB1603SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1447

        return self.__parent__._cast(_1447.JISB1603SplineJointDesign)

    @property
    def sae_spline_joint_design(self: "CastSelf") -> "_1454.SAESplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1454

        return self.__parent__._cast(_1454.SAESplineJointDesign)

    @property
    def standard_spline_joint_design(
        self: "CastSelf",
    ) -> "_1466.StandardSplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1466

        return self.__parent__._cast(_1466.StandardSplineJointDesign)

    @property
    def spline_joint_design(self: "CastSelf") -> "SplineJointDesign":
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
class SplineJointDesign(_1433.DetailedRigidConnectorDesign):
    """SplineJointDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPLINE_JOINT_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def base_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def base_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_space_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_tooth_thickness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def before_running_in(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.BeforeRunningIn

        if temp is None:
            return False

        return temp

    @before_running_in.setter
    @enforce_parameter_types
    def before_running_in(self: "Self", value: "bool") -> None:
        self.wrapped.BeforeRunningIn = bool(value) if value is not None else False

    @property
    def circular_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def designation(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Designation

        if temp is None:
            return ""

        return temp

    @property
    def diametral_pitch(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch.setter
    @enforce_parameter_types
    def diametral_pitch(self: "Self", value: "float") -> None:
        self.wrapped.DiametralPitch = float(value) if value is not None else 0.0

    @property
    def dudley_maximum_effective_length(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DudleyMaximumEffectiveLength

        if temp is None:
            return 0.0

        return temp

    @property
    def dudley_maximum_effective_length_option(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption":
        """EnumWithSelectedValue[mastapy._private.detailed_rigid_connectors.splines.DudleyEffectiveLengthApproximationOption]"""
        temp = self.wrapped.DudleyMaximumEffectiveLengthOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @dudley_maximum_effective_length_option.setter
    @enforce_parameter_types
    def dudley_maximum_effective_length_option(
        self: "Self", value: "_1440.DudleyEffectiveLengthApproximationOption"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DudleyMaximumEffectiveLengthOption = value

    @property
    def fatigue_life_factor_type(self: "Self") -> "_1452.SAEFatigueLifeFactorTypes":
        """mastapy._private.detailed_rigid_connectors.splines.SAEFatigueLifeFactorTypes"""
        temp = self.wrapped.FatigueLifeFactorType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.DetailedRigidConnectors.Splines.SAEFatigueLifeFactorTypes",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.detailed_rigid_connectors.splines._1452",
            "SAEFatigueLifeFactorTypes",
        )(value)

    @fatigue_life_factor_type.setter
    @enforce_parameter_types
    def fatigue_life_factor_type(
        self: "Self", value: "_1452.SAEFatigueLifeFactorTypes"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.DetailedRigidConnectors.Splines.SAEFatigueLifeFactorTypes",
        )
        self.wrapped.FatigueLifeFactorType = value

    @property
    def minimum_effective_clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def module(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    @enforce_parameter_types
    def module(self: "Self", value: "float") -> None:
        self.wrapped.Module = float(value) if value is not None else 0.0

    @property
    def number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def number_of_teeth_in_contact(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @number_of_teeth_in_contact.setter
    @enforce_parameter_types
    def number_of_teeth_in_contact(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NumberOfTeethInContact = value

    @property
    def pitch_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    @enforce_parameter_types
    def pressure_angle(self: "Self", value: "float") -> None:
        self.wrapped.PressureAngle = float(value) if value is not None else 0.0

    @property
    def root_type(self: "Self") -> "_1451.RootTypes":
        """mastapy._private.detailed_rigid_connectors.splines.RootTypes"""
        temp = self.wrapped.RootType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.RootTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.detailed_rigid_connectors.splines._1451", "RootTypes"
        )(value)

    @root_type.setter
    @enforce_parameter_types
    def root_type(self: "Self", value: "_1451.RootTypes") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.RootTypes"
        )
        self.wrapped.RootType = value

    @property
    def spline_fixture_type(self: "Self") -> "_1459.SplineFixtureTypes":
        """mastapy._private.detailed_rigid_connectors.splines.SplineFixtureTypes"""
        temp = self.wrapped.SplineFixtureType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.SplineFixtureTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.detailed_rigid_connectors.splines._1459",
            "SplineFixtureTypes",
        )(value)

    @spline_fixture_type.setter
    @enforce_parameter_types
    def spline_fixture_type(self: "Self", value: "_1459.SplineFixtureTypes") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.SplineFixtureTypes"
        )
        self.wrapped.SplineFixtureType = value

    @property
    def spline_rating_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes":
        """EnumWithSelectedValue[mastapy._private.detailed_rigid_connectors.splines.SplineRatingTypes]"""
        temp = self.wrapped.SplineRatingType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @spline_rating_type.setter
    @enforce_parameter_types
    def spline_rating_type(self: "Self", value: "_1463.SplineRatingTypes") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SplineRatingType = value

    @property
    def torque_cycles(self: "Self") -> "_1455.SAETorqueCycles":
        """mastapy._private.detailed_rigid_connectors.splines.SAETorqueCycles"""
        temp = self.wrapped.TorqueCycles

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.SAETorqueCycles"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.detailed_rigid_connectors.splines._1455",
            "SAETorqueCycles",
        )(value)

    @torque_cycles.setter
    @enforce_parameter_types
    def torque_cycles(self: "Self", value: "_1455.SAETorqueCycles") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.SAETorqueCycles"
        )
        self.wrapped.TorqueCycles = value

    @property
    def total_crowning(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TotalCrowning

        if temp is None:
            return 0.0

        return temp

    @total_crowning.setter
    @enforce_parameter_types
    def total_crowning(self: "Self", value: "float") -> None:
        self.wrapped.TotalCrowning = float(value) if value is not None else 0.0

    @property
    def use_sae_stress_concentration_factor(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSAEStressConcentrationFactor

        if temp is None:
            return False

        return temp

    @use_sae_stress_concentration_factor.setter
    @enforce_parameter_types
    def use_sae_stress_concentration_factor(self: "Self", value: "bool") -> None:
        self.wrapped.UseSAEStressConcentrationFactor = (
            bool(value) if value is not None else False
        )

    @property
    def use_user_input_allowable_stresses(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseUserInputAllowableStresses

        if temp is None:
            return False

        return temp

    @use_user_input_allowable_stresses.setter
    @enforce_parameter_types
    def use_user_input_allowable_stresses(self: "Self", value: "bool") -> None:
        self.wrapped.UseUserInputAllowableStresses = (
            bool(value) if value is not None else False
        )

    @property
    def user_specified_external_teeth_stress_concentration_factor(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedExternalTeethStressConcentrationFactor

        if temp is None:
            return 0.0

        return temp

    @user_specified_external_teeth_stress_concentration_factor.setter
    @enforce_parameter_types
    def user_specified_external_teeth_stress_concentration_factor(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.UserSpecifiedExternalTeethStressConcentrationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def user_specified_internal_teeth_stress_concentration_factor(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedInternalTeethStressConcentrationFactor

        if temp is None:
            return 0.0

        return temp

    @user_specified_internal_teeth_stress_concentration_factor.setter
    @enforce_parameter_types
    def user_specified_internal_teeth_stress_concentration_factor(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.UserSpecifiedInternalTeethStressConcentrationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def wall_thickness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WallThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def with_crown(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.WithCrown

        if temp is None:
            return False

        return temp

    @with_crown.setter
    @enforce_parameter_types
    def with_crown(self: "Self", value: "bool") -> None:
        self.wrapped.WithCrown = bool(value) if value is not None else False

    @property
    def external_half(self: "Self") -> "_1460.SplineHalfDesign":
        """mastapy._private.detailed_rigid_connectors.splines.SplineHalfDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalHalf

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def internal_half(self: "Self") -> "_1460.SplineHalfDesign":
        """mastapy._private.detailed_rigid_connectors.splines.SplineHalfDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalHalf

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SplineJointDesign":
        """Cast to another type.

        Returns:
            _Cast_SplineJointDesign
        """
        return _Cast_SplineJointDesign(self)
