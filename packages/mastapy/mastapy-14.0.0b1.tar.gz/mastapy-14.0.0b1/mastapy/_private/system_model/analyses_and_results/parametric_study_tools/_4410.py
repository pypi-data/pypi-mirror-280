"""AssemblyParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
    _4403,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2487
    from mastapy._private.system_model.analyses_and_results.static_loads import _6965
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4457,
        _4411,
        _4413,
        _4416,
        _4422,
        _4423,
        _4444,
        _4426,
        _4431,
        _4434,
        _4446,
        _4448,
        _4452,
        _4466,
        _4465,
        _4467,
        _4474,
        _4481,
        _4484,
        _4485,
        _4486,
        _4488,
        _4491,
        _4505,
        _4508,
        _4509,
        _4510,
        _4512,
        _4514,
        _4518,
        _4519,
        _4524,
        _4527,
        _4530,
        _4533,
        _4537,
        _4541,
        _4544,
        _4548,
        _4551,
        _4517,
        _4502,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2775,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7710
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="AssemblyParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AssemblyParametricStudyTool._Cast_AssemblyParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyParametricStudyTool:
    """Special nested class for casting AssemblyParametricStudyTool to subclasses."""

    __parent__: "AssemblyParametricStudyTool"

    @property
    def abstract_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4403.AbstractAssemblyParametricStudyTool":
        return self.__parent__._cast(_4403.AbstractAssemblyParametricStudyTool)

    @property
    def part_parametric_study_tool(self: "CastSelf") -> "_4502.PartParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4502,
        )

        return self.__parent__._cast(_4502.PartParametricStudyTool)

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
    def root_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4517.RootAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4517,
        )

        return self.__parent__._cast(_4517.RootAssemblyParametricStudyTool)

    @property
    def assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "AssemblyParametricStudyTool":
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
class AssemblyParametricStudyTool(_4403.AbstractAssemblyParametricStudyTool):
    """AssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ASSEMBLY_PARAMETRIC_STUDY_TOOL

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
    def all_duty_cycle_results(
        self: "Self",
    ) -> "List[_4457.DutyCycleResultsForAllComponents]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.DutyCycleResultsForAllComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDutyCycleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_system_deflection_results(
        self: "Self",
    ) -> "List[_2775.AssemblySystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bearings(self: "Self") -> "List[_4411.BearingParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.BearingParametricStudyTool]

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
    def belt_drives(self: "Self") -> "List[_4413.BeltDriveParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.BeltDriveParametricStudyTool]

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
    ) -> "List[_4416.BevelDifferentialGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearSetParametricStudyTool]

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
    def bolted_joints(self: "Self") -> "List[_4422.BoltedJointParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.BoltedJointParametricStudyTool]

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
    def bolts(self: "Self") -> "List[_4423.BoltParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.BoltParametricStudyTool]

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
    def cv_ts(self: "Self") -> "List[_4444.CVTParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CVTParametricStudyTool]

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
    def clutches(self: "Self") -> "List[_4426.ClutchParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ClutchParametricStudyTool]

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
    ) -> "List[_4431.ConceptCouplingParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingParametricStudyTool]

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
    ) -> "List[_4434.ConceptGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ConceptGearSetParametricStudyTool]

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
    ) -> "List[_4446.CycloidalAssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CycloidalAssemblyParametricStudyTool]

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
    def cycloidal_discs(self: "Self") -> "List[_4448.CycloidalDiscParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscParametricStudyTool]

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
    ) -> "List[_4452.CylindricalGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CylindricalGearSetParametricStudyTool]

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
    def fe_parts(self: "Self") -> "List[_4466.FEPartParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.FEPartParametricStudyTool]

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
    def face_gear_sets(self: "Self") -> "List[_4465.FaceGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.FaceGearSetParametricStudyTool]

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
    ) -> "List[_4467.FlexiblePinAssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.FlexiblePinAssemblyParametricStudyTool]

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
    ) -> "List[_4474.HypoidGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.HypoidGearSetParametricStudyTool]

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
    ) -> "List[_4481.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]

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
    ) -> "List[_4484.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool]

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
    def mass_discs(self: "Self") -> "List[_4485.MassDiscParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.MassDiscParametricStudyTool]

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
    ) -> "List[_4486.MeasurementComponentParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.MeasurementComponentParametricStudyTool]

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
    def microphones(self: "Self") -> "List[_4488.MicrophoneParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.MicrophoneParametricStudyTool]

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
    def oil_seals(self: "Self") -> "List[_4491.OilSealParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.OilSealParametricStudyTool]

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
    ) -> "List[_4505.PartToPartShearCouplingParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingParametricStudyTool]

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
    def planet_carriers(self: "Self") -> "List[_4508.PlanetCarrierParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.PlanetCarrierParametricStudyTool]

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
    def point_loads(self: "Self") -> "List[_4509.PointLoadParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool]

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
    def power_loads(self: "Self") -> "List[_4510.PowerLoadParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.PowerLoadParametricStudyTool]

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
    def ring_pins(self: "Self") -> "List[_4512.RingPinsParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.RingPinsParametricStudyTool]

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
    ) -> "List[_4514.RollingRingAssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.RollingRingAssemblyParametricStudyTool]

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
    ) -> "List[_4518.ShaftHubConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ShaftHubConnectionParametricStudyTool]

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
    def shafts(self: "Self") -> "List[_4519.ShaftParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ShaftParametricStudyTool]

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
    ) -> "List[_4524.SpiralBevelGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearSetParametricStudyTool]

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
    def spring_dampers(self: "Self") -> "List[_4527.SpringDamperParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.SpringDamperParametricStudyTool]

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
    ) -> "List[_4530.StraightBevelDiffGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearSetParametricStudyTool]

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
    ) -> "List[_4533.StraightBevelGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearSetParametricStudyTool]

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
    def synchronisers(self: "Self") -> "List[_4537.SynchroniserParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.SynchroniserParametricStudyTool]

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
    ) -> "List[_4541.TorqueConverterParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.TorqueConverterParametricStudyTool]

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
    ) -> "List[_4544.UnbalancedMassParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.UnbalancedMassParametricStudyTool]

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
    def worm_gear_sets(self: "Self") -> "List[_4548.WormGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.WormGearSetParametricStudyTool]

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
    ) -> "List[_4551.ZerolBevelGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearSetParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_AssemblyParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_AssemblyParametricStudyTool
        """
        return _Cast_AssemblyParametricStudyTool(self)
