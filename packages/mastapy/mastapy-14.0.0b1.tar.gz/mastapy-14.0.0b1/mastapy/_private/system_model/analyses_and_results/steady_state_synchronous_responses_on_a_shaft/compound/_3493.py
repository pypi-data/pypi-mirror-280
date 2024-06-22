"""ComponentCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3549,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3361,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3469,
        _3470,
        _3472,
        _3476,
        _3479,
        _3482,
        _3483,
        _3484,
        _3487,
        _3491,
        _3496,
        _3497,
        _3500,
        _3504,
        _3507,
        _3510,
        _3513,
        _3515,
        _3518,
        _3519,
        _3520,
        _3521,
        _3524,
        _3526,
        _3529,
        _3530,
        _3534,
        _3537,
        _3540,
        _3543,
        _3544,
        _3546,
        _3547,
        _3548,
        _3552,
        _3555,
        _3556,
        _3557,
        _3558,
        _3559,
        _3562,
        _3565,
        _3566,
        _3569,
        _3574,
        _3575,
        _3578,
        _3581,
        _3582,
        _3584,
        _3585,
        _3586,
        _3589,
        _3590,
        _3591,
        _3592,
        _3593,
        _3596,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="ComponentCompoundSteadyStateSynchronousResponseOnAShaft"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSteadyStateSynchronousResponseOnAShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft:
    """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

    __parent__: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft"

    @property
    def part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3549.PartCompoundSteadyStateSynchronousResponseOnAShaft":
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
    def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3469.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3469,
        )

        return self.__parent__._cast(
            _3469.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3470.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3470,
        )

        return self.__parent__._cast(
            _3470.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3472.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3472,
        )

        return self.__parent__._cast(
            _3472.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bearing_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3476.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3476,
        )

        return self.__parent__._cast(
            _3476.BearingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3479.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3479,
        )

        return self.__parent__._cast(
            _3479.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3482.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3482,
        )

        return self.__parent__._cast(
            _3482.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3483.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3483,
        )

        return self.__parent__._cast(
            _3483.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3484.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3484,
        )

        return self.__parent__._cast(
            _3484.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bolt_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3487.BoltCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3487,
        )

        return self.__parent__._cast(
            _3487.BoltCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3491.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3491,
        )

        return self.__parent__._cast(
            _3491.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3496.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3496,
        )

        return self.__parent__._cast(
            _3496.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3497.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3497,
        )

        return self.__parent__._cast(
            _3497.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3500.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3500,
        )

        return self.__parent__._cast(
            _3500.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def connector_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3504.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3504,
        )

        return self.__parent__._cast(
            _3504.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3507.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3507,
        )

        return self.__parent__._cast(
            _3507.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3510.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3510,
        )

        return self.__parent__._cast(
            _3510.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3513.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3513,
        )

        return self.__parent__._cast(
            _3513.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3515.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3515,
        )

        return self.__parent__._cast(
            _3515.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3518.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3518,
        )

        return self.__parent__._cast(
            _3518.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def datum_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3519.DatumCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3519,
        )

        return self.__parent__._cast(
            _3519.DatumCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3520.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3520,
        )

        return self.__parent__._cast(
            _3520.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3521.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3521,
        )

        return self.__parent__._cast(
            _3521.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3524.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3524,
        )

        return self.__parent__._cast(
            _3524.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3526.GearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3526,
        )

        return self.__parent__._cast(
            _3526.GearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3529.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3529,
        )

        return self.__parent__._cast(
            _3529.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3530.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3530,
        )

        return self.__parent__._cast(
            _3530.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3534.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3534,
        )

        return self.__parent__._cast(
            _3534.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3537.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3537,
        )

        return self.__parent__._cast(
            _3537.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3540.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3540,
        )

        return self.__parent__._cast(
            _3540.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3543.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3543,
        )

        return self.__parent__._cast(
            _3543.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3544.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3544,
        )

        return self.__parent__._cast(
            _3544.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def microphone_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3546.MicrophoneCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3546,
        )

        return self.__parent__._cast(
            _3546.MicrophoneCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3547.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3547,
        )

        return self.__parent__._cast(
            _3547.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3548.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3548,
        )

        return self.__parent__._cast(
            _3548.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3552.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3552,
        )

        return self.__parent__._cast(
            _3552.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3555.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3555,
        )

        return self.__parent__._cast(
            _3555.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def point_load_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3556.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3556,
        )

        return self.__parent__._cast(
            _3556.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def power_load_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3557.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3557,
        )

        return self.__parent__._cast(
            _3557.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def pulley_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3558.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3558,
        )

        return self.__parent__._cast(
            _3558.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3559.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3559,
        )

        return self.__parent__._cast(
            _3559.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3562.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3562,
        )

        return self.__parent__._cast(
            _3562.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def shaft_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3565.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3565,
        )

        return self.__parent__._cast(
            _3565.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3566.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3566,
        )

        return self.__parent__._cast(
            _3566.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3569.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3569,
        )

        return self.__parent__._cast(
            _3569.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3574.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3574,
        )

        return self.__parent__._cast(
            _3574.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3575.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3575,
        )

        return self.__parent__._cast(
            _3575.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3578.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3578,
        )

        return self.__parent__._cast(
            _3578.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3581.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3581,
        )

        return self.__parent__._cast(
            _3581.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3582.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3582,
        )

        return self.__parent__._cast(
            _3582.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3584.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3584,
        )

        return self.__parent__._cast(
            _3584.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3585.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3585,
        )

        return self.__parent__._cast(
            _3585.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3586.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3586,
        )

        return self.__parent__._cast(
            _3586.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3589.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3589,
        )

        return self.__parent__._cast(
            _3589.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3590.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3590,
        )

        return self.__parent__._cast(
            _3590.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3591.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3591,
        )

        return self.__parent__._cast(
            _3591.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3592.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3592,
        )

        return self.__parent__._cast(
            _3592.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3593.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3593,
        )

        return self.__parent__._cast(
            _3593.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3596.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3596,
        )

        return self.__parent__._cast(
            _3596.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
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
class ComponentCompoundSteadyStateSynchronousResponseOnAShaft(
    _3549.PartCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ComponentCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3361.ComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3361.ComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "_Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        """Cast to another type.

        Returns:
            _Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft
        """
        return _Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft(self)
