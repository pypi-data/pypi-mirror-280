"""MountableComponentCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6844,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "MountableComponentCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6767,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6823,
        _6827,
        _6830,
        _6833,
        _6834,
        _6835,
        _6842,
        _6847,
        _6848,
        _6851,
        _6855,
        _6858,
        _6861,
        _6866,
        _6869,
        _6872,
        _6877,
        _6881,
        _6885,
        _6888,
        _6891,
        _6894,
        _6895,
        _6899,
        _6903,
        _6906,
        _6907,
        _6908,
        _6909,
        _6910,
        _6913,
        _6917,
        _6920,
        _6925,
        _6926,
        _6929,
        _6932,
        _6933,
        _6935,
        _6936,
        _6937,
        _6940,
        _6941,
        _6942,
        _6943,
        _6944,
        _6947,
        _6900,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="MountableComponentCompoundCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="MountableComponentCompoundCriticalSpeedAnalysis._Cast_MountableComponentCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentCompoundCriticalSpeedAnalysis:
    """Special nested class for casting MountableComponentCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "MountableComponentCompoundCriticalSpeedAnalysis"

    @property
    def component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6844.ComponentCompoundCriticalSpeedAnalysis":
        return self.__parent__._cast(_6844.ComponentCompoundCriticalSpeedAnalysis)

    @property
    def part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6900.PartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6900,
        )

        return self.__parent__._cast(_6900.PartCompoundCriticalSpeedAnalysis)

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
    def agma_gleason_conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6823.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6823,
        )

        return self.__parent__._cast(
            _6823.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bearing_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6827.BearingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6827,
        )

        return self.__parent__._cast(_6827.BearingCompoundCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6830.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6830,
        )

        return self.__parent__._cast(
            _6830.BevelDifferentialGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6833.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6833,
        )

        return self.__parent__._cast(
            _6833.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6834.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6834,
        )

        return self.__parent__._cast(
            _6834.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6835.BevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6835,
        )

        return self.__parent__._cast(_6835.BevelGearCompoundCriticalSpeedAnalysis)

    @property
    def clutch_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6842.ClutchHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6842,
        )

        return self.__parent__._cast(_6842.ClutchHalfCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6847.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6847,
        )

        return self.__parent__._cast(
            _6847.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def concept_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6848.ConceptGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6848,
        )

        return self.__parent__._cast(_6848.ConceptGearCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6851.ConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6851,
        )

        return self.__parent__._cast(_6851.ConicalGearCompoundCriticalSpeedAnalysis)

    @property
    def connector_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6855.ConnectorCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6855,
        )

        return self.__parent__._cast(_6855.ConnectorCompoundCriticalSpeedAnalysis)

    @property
    def coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6858.CouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6858,
        )

        return self.__parent__._cast(_6858.CouplingHalfCompoundCriticalSpeedAnalysis)

    @property
    def cvt_pulley_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6861.CVTPulleyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6861,
        )

        return self.__parent__._cast(_6861.CVTPulleyCompoundCriticalSpeedAnalysis)

    @property
    def cylindrical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6866.CylindricalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6866,
        )

        return self.__parent__._cast(_6866.CylindricalGearCompoundCriticalSpeedAnalysis)

    @property
    def cylindrical_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6869.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6869,
        )

        return self.__parent__._cast(
            _6869.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def face_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6872.FaceGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6872,
        )

        return self.__parent__._cast(_6872.FaceGearCompoundCriticalSpeedAnalysis)

    @property
    def gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6877.GearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6877,
        )

        return self.__parent__._cast(_6877.GearCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6881.HypoidGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6881,
        )

        return self.__parent__._cast(_6881.HypoidGearCompoundCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6885.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6885,
        )

        return self.__parent__._cast(
            _6885.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6888.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6888,
        )

        return self.__parent__._cast(
            _6888.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6891.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6891,
        )

        return self.__parent__._cast(
            _6891.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
        )

    @property
    def mass_disc_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6894.MassDiscCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6894,
        )

        return self.__parent__._cast(_6894.MassDiscCompoundCriticalSpeedAnalysis)

    @property
    def measurement_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6895.MeasurementComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6895,
        )

        return self.__parent__._cast(
            _6895.MeasurementComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def oil_seal_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6899.OilSealCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6899,
        )

        return self.__parent__._cast(_6899.OilSealCompoundCriticalSpeedAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6903.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6903,
        )

        return self.__parent__._cast(
            _6903.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def planet_carrier_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6906.PlanetCarrierCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6906,
        )

        return self.__parent__._cast(_6906.PlanetCarrierCompoundCriticalSpeedAnalysis)

    @property
    def point_load_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6907.PointLoadCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6907,
        )

        return self.__parent__._cast(_6907.PointLoadCompoundCriticalSpeedAnalysis)

    @property
    def power_load_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6908.PowerLoadCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6908,
        )

        return self.__parent__._cast(_6908.PowerLoadCompoundCriticalSpeedAnalysis)

    @property
    def pulley_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6909.PulleyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6909,
        )

        return self.__parent__._cast(_6909.PulleyCompoundCriticalSpeedAnalysis)

    @property
    def ring_pins_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6910.RingPinsCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6910,
        )

        return self.__parent__._cast(_6910.RingPinsCompoundCriticalSpeedAnalysis)

    @property
    def rolling_ring_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6913.RollingRingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6913,
        )

        return self.__parent__._cast(_6913.RollingRingCompoundCriticalSpeedAnalysis)

    @property
    def shaft_hub_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6917.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6917,
        )

        return self.__parent__._cast(
            _6917.ShaftHubConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6920.SpiralBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6920,
        )

        return self.__parent__._cast(_6920.SpiralBevelGearCompoundCriticalSpeedAnalysis)

    @property
    def spring_damper_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6925.SpringDamperHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6925,
        )

        return self.__parent__._cast(
            _6925.SpringDamperHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_diff_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6926.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6926,
        )

        return self.__parent__._cast(
            _6926.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6929.StraightBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6929,
        )

        return self.__parent__._cast(
            _6929.StraightBevelGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6932.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6932,
        )

        return self.__parent__._cast(
            _6932.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6933.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6933,
        )

        return self.__parent__._cast(
            _6933.StraightBevelSunGearCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6935.SynchroniserHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6935,
        )

        return self.__parent__._cast(
            _6935.SynchroniserHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6936.SynchroniserPartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6936,
        )

        return self.__parent__._cast(
            _6936.SynchroniserPartCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_sleeve_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6937.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6937,
        )

        return self.__parent__._cast(
            _6937.SynchroniserSleeveCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_pump_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6940.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6940,
        )

        return self.__parent__._cast(
            _6940.TorqueConverterPumpCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_turbine_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6941.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6941,
        )

        return self.__parent__._cast(
            _6941.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
        )

    @property
    def unbalanced_mass_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6942.UnbalancedMassCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6942,
        )

        return self.__parent__._cast(_6942.UnbalancedMassCompoundCriticalSpeedAnalysis)

    @property
    def virtual_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6943.VirtualComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6943,
        )

        return self.__parent__._cast(
            _6943.VirtualComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def worm_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6944.WormGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6944,
        )

        return self.__parent__._cast(_6944.WormGearCompoundCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6947.ZerolBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6947,
        )

        return self.__parent__._cast(_6947.ZerolBevelGearCompoundCriticalSpeedAnalysis)

    @property
    def mountable_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "MountableComponentCompoundCriticalSpeedAnalysis":
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
class MountableComponentCompoundCriticalSpeedAnalysis(
    _6844.ComponentCompoundCriticalSpeedAnalysis
):
    """MountableComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6767.MountableComponentCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.MountableComponentCriticalSpeedAnalysis]

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
    ) -> "List[_6767.MountableComponentCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.MountableComponentCriticalSpeedAnalysis]

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
    ) -> "_Cast_MountableComponentCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentCompoundCriticalSpeedAnalysis
        """
        return _Cast_MountableComponentCompoundCriticalSpeedAnalysis(self)
