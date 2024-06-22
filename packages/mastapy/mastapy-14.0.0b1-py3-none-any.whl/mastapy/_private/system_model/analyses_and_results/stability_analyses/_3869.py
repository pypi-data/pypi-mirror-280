"""AssemblyStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.stability_analyses import _3862
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2487
    from mastapy._private.system_model.analyses_and_results.static_loads import _6965
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3870,
        _3872,
        _3874,
        _3881,
        _3882,
        _3905,
        _3885,
        _3890,
        _3892,
        _3906,
        _3909,
        _3911,
        _3920,
        _3918,
        _3921,
        _3927,
        _3934,
        _3937,
        _3939,
        _3940,
        _3942,
        _3944,
        _3948,
        _3951,
        _3952,
        _3953,
        _3955,
        _3957,
        _3961,
        _3962,
        _3966,
        _3970,
        _3975,
        _3978,
        _3985,
        _3988,
        _3990,
        _3993,
        _3996,
        _3960,
        _3945,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="AssemblyStabilityAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="AssemblyStabilityAnalysis._Cast_AssemblyStabilityAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyStabilityAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyStabilityAnalysis:
    """Special nested class for casting AssemblyStabilityAnalysis to subclasses."""

    __parent__: "AssemblyStabilityAnalysis"

    @property
    def abstract_assembly_stability_analysis(
        self: "CastSelf",
    ) -> "_3862.AbstractAssemblyStabilityAnalysis":
        return self.__parent__._cast(_3862.AbstractAssemblyStabilityAnalysis)

    @property
    def part_stability_analysis(self: "CastSelf") -> "_3945.PartStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3945,
        )

        return self.__parent__._cast(_3945.PartStabilityAnalysis)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def root_assembly_stability_analysis(
        self: "CastSelf",
    ) -> "_3960.RootAssemblyStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3960,
        )

        return self.__parent__._cast(_3960.RootAssemblyStabilityAnalysis)

    @property
    def assembly_stability_analysis(self: "CastSelf") -> "AssemblyStabilityAnalysis":
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
class AssemblyStabilityAnalysis(_3862.AbstractAssemblyStabilityAnalysis):
    """AssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ASSEMBLY_STABILITY_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2487.Assembly":
        """mastapy._private.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_6965.AssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearings(self: "Self") -> "List[_3870.BearingStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.BearingStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def belt_drives(self: "Self") -> "List[_3872.BeltDriveStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.BeltDriveStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gear_sets(
        self: "Self",
    ) -> "List[_3874.BevelDifferentialGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolted_joints(self: "Self") -> "List[_3881.BoltedJointStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.BoltedJointStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolts(self: "Self") -> "List[_3882.BoltStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.BoltStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cv_ts(self: "Self") -> "List[_3905.CVTStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.CVTStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def clutches(self: "Self") -> "List[_3885.ClutchStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ClutchStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_couplings(
        self: "Self",
    ) -> "List[_3890.ConceptCouplingStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ConceptCouplingStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gear_sets(
        self: "Self",
    ) -> "List[_3892.ConceptGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ConceptGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_assemblies(
        self: "Self",
    ) -> "List[_3906.CycloidalAssemblyStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.CycloidalAssemblyStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_discs(self: "Self") -> "List[_3909.CycloidalDiscStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.CycloidalDiscStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(
        self: "Self",
    ) -> "List[_3911.CylindricalGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.CylindricalGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(self: "Self") -> "List[_3920.FEPartStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.FEPartStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gear_sets(self: "Self") -> "List[_3918.FaceGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.FaceGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_assemblies(
        self: "Self",
    ) -> "List[_3921.FlexiblePinAssemblyStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.FlexiblePinAssemblyStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gear_sets(self: "Self") -> "List[_3927.HypoidGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.HypoidGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(
        self: "Self",
    ) -> "List[_3934.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(
        self: "Self",
    ) -> "List[_3937.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_discs(self: "Self") -> "List[_3939.MassDiscStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.MassDiscStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def measurement_components(
        self: "Self",
    ) -> "List[_3940.MeasurementComponentStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.MeasurementComponentStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def microphones(self: "Self") -> "List[_3942.MicrophoneStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.MicrophoneStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Microphones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def oil_seals(self: "Self") -> "List[_3944.OilSealStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.OilSealStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def part_to_part_shear_couplings(
        self: "Self",
    ) -> "List[_3948.PartToPartShearCouplingStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.PartToPartShearCouplingStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planet_carriers(self: "Self") -> "List[_3951.PlanetCarrierStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.PlanetCarrierStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(self: "Self") -> "List[_3952.PointLoadStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.PointLoadStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_loads(self: "Self") -> "List[_3953.PowerLoadStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.PowerLoadStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_pins(self: "Self") -> "List[_3955.RingPinsStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.RingPinsStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rolling_ring_assemblies(
        self: "Self",
    ) -> "List[_3957.RollingRingAssemblyStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.RollingRingAssemblyStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_hub_connections(
        self: "Self",
    ) -> "List[_3961.ShaftHubConnectionStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ShaftHubConnectionStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shafts(self: "Self") -> "List[_3962.ShaftStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ShaftStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gear_sets(
        self: "Self",
    ) -> "List[_3966.SpiralBevelGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.SpiralBevelGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dampers(self: "Self") -> "List[_3970.SpringDamperStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.SpringDamperStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gear_sets(
        self: "Self",
    ) -> "List[_3975.StraightBevelDiffGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gear_sets(
        self: "Self",
    ) -> "List[_3978.StraightBevelGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.StraightBevelGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def synchronisers(self: "Self") -> "List[_3985.SynchroniserStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.SynchroniserStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def torque_converters(
        self: "Self",
    ) -> "List[_3988.TorqueConverterStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.TorqueConverterStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def unbalanced_masses(
        self: "Self",
    ) -> "List[_3990.UnbalancedMassStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.UnbalancedMassStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_sets(self: "Self") -> "List[_3993.WormGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.WormGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gear_sets(
        self: "Self",
    ) -> "List[_3996.ZerolBevelGearSetStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ZerolBevelGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_AssemblyStabilityAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AssemblyStabilityAnalysis
        """
        return _Cast_AssemblyStabilityAnalysis(self)
