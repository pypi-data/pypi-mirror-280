"""KlingelnbergCycloPalloidConicalGearSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.rating import _375
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030",
    "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.klingelnberg_conical.kn3030 import _428

    Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSingleFlankRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergCycloPalloidConicalGearSingleFlankRating._Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSingleFlankRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating:
    """Special nested class for casting KlingelnbergCycloPalloidConicalGearSingleFlankRating to subclasses."""

    __parent__: "KlingelnbergCycloPalloidConicalGearSingleFlankRating"

    @property
    def gear_single_flank_rating(self: "CastSelf") -> "_375.GearSingleFlankRating":
        return self.__parent__._cast(_375.GearSingleFlankRating)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_428.KlingelnbergCycloPalloidHypoidGearSingleFlankRating":
        from mastapy._private.gears.rating.klingelnberg_conical.kn3030 import _428

        return self.__parent__._cast(
            _428.KlingelnbergCycloPalloidHypoidGearSingleFlankRating
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "KlingelnbergCycloPalloidConicalGearSingleFlankRating":
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
class KlingelnbergCycloPalloidConicalGearSingleFlankRating(_375.GearSingleFlankRating):
    """KlingelnbergCycloPalloidConicalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SINGLE_FLANK_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def allowable_bending_stress_number(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBendingStressNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress_number(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStressNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_stress_limit(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_stress_safety_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_roughness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankRoughness

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_tangential_force(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedTangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_torque(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_sensitivity_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSensitivityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_speed(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFormFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating
        """
        return _Cast_KlingelnbergCycloPalloidConicalGearSingleFlankRating(self)
