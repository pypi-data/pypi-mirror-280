"""ISO6336AbstractMetalGearSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private.gears.rating.cylindrical.iso6336 import _528
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ISO6336AbstractMetalGearSingleFlankRating",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.cylindrical.iso6336 import _522, _524, _526
    from mastapy._private.gears.rating.cylindrical.din3990 import _543
    from mastapy._private.gears.rating.cylindrical import _476
    from mastapy._private.gears.rating import _375

    Self = TypeVar("Self", bound="ISO6336AbstractMetalGearSingleFlankRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336AbstractMetalGearSingleFlankRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISO6336AbstractMetalGearSingleFlankRating:
    """Special nested class for casting ISO6336AbstractMetalGearSingleFlankRating to subclasses."""

    __parent__: "ISO6336AbstractMetalGearSingleFlankRating"

    @property
    def iso6336_abstract_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_528.ISO6336AbstractGearSingleFlankRating":
        return self.__parent__._cast(_528.ISO6336AbstractGearSingleFlankRating)

    @property
    def cylindrical_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_476.CylindricalGearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical import _476

        return self.__parent__._cast(_476.CylindricalGearSingleFlankRating)

    @property
    def gear_single_flank_rating(self: "CastSelf") -> "_375.GearSingleFlankRating":
        from mastapy._private.gears.rating import _375

        return self.__parent__._cast(_375.GearSingleFlankRating)

    @property
    def iso63361996_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_522.ISO63361996GearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _522

        return self.__parent__._cast(_522.ISO63361996GearSingleFlankRating)

    @property
    def iso63362006_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_524.ISO63362006GearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _524

        return self.__parent__._cast(_524.ISO63362006GearSingleFlankRating)

    @property
    def iso63362019_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_526.ISO63362019GearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _526

        return self.__parent__._cast(_526.ISO63362019GearSingleFlankRating)

    @property
    def din3990_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_543.DIN3990GearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.din3990 import _543

        return self.__parent__._cast(_543.DIN3990GearSingleFlankRating)

    @property
    def iso6336_abstract_metal_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "ISO6336AbstractMetalGearSingleFlankRating":
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
class ISO6336AbstractMetalGearSingleFlankRating(
    _528.ISO6336AbstractGearSingleFlankRating
):
    """ISO6336AbstractMetalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def addendum_contact_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_deviation(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def life_factor_for_bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_reference_bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForReferenceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_reference_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_static_bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForStaticBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_static_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorForStaticContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_of_inertia_per_unit_face_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentOfInertiaPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def relative_individual_gear_mass_per_unit_face_width_referenced_to_line_of_action(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeIndividualGearMassPerUnitFaceWidthReferencedToLineOfAction
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactorForStaticStress

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
    def relative_surface_factor_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def shot_peening_bending_stress_benefit(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShotPeeningBendingStressBenefit

        if temp is None:
            return 0.0

        return temp

    @property
    def single_pair_tooth_contact_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePairToothContactFactor

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
    def size_factor_tooth_root(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_reference_bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForReferenceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_reference_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def static_size_factor_tooth_root(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSizeFactorToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkHardeningFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_ISO6336AbstractMetalGearSingleFlankRating":
        """Cast to another type.

        Returns:
            _Cast_ISO6336AbstractMetalGearSingleFlankRating
        """
        return _Cast_ISO6336AbstractMetalGearSingleFlankRating(self)
