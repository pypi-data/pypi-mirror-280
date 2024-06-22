"""AbstractGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.analysis import _1255
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearSetRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears import _338
    from mastapy._private.gears.rating import _363, _364, _373, _374
    from mastapy._private.gears.rating.zerol_bevel import _382
    from mastapy._private.gears.rating.worm import _386, _387
    from mastapy._private.gears.rating.straight_bevel import _408
    from mastapy._private.gears.rating.straight_bevel_diff import _411
    from mastapy._private.gears.rating.spiral_bevel import _415
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _418
    from mastapy._private.gears.rating.klingelnberg_hypoid import _421
    from mastapy._private.gears.rating.klingelnberg_conical import _424
    from mastapy._private.gears.rating.hypoid import _451
    from mastapy._private.gears.rating.face import _460, _461
    from mastapy._private.gears.rating.cylindrical import _474, _475, _491
    from mastapy._private.gears.rating.conical import _552, _553
    from mastapy._private.gears.rating.concept import _563, _564
    from mastapy._private.gears.rating.bevel import _567
    from mastapy._private.gears.rating.agma_gleason_conical import _578

    Self = TypeVar("Self", bound="AbstractGearSetRating")
    CastSelf = TypeVar(
        "CastSelf", bound="AbstractGearSetRating._Cast_AbstractGearSetRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractGearSetRating:
    """Special nested class for casting AbstractGearSetRating to subclasses."""

    __parent__: "AbstractGearSetRating"

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        return self.__parent__._cast(_1255.AbstractGearSetAnalysis)

    @property
    def gear_set_duty_cycle_rating(self: "CastSelf") -> "_373.GearSetDutyCycleRating":
        from mastapy._private.gears.rating import _373

        return self.__parent__._cast(_373.GearSetDutyCycleRating)

    @property
    def gear_set_rating(self: "CastSelf") -> "_374.GearSetRating":
        from mastapy._private.gears.rating import _374

        return self.__parent__._cast(_374.GearSetRating)

    @property
    def zerol_bevel_gear_set_rating(self: "CastSelf") -> "_382.ZerolBevelGearSetRating":
        from mastapy._private.gears.rating.zerol_bevel import _382

        return self.__parent__._cast(_382.ZerolBevelGearSetRating)

    @property
    def worm_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_386.WormGearSetDutyCycleRating":
        from mastapy._private.gears.rating.worm import _386

        return self.__parent__._cast(_386.WormGearSetDutyCycleRating)

    @property
    def worm_gear_set_rating(self: "CastSelf") -> "_387.WormGearSetRating":
        from mastapy._private.gears.rating.worm import _387

        return self.__parent__._cast(_387.WormGearSetRating)

    @property
    def straight_bevel_gear_set_rating(
        self: "CastSelf",
    ) -> "_408.StraightBevelGearSetRating":
        from mastapy._private.gears.rating.straight_bevel import _408

        return self.__parent__._cast(_408.StraightBevelGearSetRating)

    @property
    def straight_bevel_diff_gear_set_rating(
        self: "CastSelf",
    ) -> "_411.StraightBevelDiffGearSetRating":
        from mastapy._private.gears.rating.straight_bevel_diff import _411

        return self.__parent__._cast(_411.StraightBevelDiffGearSetRating)

    @property
    def spiral_bevel_gear_set_rating(
        self: "CastSelf",
    ) -> "_415.SpiralBevelGearSetRating":
        from mastapy._private.gears.rating.spiral_bevel import _415

        return self.__parent__._cast(_415.SpiralBevelGearSetRating)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
        self: "CastSelf",
    ) -> "_418.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _418

        return self.__parent__._cast(
            _418.KlingelnbergCycloPalloidSpiralBevelGearSetRating
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
        self: "CastSelf",
    ) -> "_421.KlingelnbergCycloPalloidHypoidGearSetRating":
        from mastapy._private.gears.rating.klingelnberg_hypoid import _421

        return self.__parent__._cast(_421.KlingelnbergCycloPalloidHypoidGearSetRating)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_rating(
        self: "CastSelf",
    ) -> "_424.KlingelnbergCycloPalloidConicalGearSetRating":
        from mastapy._private.gears.rating.klingelnberg_conical import _424

        return self.__parent__._cast(_424.KlingelnbergCycloPalloidConicalGearSetRating)

    @property
    def hypoid_gear_set_rating(self: "CastSelf") -> "_451.HypoidGearSetRating":
        from mastapy._private.gears.rating.hypoid import _451

        return self.__parent__._cast(_451.HypoidGearSetRating)

    @property
    def face_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_460.FaceGearSetDutyCycleRating":
        from mastapy._private.gears.rating.face import _460

        return self.__parent__._cast(_460.FaceGearSetDutyCycleRating)

    @property
    def face_gear_set_rating(self: "CastSelf") -> "_461.FaceGearSetRating":
        from mastapy._private.gears.rating.face import _461

        return self.__parent__._cast(_461.FaceGearSetRating)

    @property
    def cylindrical_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_474.CylindricalGearSetDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _474

        return self.__parent__._cast(_474.CylindricalGearSetDutyCycleRating)

    @property
    def cylindrical_gear_set_rating(
        self: "CastSelf",
    ) -> "_475.CylindricalGearSetRating":
        from mastapy._private.gears.rating.cylindrical import _475

        return self.__parent__._cast(_475.CylindricalGearSetRating)

    @property
    def reduced_cylindrical_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_491.ReducedCylindricalGearSetDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _491

        return self.__parent__._cast(_491.ReducedCylindricalGearSetDutyCycleRating)

    @property
    def conical_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_552.ConicalGearSetDutyCycleRating":
        from mastapy._private.gears.rating.conical import _552

        return self.__parent__._cast(_552.ConicalGearSetDutyCycleRating)

    @property
    def conical_gear_set_rating(self: "CastSelf") -> "_553.ConicalGearSetRating":
        from mastapy._private.gears.rating.conical import _553

        return self.__parent__._cast(_553.ConicalGearSetRating)

    @property
    def concept_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_563.ConceptGearSetDutyCycleRating":
        from mastapy._private.gears.rating.concept import _563

        return self.__parent__._cast(_563.ConceptGearSetDutyCycleRating)

    @property
    def concept_gear_set_rating(self: "CastSelf") -> "_564.ConceptGearSetRating":
        from mastapy._private.gears.rating.concept import _564

        return self.__parent__._cast(_564.ConceptGearSetRating)

    @property
    def bevel_gear_set_rating(self: "CastSelf") -> "_567.BevelGearSetRating":
        from mastapy._private.gears.rating.bevel import _567

        return self.__parent__._cast(_567.BevelGearSetRating)

    @property
    def agma_gleason_conical_gear_set_rating(
        self: "CastSelf",
    ) -> "_578.AGMAGleasonConicalGearSetRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _578

        return self.__parent__._cast(_578.AGMAGleasonConicalGearSetRating)

    @property
    def abstract_gear_set_rating(self: "CastSelf") -> "AbstractGearSetRating":
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
class AbstractGearSetRating(_1255.AbstractGearSetAnalysis):
    """AbstractGearSetRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_GEAR_SET_RATING

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
    def normalised_safety_factor_for_fatigue_and_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForFatigueAndStatic

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
    def transmission_properties_gears(self: "Self") -> "_338.GearSetDesignGroup":
        """mastapy._private.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: "Self") -> "List[_363.AbstractGearMeshRating]":
        """List[mastapy._private.gears.rating.AbstractGearMeshRating]

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
    def gear_ratings(self: "Self") -> "List[_364.AbstractGearRating]":
        """List[mastapy._private.gears.rating.AbstractGearRating]

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
    def cast_to(self: "Self") -> "_Cast_AbstractGearSetRating":
        """Cast to another type.

        Returns:
            _Cast_AbstractGearSetRating
        """
        return _Cast_AbstractGearSetRating(self)
