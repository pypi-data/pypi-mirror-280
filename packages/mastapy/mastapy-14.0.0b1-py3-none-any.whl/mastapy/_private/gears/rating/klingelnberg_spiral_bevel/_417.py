"""KlingelnbergCycloPalloidSpiralBevelGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.rating.klingelnberg_conical import _423
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _997
    from mastapy._private.gears.rating.conical import _551
    from mastapy._private.gears.rating import _372, _364
    from mastapy._private.gears.analysis import _1253

    Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergCycloPalloidSpiralBevelGearRating:
    """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearRating to subclasses."""

    __parent__: "KlingelnbergCycloPalloidSpiralBevelGearRating"

    @property
    def klingelnberg_cyclo_palloid_conical_gear_rating(
        self: "CastSelf",
    ) -> "_423.KlingelnbergCycloPalloidConicalGearRating":
        return self.__parent__._cast(_423.KlingelnbergCycloPalloidConicalGearRating)

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
        self: "CastSelf",
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearRating":
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
class KlingelnbergCycloPalloidSpiralBevelGearRating(
    _423.KlingelnbergCycloPalloidConicalGearRating
):
    """KlingelnbergCycloPalloidSpiralBevelGearRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "Self",
    ) -> "_997.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_KlingelnbergCycloPalloidSpiralBevelGearRating":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergCycloPalloidSpiralBevelGearRating
        """
        return _Cast_KlingelnbergCycloPalloidSpiralBevelGearRating(self)
