"""GearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.rating import _364
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearRating")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.materials import _291
    from mastapy._private.gears.rating import _366
    from mastapy._private.gears.rating.zerol_bevel import _381
    from mastapy._private.gears.rating.worm import _385
    from mastapy._private.gears.rating.straight_bevel import _407
    from mastapy._private.gears.rating.straight_bevel_diff import _410
    from mastapy._private.gears.rating.spiral_bevel import _414
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _417
    from mastapy._private.gears.rating.klingelnberg_hypoid import _420
    from mastapy._private.gears.rating.klingelnberg_conical import _423
    from mastapy._private.gears.rating.hypoid import _450
    from mastapy._private.gears.rating.face import _459
    from mastapy._private.gears.rating.cylindrical import _471
    from mastapy._private.gears.rating.conical import _551
    from mastapy._private.gears.rating.concept import _562
    from mastapy._private.gears.rating.bevel import _566
    from mastapy._private.gears.rating.agma_gleason_conical import _577
    from mastapy._private.gears.analysis import _1253

    Self = TypeVar("Self", bound="GearRating")
    CastSelf = TypeVar("CastSelf", bound="GearRating._Cast_GearRating")


__docformat__ = "restructuredtext en"
__all__ = ("GearRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearRating:
    """Special nested class for casting GearRating to subclasses."""

    __parent__: "GearRating"

    @property
    def abstract_gear_rating(self: "CastSelf") -> "_364.AbstractGearRating":
        return self.__parent__._cast(_364.AbstractGearRating)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def zerol_bevel_gear_rating(self: "CastSelf") -> "_381.ZerolBevelGearRating":
        from mastapy._private.gears.rating.zerol_bevel import _381

        return self.__parent__._cast(_381.ZerolBevelGearRating)

    @property
    def worm_gear_rating(self: "CastSelf") -> "_385.WormGearRating":
        from mastapy._private.gears.rating.worm import _385

        return self.__parent__._cast(_385.WormGearRating)

    @property
    def straight_bevel_gear_rating(self: "CastSelf") -> "_407.StraightBevelGearRating":
        from mastapy._private.gears.rating.straight_bevel import _407

        return self.__parent__._cast(_407.StraightBevelGearRating)

    @property
    def straight_bevel_diff_gear_rating(
        self: "CastSelf",
    ) -> "_410.StraightBevelDiffGearRating":
        from mastapy._private.gears.rating.straight_bevel_diff import _410

        return self.__parent__._cast(_410.StraightBevelDiffGearRating)

    @property
    def spiral_bevel_gear_rating(self: "CastSelf") -> "_414.SpiralBevelGearRating":
        from mastapy._private.gears.rating.spiral_bevel import _414

        return self.__parent__._cast(_414.SpiralBevelGearRating)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
        self: "CastSelf",
    ) -> "_417.KlingelnbergCycloPalloidSpiralBevelGearRating":
        from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _417

        return self.__parent__._cast(_417.KlingelnbergCycloPalloidSpiralBevelGearRating)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_rating(
        self: "CastSelf",
    ) -> "_420.KlingelnbergCycloPalloidHypoidGearRating":
        from mastapy._private.gears.rating.klingelnberg_hypoid import _420

        return self.__parent__._cast(_420.KlingelnbergCycloPalloidHypoidGearRating)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_rating(
        self: "CastSelf",
    ) -> "_423.KlingelnbergCycloPalloidConicalGearRating":
        from mastapy._private.gears.rating.klingelnberg_conical import _423

        return self.__parent__._cast(_423.KlingelnbergCycloPalloidConicalGearRating)

    @property
    def hypoid_gear_rating(self: "CastSelf") -> "_450.HypoidGearRating":
        from mastapy._private.gears.rating.hypoid import _450

        return self.__parent__._cast(_450.HypoidGearRating)

    @property
    def face_gear_rating(self: "CastSelf") -> "_459.FaceGearRating":
        from mastapy._private.gears.rating.face import _459

        return self.__parent__._cast(_459.FaceGearRating)

    @property
    def cylindrical_gear_rating(self: "CastSelf") -> "_471.CylindricalGearRating":
        from mastapy._private.gears.rating.cylindrical import _471

        return self.__parent__._cast(_471.CylindricalGearRating)

    @property
    def conical_gear_rating(self: "CastSelf") -> "_551.ConicalGearRating":
        from mastapy._private.gears.rating.conical import _551

        return self.__parent__._cast(_551.ConicalGearRating)

    @property
    def concept_gear_rating(self: "CastSelf") -> "_562.ConceptGearRating":
        from mastapy._private.gears.rating.concept import _562

        return self.__parent__._cast(_562.ConceptGearRating)

    @property
    def bevel_gear_rating(self: "CastSelf") -> "_566.BevelGearRating":
        from mastapy._private.gears.rating.bevel import _566

        return self.__parent__._cast(_566.BevelGearRating)

    @property
    def agma_gleason_conical_gear_rating(
        self: "CastSelf",
    ) -> "_577.AGMAGleasonConicalGearRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _577

        return self.__parent__._cast(_577.AGMAGleasonConicalGearRating)

    @property
    def gear_rating(self: "CastSelf") -> "GearRating":
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
class GearRating(_364.AbstractGearRating):
    """GearRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bending_safety_factor_results(self: "Self") -> "_291.SafetyFactorItem":
        """mastapy._private.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_safety_factor_results(self: "Self") -> "_291.SafetyFactorItem":
        """mastapy._private.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_safety_factor(self: "Self") -> "_366.BendingAndContactReportingObject":
        """mastapy._private.gears.rating.BendingAndContactReportingObject

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearRating":
        """Cast to another type.

        Returns:
            _Cast_GearRating
        """
        return _Cast_GearRating(self)
