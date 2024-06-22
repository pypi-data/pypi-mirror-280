"""BearingDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEARING_DESIGN = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "BearingDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.math_utility import _1564
    from mastapy._private.bearings.bearing_designs import _2184, _2185, _2186, _2187
    from mastapy._private.bearings.bearing_designs.rolling import (
        _2188,
        _2189,
        _2190,
        _2191,
        _2192,
        _2193,
        _2195,
        _2201,
        _2202,
        _2203,
        _2207,
        _2212,
        _2213,
        _2214,
        _2215,
        _2218,
        _2219,
        _2222,
        _2223,
        _2224,
        _2225,
        _2226,
        _2227,
    )
    from mastapy._private.bearings.bearing_designs.fluid_film import (
        _2240,
        _2242,
        _2244,
        _2246,
        _2247,
        _2248,
    )
    from mastapy._private.bearings.bearing_designs.concept import _2250, _2251, _2252

    Self = TypeVar("Self", bound="BearingDesign")
    CastSelf = TypeVar("CastSelf", bound="BearingDesign._Cast_BearingDesign")


__docformat__ = "restructuredtext en"
__all__ = ("BearingDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BearingDesign:
    """Special nested class for casting BearingDesign to subclasses."""

    __parent__: "BearingDesign"

    @property
    def detailed_bearing(self: "CastSelf") -> "_2184.DetailedBearing":
        from mastapy._private.bearings.bearing_designs import _2184

        return self.__parent__._cast(_2184.DetailedBearing)

    @property
    def dummy_rolling_bearing(self: "CastSelf") -> "_2185.DummyRollingBearing":
        from mastapy._private.bearings.bearing_designs import _2185

        return self.__parent__._cast(_2185.DummyRollingBearing)

    @property
    def linear_bearing(self: "CastSelf") -> "_2186.LinearBearing":
        from mastapy._private.bearings.bearing_designs import _2186

        return self.__parent__._cast(_2186.LinearBearing)

    @property
    def non_linear_bearing(self: "CastSelf") -> "_2187.NonLinearBearing":
        from mastapy._private.bearings.bearing_designs import _2187

        return self.__parent__._cast(_2187.NonLinearBearing)

    @property
    def angular_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2188.AngularContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2188

        return self.__parent__._cast(_2188.AngularContactBallBearing)

    @property
    def angular_contact_thrust_ball_bearing(
        self: "CastSelf",
    ) -> "_2189.AngularContactThrustBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2189

        return self.__parent__._cast(_2189.AngularContactThrustBallBearing)

    @property
    def asymmetric_spherical_roller_bearing(
        self: "CastSelf",
    ) -> "_2190.AsymmetricSphericalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2190

        return self.__parent__._cast(_2190.AsymmetricSphericalRollerBearing)

    @property
    def axial_thrust_cylindrical_roller_bearing(
        self: "CastSelf",
    ) -> "_2191.AxialThrustCylindricalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2191

        return self.__parent__._cast(_2191.AxialThrustCylindricalRollerBearing)

    @property
    def axial_thrust_needle_roller_bearing(
        self: "CastSelf",
    ) -> "_2192.AxialThrustNeedleRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2192

        return self.__parent__._cast(_2192.AxialThrustNeedleRollerBearing)

    @property
    def ball_bearing(self: "CastSelf") -> "_2193.BallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2193

        return self.__parent__._cast(_2193.BallBearing)

    @property
    def barrel_roller_bearing(self: "CastSelf") -> "_2195.BarrelRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2195

        return self.__parent__._cast(_2195.BarrelRollerBearing)

    @property
    def crossed_roller_bearing(self: "CastSelf") -> "_2201.CrossedRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2201

        return self.__parent__._cast(_2201.CrossedRollerBearing)

    @property
    def cylindrical_roller_bearing(
        self: "CastSelf",
    ) -> "_2202.CylindricalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2202

        return self.__parent__._cast(_2202.CylindricalRollerBearing)

    @property
    def deep_groove_ball_bearing(self: "CastSelf") -> "_2203.DeepGrooveBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2203

        return self.__parent__._cast(_2203.DeepGrooveBallBearing)

    @property
    def four_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2207.FourPointContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2207

        return self.__parent__._cast(_2207.FourPointContactBallBearing)

    @property
    def multi_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2212.MultiPointContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2212

        return self.__parent__._cast(_2212.MultiPointContactBallBearing)

    @property
    def needle_roller_bearing(self: "CastSelf") -> "_2213.NeedleRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2213

        return self.__parent__._cast(_2213.NeedleRollerBearing)

    @property
    def non_barrel_roller_bearing(self: "CastSelf") -> "_2214.NonBarrelRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2214

        return self.__parent__._cast(_2214.NonBarrelRollerBearing)

    @property
    def roller_bearing(self: "CastSelf") -> "_2215.RollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2215

        return self.__parent__._cast(_2215.RollerBearing)

    @property
    def rolling_bearing(self: "CastSelf") -> "_2218.RollingBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2218

        return self.__parent__._cast(_2218.RollingBearing)

    @property
    def self_aligning_ball_bearing(self: "CastSelf") -> "_2219.SelfAligningBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2219

        return self.__parent__._cast(_2219.SelfAligningBallBearing)

    @property
    def spherical_roller_bearing(self: "CastSelf") -> "_2222.SphericalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2222

        return self.__parent__._cast(_2222.SphericalRollerBearing)

    @property
    def spherical_roller_thrust_bearing(
        self: "CastSelf",
    ) -> "_2223.SphericalRollerThrustBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2223

        return self.__parent__._cast(_2223.SphericalRollerThrustBearing)

    @property
    def taper_roller_bearing(self: "CastSelf") -> "_2224.TaperRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2224

        return self.__parent__._cast(_2224.TaperRollerBearing)

    @property
    def three_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2225.ThreePointContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2225

        return self.__parent__._cast(_2225.ThreePointContactBallBearing)

    @property
    def thrust_ball_bearing(self: "CastSelf") -> "_2226.ThrustBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2226

        return self.__parent__._cast(_2226.ThrustBallBearing)

    @property
    def toroidal_roller_bearing(self: "CastSelf") -> "_2227.ToroidalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2227

        return self.__parent__._cast(_2227.ToroidalRollerBearing)

    @property
    def pad_fluid_film_bearing(self: "CastSelf") -> "_2240.PadFluidFilmBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2240

        return self.__parent__._cast(_2240.PadFluidFilmBearing)

    @property
    def plain_grease_filled_journal_bearing(
        self: "CastSelf",
    ) -> "_2242.PlainGreaseFilledJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2242

        return self.__parent__._cast(_2242.PlainGreaseFilledJournalBearing)

    @property
    def plain_journal_bearing(self: "CastSelf") -> "_2244.PlainJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2244

        return self.__parent__._cast(_2244.PlainJournalBearing)

    @property
    def plain_oil_fed_journal_bearing(
        self: "CastSelf",
    ) -> "_2246.PlainOilFedJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2246

        return self.__parent__._cast(_2246.PlainOilFedJournalBearing)

    @property
    def tilting_pad_journal_bearing(
        self: "CastSelf",
    ) -> "_2247.TiltingPadJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2247

        return self.__parent__._cast(_2247.TiltingPadJournalBearing)

    @property
    def tilting_pad_thrust_bearing(self: "CastSelf") -> "_2248.TiltingPadThrustBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2248

        return self.__parent__._cast(_2248.TiltingPadThrustBearing)

    @property
    def concept_axial_clearance_bearing(
        self: "CastSelf",
    ) -> "_2250.ConceptAxialClearanceBearing":
        from mastapy._private.bearings.bearing_designs.concept import _2250

        return self.__parent__._cast(_2250.ConceptAxialClearanceBearing)

    @property
    def concept_clearance_bearing(self: "CastSelf") -> "_2251.ConceptClearanceBearing":
        from mastapy._private.bearings.bearing_designs.concept import _2251

        return self.__parent__._cast(_2251.ConceptClearanceBearing)

    @property
    def concept_radial_clearance_bearing(
        self: "CastSelf",
    ) -> "_2252.ConceptRadialClearanceBearing":
        from mastapy._private.bearings.bearing_designs.concept import _2252

        return self.__parent__._cast(_2252.ConceptRadialClearanceBearing)

    @property
    def bearing_design(self: "CastSelf") -> "BearingDesign":
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
class BearingDesign(_0.APIBase):
    """BearingDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEARING_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bore(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: "Self", value: "float") -> None:
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def mass(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

    @property
    def outer_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: "Self", value: "float") -> None:
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def type_(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return ""

        return temp

    @property
    def width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: "Self", value: "float") -> None:
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def mass_properties_of_elements_from_geometry(
        self: "Self",
    ) -> "_1564.MassProperties":
        """mastapy._private.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfElementsFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_of_inner_ring_from_geometry(
        self: "Self",
    ) -> "_1564.MassProperties":
        """mastapy._private.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfInnerRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_of_outer_ring_from_geometry(
        self: "Self",
    ) -> "_1564.MassProperties":
        """mastapy._private.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfOuterRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_mass_properties(self: "Self") -> "_1564.MassProperties":
        """mastapy._private.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMassProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: "Self") -> "_Cast_BearingDesign":
        """Cast to another type.

        Returns:
            _Cast_BearingDesign
        """
        return _Cast_BearingDesign(self)
