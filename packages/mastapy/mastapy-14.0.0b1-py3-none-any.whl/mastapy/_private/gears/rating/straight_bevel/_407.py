"""StraightBevelGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.rating.bevel import _566
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.StraightBevel", "StraightBevelGearRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.straight_bevel import _985
    from mastapy._private.gears.rating.agma_gleason_conical import _577
    from mastapy._private.gears.rating.conical import _551
    from mastapy._private.gears.rating import _372, _364
    from mastapy._private.gears.analysis import _1253

    Self = TypeVar("Self", bound="StraightBevelGearRating")
    CastSelf = TypeVar(
        "CastSelf", bound="StraightBevelGearRating._Cast_StraightBevelGearRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelGearRating:
    """Special nested class for casting StraightBevelGearRating to subclasses."""

    __parent__: "StraightBevelGearRating"

    @property
    def bevel_gear_rating(self: "CastSelf") -> "_566.BevelGearRating":
        return self.__parent__._cast(_566.BevelGearRating)

    @property
    def agma_gleason_conical_gear_rating(
        self: "CastSelf",
    ) -> "_577.AGMAGleasonConicalGearRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _577

        return self.__parent__._cast(_577.AGMAGleasonConicalGearRating)

    @property
    def conical_gear_rating(self: "CastSelf") -> "_551.ConicalGearRating":
        from mastapy._private.gears.rating.conical import _551

        return self.__parent__._cast(_551.ConicalGearRating)

    @property
    def gear_rating(self: "CastSelf") -> "_372.GearRating":
        from mastapy._private.gears.rating import _372

        return self.__parent__._cast(_372.GearRating)

    @property
    def abstract_gear_rating(self: "CastSelf") -> "_364.AbstractGearRating":
        from mastapy._private.gears.rating import _364

        return self.__parent__._cast(_364.AbstractGearRating)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def straight_bevel_gear_rating(self: "CastSelf") -> "StraightBevelGearRating":
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
class StraightBevelGearRating(_566.BevelGearRating):
    """StraightBevelGearRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_GEAR_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def straight_bevel_gear(self: "Self") -> "_985.StraightBevelGearDesign":
        """mastapy._private.gears.gear_designs.straight_bevel.StraightBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelGearRating":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelGearRating
        """
        return _Cast_StraightBevelGearRating(self)
