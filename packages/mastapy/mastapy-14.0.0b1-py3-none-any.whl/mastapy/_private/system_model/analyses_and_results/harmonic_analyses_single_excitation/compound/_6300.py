"""ComponentCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6356,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ComponentCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6167,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6276,
        _6277,
        _6279,
        _6283,
        _6286,
        _6289,
        _6290,
        _6291,
        _6294,
        _6298,
        _6303,
        _6304,
        _6307,
        _6311,
        _6314,
        _6317,
        _6320,
        _6322,
        _6325,
        _6326,
        _6327,
        _6328,
        _6331,
        _6333,
        _6336,
        _6337,
        _6341,
        _6344,
        _6347,
        _6350,
        _6351,
        _6353,
        _6354,
        _6355,
        _6359,
        _6362,
        _6363,
        _6364,
        _6365,
        _6366,
        _6369,
        _6372,
        _6373,
        _6376,
        _6381,
        _6382,
        _6385,
        _6388,
        _6389,
        _6391,
        _6392,
        _6393,
        _6396,
        _6397,
        _6398,
        _6399,
        _6400,
        _6403,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ComponentCompoundHarmonicAnalysisOfSingleExcitation")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting ComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "ComponentCompoundHarmonicAnalysisOfSingleExcitation"

    @property
    def part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6356.PartCompoundHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6356.PartCompoundHarmonicAnalysisOfSingleExcitation
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
    def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6276.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6276,
        )

        return self.__parent__._cast(
            _6276.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6277.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6277,
        )

        return self.__parent__._cast(
            _6277.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6279.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6279,
        )

        return self.__parent__._cast(
            _6279.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bearing_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6283.BearingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6283,
        )

        return self.__parent__._cast(
            _6283.BearingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6286.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6286,
        )

        return self.__parent__._cast(
            _6286.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6289.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6289,
        )

        return self.__parent__._cast(
            _6289.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6290.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6290,
        )

        return self.__parent__._cast(
            _6290.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6291.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6291,
        )

        return self.__parent__._cast(
            _6291.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bolt_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6294.BoltCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6294,
        )

        return self.__parent__._cast(
            _6294.BoltCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def clutch_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6298.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6298,
        )

        return self.__parent__._cast(
            _6298.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6303.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6303,
        )

        return self.__parent__._cast(
            _6303.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6304.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6304,
        )

        return self.__parent__._cast(
            _6304.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6307.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6307,
        )

        return self.__parent__._cast(
            _6307.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def connector_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6311.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6311,
        )

        return self.__parent__._cast(
            _6311.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6314.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6314,
        )

        return self.__parent__._cast(
            _6314.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6317.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6317,
        )

        return self.__parent__._cast(
            _6317.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6320.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6320,
        )

        return self.__parent__._cast(
            _6320.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6322.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6322,
        )

        return self.__parent__._cast(
            _6322.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6325.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6325,
        )

        return self.__parent__._cast(
            _6325.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def datum_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6326.DatumCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6326,
        )

        return self.__parent__._cast(
            _6326.DatumCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def external_cad_model_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6327.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6327,
        )

        return self.__parent__._cast(
            _6327.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def face_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6328.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6328,
        )

        return self.__parent__._cast(
            _6328.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def fe_part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6331.FEPartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6331,
        )

        return self.__parent__._cast(
            _6331.FEPartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6333.GearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6333,
        )

        return self.__parent__._cast(
            _6333.GearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6336.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6336,
        )

        return self.__parent__._cast(
            _6336.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6337.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6337,
        )

        return self.__parent__._cast(
            _6337.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6341.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6341,
        )

        return self.__parent__._cast(
            _6341.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6344.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6344,
        )

        return self.__parent__._cast(
            _6344.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6347.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6347,
        )

        return self.__parent__._cast(
            _6347.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def mass_disc_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6350.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6350,
        )

        return self.__parent__._cast(
            _6350.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def measurement_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6351.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6351,
        )

        return self.__parent__._cast(
            _6351.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def microphone_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6353.MicrophoneCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6353,
        )

        return self.__parent__._cast(
            _6353.MicrophoneCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def mountable_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6354.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6354,
        )

        return self.__parent__._cast(
            _6354.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def oil_seal_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6355.OilSealCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6355,
        )

        return self.__parent__._cast(
            _6355.OilSealCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6359.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6359,
        )

        return self.__parent__._cast(
            _6359.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def planet_carrier_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6362.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6362,
        )

        return self.__parent__._cast(
            _6362.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def point_load_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6363.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6363,
        )

        return self.__parent__._cast(
            _6363.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def power_load_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6364.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6364,
        )

        return self.__parent__._cast(
            _6364.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def pulley_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6365.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6365,
        )

        return self.__parent__._cast(
            _6365.PulleyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def ring_pins_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6366.RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6366,
        )

        return self.__parent__._cast(
            _6366.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def rolling_ring_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6369.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6369,
        )

        return self.__parent__._cast(
            _6369.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def shaft_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6372.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6372,
        )

        return self.__parent__._cast(
            _6372.ShaftCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6373.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6373,
        )

        return self.__parent__._cast(
            _6373.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6376.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6376,
        )

        return self.__parent__._cast(
            _6376.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6381.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6381,
        )

        return self.__parent__._cast(
            _6381.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6382.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6382,
        )

        return self.__parent__._cast(
            _6382.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6385.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6385,
        )

        return self.__parent__._cast(
            _6385.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6388.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6388,
        )

        return self.__parent__._cast(
            _6388.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6389.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6389,
        )

        return self.__parent__._cast(
            _6389.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6391.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6391,
        )

        return self.__parent__._cast(
            _6391.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6392.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6392,
        )

        return self.__parent__._cast(
            _6392.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6393.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6393,
        )

        return self.__parent__._cast(
            _6393.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6396.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6396,
        )

        return self.__parent__._cast(
            _6396.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6397.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6397,
        )

        return self.__parent__._cast(
            _6397.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6398.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6398,
        )

        return self.__parent__._cast(
            _6398.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def virtual_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6399.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6399,
        )

        return self.__parent__._cast(
            _6399.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def worm_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6400.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6400,
        )

        return self.__parent__._cast(
            _6400.WormGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6403.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6403,
        )

        return self.__parent__._cast(
            _6403.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "ComponentCompoundHarmonicAnalysisOfSingleExcitation":
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
class ComponentCompoundHarmonicAnalysisOfSingleExcitation(
    _6356.PartCompoundHarmonicAnalysisOfSingleExcitation
):
    """ComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6167.ComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.ComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6167.ComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.ComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "_Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_ComponentCompoundHarmonicAnalysisOfSingleExcitation(self)
