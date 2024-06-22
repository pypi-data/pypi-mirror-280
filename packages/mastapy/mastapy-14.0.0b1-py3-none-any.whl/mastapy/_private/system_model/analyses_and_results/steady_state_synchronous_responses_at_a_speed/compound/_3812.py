"""PartCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7711
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3680,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3731,
        _3732,
        _3733,
        _3735,
        _3737,
        _3738,
        _3739,
        _3741,
        _3742,
        _3744,
        _3745,
        _3746,
        _3747,
        _3749,
        _3750,
        _3751,
        _3752,
        _3754,
        _3756,
        _3757,
        _3759,
        _3760,
        _3762,
        _3763,
        _3765,
        _3767,
        _3768,
        _3770,
        _3772,
        _3773,
        _3774,
        _3776,
        _3778,
        _3780,
        _3781,
        _3782,
        _3783,
        _3784,
        _3786,
        _3787,
        _3788,
        _3789,
        _3791,
        _3792,
        _3793,
        _3795,
        _3797,
        _3799,
        _3800,
        _3802,
        _3803,
        _3805,
        _3806,
        _3807,
        _3808,
        _3809,
        _3810,
        _3811,
        _3813,
        _3815,
        _3817,
        _3818,
        _3819,
        _3820,
        _3821,
        _3822,
        _3824,
        _3825,
        _3827,
        _3828,
        _3829,
        _3831,
        _3832,
        _3834,
        _3835,
        _3837,
        _3838,
        _3840,
        _3841,
        _3843,
        _3844,
        _3845,
        _3846,
        _3847,
        _3848,
        _3849,
        _3850,
        _3852,
        _3853,
        _3854,
        _3855,
        _3856,
        _3858,
        _3859,
        _3861,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="PartCompoundSteadyStateSynchronousResponseAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting PartCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "PartCompoundSteadyStateSynchronousResponseAtASpeed"

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
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
    def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3731.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3731,
        )

        return self.__parent__._cast(
            _3731.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3732.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3732,
        )

        return self.__parent__._cast(
            _3732.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3733.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3733,
        )

        return self.__parent__._cast(
            _3733.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
        )

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
    def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3737.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3737,
        )

        return self.__parent__._cast(
            _3737.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3738.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3738,
        )

        return self.__parent__._cast(
            _3738.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
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
    def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3741.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3741,
        )

        return self.__parent__._cast(
            _3741.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
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
    def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3744.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3744,
        )

        return self.__parent__._cast(
            _3744.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3749.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3749,
        )

        return self.__parent__._cast(
            _3749.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolt_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3750.BoltCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3750,
        )

        return self.__parent__._cast(
            _3750.BoltCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3751.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3751,
        )

        return self.__parent__._cast(
            _3751.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3752.ClutchCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3752,
        )

        return self.__parent__._cast(
            _3752.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
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
    def component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3756.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3756,
        )

        return self.__parent__._cast(
            _3756.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3757.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3757,
        )

        return self.__parent__._cast(
            _3757.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
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
    def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3762.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3762,
        )

        return self.__parent__._cast(
            _3762.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3765.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3765,
        )

        return self.__parent__._cast(
            _3765.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3768.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3768,
        )

        return self.__parent__._cast(
            _3768.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
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
    def cvt_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3772.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3772,
        )

        return self.__parent__._cast(
            _3772.CVTCompoundSteadyStateSynchronousResponseAtASpeed
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
    def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3774.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3774,
        )

        return self.__parent__._cast(
            _3774.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3776.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3776,
        )

        return self.__parent__._cast(
            _3776.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
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
    def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3780.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3780,
        )

        return self.__parent__._cast(
            _3780.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def datum_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3782.DatumCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3782,
        )

        return self.__parent__._cast(
            _3782.DatumCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3783.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3783,
        )

        return self.__parent__._cast(
            _3783.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
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
    def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3786.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3786,
        )

        return self.__parent__._cast(
            _3786.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def fe_part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3787.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3787,
        )

        return self.__parent__._cast(
            _3787.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3788.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3788,
        )

        return self.__parent__._cast(
            _3788.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
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
    def gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3791.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3791,
        )

        return self.__parent__._cast(
            _3791.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3792.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3792,
        )

        return self.__parent__._cast(
            _3792.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
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
    def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3795.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3795,
        )

        return self.__parent__._cast(
            _3795.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3799.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3799,
        )

        return self.__parent__._cast(
            _3799.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3802.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3802,
        )

        return self.__parent__._cast(
            _3802.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3805.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3805,
        )

        return self.__parent__._cast(
            _3805.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def microphone_array_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3808.MicrophoneArrayCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3808,
        )

        return self.__parent__._cast(
            _3808.MicrophoneArrayCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3809.MicrophoneCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3809,
        )

        return self.__parent__._cast(
            _3809.MicrophoneCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3810.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3810,
        )

        return self.__parent__._cast(
            _3810.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
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
    def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3813.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3813,
        )

        return self.__parent__._cast(
            _3813.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
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
    def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3817.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3817,
        )

        return self.__parent__._cast(
            _3817.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3824.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3824,
        )

        return self.__parent__._cast(
            _3824.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
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
    def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3827.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3827,
        )

        return self.__parent__._cast(
            _3827.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3828.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3828,
        )

        return self.__parent__._cast(
            _3828.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
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
    def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3831.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3831,
        )

        return self.__parent__._cast(
            _3831.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
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
    def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3834.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3834,
        )

        return self.__parent__._cast(
            _3834.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3835.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3835,
        )

        return self.__parent__._cast(
            _3835.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
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
    def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3840.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3840,
        )

        return self.__parent__._cast(
            _3840.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3843.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3843,
        )

        return self.__parent__._cast(
            _3843.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3846.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3846,
        )

        return self.__parent__._cast(
            _3846.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
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
    def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3850.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3850,
        )

        return self.__parent__._cast(
            _3850.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
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
    def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3858.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3858,
        )

        return self.__parent__._cast(
            _3858.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
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
    def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3861.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3861,
        )

        return self.__parent__._cast(
            _3861.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "PartCompoundSteadyStateSynchronousResponseAtASpeed":
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
class PartCompoundSteadyStateSynchronousResponseAtASpeed(_7711.PartCompoundAnalysis):
    """PartCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3680.PartSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3680.PartSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "_Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed(self)
