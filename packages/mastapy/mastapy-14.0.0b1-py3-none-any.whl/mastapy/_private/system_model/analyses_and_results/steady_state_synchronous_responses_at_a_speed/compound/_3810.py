"""MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3756,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3678,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3735,
        _3739,
        _3742,
        _3745,
        _3746,
        _3747,
        _3754,
        _3759,
        _3760,
        _3763,
        _3767,
        _3770,
        _3773,
        _3778,
        _3781,
        _3784,
        _3789,
        _3793,
        _3797,
        _3800,
        _3803,
        _3806,
        _3807,
        _3811,
        _3815,
        _3818,
        _3819,
        _3820,
        _3821,
        _3822,
        _3825,
        _3829,
        _3832,
        _3837,
        _3838,
        _3841,
        _3844,
        _3845,
        _3847,
        _3848,
        _3849,
        _3852,
        _3853,
        _3854,
        _3855,
        _3856,
        _3859,
        _3812,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"

    @property
    def component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3756.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3756.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3812.PartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3812,
        )

        return self.__parent__._cast(
            _3812.PartCompoundSteadyStateSynchronousResponseAtASpeed
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
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3735.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3735,
        )

        return self.__parent__._cast(
            _3735.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bearing_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3739.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3739,
        )

        return self.__parent__._cast(
            _3739.BearingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3742.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3742,
        )

        return self.__parent__._cast(
            _3742.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3745.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3745,
        )

        return self.__parent__._cast(
            _3745.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3746.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3746,
        )

        return self.__parent__._cast(
            _3746.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3747.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3747,
        )

        return self.__parent__._cast(
            _3747.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3754.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3754,
        )

        return self.__parent__._cast(
            _3754.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3759.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3759,
        )

        return self.__parent__._cast(
            _3759.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3760.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3760,
        )

        return self.__parent__._cast(
            _3760.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3763.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3763,
        )

        return self.__parent__._cast(
            _3763.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connector_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3767.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3767,
        )

        return self.__parent__._cast(
            _3767.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3770.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3770,
        )

        return self.__parent__._cast(
            _3770.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3773.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3773,
        )

        return self.__parent__._cast(
            _3773.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3778.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3778,
        )

        return self.__parent__._cast(
            _3778.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3781.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3781,
        )

        return self.__parent__._cast(
            _3781.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3784.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3784,
        )

        return self.__parent__._cast(
            _3784.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3789.GearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3789,
        )

        return self.__parent__._cast(
            _3789.GearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3793.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3793,
        )

        return self.__parent__._cast(
            _3793.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3797.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3797,
        )

        return self.__parent__._cast(
            _3797.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3800.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3800,
        )

        return self.__parent__._cast(
            _3800.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3803.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3803,
        )

        return self.__parent__._cast(
            _3803.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3806.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3806,
        )

        return self.__parent__._cast(
            _3806.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3807.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3807,
        )

        return self.__parent__._cast(
            _3807.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3811.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3811,
        )

        return self.__parent__._cast(
            _3811.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3815.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3815,
        )

        return self.__parent__._cast(
            _3815.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3818.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3818,
        )

        return self.__parent__._cast(
            _3818.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def point_load_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3819.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3819,
        )

        return self.__parent__._cast(
            _3819.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def power_load_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3820.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3820,
        )

        return self.__parent__._cast(
            _3820.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def pulley_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3821.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3821,
        )

        return self.__parent__._cast(
            _3821.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3822.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3822,
        )

        return self.__parent__._cast(
            _3822.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3825.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3825,
        )

        return self.__parent__._cast(
            _3825.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3829.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3829,
        )

        return self.__parent__._cast(
            _3829.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3832.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3832,
        )

        return self.__parent__._cast(
            _3832.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3837.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3837,
        )

        return self.__parent__._cast(
            _3837.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3838.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3838,
        )

        return self.__parent__._cast(
            _3838.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3841.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3841,
        )

        return self.__parent__._cast(
            _3841.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3844.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3844,
        )

        return self.__parent__._cast(
            _3844.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3845.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3845,
        )

        return self.__parent__._cast(
            _3845.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3847.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3847,
        )

        return self.__parent__._cast(
            _3847.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3848.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3848,
        )

        return self.__parent__._cast(
            _3848.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3849.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3849,
        )

        return self.__parent__._cast(
            _3849.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3852.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3852,
        )

        return self.__parent__._cast(
            _3852.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3853.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3853,
        )

        return self.__parent__._cast(
            _3853.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3854.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3854,
        )

        return self.__parent__._cast(
            _3854.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3855.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3855,
        )

        return self.__parent__._cast(
            _3855.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3856.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3856,
        )

        return self.__parent__._cast(
            _3856.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3859.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3859,
        )

        return self.__parent__._cast(
            _3859.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
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
class MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed(
    _3756.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3678.MountableComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.MountableComponentSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3678.MountableComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.MountableComponentSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
