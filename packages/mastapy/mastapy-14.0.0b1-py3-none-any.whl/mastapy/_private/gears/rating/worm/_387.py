"""WormGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.rating import _374
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_WORM_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormGearSetRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.worm import _983
    from mastapy._private.gears.rating.worm import _385, _384
    from mastapy._private.gears.rating import _365
    from mastapy._private.gears.analysis import _1255

    Self = TypeVar("Self", bound="WormGearSetRating")
    CastSelf = TypeVar("CastSelf", bound="WormGearSetRating._Cast_WormGearSetRating")


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGearSetRating:
    """Special nested class for casting WormGearSetRating to subclasses."""

    __parent__: "WormGearSetRating"

    @property
    def gear_set_rating(self: "CastSelf") -> "_374.GearSetRating":
        return self.__parent__._cast(_374.GearSetRating)

    @property
    def abstract_gear_set_rating(self: "CastSelf") -> "_365.AbstractGearSetRating":
        from mastapy._private.gears.rating import _365

        return self.__parent__._cast(_365.AbstractGearSetRating)

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        from mastapy._private.gears.analysis import _1255

        return self.__parent__._cast(_1255.AbstractGearSetAnalysis)

    @property
    def worm_gear_set_rating(self: "CastSelf") -> "WormGearSetRating":
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
class WormGearSetRating(_374.GearSetRating):
    """WormGearSetRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GEAR_SET_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def rating(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return ""

        return temp

    @property
    def worm_gear_set(self: "Self") -> "_983.WormGearSetDesign":
        """mastapy._private.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: "Self") -> "List[_385.WormGearRating]":
        """List[mastapy._private.gears.rating.worm.WormGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_ratings(self: "Self") -> "List[_385.WormGearRating]":
        """List[mastapy._private.gears.rating.worm.WormGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: "Self") -> "List[_384.WormGearMeshRating]":
        """List[mastapy._private.gears.rating.worm.WormGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_mesh_ratings(self: "Self") -> "List[_384.WormGearMeshRating]":
        """List[mastapy._private.gears.rating.worm.WormGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_WormGearSetRating":
        """Cast to another type.

        Returns:
            _Cast_WormGearSetRating
        """
        return _Cast_WormGearSetRating(self)
