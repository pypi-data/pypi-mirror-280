"""LoadedRollingBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from PIL.Image import Image

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollingBearingRow"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.bearings.bearing_results.rolling import (
        _2086,
        _2026,
        _2067,
        _2085,
        _2121,
        _2126,
        _2037,
        _2040,
        _2043,
        _2048,
        _2051,
        _2056,
        _2059,
        _2063,
        _2066,
        _2071,
        _2075,
        _2078,
        _2083,
        _2090,
        _2094,
        _2097,
        _2102,
        _2105,
        _2108,
        _2111,
    )

    Self = TypeVar("Self", bound="LoadedRollingBearingRow")
    CastSelf = TypeVar(
        "CastSelf", bound="LoadedRollingBearingRow._Cast_LoadedRollingBearingRow"
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingRow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedRollingBearingRow:
    """Special nested class for casting LoadedRollingBearingRow to subclasses."""

    __parent__: "LoadedRollingBearingRow"

    @property
    def loaded_angular_contact_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2037.LoadedAngularContactBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2037

        return self.__parent__._cast(_2037.LoadedAngularContactBallBearingRow)

    @property
    def loaded_angular_contact_thrust_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2040.LoadedAngularContactThrustBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2040

        return self.__parent__._cast(_2040.LoadedAngularContactThrustBallBearingRow)

    @property
    def loaded_asymmetric_spherical_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2043.LoadedAsymmetricSphericalRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2043

        return self.__parent__._cast(_2043.LoadedAsymmetricSphericalRollerBearingRow)

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2048.LoadedAxialThrustCylindricalRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2048

        return self.__parent__._cast(_2048.LoadedAxialThrustCylindricalRollerBearingRow)

    @property
    def loaded_axial_thrust_needle_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2051.LoadedAxialThrustNeedleRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2051

        return self.__parent__._cast(_2051.LoadedAxialThrustNeedleRollerBearingRow)

    @property
    def loaded_ball_bearing_row(self: "CastSelf") -> "_2056.LoadedBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2056

        return self.__parent__._cast(_2056.LoadedBallBearingRow)

    @property
    def loaded_crossed_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2059.LoadedCrossedRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2059

        return self.__parent__._cast(_2059.LoadedCrossedRollerBearingRow)

    @property
    def loaded_cylindrical_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2063.LoadedCylindricalRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2063

        return self.__parent__._cast(_2063.LoadedCylindricalRollerBearingRow)

    @property
    def loaded_deep_groove_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2066.LoadedDeepGrooveBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2066

        return self.__parent__._cast(_2066.LoadedDeepGrooveBallBearingRow)

    @property
    def loaded_four_point_contact_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2071.LoadedFourPointContactBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2071

        return self.__parent__._cast(_2071.LoadedFourPointContactBallBearingRow)

    @property
    def loaded_needle_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2075.LoadedNeedleRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2075

        return self.__parent__._cast(_2075.LoadedNeedleRollerBearingRow)

    @property
    def loaded_non_barrel_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2078.LoadedNonBarrelRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2078

        return self.__parent__._cast(_2078.LoadedNonBarrelRollerBearingRow)

    @property
    def loaded_roller_bearing_row(self: "CastSelf") -> "_2083.LoadedRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2083

        return self.__parent__._cast(_2083.LoadedRollerBearingRow)

    @property
    def loaded_self_aligning_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2090.LoadedSelfAligningBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2090

        return self.__parent__._cast(_2090.LoadedSelfAligningBallBearingRow)

    @property
    def loaded_spherical_roller_radial_bearing_row(
        self: "CastSelf",
    ) -> "_2094.LoadedSphericalRollerRadialBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2094

        return self.__parent__._cast(_2094.LoadedSphericalRollerRadialBearingRow)

    @property
    def loaded_spherical_roller_thrust_bearing_row(
        self: "CastSelf",
    ) -> "_2097.LoadedSphericalRollerThrustBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2097

        return self.__parent__._cast(_2097.LoadedSphericalRollerThrustBearingRow)

    @property
    def loaded_taper_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2102.LoadedTaperRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2102

        return self.__parent__._cast(_2102.LoadedTaperRollerBearingRow)

    @property
    def loaded_three_point_contact_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2105.LoadedThreePointContactBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2105

        return self.__parent__._cast(_2105.LoadedThreePointContactBallBearingRow)

    @property
    def loaded_thrust_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2108.LoadedThrustBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2108

        return self.__parent__._cast(_2108.LoadedThrustBallBearingRow)

    @property
    def loaded_toroidal_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2111.LoadedToroidalRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2111

        return self.__parent__._cast(_2111.LoadedToroidalRollerBearingRow)

    @property
    def loaded_rolling_bearing_row(self: "CastSelf") -> "LoadedRollingBearingRow":
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
class LoadedRollingBearingRow(_0.APIBase):
    """LoadedRollingBearingRow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_ROLLING_BEARING_ROW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def dynamic_equivalent_reference_load(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def life_modification_factor_for_systems_approach(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeModificationFactorForSystemsApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_contact_stress_chart_inner(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_left(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_outer(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_right(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def row_id(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RowID

        if temp is None:
            return ""

        return temp

    @property
    def subsurface_shear_stress_chart_inner(
        self: "Self",
    ) -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressChartInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def subsurface_shear_stress_chart_outer(
        self: "Self",
    ) -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressChartOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loaded_bearing(self: "Self") -> "_2086.LoadedRollingBearingResults":
        """mastapy._private.bearings.bearing_results.rolling.LoadedRollingBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_operating_internal_clearance(self: "Self") -> "_2026.InternalClearance":
        """mastapy._private.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_operating_internal_clearance(self: "Self") -> "_2026.InternalClearance":
        """mastapy._private.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def elements(self: "Self") -> "List[_2067.LoadedElement]":
        """List[mastapy._private.bearings.bearing_results.rolling.LoadedElement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Elements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def race_results(self: "Self") -> "List[_2085.LoadedRollingBearingRaceResults]":
        """List[mastapy._private.bearings.bearing_results.rolling.LoadedRollingBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_force_and_displacement_results(
        self: "Self",
    ) -> "List[_2121.RingForceAndDisplacement]":
        """List[mastapy._private.bearings.bearing_results.rolling.RingForceAndDisplacement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingForceAndDisplacementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_inner(
        self: "Self",
    ) -> "List[_2126.StressAtPosition]":
        """List[mastapy._private.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_outer(
        self: "Self",
    ) -> "List[_2126.StressAtPosition]":
        """List[mastapy._private.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedRollingBearingRow":
        """Cast to another type.

        Returns:
            _Cast_LoadedRollingBearingRow
        """
        return _Cast_LoadedRollingBearingRow(self)
