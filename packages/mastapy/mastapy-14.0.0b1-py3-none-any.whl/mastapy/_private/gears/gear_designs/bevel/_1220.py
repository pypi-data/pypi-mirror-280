"""BevelGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    utility,
)
from mastapy._private._internal.implicit import overridable, enum_with_selected_value
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.gear_designs.bevel import _1228
from mastapy._private.gears.gear_designs.agma_gleason_conical import _1233
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEVEL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "BevelGearSetDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1189, _1194
    from mastapy._private.math_utility import _1565
    from mastapy._private.gears.gear_designs.bevel import _1229, _1227
    from mastapy._private.gears import _357
    from mastapy._private.gears.gear_designs.zerol_bevel import _978
    from mastapy._private.gears.gear_designs.straight_bevel import _987
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _991
    from mastapy._private.gears.gear_designs.spiral_bevel import _995
    from mastapy._private.gears.gear_designs import _974, _972

    Self = TypeVar("Self", bound="BevelGearSetDesign")
    CastSelf = TypeVar("CastSelf", bound="BevelGearSetDesign._Cast_BevelGearSetDesign")


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelGearSetDesign:
    """Special nested class for casting BevelGearSetDesign to subclasses."""

    __parent__: "BevelGearSetDesign"

    @property
    def agma_gleason_conical_gear_set_design(
        self: "CastSelf",
    ) -> "_1233.AGMAGleasonConicalGearSetDesign":
        return self.__parent__._cast(_1233.AGMAGleasonConicalGearSetDesign)

    @property
    def conical_gear_set_design(self: "CastSelf") -> "_1194.ConicalGearSetDesign":
        from mastapy._private.gears.gear_designs.conical import _1194

        return self.__parent__._cast(_1194.ConicalGearSetDesign)

    @property
    def gear_set_design(self: "CastSelf") -> "_974.GearSetDesign":
        from mastapy._private.gears.gear_designs import _974

        return self.__parent__._cast(_974.GearSetDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_gear_set_design(self: "CastSelf") -> "_978.ZerolBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _978

        return self.__parent__._cast(_978.ZerolBevelGearSetDesign)

    @property
    def straight_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_987.StraightBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _987

        return self.__parent__._cast(_987.StraightBevelGearSetDesign)

    @property
    def straight_bevel_diff_gear_set_design(
        self: "CastSelf",
    ) -> "_991.StraightBevelDiffGearSetDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _991

        return self.__parent__._cast(_991.StraightBevelDiffGearSetDesign)

    @property
    def spiral_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_995.SpiralBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _995

        return self.__parent__._cast(_995.SpiralBevelGearSetDesign)

    @property
    def bevel_gear_set_design(self: "CastSelf") -> "BevelGearSetDesign":
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
class BevelGearSetDesign(_1233.AGMAGleasonConicalGearSetDesign):
    """BevelGearSetDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_GEAR_SET_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def allowable_scoring_index(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AllowableScoringIndex

        if temp is None:
            return 0.0

        return temp

    @allowable_scoring_index.setter
    @enforce_parameter_types
    def allowable_scoring_index(self: "Self", value: "float") -> None:
        self.wrapped.AllowableScoringIndex = float(value) if value is not None else 0.0

    @property
    def backlash_distribution_rule(self: "Self") -> "_1189.BacklashDistributionRule":
        """mastapy._private.gears.gear_designs.conical.BacklashDistributionRule"""
        temp = self.wrapped.BacklashDistributionRule

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.BacklashDistributionRule"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.conical._1189",
            "BacklashDistributionRule",
        )(value)

    @backlash_distribution_rule.setter
    @enforce_parameter_types
    def backlash_distribution_rule(
        self: "Self", value: "_1189.BacklashDistributionRule"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.BacklashDistributionRule"
        )
        self.wrapped.BacklashDistributionRule = value

    @property
    def backlash_used_for_tooth_thickness_calculation(
        self: "Self",
    ) -> "_1565.MaxMinMean":
        """mastapy._private.math_utility.MaxMinMean"""
        temp = self.wrapped.BacklashUsedForToothThicknessCalculation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.MaxMinMean")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.math_utility._1565", "MaxMinMean"
        )(value)

    @backlash_used_for_tooth_thickness_calculation.setter
    @enforce_parameter_types
    def backlash_used_for_tooth_thickness_calculation(
        self: "Self", value: "_1565.MaxMinMean"
    ) -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.MathUtility.MaxMinMean")
        self.wrapped.BacklashUsedForToothThicknessCalculation = value

    @property
    def basic_crown_gear_addendum_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicCrownGearAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_crown_gear_dedendum_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicCrownGearDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def circular_thickness_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.CircularThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @circular_thickness_factor.setter
    @enforce_parameter_types
    def circular_thickness_factor(self: "Self", value: "float") -> None:
        self.wrapped.CircularThicknessFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clearance

        if temp is None:
            return 0.0

        return temp

    @property
    def diametral_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def factor_of_safety_for_scoring(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.FactorOfSafetyForScoring

        if temp is None:
            return 0.0

        return temp

    @factor_of_safety_for_scoring.setter
    @enforce_parameter_types
    def factor_of_safety_for_scoring(self: "Self", value: "float") -> None:
        self.wrapped.FactorOfSafetyForScoring = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_circular_thickness_factor(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.IdealCircularThicknessFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ideal_circular_thickness_factor.setter
    @enforce_parameter_types
    def ideal_circular_thickness_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.IdealCircularThicknessFactor = value

    @property
    def ideal_pinion_mean_transverse_circular_thickness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.IdealPinionMeanTransverseCircularThickness

        if temp is None:
            return 0.0

        return temp

    @ideal_pinion_mean_transverse_circular_thickness.setter
    @enforce_parameter_types
    def ideal_pinion_mean_transverse_circular_thickness(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.IdealPinionMeanTransverseCircularThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_pinion_outer_transverse_circular_thickness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.IdealPinionOuterTransverseCircularThickness

        if temp is None:
            return 0.0

        return temp

    @ideal_pinion_outer_transverse_circular_thickness.setter
    @enforce_parameter_types
    def ideal_pinion_outer_transverse_circular_thickness(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.IdealPinionOuterTransverseCircularThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_wheel_finish_cutter_point_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.IdealWheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @ideal_wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def ideal_wheel_finish_cutter_point_width(self: "Self", value: "float") -> None:
        self.wrapped.IdealWheelFinishCutterPointWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_wheel_mean_slot_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.IdealWheelMeanSlotWidth

        if temp is None:
            return 0.0

        return temp

    @ideal_wheel_mean_slot_width.setter
    @enforce_parameter_types
    def ideal_wheel_mean_slot_width(self: "Self", value: "float") -> None:
        self.wrapped.IdealWheelMeanSlotWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def mean_addendum_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @mean_addendum_factor.setter
    @enforce_parameter_types
    def mean_addendum_factor(self: "Self", value: "float") -> None:
        self.wrapped.MeanAddendumFactor = float(value) if value is not None else 0.0

    @property
    def mean_circular_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_clearance_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @mean_clearance_factor.setter
    @enforce_parameter_types
    def mean_clearance_factor(self: "Self", value: "float") -> None:
        self.wrapped.MeanClearanceFactor = float(value) if value is not None else 0.0

    @property
    def mean_depth_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanDepthFactor

        if temp is None:
            return 0.0

        return temp

    @mean_depth_factor.setter
    @enforce_parameter_types
    def mean_depth_factor(self: "Self", value: "float") -> None:
        self.wrapped.MeanDepthFactor = float(value) if value is not None else 0.0

    @property
    def mean_diametral_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDiametralPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_whole_depth(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_working_depth(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(
        self: "Self",
    ) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def outer_wheel_addendum(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OuterWheelAddendum

        if temp is None:
            return 0.0

        return temp

    @outer_wheel_addendum.setter
    @enforce_parameter_types
    def outer_wheel_addendum(self: "Self", value: "float") -> None:
        self.wrapped.OuterWheelAddendum = float(value) if value is not None else 0.0

    @property
    def outer_whole_depth(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OuterWholeDepth

        if temp is None:
            return 0.0

        return temp

    @outer_whole_depth.setter
    @enforce_parameter_types
    def outer_whole_depth(self: "Self", value: "float") -> None:
        self.wrapped.OuterWholeDepth = float(value) if value is not None else 0.0

    @property
    def outer_working_depth(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OuterWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @outer_working_depth.setter
    @enforce_parameter_types
    def outer_working_depth(self: "Self", value: "float") -> None:
        self.wrapped.OuterWorkingDepth = float(value) if value is not None else 0.0

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
    def profile_shift_coefficient(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def round_cutter_specifications(
        self: "Self",
    ) -> "_1229.WheelFinishCutterPointWidthRestrictionMethod":
        """mastapy._private.gears.gear_designs.bevel.WheelFinishCutterPointWidthRestrictionMethod"""
        temp = self.wrapped.RoundCutterSpecifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.WheelFinishCutterPointWidthRestrictionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.bevel._1229",
            "WheelFinishCutterPointWidthRestrictionMethod",
        )(value)

    @round_cutter_specifications.setter
    @enforce_parameter_types
    def round_cutter_specifications(
        self: "Self", value: "_1229.WheelFinishCutterPointWidthRestrictionMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.WheelFinishCutterPointWidthRestrictionMethod",
        )
        self.wrapped.RoundCutterSpecifications = value

    @property
    def specified_pinion_dedendum_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecifiedPinionDedendumAngle

        if temp is None:
            return 0.0

        return temp

    @specified_pinion_dedendum_angle.setter
    @enforce_parameter_types
    def specified_pinion_dedendum_angle(self: "Self", value: "float") -> None:
        self.wrapped.SpecifiedPinionDedendumAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_wheel_dedendum_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecifiedWheelDedendumAngle

        if temp is None:
            return 0.0

        return temp

    @specified_wheel_dedendum_angle.setter
    @enforce_parameter_types
    def specified_wheel_dedendum_angle(self: "Self", value: "float") -> None:
        self.wrapped.SpecifiedWheelDedendumAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def strength_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @strength_factor.setter
    @enforce_parameter_types
    def strength_factor(self: "Self", value: "float") -> None:
        self.wrapped.StrengthFactor = float(value) if value is not None else 0.0

    @property
    def thickness_modification_coefficient_theoretical(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThicknessModificationCoefficientTheoretical

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_proportions_input_method(
        self: "Self",
    ) -> "_1227.ToothProportionsInputMethod":
        """mastapy._private.gears.gear_designs.bevel.ToothProportionsInputMethod"""
        temp = self.wrapped.ToothProportionsInputMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Bevel.ToothProportionsInputMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.bevel._1227",
            "ToothProportionsInputMethod",
        )(value)

    @tooth_proportions_input_method.setter
    @enforce_parameter_types
    def tooth_proportions_input_method(
        self: "Self", value: "_1227.ToothProportionsInputMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Bevel.ToothProportionsInputMethod"
        )
        self.wrapped.ToothProportionsInputMethod = value

    @property
    def tooth_taper_root_line_tilt_method(
        self: "Self",
    ) -> "_357.SpiralBevelRootLineTilt":
        """mastapy._private.gears.SpiralBevelRootLineTilt"""
        temp = self.wrapped.ToothTaperRootLineTiltMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.SpiralBevelRootLineTilt"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears._357", "SpiralBevelRootLineTilt"
        )(value)

    @tooth_taper_root_line_tilt_method.setter
    @enforce_parameter_types
    def tooth_taper_root_line_tilt_method(
        self: "Self", value: "_357.SpiralBevelRootLineTilt"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.SpiralBevelRootLineTilt"
        )
        self.wrapped.ToothTaperRootLineTiltMethod = value

    @property
    def tooth_thickness_specification_method(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ToothThicknessSpecificationMethod":
        """EnumWithSelectedValue[mastapy._private.gears.gear_designs.bevel.ToothThicknessSpecificationMethod]"""
        temp = self.wrapped.ToothThicknessSpecificationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ToothThicknessSpecificationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @tooth_thickness_specification_method.setter
    @enforce_parameter_types
    def tooth_thickness_specification_method(
        self: "Self", value: "_1228.ToothThicknessSpecificationMethod"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ToothThicknessSpecificationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToothThicknessSpecificationMethod = value

    @property
    def use_recommended_tooth_proportions(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseRecommendedToothProportions

        if temp is None:
            return False

        return temp

    @use_recommended_tooth_proportions.setter
    @enforce_parameter_types
    def use_recommended_tooth_proportions(self: "Self", value: "bool") -> None:
        self.wrapped.UseRecommendedToothProportions = (
            bool(value) if value is not None else False
        )

    @property
    def wheel_addendum_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_addendum_multiplier(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelAddendumMultiplier

        if temp is None:
            return 0.0

        return temp

    @wheel_addendum_multiplier.setter
    @enforce_parameter_types
    def wheel_addendum_multiplier(self: "Self", value: "float") -> None:
        self.wrapped.WheelAddendumMultiplier = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_finish_cutter_point_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def wheel_finish_cutter_point_width(self: "Self", value: "float") -> None:
        self.wrapped.WheelFinishCutterPointWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_inner_spiral_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def whole_depth_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WholeDepthFactor

        if temp is None:
            return 0.0

        return temp

    @whole_depth_factor.setter
    @enforce_parameter_types
    def whole_depth_factor(self: "Self", value: "float") -> None:
        self.wrapped.WholeDepthFactor = float(value) if value is not None else 0.0

    @property
    def working_depth_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WorkingDepthFactor

        if temp is None:
            return 0.0

        return temp

    @working_depth_factor.setter
    @enforce_parameter_types
    def working_depth_factor(self: "Self", value: "float") -> None:
        self.wrapped.WorkingDepthFactor = float(value) if value is not None else 0.0

    @property
    def mean_spiral_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @mean_spiral_angle.setter
    @enforce_parameter_types
    def mean_spiral_angle(self: "Self", value: "float") -> None:
        self.wrapped.MeanSpiralAngle = float(value) if value is not None else 0.0

    @property
    def transverse_circular_thickness_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TransverseCircularThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @transverse_circular_thickness_factor.setter
    @enforce_parameter_types
    def transverse_circular_thickness_factor(self: "Self", value: "float") -> None:
        self.wrapped.TransverseCircularThicknessFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: "Self") -> "_Cast_BevelGearSetDesign":
        """Cast to another type.

        Returns:
            _Cast_BevelGearSetDesign
        """
        return _Cast_BevelGearSetDesign(self)
