"""CylindricalGearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.rating import _371
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearMeshRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears import _333, _351
    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.gears.rating.cylindrical.agma import _546
    from mastapy._private.gears.gear_designs.cylindrical import _1048
    from mastapy._private.gears.rating.cylindrical import _478, _475, _471
    from mastapy._private.gears.rating.cylindrical.iso6336 import _531
    from mastapy._private.gears.load_case.cylindrical import _907
    from mastapy._private.gears.rating.cylindrical.vdi import _500
    from mastapy._private.gears.rating import _363
    from mastapy._private.gears.analysis import _1254

    Self = TypeVar("Self", bound="CylindricalGearMeshRating")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearMeshRating._Cast_CylindricalGearMeshRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMeshRating:
    """Special nested class for casting CylindricalGearMeshRating to subclasses."""

    __parent__: "CylindricalGearMeshRating"

    @property
    def gear_mesh_rating(self: "CastSelf") -> "_371.GearMeshRating":
        return self.__parent__._cast(_371.GearMeshRating)

    @property
    def abstract_gear_mesh_rating(self: "CastSelf") -> "_363.AbstractGearMeshRating":
        from mastapy._private.gears.rating import _363

        return self.__parent__._cast(_363.AbstractGearMeshRating)

    @property
    def abstract_gear_mesh_analysis(
        self: "CastSelf",
    ) -> "_1254.AbstractGearMeshAnalysis":
        from mastapy._private.gears.analysis import _1254

        return self.__parent__._cast(_1254.AbstractGearMeshAnalysis)

    @property
    def cylindrical_gear_mesh_rating(self: "CastSelf") -> "CylindricalGearMeshRating":
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
class CylindricalGearMeshRating(_371.GearMeshRating):
    """CylindricalGearMeshRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MESH_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def active_flank(self: "Self") -> "_333.CylindricalFlanks":
        """mastapy._private.gears.CylindricalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.CylindricalFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears._333", "CylindricalFlanks"
        )(value)

    @property
    def load_intensity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadIntensity

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor_source(
        self: "Self",
    ) -> "_351.PlanetaryRatingLoadSharingOption":
        """mastapy._private.gears.PlanetaryRatingLoadSharingOption

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactorSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears._351", "PlanetaryRatingLoadSharingOption"
        )(value)

    @property
    def mechanical_advantage(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MechanicalAdvantage

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_benedict_and_kelley(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionBenedictAndKelley

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_drozdov_and_gavrikov(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionDrozdovAndGavrikov

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotc60(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTC60

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417912001(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417912001

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417912001_with_surface_roughness_parameter(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MeshCoefficientOfFrictionISOTR1417912001WithSurfaceRoughnessParameter
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417922001_martins_et_al(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417922001MartinsEtAl

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417922001(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417922001

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_misharin(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionMisharin

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_o_donoghue_and_cameron(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionODonoghueAndCameron

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_at_diameter_benedict_and_kelley(
        self: "Self",
    ) -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionAtDiameterBenedictAndKelley

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sliding_ratio_at_end_of_recess(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingRatioAtEndOfRecess

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_ratio_at_start_of_approach(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingRatioAtStartOfApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_loss_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def agma_cylindrical_mesh_single_flank_rating(
        self: "Self",
    ) -> "_546.AGMA2101MeshSingleFlankRating":
        """mastapy._private.gears.rating.cylindrical.agma.AGMA2101MeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMACylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_mesh(self: "Self") -> "_1048.CylindricalGearMeshDesign":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_mesh_single_flank_rating(
        self: "Self",
    ) -> "_478.CylindricalMeshSingleFlankRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_rating(self: "Self") -> "_475.CylindricalGearSetRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isodin_cylindrical_mesh_single_flank_rating(
        self: "Self",
    ) -> "_531.ISO6336AbstractMetalMeshSingleFlankRating":
        """mastapy._private.gears.rating.cylindrical.iso6336.ISO6336AbstractMetalMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISODINCylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_load_case(self: "Self") -> "_907.CylindricalMeshLoadCase":
        """mastapy._private.gears.load_case.cylindrical.CylindricalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_single_flank_rating(
        self: "Self",
    ) -> "_478.CylindricalMeshSingleFlankRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def vdi_cylindrical_gear_single_flank_rating(
        self: "Self",
    ) -> "_500.VDI2737InternalGearSingleFlankRating":
        """mastapy._private.gears.rating.cylindrical.vdi.VDI2737InternalGearSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VDICylindricalGearSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_ratings(self: "Self") -> "List[_471.CylindricalGearRating]":
        """List[mastapy._private.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMeshRating":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMeshRating
        """
        return _Cast_CylindricalGearMeshRating(self)
