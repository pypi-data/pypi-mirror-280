"""NonLinearBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.bearings.bearing_designs import _2183
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_NON_LINEAR_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "NonLinearBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_designs import _2184
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

    Self = TypeVar("Self", bound="NonLinearBearing")
    CastSelf = TypeVar("CastSelf", bound="NonLinearBearing._Cast_NonLinearBearing")


__docformat__ = "restructuredtext en"
__all__ = ("NonLinearBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_NonLinearBearing:
    """Special nested class for casting NonLinearBearing to subclasses."""

    __parent__: "NonLinearBearing"

    @property
    def bearing_design(self: "CastSelf") -> "_2183.BearingDesign":
        return self.__parent__._cast(_2183.BearingDesign)

    @property
    def detailed_bearing(self: "CastSelf") -> "_2184.DetailedBearing":
        from mastapy._private.bearings.bearing_designs import _2184

        return self.__parent__._cast(_2184.DetailedBearing)

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
    def non_linear_bearing(self: "CastSelf") -> "NonLinearBearing":
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
class NonLinearBearing(_2183.BearingDesign):
    """NonLinearBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _NON_LINEAR_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_NonLinearBearing":
        """Cast to another type.

        Returns:
            _Cast_NonLinearBearing
        """
        return _Cast_NonLinearBearing(self)
