"""LoadedElement"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedElement"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bearings.bearing_results import _1997
    from mastapy._private.bearings.bearing_results.rolling import (
        _2026,
        _2126,
        _2035,
        _2038,
        _2041,
        _2046,
        _2049,
        _2053,
        _2057,
        _2061,
        _2064,
        _2068,
        _2072,
        _2073,
        _2080,
        _2081,
        _2088,
        _2091,
        _2092,
        _2098,
        _2100,
        _2103,
        _2106,
        _2109,
    )

    Self = TypeVar("Self", bound="LoadedElement")
    CastSelf = TypeVar("CastSelf", bound="LoadedElement._Cast_LoadedElement")


__docformat__ = "restructuredtext en"
__all__ = ("LoadedElement",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedElement:
    """Special nested class for casting LoadedElement to subclasses."""

    __parent__: "LoadedElement"

    @property
    def loaded_angular_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2035.LoadedAngularContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2035

        return self.__parent__._cast(_2035.LoadedAngularContactBallBearingElement)

    @property
    def loaded_angular_contact_thrust_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2038.LoadedAngularContactThrustBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2038

        return self.__parent__._cast(_2038.LoadedAngularContactThrustBallBearingElement)

    @property
    def loaded_asymmetric_spherical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2041.LoadedAsymmetricSphericalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2041

        return self.__parent__._cast(
            _2041.LoadedAsymmetricSphericalRollerBearingElement
        )

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2046.LoadedAxialThrustCylindricalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2046

        return self.__parent__._cast(
            _2046.LoadedAxialThrustCylindricalRollerBearingElement
        )

    @property
    def loaded_axial_thrust_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2049.LoadedAxialThrustNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2049

        return self.__parent__._cast(_2049.LoadedAxialThrustNeedleRollerBearingElement)

    @property
    def loaded_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2053.LoadedBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2053

        return self.__parent__._cast(_2053.LoadedBallBearingElement)

    @property
    def loaded_crossed_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2057.LoadedCrossedRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2057

        return self.__parent__._cast(_2057.LoadedCrossedRollerBearingElement)

    @property
    def loaded_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2061.LoadedCylindricalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2061

        return self.__parent__._cast(_2061.LoadedCylindricalRollerBearingElement)

    @property
    def loaded_deep_groove_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2064.LoadedDeepGrooveBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2064

        return self.__parent__._cast(_2064.LoadedDeepGrooveBallBearingElement)

    @property
    def loaded_four_point_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2068.LoadedFourPointContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2068

        return self.__parent__._cast(_2068.LoadedFourPointContactBallBearingElement)

    @property
    def loaded_multi_point_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2072.LoadedMultiPointContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2072

        return self.__parent__._cast(_2072.LoadedMultiPointContactBallBearingElement)

    @property
    def loaded_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2073.LoadedNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2073

        return self.__parent__._cast(_2073.LoadedNeedleRollerBearingElement)

    @property
    def loaded_non_barrel_roller_element(
        self: "CastSelf",
    ) -> "_2080.LoadedNonBarrelRollerElement":
        from mastapy._private.bearings.bearing_results.rolling import _2080

        return self.__parent__._cast(_2080.LoadedNonBarrelRollerElement)

    @property
    def loaded_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2081.LoadedRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2081

        return self.__parent__._cast(_2081.LoadedRollerBearingElement)

    @property
    def loaded_self_aligning_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2088.LoadedSelfAligningBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2088

        return self.__parent__._cast(_2088.LoadedSelfAligningBallBearingElement)

    @property
    def loaded_spherical_radial_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2091.LoadedSphericalRadialRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2091

        return self.__parent__._cast(_2091.LoadedSphericalRadialRollerBearingElement)

    @property
    def loaded_spherical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2092.LoadedSphericalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2092

        return self.__parent__._cast(_2092.LoadedSphericalRollerBearingElement)

    @property
    def loaded_spherical_thrust_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2098.LoadedSphericalThrustRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2098

        return self.__parent__._cast(_2098.LoadedSphericalThrustRollerBearingElement)

    @property
    def loaded_taper_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2100.LoadedTaperRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2100

        return self.__parent__._cast(_2100.LoadedTaperRollerBearingElement)

    @property
    def loaded_three_point_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2103.LoadedThreePointContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2103

        return self.__parent__._cast(_2103.LoadedThreePointContactBallBearingElement)

    @property
    def loaded_thrust_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2106.LoadedThrustBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2106

        return self.__parent__._cast(_2106.LoadedThrustBallBearingElement)

    @property
    def loaded_toroidal_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2109.LoadedToroidalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2109

        return self.__parent__._cast(_2109.LoadedToroidalRollerBearingElement)

    @property
    def loaded_element(self: "CastSelf") -> "LoadedElement":
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
class LoadedElement(_0.APIBase):
    """LoadedElement

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_ELEMENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_loading(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def element_id(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementId

        if temp is None:
            return ""

        return temp

    @property
    def element_raceway_contact_area_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaInner

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @normal_load_inner.setter
    @enforce_parameter_types
    def normal_load_inner(self: "Self", value: "float") -> None:
        self.wrapped.NormalLoadInner = float(value) if value is not None else 0.0

    @property
    def normal_load_outer(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @normal_load_outer.setter
    @enforce_parameter_types
    def normal_load_outer(self: "Self", value: "float") -> None:
        self.wrapped.NormalLoadOuter = float(value) if value is not None else 0.0

    @property
    def race_deflection_inner(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RaceDeflectionInner

        if temp is None:
            return 0.0

        return temp

    @race_deflection_inner.setter
    @enforce_parameter_types
    def race_deflection_inner(self: "Self", value: "float") -> None:
        self.wrapped.RaceDeflectionInner = float(value) if value is not None else 0.0

    @property
    def race_deflection_outer(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RaceDeflectionOuter

        if temp is None:
            return 0.0

        return temp

    @race_deflection_outer.setter
    @enforce_parameter_types
    def race_deflection_outer(self: "Self", value: "float") -> None:
        self.wrapped.RaceDeflectionOuter = float(value) if value is not None else 0.0

    @property
    def race_deflection_total(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RaceDeflectionTotal

        if temp is None:
            return 0.0

        return temp

    @race_deflection_total.setter
    @enforce_parameter_types
    def race_deflection_total(self: "Self", value: "float") -> None:
        self.wrapped.RaceDeflectionTotal = float(value) if value is not None else 0.0

    @property
    def race_separation_at_element_axial(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceSeparationAtElementAxial

        if temp is None:
            return 0.0

        return temp

    @property
    def race_separation_at_element_radial(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceSeparationAtElementRadial

        if temp is None:
            return 0.0

        return temp

    @property
    def force_from_inner_race(self: "Self") -> "_1997.ElementForce":
        """mastapy._private.bearings.bearing_results.ElementForce

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceFromInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def operating_internal_clearance(self: "Self") -> "_2026.InternalClearance":
        """mastapy._private.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def subsurface_shear_stress_distribution_inner(
        self: "Self",
    ) -> "List[_2126.StressAtPosition]":
        """List[mastapy._private.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressDistributionInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_distribution_outer(
        self: "Self",
    ) -> "List[_2126.StressAtPosition]":
        """List[mastapy._private.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressDistributionOuter

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
    def cast_to(self: "Self") -> "_Cast_LoadedElement":
        """Cast to another type.

        Returns:
            _Cast_LoadedElement
        """
        return _Cast_LoadedElement(self)
