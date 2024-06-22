"""CylindricalGearMicroGeometryBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.analysis import _1259
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMicroGeometryBase",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.utility.report import _1834
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1126,
        _1141,
        _1132,
        _1136,
    )
    from mastapy._private.gears.gear_designs.cylindrical import _1042, _1055
    from mastapy._private.gears.analysis import _1256, _1253

    Self = TypeVar("Self", bound="CylindricalGearMicroGeometryBase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometryBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMicroGeometryBase:
    """Special nested class for casting CylindricalGearMicroGeometryBase to subclasses."""

    __parent__: "CylindricalGearMicroGeometryBase"

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        return self.__parent__._cast(_1259.GearImplementationDetail)

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def cylindrical_gear_micro_geometry(
        self: "CastSelf",
    ) -> "_1132.CylindricalGearMicroGeometry":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1132

        return self.__parent__._cast(_1132.CylindricalGearMicroGeometry)

    @property
    def cylindrical_gear_micro_geometry_per_tooth(
        self: "CastSelf",
    ) -> "_1136.CylindricalGearMicroGeometryPerTooth":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1136

        return self.__parent__._cast(_1136.CylindricalGearMicroGeometryPerTooth)

    @property
    def cylindrical_gear_micro_geometry_base(
        self: "CastSelf",
    ) -> "CylindricalGearMicroGeometryBase":
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
class CylindricalGearMicroGeometryBase(_1259.GearImplementationDetail):
    """CylindricalGearMicroGeometryBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @adjust_micro_geometry_for_analysis_when_including_pitch_errors.setter
    @enforce_parameter_types
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors = value

    @property
    def comment(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: "Self", value: "str") -> None:
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def lead_form_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_slope_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadSlopeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_total_nominal_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_total_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_control_point_is_user_specified(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ProfileControlPointIsUserSpecified

        if temp is None:
            return False

        return temp

    @profile_control_point_is_user_specified.setter
    @enforce_parameter_types
    def profile_control_point_is_user_specified(self: "Self", value: "bool") -> None:
        self.wrapped.ProfileControlPointIsUserSpecified = (
            bool(value) if value is not None else False
        )

    @property
    def profile_form_10_percent_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileForm10PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_50_percent_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileForm50PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_90_percent_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileForm90PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_total_nominal_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_total_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def use_same_micro_geometry_on_both_flanks(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSameMicroGeometryOnBothFlanks

        if temp is None:
            return False

        return temp

    @use_same_micro_geometry_on_both_flanks.setter
    @enforce_parameter_types
    def use_same_micro_geometry_on_both_flanks(self: "Self", value: "bool") -> None:
        self.wrapped.UseSameMicroGeometryOnBothFlanks = (
            bool(value) if value is not None else False
        )

    @property
    def common_micro_geometry_of_left_flank(
        self: "Self",
    ) -> "_1126.CylindricalGearCommonFlankMicroGeometry":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearCommonFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommonMicroGeometryOfLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def common_micro_geometry_of_right_flank(
        self: "Self",
    ) -> "_1126.CylindricalGearCommonFlankMicroGeometry":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearCommonFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommonMicroGeometryOfRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear(self: "Self") -> "_1042.CylindricalGearDesign":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_control_point(
        self: "Self",
    ) -> "_1055.CylindricalGearProfileMeasurement":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileControlPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def common_micro_geometries_of_flanks(
        self: "Self",
    ) -> "List[_1126.CylindricalGearCommonFlankMicroGeometry]":
        """List[mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearCommonFlankMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommonMicroGeometriesOfFlanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tooth_micro_geometries(
        self: "Self",
    ) -> "List[_1141.CylindricalGearToothMicroGeometry]":
        """List[mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearToothMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMicroGeometryBase":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMicroGeometryBase
        """
        return _Cast_CylindricalGearMicroGeometryBase(self)
