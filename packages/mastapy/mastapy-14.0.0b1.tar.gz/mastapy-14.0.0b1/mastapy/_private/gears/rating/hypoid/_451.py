"""HypoidGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private.gears.rating.agma_gleason_conical import _578
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HYPOID_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid", "HypoidGearSetRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.hypoid import _1011
    from mastapy._private.gears.rating.hypoid import _450, _449
    from mastapy._private.gears.rating.conical import _553
    from mastapy._private.gears.rating import _374, _365
    from mastapy._private.gears.analysis import _1255

    Self = TypeVar("Self", bound="HypoidGearSetRating")
    CastSelf = TypeVar(
        "CastSelf", bound="HypoidGearSetRating._Cast_HypoidGearSetRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HypoidGearSetRating:
    """Special nested class for casting HypoidGearSetRating to subclasses."""

    __parent__: "HypoidGearSetRating"

    @property
    def agma_gleason_conical_gear_set_rating(
        self: "CastSelf",
    ) -> "_578.AGMAGleasonConicalGearSetRating":
        return self.__parent__._cast(_578.AGMAGleasonConicalGearSetRating)

    @property
    def conical_gear_set_rating(self: "CastSelf") -> "_553.ConicalGearSetRating":
        from mastapy._private.gears.rating.conical import _553

        return self.__parent__._cast(_553.ConicalGearSetRating)

    @property
    def gear_set_rating(self: "CastSelf") -> "_374.GearSetRating":
        from mastapy._private.gears.rating import _374

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
    def hypoid_gear_set_rating(self: "CastSelf") -> "HypoidGearSetRating":
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
class HypoidGearSetRating(_578.AGMAGleasonConicalGearSetRating):
    """HypoidGearSetRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HYPOID_GEAR_SET_RATING

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
    def size_factor_bending(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def size_factor_contact(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def hypoid_gear_set(self: "Self") -> "_1011.HypoidGearSetDesign":
        """mastapy._private.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_ratings(self: "Self") -> "List[_450.HypoidGearRating]":
        """List[mastapy._private.gears.rating.hypoid.HypoidGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_mesh_ratings(self: "Self") -> "List[_449.HypoidGearMeshRating]":
        """List[mastapy._private.gears.rating.hypoid.HypoidGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_HypoidGearSetRating":
        """Cast to another type.

        Returns:
            _Cast_HypoidGearSetRating
        """
        return _Cast_HypoidGearSetRating(self)
