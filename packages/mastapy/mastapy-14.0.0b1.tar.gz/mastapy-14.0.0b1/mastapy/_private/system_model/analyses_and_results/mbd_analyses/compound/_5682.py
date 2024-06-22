"""ComponentCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5738,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ComponentCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5528
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5658,
        _5659,
        _5661,
        _5665,
        _5668,
        _5671,
        _5672,
        _5673,
        _5676,
        _5680,
        _5685,
        _5686,
        _5689,
        _5693,
        _5696,
        _5699,
        _5702,
        _5704,
        _5707,
        _5708,
        _5709,
        _5710,
        _5713,
        _5715,
        _5718,
        _5719,
        _5723,
        _5726,
        _5729,
        _5732,
        _5733,
        _5735,
        _5736,
        _5737,
        _5741,
        _5744,
        _5745,
        _5746,
        _5747,
        _5748,
        _5751,
        _5754,
        _5755,
        _5758,
        _5763,
        _5764,
        _5767,
        _5770,
        _5771,
        _5773,
        _5774,
        _5775,
        _5778,
        _5779,
        _5780,
        _5781,
        _5782,
        _5785,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ComponentCompoundMultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting ComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "ComponentCompoundMultibodyDynamicsAnalysis"

    @property
    def part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5738.PartCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5738.PartCompoundMultibodyDynamicsAnalysis)

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
    def abstract_shaft_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5658.AbstractShaftCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5658,
        )

        return self.__parent__._cast(
            _5658.AbstractShaftCompoundMultibodyDynamicsAnalysis
        )

    @property
    def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5659.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5659,
        )

        return self.__parent__._cast(
            _5659.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5661.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5661,
        )

        return self.__parent__._cast(
            _5661.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bearing_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5665.BearingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5665,
        )

        return self.__parent__._cast(_5665.BearingCompoundMultibodyDynamicsAnalysis)

    @property
    def bevel_differential_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5668.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5668,
        )

        return self.__parent__._cast(
            _5668.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5671.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5671,
        )

        return self.__parent__._cast(
            _5671.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5672.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5672,
        )

        return self.__parent__._cast(
            _5672.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5673.BevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5673,
        )

        return self.__parent__._cast(_5673.BevelGearCompoundMultibodyDynamicsAnalysis)

    @property
    def bolt_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5676.BoltCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5676,
        )

        return self.__parent__._cast(_5676.BoltCompoundMultibodyDynamicsAnalysis)

    @property
    def clutch_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5680.ClutchHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5680,
        )

        return self.__parent__._cast(_5680.ClutchHalfCompoundMultibodyDynamicsAnalysis)

    @property
    def concept_coupling_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5685.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5685,
        )

        return self.__parent__._cast(
            _5685.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def concept_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5686.ConceptGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5686,
        )

        return self.__parent__._cast(_5686.ConceptGearCompoundMultibodyDynamicsAnalysis)

    @property
    def conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5689.ConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5689,
        )

        return self.__parent__._cast(_5689.ConicalGearCompoundMultibodyDynamicsAnalysis)

    @property
    def connector_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5693.ConnectorCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5693,
        )

        return self.__parent__._cast(_5693.ConnectorCompoundMultibodyDynamicsAnalysis)

    @property
    def coupling_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5696.CouplingHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5696,
        )

        return self.__parent__._cast(
            _5696.CouplingHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cvt_pulley_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5699.CVTPulleyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5699,
        )

        return self.__parent__._cast(_5699.CVTPulleyCompoundMultibodyDynamicsAnalysis)

    @property
    def cycloidal_disc_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5702.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5702,
        )

        return self.__parent__._cast(
            _5702.CycloidalDiscCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cylindrical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5704.CylindricalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5704,
        )

        return self.__parent__._cast(
            _5704.CylindricalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5707.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5707,
        )

        return self.__parent__._cast(
            _5707.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def datum_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5708.DatumCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5708,
        )

        return self.__parent__._cast(_5708.DatumCompoundMultibodyDynamicsAnalysis)

    @property
    def external_cad_model_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5709.ExternalCADModelCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5709,
        )

        return self.__parent__._cast(
            _5709.ExternalCADModelCompoundMultibodyDynamicsAnalysis
        )

    @property
    def face_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5710.FaceGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5710,
        )

        return self.__parent__._cast(_5710.FaceGearCompoundMultibodyDynamicsAnalysis)

    @property
    def fe_part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5713.FEPartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5713,
        )

        return self.__parent__._cast(_5713.FEPartCompoundMultibodyDynamicsAnalysis)

    @property
    def gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5715.GearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5715,
        )

        return self.__parent__._cast(_5715.GearCompoundMultibodyDynamicsAnalysis)

    @property
    def guide_dxf_model_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5718.GuideDxfModelCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5718,
        )

        return self.__parent__._cast(
            _5718.GuideDxfModelCompoundMultibodyDynamicsAnalysis
        )

    @property
    def hypoid_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5719.HypoidGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5719,
        )

        return self.__parent__._cast(_5719.HypoidGearCompoundMultibodyDynamicsAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5723.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5723,
        )

        return self.__parent__._cast(
            _5723.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5726.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5726,
        )

        return self.__parent__._cast(
            _5726.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> (
        "_5729.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5729,
        )

        return self.__parent__._cast(
            _5729.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def mass_disc_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5732.MassDiscCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5732,
        )

        return self.__parent__._cast(_5732.MassDiscCompoundMultibodyDynamicsAnalysis)

    @property
    def measurement_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5733.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5733,
        )

        return self.__parent__._cast(
            _5733.MeasurementComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def microphone_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5735.MicrophoneCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5735,
        )

        return self.__parent__._cast(_5735.MicrophoneCompoundMultibodyDynamicsAnalysis)

    @property
    def mountable_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5736.MountableComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5736,
        )

        return self.__parent__._cast(
            _5736.MountableComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def oil_seal_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5737.OilSealCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5737,
        )

        return self.__parent__._cast(_5737.OilSealCompoundMultibodyDynamicsAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5741.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5741,
        )

        return self.__parent__._cast(
            _5741.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def planet_carrier_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5744.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5744,
        )

        return self.__parent__._cast(
            _5744.PlanetCarrierCompoundMultibodyDynamicsAnalysis
        )

    @property
    def point_load_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5745.PointLoadCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5745,
        )

        return self.__parent__._cast(_5745.PointLoadCompoundMultibodyDynamicsAnalysis)

    @property
    def power_load_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5746.PowerLoadCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5746,
        )

        return self.__parent__._cast(_5746.PowerLoadCompoundMultibodyDynamicsAnalysis)

    @property
    def pulley_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5747.PulleyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5747,
        )

        return self.__parent__._cast(_5747.PulleyCompoundMultibodyDynamicsAnalysis)

    @property
    def ring_pins_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5748.RingPinsCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5748,
        )

        return self.__parent__._cast(_5748.RingPinsCompoundMultibodyDynamicsAnalysis)

    @property
    def rolling_ring_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5751.RollingRingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5751,
        )

        return self.__parent__._cast(_5751.RollingRingCompoundMultibodyDynamicsAnalysis)

    @property
    def shaft_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5754.ShaftCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5754,
        )

        return self.__parent__._cast(_5754.ShaftCompoundMultibodyDynamicsAnalysis)

    @property
    def shaft_hub_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5755.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5755,
        )

        return self.__parent__._cast(
            _5755.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spiral_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5758.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5758,
        )

        return self.__parent__._cast(
            _5758.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spring_damper_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5763.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5763,
        )

        return self.__parent__._cast(
            _5763.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5764.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5764,
        )

        return self.__parent__._cast(
            _5764.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5767.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5767,
        )

        return self.__parent__._cast(
            _5767.StraightBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5770.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5770,
        )

        return self.__parent__._cast(
            _5770.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5771.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5771,
        )

        return self.__parent__._cast(
            _5771.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5773.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5773,
        )

        return self.__parent__._cast(
            _5773.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5774.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5774,
        )

        return self.__parent__._cast(
            _5774.SynchroniserPartCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_sleeve_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5775.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5775,
        )

        return self.__parent__._cast(
            _5775.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
        )

    @property
    def torque_converter_pump_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5778.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5778,
        )

        return self.__parent__._cast(
            _5778.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
        )

    @property
    def torque_converter_turbine_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5779.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5779,
        )

        return self.__parent__._cast(
            _5779.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
        )

    @property
    def unbalanced_mass_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5780.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5780,
        )

        return self.__parent__._cast(
            _5780.UnbalancedMassCompoundMultibodyDynamicsAnalysis
        )

    @property
    def virtual_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5781.VirtualComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5781,
        )

        return self.__parent__._cast(
            _5781.VirtualComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def worm_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5782.WormGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5782,
        )

        return self.__parent__._cast(_5782.WormGearCompoundMultibodyDynamicsAnalysis)

    @property
    def zerol_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5785.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5785,
        )

        return self.__parent__._cast(
            _5785.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "ComponentCompoundMultibodyDynamicsAnalysis":
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
class ComponentCompoundMultibodyDynamicsAnalysis(
    _5738.PartCompoundMultibodyDynamicsAnalysis
):
    """ComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_5528.ComponentMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis]

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
    ) -> "List[_5528.ComponentMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_ComponentCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ComponentCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_ComponentCompoundMultibodyDynamicsAnalysis(self)
