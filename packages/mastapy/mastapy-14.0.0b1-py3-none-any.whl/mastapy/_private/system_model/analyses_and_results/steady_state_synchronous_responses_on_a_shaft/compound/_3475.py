"""AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3468,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2487
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3343,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3476,
        _3478,
        _3481,
        _3488,
        _3487,
        _3509,
        _3489,
        _3494,
        _3499,
        _3511,
        _3513,
        _3517,
        _3524,
        _3523,
        _3525,
        _3532,
        _3539,
        _3542,
        _3543,
        _3544,
        _3546,
        _3548,
        _3550,
        _3555,
        _3556,
        _3557,
        _3559,
        _3561,
        _3566,
        _3565,
        _3571,
        _3572,
        _3577,
        _3580,
        _3583,
        _3587,
        _3591,
        _3595,
        _3598,
        _3564,
        _3549,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyCompoundSteadyStateSynchronousResponseOnAShaft:
    """Special nested class for casting AssemblyCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

    __parent__: "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"

    @property
    def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3468.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        return self.__parent__._cast(
            _3468.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3549.PartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3549,
        )

        return self.__parent__._cast(
            _3549.PartCompoundSteadyStateSynchronousResponseOnAShaft
        )

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
    def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3564.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3564,
        )

        return self.__parent__._cast(
            _3564.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
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
class AssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
    _3468.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
):
    """AssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

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
    ) -> "List[_3343.AssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AssemblySteadyStateSynchronousResponseOnAShaft]

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
    def bearings(
        self: "Self",
    ) -> "List[_3476.BearingCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BearingCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def belt_drives(
        self: "Self",
    ) -> "List[_3478.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3481.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3488.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def bolts(
        self: "Self",
    ) -> "List[_3487.BoltCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BoltCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def cv_ts(
        self: "Self",
    ) -> "List[_3509.CVTCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.CVTCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def clutches(
        self: "Self",
    ) -> "List[_3489.ClutchCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ClutchCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3494.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3499.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3511.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3513.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3517.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def fe_parts(
        self: "Self",
    ) -> "List[_3524.FEPartCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.FEPartCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3523.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> (
        "List[_3525.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3532.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3539.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3542.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def mass_discs(
        self: "Self",
    ) -> "List[_3543.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> (
        "List[_3544.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3546.MicrophoneCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.MicrophoneCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def oil_seals(
        self: "Self",
    ) -> "List[_3548.OilSealCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.OilSealCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3550.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3555.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def point_loads(
        self: "Self",
    ) -> "List[_3556.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def power_loads(
        self: "Self",
    ) -> "List[_3557.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def ring_pins(
        self: "Self",
    ) -> "List[_3559.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> (
        "List[_3561.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3566.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def shafts(
        self: "Self",
    ) -> "List[_3565.ShaftCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ShaftCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3571.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3572.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3577.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> (
        "List[_3580.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3583.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3587.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3591.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3595.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3598.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3343.AssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AssemblySteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        """Cast to another type.

        Returns:
            _Cast_AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        """
        return _Cast_AssemblyCompoundSteadyStateSynchronousResponseOnAShaft(self)
