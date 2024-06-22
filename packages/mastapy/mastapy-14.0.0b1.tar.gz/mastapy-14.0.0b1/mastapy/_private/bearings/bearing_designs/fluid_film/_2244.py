"""PlainJournalBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.bearings.bearing_designs import _2184
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PLAIN_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PlainJournalBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_designs.fluid_film import _2242, _2246
    from mastapy._private.bearings.bearing_designs import _2187, _2183

    Self = TypeVar("Self", bound="PlainJournalBearing")
    CastSelf = TypeVar(
        "CastSelf", bound="PlainJournalBearing._Cast_PlainJournalBearing"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlainJournalBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PlainJournalBearing:
    """Special nested class for casting PlainJournalBearing to subclasses."""

    __parent__: "PlainJournalBearing"

    @property
    def detailed_bearing(self: "CastSelf") -> "_2184.DetailedBearing":
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
    def plain_grease_filled_journal_bearing(
        self: "CastSelf",
    ) -> "_2242.PlainGreaseFilledJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2242

        return self.__parent__._cast(_2242.PlainGreaseFilledJournalBearing)

    @property
    def plain_oil_fed_journal_bearing(
        self: "CastSelf",
    ) -> "_2246.PlainOilFedJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2246

        return self.__parent__._cast(_2246.PlainOilFedJournalBearing)

    @property
    def plain_journal_bearing(self: "CastSelf") -> "PlainJournalBearing":
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
class PlainJournalBearing(_2184.DetailedBearing):
    """PlainJournalBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PLAIN_JOURNAL_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def diametrical_clearance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DiametricalClearance

        if temp is None:
            return 0.0

        return temp

    @diametrical_clearance.setter
    @enforce_parameter_types
    def diametrical_clearance(self: "Self", value: "float") -> None:
        self.wrapped.DiametricalClearance = float(value) if value is not None else 0.0

    @property
    def land_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LandWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def land_width_to_diameter_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LandWidthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_PlainJournalBearing":
        """Cast to another type.

        Returns:
            _Cast_PlainJournalBearing
        """
        return _Cast_PlainJournalBearing(self)
