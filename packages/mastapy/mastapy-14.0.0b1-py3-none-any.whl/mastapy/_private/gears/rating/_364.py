"""AbstractGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.analysis import _1253
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating import _368, _372
    from mastapy._private.gears.rating.zerol_bevel import _381
    from mastapy._private.gears.rating.worm import _383, _385
    from mastapy._private.gears.rating.straight_bevel import _407
    from mastapy._private.gears.rating.straight_bevel_diff import _410
    from mastapy._private.gears.rating.spiral_bevel import _414
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _417
    from mastapy._private.gears.rating.klingelnberg_hypoid import _420
    from mastapy._private.gears.rating.klingelnberg_conical import _423
    from mastapy._private.gears.rating.hypoid import _450
    from mastapy._private.gears.rating.face import _456, _459
    from mastapy._private.gears.rating.cylindrical import _466, _471
    from mastapy._private.gears.rating.conical import _549, _551
    from mastapy._private.gears.rating.concept import _559, _562
    from mastapy._private.gears.rating.bevel import _566
    from mastapy._private.gears.rating.agma_gleason_conical import _577

    Self = TypeVar("Self", bound="AbstractGearRating")
    CastSelf = TypeVar("CastSelf", bound="AbstractGearRating._Cast_AbstractGearRating")


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractGearRating:
    """Special nested class for casting AbstractGearRating to subclasses."""

    __parent__: "AbstractGearRating"

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def gear_duty_cycle_rating(self: "CastSelf") -> "_368.GearDutyCycleRating":
        from mastapy._private.gears.rating import _368

        return self.__parent__._cast(_368.GearDutyCycleRating)

    @property
    def gear_rating(self: "CastSelf") -> "_372.GearRating":
        from mastapy._private.gears.rating import _372

        return self.__parent__._cast(_372.GearRating)

    @property
    def zerol_bevel_gear_rating(self: "CastSelf") -> "_381.ZerolBevelGearRating":
        from mastapy._private.gears.rating.zerol_bevel import _381

        return self.__parent__._cast(_381.ZerolBevelGearRating)

    @property
    def worm_gear_duty_cycle_rating(self: "CastSelf") -> "_383.WormGearDutyCycleRating":
        from mastapy._private.gears.rating.worm import _383

        return self.__parent__._cast(_383.WormGearDutyCycleRating)

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
    def face_gear_duty_cycle_rating(self: "CastSelf") -> "_456.FaceGearDutyCycleRating":
        from mastapy._private.gears.rating.face import _456

        return self.__parent__._cast(_456.FaceGearDutyCycleRating)

    @property
    def face_gear_rating(self: "CastSelf") -> "_459.FaceGearRating":
        from mastapy._private.gears.rating.face import _459

        return self.__parent__._cast(_459.FaceGearRating)

    @property
    def cylindrical_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_466.CylindricalGearDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _466

        return self.__parent__._cast(_466.CylindricalGearDutyCycleRating)

    @property
    def cylindrical_gear_rating(self: "CastSelf") -> "_471.CylindricalGearRating":
        from mastapy._private.gears.rating.cylindrical import _471

        return self.__parent__._cast(_471.CylindricalGearRating)

    @property
    def conical_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_549.ConicalGearDutyCycleRating":
        from mastapy._private.gears.rating.conical import _549

        return self.__parent__._cast(_549.ConicalGearDutyCycleRating)

    @property
    def conical_gear_rating(self: "CastSelf") -> "_551.ConicalGearRating":
        from mastapy._private.gears.rating.conical import _551

        return self.__parent__._cast(_551.ConicalGearRating)

    @property
    def concept_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_559.ConceptGearDutyCycleRating":
        from mastapy._private.gears.rating.concept import _559

        return self.__parent__._cast(_559.ConceptGearDutyCycleRating)

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
    def abstract_gear_rating(self: "CastSelf") -> "AbstractGearRating":
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
class AbstractGearRating(_1253.AbstractGearAnalysis):
    """AbstractGearRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_GEAR_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bending_safety_factor_for_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_reliability_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_reliability_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_bending_safety_factor_for_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedBendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_bending_safety_factor_for_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedBendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_contact_safety_factor_for_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_contact_safety_factor_for_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_safety_factor_for_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_safety_factor_for_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def total_gear_reliability(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractGearRating":
        """Cast to another type.

        Returns:
            _Cast_AbstractGearRating
        """
        return _Cast_AbstractGearRating(self)
