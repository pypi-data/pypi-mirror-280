"""ConceptClearanceBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.bearings.bearing_designs import _2187
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONCEPT_CLEARANCE_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Concept", "ConceptClearanceBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_designs.concept import _2250, _2252
    from mastapy._private.bearings.bearing_designs import _2183

    Self = TypeVar("Self", bound="ConceptClearanceBearing")
    CastSelf = TypeVar(
        "CastSelf", bound="ConceptClearanceBearing._Cast_ConceptClearanceBearing"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptClearanceBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConceptClearanceBearing:
    """Special nested class for casting ConceptClearanceBearing to subclasses."""

    __parent__: "ConceptClearanceBearing"

    @property
    def non_linear_bearing(self: "CastSelf") -> "_2187.NonLinearBearing":
        return self.__parent__._cast(_2187.NonLinearBearing)

    @property
    def bearing_design(self: "CastSelf") -> "_2183.BearingDesign":
        from mastapy._private.bearings.bearing_designs import _2183

        return self.__parent__._cast(_2183.BearingDesign)

    @property
    def concept_axial_clearance_bearing(
        self: "CastSelf",
    ) -> "_2250.ConceptAxialClearanceBearing":
        from mastapy._private.bearings.bearing_designs.concept import _2250

        return self.__parent__._cast(_2250.ConceptAxialClearanceBearing)

    @property
    def concept_radial_clearance_bearing(
        self: "CastSelf",
    ) -> "_2252.ConceptRadialClearanceBearing":
        from mastapy._private.bearings.bearing_designs.concept import _2252

        return self.__parent__._cast(_2252.ConceptRadialClearanceBearing)

    @property
    def concept_clearance_bearing(self: "CastSelf") -> "ConceptClearanceBearing":
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
class ConceptClearanceBearing(_2187.NonLinearBearing):
    """ConceptClearanceBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONCEPT_CLEARANCE_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def contact_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ContactDiameter

        if temp is None:
            return 0.0

        return temp

    @contact_diameter.setter
    @enforce_parameter_types
    def contact_diameter(self: "Self", value: "float") -> None:
        self.wrapped.ContactDiameter = float(value) if value is not None else 0.0

    @property
    def contact_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness.setter
    @enforce_parameter_types
    def contact_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.ContactStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_ConceptClearanceBearing":
        """Cast to another type.

        Returns:
            _Cast_ConceptClearanceBearing
        """
        return _Cast_ConceptClearanceBearing(self)
