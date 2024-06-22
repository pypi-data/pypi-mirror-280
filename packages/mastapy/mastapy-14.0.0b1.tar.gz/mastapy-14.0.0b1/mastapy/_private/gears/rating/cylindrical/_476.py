"""CylindricalGearSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private.gears.rating import _375
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearSingleFlankRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.cylindrical import _472
    from mastapy._private.gears.rating import _367
    from mastapy._private.materials import _286
    from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import (
        _502,
        _507,
        _508,
    )
    from mastapy._private.gears.rating.cylindrical.iso6336 import (
        _522,
        _524,
        _526,
        _528,
        _530,
    )
    from mastapy._private.gears.rating.cylindrical.din3990 import _543
    from mastapy._private.gears.rating.cylindrical.agma import _545

    Self = TypeVar("Self", bound="CylindricalGearSingleFlankRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearSingleFlankRating._Cast_CylindricalGearSingleFlankRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSingleFlankRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSingleFlankRating:
    """Special nested class for casting CylindricalGearSingleFlankRating to subclasses."""

    __parent__: "CylindricalGearSingleFlankRating"

    @property
    def gear_single_flank_rating(self: "CastSelf") -> "_375.GearSingleFlankRating":
        return self.__parent__._cast(_375.GearSingleFlankRating)

    @property
    def plastic_gear_vdi2736_abstract_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_502.PlasticGearVDI2736AbstractGearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _502

        return self.__parent__._cast(
            _502.PlasticGearVDI2736AbstractGearSingleFlankRating
        )

    @property
    def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(
        self: "CastSelf",
    ) -> "_507.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _507

        return self.__parent__._cast(
            _507.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh
        )

    @property
    def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(
        self: "CastSelf",
    ) -> "_508.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _508

        return self.__parent__._cast(
            _508.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
        )

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
    def iso6336_abstract_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_528.ISO6336AbstractGearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _528

        return self.__parent__._cast(_528.ISO6336AbstractGearSingleFlankRating)

    @property
    def iso6336_abstract_metal_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_530.ISO6336AbstractMetalGearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _530

        return self.__parent__._cast(_530.ISO6336AbstractMetalGearSingleFlankRating)

    @property
    def din3990_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_543.DIN3990GearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.din3990 import _543

        return self.__parent__._cast(_543.DIN3990GearSingleFlankRating)

    @property
    def agma2101_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "_545.AGMA2101GearSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.agma import _545

        return self.__parent__._cast(_545.AGMA2101GearSingleFlankRating)

    @property
    def cylindrical_gear_single_flank_rating(
        self: "CastSelf",
    ) -> "CylindricalGearSingleFlankRating":
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
class CylindricalGearSingleFlankRating(_375.GearSingleFlankRating):
    """CylindricalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SINGLE_FLANK_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def allowable_stress_number_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_number_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def averaged_linear_wear(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragedLinearWear

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def base_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_helix_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseHelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def base_transverse_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseTransversePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_moment_arm(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingMomentArm

        if temp is None:
            return 0.0

        return temp

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
    def calculated_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_tip_relief(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedTipRelief

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
    def contact_stress_source(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressSource

        if temp is None:
            return ""

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
    def damage_wear(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageWear

        if temp is None:
            return 0.0

        return temp

    @property
    def fillet_roughness_rz(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletRoughnessRz

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_roughness_rz(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankRoughnessRz

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_rotation_speed(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRotationSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_data_source_for_rating(
        self: "Self",
    ) -> "_472.CylindricalGearRatingGeometryDataSource":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearRatingGeometryDataSource

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryDataSourceForRating

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.CylindricalGearRatingGeometryDataSource",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating.cylindrical._472",
            "CylindricalGearRatingGeometryDataSource",
        )(value)

    @property
    def helix_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def is_gear_driving_or_driven(self: "Self") -> "_367.FlankLoadingState":
        """mastapy._private.gears.rating.FlankLoadingState

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsGearDrivingOrDriven

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.FlankLoadingState"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._367", "FlankLoadingState"
        )(value)

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
    def metal_plastic(self: "Self") -> "_286.MetalPlasticType":
        """mastapy._private.materials.MetalPlasticType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MetalPlastic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.MetalPlasticType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._286", "MetalPlasticType"
        )(value)

    @property
    def minimum_factor_of_safety_bending_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFactorOfSafetyBendingFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_factor_of_safety_pitting_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFactorOfSafetyPittingFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_stress_number_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_module(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStressForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStressForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_linear_wear(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleLinearWear

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_bending_stress_for_reference_stress(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothRootBendingStressForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_bending_stress_for_static_stress(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothRootBendingStressForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_stress_limit(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_stress_limit_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingStressLimitForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_stress_limit_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingStressLimitForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def reversed_bending_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReversedBendingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def rim_thickness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RimThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RimThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_over_normal_module(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RimThicknessOverNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_wear(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorWear

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_cycle_factor_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCycleFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_contact_coefficient_for_report(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalContactCoefficientForReport

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chord_at_critical_section(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootChordAtCriticalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_limit(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_limit_for_reference_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressLimitForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_limit_for_static_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressLimitForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_source(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressSource

        if temp is None:
            return ""

        return temp

    @property
    def transverse_module(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseModule

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def welding_structural_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WeldingStructuralFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSingleFlankRating":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSingleFlankRating
        """
        return _Cast_CylindricalGearSingleFlankRating(self)
