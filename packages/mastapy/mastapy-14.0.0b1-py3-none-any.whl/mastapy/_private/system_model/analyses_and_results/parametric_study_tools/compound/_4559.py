"""AssemblyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4552,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4457,
        _4410,
    )
    from mastapy._private.system_model.part_model import _2487
    from mastapy._private.system_model.analyses_and_results.static_loads import _6965
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4560,
        _4562,
        _4565,
        _4572,
        _4571,
        _4593,
        _4573,
        _4578,
        _4583,
        _4595,
        _4597,
        _4601,
        _4608,
        _4607,
        _4609,
        _4616,
        _4623,
        _4626,
        _4627,
        _4628,
        _4630,
        _4632,
        _4634,
        _4639,
        _4640,
        _4641,
        _4643,
        _4645,
        _4650,
        _4649,
        _4655,
        _4656,
        _4661,
        _4664,
        _4667,
        _4671,
        _4675,
        _4679,
        _4682,
        _4648,
        _4633,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="AssemblyCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AssemblyCompoundParametricStudyTool._Cast_AssemblyCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyCompoundParametricStudyTool:
    """Special nested class for casting AssemblyCompoundParametricStudyTool to subclasses."""

    __parent__: "AssemblyCompoundParametricStudyTool"

    @property
    def abstract_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4552.AbstractAssemblyCompoundParametricStudyTool":
        return self.__parent__._cast(_4552.AbstractAssemblyCompoundParametricStudyTool)

    @property
    def part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4633.PartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4633,
        )

        return self.__parent__._cast(_4633.PartCompoundParametricStudyTool)

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
    def root_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4648.RootAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4648,
        )

        return self.__parent__._cast(_4648.RootAssemblyCompoundParametricStudyTool)

    @property
    def assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "AssemblyCompoundParametricStudyTool":
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
class AssemblyCompoundParametricStudyTool(
    _4552.AbstractAssemblyCompoundParametricStudyTool
):
    """AssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def all_duty_cycle_results(
        self: "Self",
    ) -> "_4457.DutyCycleResultsForAllComponents":
        """mastapy._private.system_model.analyses_and_results.parametric_study_tools.DutyCycleResultsForAllComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def properties_changing_all_load_cases(self: "Self") -> "_6965.AssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4410.AssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.AssemblyParametricStudyTool]

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
    def bearings(self: "Self") -> "List[_4560.BearingCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.BearingCompoundParametricStudyTool]

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
    def belt_drives(self: "Self") -> "List[_4562.BeltDriveCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.BeltDriveCompoundParametricStudyTool]

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
    ) -> "List[_4565.BevelDifferentialGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearSetCompoundParametricStudyTool]

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
    def bolted_joints(
        self: "Self",
    ) -> "List[_4572.BoltedJointCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.BoltedJointCompoundParametricStudyTool]

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
    def bolts(self: "Self") -> "List[_4571.BoltCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.BoltCompoundParametricStudyTool]

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
    def cv_ts(self: "Self") -> "List[_4593.CVTCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.CVTCompoundParametricStudyTool]

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
    def clutches(self: "Self") -> "List[_4573.ClutchCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.ClutchCompoundParametricStudyTool]

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
    ) -> "List[_4578.ConceptCouplingCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingCompoundParametricStudyTool]

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
    ) -> "List[_4583.ConceptGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearSetCompoundParametricStudyTool]

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
    ) -> "List[_4595.CycloidalAssemblyCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.CycloidalAssemblyCompoundParametricStudyTool]

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
    ) -> "List[_4597.CycloidalDiscCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.CycloidalDiscCompoundParametricStudyTool]

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
    ) -> "List[_4601.CylindricalGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearSetCompoundParametricStudyTool]

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
    def fe_parts(self: "Self") -> "List[_4608.FEPartCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.FEPartCompoundParametricStudyTool]

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
    def face_gear_sets(
        self: "Self",
    ) -> "List[_4607.FaceGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearSetCompoundParametricStudyTool]

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
    ) -> "List[_4609.FlexiblePinAssemblyCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.FlexiblePinAssemblyCompoundParametricStudyTool]

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
    ) -> "List[_4616.HypoidGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearSetCompoundParametricStudyTool]

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
    ) -> "List[_4623.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool]

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
    ) -> "List[_4626.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool]

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
    def mass_discs(self: "Self") -> "List[_4627.MassDiscCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.MassDiscCompoundParametricStudyTool]

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
    ) -> "List[_4628.MeasurementComponentCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.MeasurementComponentCompoundParametricStudyTool]

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
    def microphones(
        self: "Self",
    ) -> "List[_4630.MicrophoneCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.MicrophoneCompoundParametricStudyTool]

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
    def oil_seals(self: "Self") -> "List[_4632.OilSealCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.OilSealCompoundParametricStudyTool]

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
    ) -> "List[_4634.PartToPartShearCouplingCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingCompoundParametricStudyTool]

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
    ) -> "List[_4639.PlanetCarrierCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.PlanetCarrierCompoundParametricStudyTool]

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
    def point_loads(self: "Self") -> "List[_4640.PointLoadCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.PointLoadCompoundParametricStudyTool]

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
    def power_loads(self: "Self") -> "List[_4641.PowerLoadCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.PowerLoadCompoundParametricStudyTool]

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
    def ring_pins(self: "Self") -> "List[_4643.RingPinsCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.RingPinsCompoundParametricStudyTool]

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
    ) -> "List[_4645.RollingRingAssemblyCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingAssemblyCompoundParametricStudyTool]

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
    ) -> "List[_4650.ShaftHubConnectionCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.ShaftHubConnectionCompoundParametricStudyTool]

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
    def shafts(self: "Self") -> "List[_4649.ShaftCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.ShaftCompoundParametricStudyTool]

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
    ) -> "List[_4655.SpiralBevelGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearSetCompoundParametricStudyTool]

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
    def spring_dampers(
        self: "Self",
    ) -> "List[_4656.SpringDamperCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperCompoundParametricStudyTool]

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
    ) -> "List[_4661.StraightBevelDiffGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearSetCompoundParametricStudyTool]

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
    ) -> "List[_4664.StraightBevelGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearSetCompoundParametricStudyTool]

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
    def synchronisers(
        self: "Self",
    ) -> "List[_4667.SynchroniserCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserCompoundParametricStudyTool]

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
    ) -> "List[_4671.TorqueConverterCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterCompoundParametricStudyTool]

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
    ) -> "List[_4675.UnbalancedMassCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.UnbalancedMassCompoundParametricStudyTool]

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
    def worm_gear_sets(
        self: "Self",
    ) -> "List[_4679.WormGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.WormGearSetCompoundParametricStudyTool]

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
    ) -> "List[_4682.ZerolBevelGearSetCompoundParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearSetCompoundParametricStudyTool]

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
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_4410.AssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.AssemblyParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_AssemblyCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_AssemblyCompoundParametricStudyTool
        """
        return _Cast_AssemblyCompoundParametricStudyTool(self)
