"""CylindricalGearMicroGeometrySettingsItem"""
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
from mastapy._private.gears import _329
from mastapy._private.gears.micro_geometry import _584, _585, _586, _587
from mastapy._private.utility.databases import _1879
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearMicroGeometrySettingsItem",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.micro_geometry import _582, _588, _589, _591, _592
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1156
    from mastapy._private.gears.gear_designs.cylindrical import (
        _1075,
        _1101,
        _1091,
        _1092,
    )

    Self = TypeVar("Self", bound="CylindricalGearMicroGeometrySettingsItem")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearMicroGeometrySettingsItem._Cast_CylindricalGearMicroGeometrySettingsItem",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometrySettingsItem",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMicroGeometrySettingsItem:
    """Special nested class for casting CylindricalGearMicroGeometrySettingsItem to subclasses."""

    __parent__: "CylindricalGearMicroGeometrySettingsItem"

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def cylindrical_gear_micro_geometry_settings_item(
        self: "CastSelf",
    ) -> "CylindricalGearMicroGeometrySettingsItem":
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
class CylindricalGearMicroGeometrySettingsItem(_1879.NamedDatabaseItem):
    """CylindricalGearMicroGeometrySettingsItem

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_ITEM

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def add_flank_side_labels_to_micro_geometry_lead_tolerance_charts(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = self.wrapped.AddFlankSideLabelsToMicroGeometryLeadToleranceCharts

        if temp is None:
            return False

        return temp

    @add_flank_side_labels_to_micro_geometry_lead_tolerance_charts.setter
    @enforce_parameter_types
    def add_flank_side_labels_to_micro_geometry_lead_tolerance_charts(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.AddFlankSideLabelsToMicroGeometryLeadToleranceCharts = (
            bool(value) if value is not None else False
        )

    @property
    def adjust_micro_geometry_for_analysis_by_default_when_including_pitch_errors(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.AdjustMicroGeometryForAnalysisByDefaultWhenIncludingPitchErrors
        )

        if temp is None:
            return False

        return temp

    @adjust_micro_geometry_for_analysis_by_default_when_including_pitch_errors.setter
    @enforce_parameter_types
    def adjust_micro_geometry_for_analysis_by_default_when_including_pitch_errors(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.AdjustMicroGeometryForAnalysisByDefaultWhenIncludingPitchErrors = (
            bool(value) if value is not None else False
        )

    @property
    def centre_tolerance_charts_at_maximum_fullness(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.CentreToleranceChartsAtMaximumFullness

        if temp is None:
            return False

        return temp

    @centre_tolerance_charts_at_maximum_fullness.setter
    @enforce_parameter_types
    def centre_tolerance_charts_at_maximum_fullness(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.CentreToleranceChartsAtMaximumFullness = (
            bool(value) if value is not None else False
        )

    @property
    def crop_face_width_axis_of_micro_geometry_lead_tolerance_charts(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = self.wrapped.CropFaceWidthAxisOfMicroGeometryLeadToleranceCharts

        if temp is None:
            return False

        return temp

    @crop_face_width_axis_of_micro_geometry_lead_tolerance_charts.setter
    @enforce_parameter_types
    def crop_face_width_axis_of_micro_geometry_lead_tolerance_charts(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.CropFaceWidthAxisOfMicroGeometryLeadToleranceCharts = (
            bool(value) if value is not None else False
        )

    @property
    def crop_profile_measurement_axis_of_micro_geometry_profile_tolerance_charts(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.CropProfileMeasurementAxisOfMicroGeometryProfileToleranceCharts
        )

        if temp is None:
            return False

        return temp

    @crop_profile_measurement_axis_of_micro_geometry_profile_tolerance_charts.setter
    @enforce_parameter_types
    def crop_profile_measurement_axis_of_micro_geometry_profile_tolerance_charts(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.CropProfileMeasurementAxisOfMicroGeometryProfileToleranceCharts = (
            bool(value) if value is not None else False
        )

    @property
    def default_coefficient_of_friction_method_for_ltca(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CoefficientOfFrictionCalculationMethod":
        """EnumWithSelectedValue[mastapy._private.gears.CoefficientOfFrictionCalculationMethod]"""
        temp = self.wrapped.DefaultCoefficientOfFrictionMethodForLTCA

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CoefficientOfFrictionCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_coefficient_of_friction_method_for_ltca.setter
    @enforce_parameter_types
    def default_coefficient_of_friction_method_for_ltca(
        self: "Self", value: "_329.CoefficientOfFrictionCalculationMethod"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CoefficientOfFrictionCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultCoefficientOfFrictionMethodForLTCA = value

    @property
    def default_flank_side_with_zero_face_width(self: "Self") -> "_582.FlankSide":
        """mastapy._private.gears.micro_geometry.FlankSide"""
        temp = self.wrapped.DefaultFlankSideWithZeroFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.MicroGeometry.FlankSide"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._582", "FlankSide"
        )(value)

    @default_flank_side_with_zero_face_width.setter
    @enforce_parameter_types
    def default_flank_side_with_zero_face_width(
        self: "Self", value: "_582.FlankSide"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.MicroGeometry.FlankSide"
        )
        self.wrapped.DefaultFlankSideWithZeroFaceWidth = value

    @property
    def default_location_of_evaluation_lower_limit(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfEvaluationLowerLimit]"""
        temp = self.wrapped.DefaultLocationOfEvaluationLowerLimit

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_location_of_evaluation_lower_limit.setter
    @enforce_parameter_types
    def default_location_of_evaluation_lower_limit(
        self: "Self", value: "_584.LocationOfEvaluationLowerLimit"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfEvaluationLowerLimit = value

    @property
    def default_location_of_evaluation_upper_limit(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfEvaluationUpperLimit]"""
        temp = self.wrapped.DefaultLocationOfEvaluationUpperLimit

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_location_of_evaluation_upper_limit.setter
    @enforce_parameter_types
    def default_location_of_evaluation_upper_limit(
        self: "Self", value: "_585.LocationOfEvaluationUpperLimit"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfEvaluationUpperLimit = value

    @property
    def default_location_of_root_relief_evaluation(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfRootReliefEvaluation]"""
        temp = self.wrapped.DefaultLocationOfRootReliefEvaluation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_location_of_root_relief_evaluation.setter
    @enforce_parameter_types
    def default_location_of_root_relief_evaluation(
        self: "Self", value: "_586.LocationOfRootReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfRootReliefEvaluation = value

    @property
    def default_location_of_root_relief_start(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfRootReliefEvaluation]"""
        temp = self.wrapped.DefaultLocationOfRootReliefStart

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_location_of_root_relief_start.setter
    @enforce_parameter_types
    def default_location_of_root_relief_start(
        self: "Self", value: "_586.LocationOfRootReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfRootReliefStart = value

    @property
    def default_location_of_tip_relief_evaluation(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation":
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfTipReliefEvaluation]"""
        temp = self.wrapped.DefaultLocationOfTipReliefEvaluation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_location_of_tip_relief_evaluation.setter
    @enforce_parameter_types
    def default_location_of_tip_relief_evaluation(
        self: "Self", value: "_587.LocationOfTipReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfTipReliefEvaluation = value

    @property
    def default_location_of_tip_relief_start(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation":
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfTipReliefEvaluation]"""
        temp = self.wrapped.DefaultLocationOfTipReliefStart

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_location_of_tip_relief_start.setter
    @enforce_parameter_types
    def default_location_of_tip_relief_start(
        self: "Self", value: "_587.LocationOfTipReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfTipReliefStart = value

    @property
    def default_micro_geometry_lead_tolerance_chart_view(
        self: "Self",
    ) -> "_1156.MicroGeometryLeadToleranceChartView":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.MicroGeometryLeadToleranceChartView"""
        temp = self.wrapped.DefaultMicroGeometryLeadToleranceChartView

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.MicroGeometryLeadToleranceChartView",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1156",
            "MicroGeometryLeadToleranceChartView",
        )(value)

    @default_micro_geometry_lead_tolerance_chart_view.setter
    @enforce_parameter_types
    def default_micro_geometry_lead_tolerance_chart_view(
        self: "Self", value: "_1156.MicroGeometryLeadToleranceChartView"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.MicroGeometryLeadToleranceChartView",
        )
        self.wrapped.DefaultMicroGeometryLeadToleranceChartView = value

    @property
    def default_scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(
        self: "Self",
    ) -> "_1075.DoubleAxisScaleAndRange":
        """mastapy._private.gears.gear_designs.cylindrical.DoubleAxisScaleAndRange"""
        temp = (
            self.wrapped.DefaultScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DoubleAxisScaleAndRange"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1075",
            "DoubleAxisScaleAndRange",
        )(value)

    @default_scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts.setter
    @enforce_parameter_types
    def default_scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(
        self: "Self", value: "_1075.DoubleAxisScaleAndRange"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DoubleAxisScaleAndRange"
        )
        self.wrapped.DefaultScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts = (
            value
        )

    @property
    def draw_micro_geometry_charts_with_face_width_axis_oriented_to_view_through_air(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.DrawMicroGeometryChartsWithFaceWidthAxisOrientedToViewThroughAir
        )

        if temp is None:
            return False

        return temp

    @draw_micro_geometry_charts_with_face_width_axis_oriented_to_view_through_air.setter
    @enforce_parameter_types
    def draw_micro_geometry_charts_with_face_width_axis_oriented_to_view_through_air(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.DrawMicroGeometryChartsWithFaceWidthAxisOrientedToViewThroughAir = (
            bool(value) if value is not None else False
        )

    @property
    def draw_micro_geometry_profile_chart_with_relief_on_horizontal_axis(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = self.wrapped.DrawMicroGeometryProfileChartWithReliefOnHorizontalAxis

        if temp is None:
            return False

        return temp

    @draw_micro_geometry_profile_chart_with_relief_on_horizontal_axis.setter
    @enforce_parameter_types
    def draw_micro_geometry_profile_chart_with_relief_on_horizontal_axis(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.DrawMicroGeometryProfileChartWithReliefOnHorizontalAxis = (
            bool(value) if value is not None else False
        )

    @property
    def ltca_root_stress_surface_chart_option(
        self: "Self",
    ) -> "_1101.RootStressSurfaceChartOption":
        """mastapy._private.gears.gear_designs.cylindrical.RootStressSurfaceChartOption"""
        temp = self.wrapped.LTCARootStressSurfaceChartOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.RootStressSurfaceChartOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1101",
            "RootStressSurfaceChartOption",
        )(value)

    @ltca_root_stress_surface_chart_option.setter
    @enforce_parameter_types
    def ltca_root_stress_surface_chart_option(
        self: "Self", value: "_1101.RootStressSurfaceChartOption"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.RootStressSurfaceChartOption",
        )
        self.wrapped.LTCARootStressSurfaceChartOption = value

    @property
    def main_profile_modification_ends_at_the_start_of_root_relief_by_default(
        self: "Self",
    ) -> "_588.MainProfileReliefEndsAtTheStartOfRootReliefOption":
        """mastapy._private.gears.micro_geometry.MainProfileReliefEndsAtTheStartOfRootReliefOption"""
        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfRootReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._588",
            "MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )(value)

    @main_profile_modification_ends_at_the_start_of_root_relief_by_default.setter
    @enforce_parameter_types
    def main_profile_modification_ends_at_the_start_of_root_relief_by_default(
        self: "Self", value: "_588.MainProfileReliefEndsAtTheStartOfRootReliefOption"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )
        self.wrapped.MainProfileModificationEndsAtTheStartOfRootReliefByDefault = value

    @property
    def main_profile_modification_ends_at_the_start_of_tip_relief_by_default(
        self: "Self",
    ) -> "_589.MainProfileReliefEndsAtTheStartOfTipReliefOption":
        """mastapy._private.gears.micro_geometry.MainProfileReliefEndsAtTheStartOfTipReliefOption"""
        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfTipReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._589",
            "MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )(value)

    @main_profile_modification_ends_at_the_start_of_tip_relief_by_default.setter
    @enforce_parameter_types
    def main_profile_modification_ends_at_the_start_of_tip_relief_by_default(
        self: "Self", value: "_589.MainProfileReliefEndsAtTheStartOfTipReliefOption"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )
        self.wrapped.MainProfileModificationEndsAtTheStartOfTipReliefByDefault = value

    @property
    def measure_root_reliefs_from_extrapolated_linear_relief_by_default(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = self.wrapped.MeasureRootReliefsFromExtrapolatedLinearReliefByDefault

        if temp is None:
            return False

        return temp

    @measure_root_reliefs_from_extrapolated_linear_relief_by_default.setter
    @enforce_parameter_types
    def measure_root_reliefs_from_extrapolated_linear_relief_by_default(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.MeasureRootReliefsFromExtrapolatedLinearReliefByDefault = (
            bool(value) if value is not None else False
        )

    @property
    def measure_tip_reliefs_from_extrapolated_linear_relief_by_default(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = self.wrapped.MeasureTipReliefsFromExtrapolatedLinearReliefByDefault

        if temp is None:
            return False

        return temp

    @measure_tip_reliefs_from_extrapolated_linear_relief_by_default.setter
    @enforce_parameter_types
    def measure_tip_reliefs_from_extrapolated_linear_relief_by_default(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.MeasureTipReliefsFromExtrapolatedLinearReliefByDefault = (
            bool(value) if value is not None else False
        )

    @property
    def micro_geometry_lead_relief_definition(
        self: "Self",
    ) -> "_1091.MicroGeometryConvention":
        """mastapy._private.gears.gear_designs.cylindrical.MicroGeometryConvention"""
        temp = self.wrapped.MicroGeometryLeadReliefDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometryConvention"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1091",
            "MicroGeometryConvention",
        )(value)

    @micro_geometry_lead_relief_definition.setter
    @enforce_parameter_types
    def micro_geometry_lead_relief_definition(
        self: "Self", value: "_1091.MicroGeometryConvention"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometryConvention"
        )
        self.wrapped.MicroGeometryLeadReliefDefinition = value

    @property
    def micro_geometry_profile_relief_definition(
        self: "Self",
    ) -> "_1092.MicroGeometryProfileConvention":
        """mastapy._private.gears.gear_designs.cylindrical.MicroGeometryProfileConvention"""
        temp = self.wrapped.MicroGeometryProfileReliefDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometryProfileConvention",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1092",
            "MicroGeometryProfileConvention",
        )(value)

    @micro_geometry_profile_relief_definition.setter
    @enforce_parameter_types
    def micro_geometry_profile_relief_definition(
        self: "Self", value: "_1092.MicroGeometryProfileConvention"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometryProfileConvention",
        )
        self.wrapped.MicroGeometryProfileReliefDefinition = value

    @property
    def number_of_points_for_2d_micro_geometry_plots(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsFor2DMicroGeometryPlots

        if temp is None:
            return 0

        return temp

    @number_of_points_for_2d_micro_geometry_plots.setter
    @enforce_parameter_types
    def number_of_points_for_2d_micro_geometry_plots(
        self: "Self", value: "int"
    ) -> None:
        self.wrapped.NumberOfPointsFor2DMicroGeometryPlots = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_steps_for_ltca_contact_surface(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfStepsForLTCAContactSurface

        if temp is None:
            return 0

        return temp

    @number_of_steps_for_ltca_contact_surface.setter
    @enforce_parameter_types
    def number_of_steps_for_ltca_contact_surface(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfStepsForLTCAContactSurface = (
            int(value) if value is not None else 0
        )

    @property
    def parabolic_root_relief_starts_tangent_to_main_profile_relief_by_default(
        self: "Self",
    ) -> "_591.ParabolicRootReliefStartsTangentToMainProfileRelief":
        """mastapy._private.gears.micro_geometry.ParabolicRootReliefStartsTangentToMainProfileRelief"""
        temp = self.wrapped.ParabolicRootReliefStartsTangentToMainProfileReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicRootReliefStartsTangentToMainProfileRelief",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._591",
            "ParabolicRootReliefStartsTangentToMainProfileRelief",
        )(value)

    @parabolic_root_relief_starts_tangent_to_main_profile_relief_by_default.setter
    @enforce_parameter_types
    def parabolic_root_relief_starts_tangent_to_main_profile_relief_by_default(
        self: "Self", value: "_591.ParabolicRootReliefStartsTangentToMainProfileRelief"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicRootReliefStartsTangentToMainProfileRelief",
        )
        self.wrapped.ParabolicRootReliefStartsTangentToMainProfileReliefByDefault = (
            value
        )

    @property
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief_by_default(
        self: "Self",
    ) -> "_592.ParabolicTipReliefStartsTangentToMainProfileRelief":
        """mastapy._private.gears.micro_geometry.ParabolicTipReliefStartsTangentToMainProfileRelief"""
        temp = self.wrapped.ParabolicTipReliefStartsTangentToMainProfileReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicTipReliefStartsTangentToMainProfileRelief",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._592",
            "ParabolicTipReliefStartsTangentToMainProfileRelief",
        )(value)

    @parabolic_tip_relief_starts_tangent_to_main_profile_relief_by_default.setter
    @enforce_parameter_types
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief_by_default(
        self: "Self", value: "_592.ParabolicTipReliefStartsTangentToMainProfileRelief"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicTipReliefStartsTangentToMainProfileRelief",
        )
        self.wrapped.ParabolicTipReliefStartsTangentToMainProfileReliefByDefault = value

    @property
    def shift_micro_geometry_lead_and_profile_modification_to_have_zero_maximum(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.ShiftMicroGeometryLeadAndProfileModificationToHaveZeroMaximum
        )

        if temp is None:
            return False

        return temp

    @shift_micro_geometry_lead_and_profile_modification_to_have_zero_maximum.setter
    @enforce_parameter_types
    def shift_micro_geometry_lead_and_profile_modification_to_have_zero_maximum(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.ShiftMicroGeometryLeadAndProfileModificationToHaveZeroMaximum = (
            bool(value) if value is not None else False
        )

    @property
    def use_same_micro_geometry_on_both_flanks_by_default(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSameMicroGeometryOnBothFlanksByDefault

        if temp is None:
            return False

        return temp

    @use_same_micro_geometry_on_both_flanks_by_default.setter
    @enforce_parameter_types
    def use_same_micro_geometry_on_both_flanks_by_default(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.UseSameMicroGeometryOnBothFlanksByDefault = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMicroGeometrySettingsItem":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMicroGeometrySettingsItem
        """
        return _Cast_CylindricalGearMicroGeometrySettingsItem(self)
