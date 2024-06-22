"""AssemblyCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
    _4841,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2487
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4690
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4849,
        _4851,
        _4854,
        _4861,
        _4860,
        _4882,
        _4862,
        _4867,
        _4872,
        _4884,
        _4886,
        _4890,
        _4897,
        _4896,
        _4898,
        _4905,
        _4912,
        _4915,
        _4916,
        _4917,
        _4919,
        _4921,
        _4923,
        _4928,
        _4929,
        _4930,
        _4932,
        _4934,
        _4939,
        _4938,
        _4944,
        _4945,
        _4950,
        _4953,
        _4956,
        _4960,
        _4964,
        _4968,
        _4971,
        _4937,
        _4922,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="AssemblyCompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AssemblyCompoundModalAnalysis._Cast_AssemblyCompoundModalAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyCompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyCompoundModalAnalysis:
    """Special nested class for casting AssemblyCompoundModalAnalysis to subclasses."""

    __parent__: "AssemblyCompoundModalAnalysis"

    @property
    def abstract_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4841.AbstractAssemblyCompoundModalAnalysis":
        return self.__parent__._cast(_4841.AbstractAssemblyCompoundModalAnalysis)

    @property
    def part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4922.PartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4922,
        )

        return self.__parent__._cast(_4922.PartCompoundModalAnalysis)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7708.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def root_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4937.RootAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4937,
        )

        return self.__parent__._cast(_4937.RootAssemblyCompoundModalAnalysis)

    @property
    def assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "AssemblyCompoundModalAnalysis":
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
class AssemblyCompoundModalAnalysis(_4841.AbstractAssemblyCompoundModalAnalysis):
    """AssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ASSEMBLY_COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2487.Assembly":
        """mastapy._private.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4690.AssemblyModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bearings(self: "Self") -> "List[_4849.BearingCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BearingCompoundModalAnalysis]

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
    def belt_drives(self: "Self") -> "List[_4851.BeltDriveCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BeltDriveCompoundModalAnalysis]

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
    ) -> "List[_4854.BevelDifferentialGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearSetCompoundModalAnalysis]

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
    def bolted_joints(self: "Self") -> "List[_4861.BoltedJointCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BoltedJointCompoundModalAnalysis]

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
    def bolts(self: "Self") -> "List[_4860.BoltCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BoltCompoundModalAnalysis]

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
    def cv_ts(self: "Self") -> "List[_4882.CVTCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CVTCompoundModalAnalysis]

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
    def clutches(self: "Self") -> "List[_4862.ClutchCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ClutchCompoundModalAnalysis]

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
    ) -> "List[_4867.ConceptCouplingCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingCompoundModalAnalysis]

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
    ) -> "List[_4872.ConceptGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptGearSetCompoundModalAnalysis]

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
    ) -> "List[_4884.CycloidalAssemblyCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CycloidalAssemblyCompoundModalAnalysis]

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
    def cycloidal_discs(
        self: "Self",
    ) -> "List[_4886.CycloidalDiscCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscCompoundModalAnalysis]

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
    ) -> "List[_4890.CylindricalGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearSetCompoundModalAnalysis]

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
    def fe_parts(self: "Self") -> "List[_4897.FEPartCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FEPartCompoundModalAnalysis]

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
    def face_gear_sets(self: "Self") -> "List[_4896.FaceGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FaceGearSetCompoundModalAnalysis]

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
    ) -> "List[_4898.FlexiblePinAssemblyCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FlexiblePinAssemblyCompoundModalAnalysis]

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
    def hypoid_gear_sets(
        self: "Self",
    ) -> "List[_4905.HypoidGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.HypoidGearSetCompoundModalAnalysis]

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
    ) -> "List[_4912.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]

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
    ) -> "List[_4915.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]

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
    def mass_discs(self: "Self") -> "List[_4916.MassDiscCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MassDiscCompoundModalAnalysis]

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
    ) -> "List[_4917.MeasurementComponentCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MeasurementComponentCompoundModalAnalysis]

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
    def microphones(self: "Self") -> "List[_4919.MicrophoneCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MicrophoneCompoundModalAnalysis]

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
    def oil_seals(self: "Self") -> "List[_4921.OilSealCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.OilSealCompoundModalAnalysis]

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
    ) -> "List[_4923.PartToPartShearCouplingCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingCompoundModalAnalysis]

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
    def planet_carriers(
        self: "Self",
    ) -> "List[_4928.PlanetCarrierCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PlanetCarrierCompoundModalAnalysis]

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
    def point_loads(self: "Self") -> "List[_4929.PointLoadCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PointLoadCompoundModalAnalysis]

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
    def power_loads(self: "Self") -> "List[_4930.PowerLoadCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PowerLoadCompoundModalAnalysis]

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
    def ring_pins(self: "Self") -> "List[_4932.RingPinsCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RingPinsCompoundModalAnalysis]

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
    ) -> "List[_4934.RollingRingAssemblyCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RollingRingAssemblyCompoundModalAnalysis]

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
    ) -> "List[_4939.ShaftHubConnectionCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ShaftHubConnectionCompoundModalAnalysis]

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
    def shafts(self: "Self") -> "List[_4938.ShaftCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ShaftCompoundModalAnalysis]

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
    ) -> "List[_4944.SpiralBevelGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearSetCompoundModalAnalysis]

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
    def spring_dampers(self: "Self") -> "List[_4945.SpringDamperCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpringDamperCompoundModalAnalysis]

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
    ) -> "List[_4950.StraightBevelDiffGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearSetCompoundModalAnalysis]

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
    ) -> "List[_4953.StraightBevelGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearSetCompoundModalAnalysis]

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
    def synchronisers(self: "Self") -> "List[_4956.SynchroniserCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SynchroniserCompoundModalAnalysis]

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
    ) -> "List[_4960.TorqueConverterCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterCompoundModalAnalysis]

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
    ) -> "List[_4964.UnbalancedMassCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.UnbalancedMassCompoundModalAnalysis]

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
    def worm_gear_sets(self: "Self") -> "List[_4968.WormGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.WormGearSetCompoundModalAnalysis]

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
    ) -> "List[_4971.ZerolBevelGearSetCompoundModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearSetCompoundModalAnalysis]

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
    def assembly_analysis_cases(self: "Self") -> "List[_4690.AssemblyModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_AssemblyCompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AssemblyCompoundModalAnalysis
        """
        return _Cast_AssemblyCompoundModalAnalysis(self)
