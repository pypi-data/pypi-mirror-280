"""FourPointContactBallBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private.bearings.bearing_designs.rolling import _2212
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FOUR_POINT_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "FourPointContactBallBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_designs.rolling import _2206, _2193, _2218
    from mastapy._private.bearings.bearing_designs import _2184, _2187, _2183

    Self = TypeVar("Self", bound="FourPointContactBallBearing")
    CastSelf = TypeVar(
        "CastSelf",
        bound="FourPointContactBallBearing._Cast_FourPointContactBallBearing",
    )


__docformat__ = "restructuredtext en"
__all__ = ("FourPointContactBallBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FourPointContactBallBearing:
    """Special nested class for casting FourPointContactBallBearing to subclasses."""

    __parent__: "FourPointContactBallBearing"

    @property
    def multi_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2212.MultiPointContactBallBearing":
        return self.__parent__._cast(_2212.MultiPointContactBallBearing)

    @property
    def ball_bearing(self: "CastSelf") -> "_2193.BallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2193

        return self.__parent__._cast(_2193.BallBearing)

    @property
    def rolling_bearing(self: "CastSelf") -> "_2218.RollingBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2218

        return self.__parent__._cast(_2218.RollingBearing)

    @property
    def detailed_bearing(self: "CastSelf") -> "_2184.DetailedBearing":
        from mastapy._private.bearings.bearing_designs import _2184

        return self.__parent__._cast(_2184.DetailedBearing)

    @property
    def non_linear_bearing(self: "CastSelf") -> "_2187.NonLinearBearing":
        from mastapy._private.bearings.bearing_designs import _2187

        return self.__parent__._cast(_2187.NonLinearBearing)

    @property
    def bearing_design(self: "CastSelf") -> "_2183.BearingDesign":
        from mastapy._private.bearings.bearing_designs import _2183

        return self.__parent__._cast(_2183.BearingDesign)

    @property
    def four_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "FourPointContactBallBearing":
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
class FourPointContactBallBearing(_2212.MultiPointContactBallBearing):
    """FourPointContactBallBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FOUR_POINT_CONTACT_BALL_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_axial_internal_clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_under_axial_load(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleUnderAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def contact_angle_under_radial_load(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleUnderRadialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def contact_angle_and_internal_clearance_definition(
        self: "Self",
    ) -> "_2206.FourPointContactAngleDefinition":
        """mastapy._private.bearings.bearing_designs.rolling.FourPointContactAngleDefinition"""
        temp = self.wrapped.ContactAngleAndInternalClearanceDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.FourPointContactAngleDefinition",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.bearing_designs.rolling._2206",
            "FourPointContactAngleDefinition",
        )(value)

    @contact_angle_and_internal_clearance_definition.setter
    @enforce_parameter_types
    def contact_angle_and_internal_clearance_definition(
        self: "Self", value: "_2206.FourPointContactAngleDefinition"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.FourPointContactAngleDefinition",
        )
        self.wrapped.ContactAngleAndInternalClearanceDefinition = value

    @property
    def nominal_radial_internal_clearance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @nominal_radial_internal_clearance.setter
    @enforce_parameter_types
    def nominal_radial_internal_clearance(self: "Self", value: "float") -> None:
        self.wrapped.NominalRadialInternalClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: "Self") -> "_Cast_FourPointContactBallBearing":
        """Cast to another type.

        Returns:
            _Cast_FourPointContactBallBearing
        """
        return _Cast_FourPointContactBallBearing(self)
