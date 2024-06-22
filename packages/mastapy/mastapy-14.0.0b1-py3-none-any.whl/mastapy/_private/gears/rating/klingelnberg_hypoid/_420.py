"""KlingelnbergCycloPalloidHypoidGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.rating.klingelnberg_conical import _423
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearRating",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1001
    from mastapy._private.gears.rating.conical import _551
    from mastapy._private.gears.rating import _372, _364
    from mastapy._private.gears.analysis import _1253

    Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergCycloPalloidHypoidGearRating:
    """Special nested class for casting KlingelnbergCycloPalloidHypoidGearRating to subclasses."""

    __parent__: "KlingelnbergCycloPalloidHypoidGearRating"

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
    def klingelnberg_cyclo_palloid_hypoid_gear_rating(
        self: "CastSelf",
    ) -> "KlingelnbergCycloPalloidHypoidGearRating":
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
class KlingelnbergCycloPalloidHypoidGearRating(
    _423.KlingelnbergCycloPalloidConicalGearRating
):
    """KlingelnbergCycloPalloidHypoidGearRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(
        self: "Self",
    ) -> "_1001.KlingelnbergCycloPalloidHypoidGearDesign":
        """mastapy._private.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_KlingelnbergCycloPalloidHypoidGearRating":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergCycloPalloidHypoidGearRating
        """
        return _Cast_KlingelnbergCycloPalloidHypoidGearRating(self)
