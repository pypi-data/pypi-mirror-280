"""ComponentCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _3018,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2798,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2937,
        _2938,
        _2940,
        _2944,
        _2947,
        _2950,
        _2951,
        _2952,
        _2955,
        _2959,
        _2964,
        _2965,
        _2968,
        _2972,
        _2975,
        _2978,
        _2981,
        _2983,
        _2986,
        _2987,
        _2989,
        _2990,
        _2993,
        _2995,
        _2998,
        _2999,
        _3003,
        _3006,
        _3009,
        _3012,
        _3013,
        _3015,
        _3016,
        _3017,
        _3021,
        _3024,
        _3025,
        _3026,
        _3027,
        _3028,
        _3031,
        _3034,
        _3036,
        _3039,
        _3044,
        _3045,
        _3048,
        _3051,
        _3052,
        _3054,
        _3055,
        _3056,
        _3059,
        _3060,
        _3061,
        _3062,
        _3063,
        _3066,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ComponentCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCompoundSystemDeflection:
    """Special nested class for casting ComponentCompoundSystemDeflection to subclasses."""

    __parent__: "ComponentCompoundSystemDeflection"

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3018.PartCompoundSystemDeflection":
        return self.__parent__._cast(_3018.PartCompoundSystemDeflection)

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
    def abstract_shaft_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2937.AbstractShaftCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2937,
        )

        return self.__parent__._cast(_2937.AbstractShaftCompoundSystemDeflection)

    @property
    def abstract_shaft_or_housing_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2938.AbstractShaftOrHousingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2938,
        )

        return self.__parent__._cast(
            _2938.AbstractShaftOrHousingCompoundSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2940.AGMAGleasonConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2940,
        )

        return self.__parent__._cast(
            _2940.AGMAGleasonConicalGearCompoundSystemDeflection
        )

    @property
    def bearing_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2944.BearingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2944,
        )

        return self.__parent__._cast(_2944.BearingCompoundSystemDeflection)

    @property
    def bevel_differential_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2947.BevelDifferentialGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2947,
        )

        return self.__parent__._cast(
            _2947.BevelDifferentialGearCompoundSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2950.BevelDifferentialPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2950,
        )

        return self.__parent__._cast(
            _2950.BevelDifferentialPlanetGearCompoundSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2951.BevelDifferentialSunGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2951,
        )

        return self.__parent__._cast(
            _2951.BevelDifferentialSunGearCompoundSystemDeflection
        )

    @property
    def bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2952.BevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2952,
        )

        return self.__parent__._cast(_2952.BevelGearCompoundSystemDeflection)

    @property
    def bolt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2955.BoltCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2955,
        )

        return self.__parent__._cast(_2955.BoltCompoundSystemDeflection)

    @property
    def clutch_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2959.ClutchHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2959,
        )

        return self.__parent__._cast(_2959.ClutchHalfCompoundSystemDeflection)

    @property
    def concept_coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2964.ConceptCouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2964,
        )

        return self.__parent__._cast(_2964.ConceptCouplingHalfCompoundSystemDeflection)

    @property
    def concept_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2965.ConceptGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2965,
        )

        return self.__parent__._cast(_2965.ConceptGearCompoundSystemDeflection)

    @property
    def conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2968.ConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2968,
        )

        return self.__parent__._cast(_2968.ConicalGearCompoundSystemDeflection)

    @property
    def connector_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2972.ConnectorCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2972,
        )

        return self.__parent__._cast(_2972.ConnectorCompoundSystemDeflection)

    @property
    def coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2975.CouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2975,
        )

        return self.__parent__._cast(_2975.CouplingHalfCompoundSystemDeflection)

    @property
    def cvt_pulley_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2978.CVTPulleyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2978,
        )

        return self.__parent__._cast(_2978.CVTPulleyCompoundSystemDeflection)

    @property
    def cycloidal_disc_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2981.CycloidalDiscCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2981,
        )

        return self.__parent__._cast(_2981.CycloidalDiscCompoundSystemDeflection)

    @property
    def cylindrical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2983.CylindricalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2983,
        )

        return self.__parent__._cast(_2983.CylindricalGearCompoundSystemDeflection)

    @property
    def cylindrical_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2986.CylindricalPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2986,
        )

        return self.__parent__._cast(
            _2986.CylindricalPlanetGearCompoundSystemDeflection
        )

    @property
    def datum_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2987.DatumCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2987,
        )

        return self.__parent__._cast(_2987.DatumCompoundSystemDeflection)

    @property
    def external_cad_model_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2989.ExternalCADModelCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2989,
        )

        return self.__parent__._cast(_2989.ExternalCADModelCompoundSystemDeflection)

    @property
    def face_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2990.FaceGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2990,
        )

        return self.__parent__._cast(_2990.FaceGearCompoundSystemDeflection)

    @property
    def fe_part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2993.FEPartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2993,
        )

        return self.__parent__._cast(_2993.FEPartCompoundSystemDeflection)

    @property
    def gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2995.GearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2995,
        )

        return self.__parent__._cast(_2995.GearCompoundSystemDeflection)

    @property
    def guide_dxf_model_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2998.GuideDxfModelCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2998,
        )

        return self.__parent__._cast(_2998.GuideDxfModelCompoundSystemDeflection)

    @property
    def hypoid_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2999.HypoidGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2999,
        )

        return self.__parent__._cast(_2999.HypoidGearCompoundSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3003.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3003,
        )

        return self.__parent__._cast(
            _3003.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3006.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3006,
        )

        return self.__parent__._cast(
            _3006.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3009.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3009,
        )

        return self.__parent__._cast(
            _3009.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
        )

    @property
    def mass_disc_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3012.MassDiscCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3012,
        )

        return self.__parent__._cast(_3012.MassDiscCompoundSystemDeflection)

    @property
    def measurement_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3013.MeasurementComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3013,
        )

        return self.__parent__._cast(_3013.MeasurementComponentCompoundSystemDeflection)

    @property
    def microphone_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3015.MicrophoneCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3015,
        )

        return self.__parent__._cast(_3015.MicrophoneCompoundSystemDeflection)

    @property
    def mountable_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3016.MountableComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3016,
        )

        return self.__parent__._cast(_3016.MountableComponentCompoundSystemDeflection)

    @property
    def oil_seal_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3017.OilSealCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3017,
        )

        return self.__parent__._cast(_3017.OilSealCompoundSystemDeflection)

    @property
    def part_to_part_shear_coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3021.PartToPartShearCouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3021,
        )

        return self.__parent__._cast(
            _3021.PartToPartShearCouplingHalfCompoundSystemDeflection
        )

    @property
    def planet_carrier_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3024.PlanetCarrierCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3024,
        )

        return self.__parent__._cast(_3024.PlanetCarrierCompoundSystemDeflection)

    @property
    def point_load_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3025.PointLoadCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3025,
        )

        return self.__parent__._cast(_3025.PointLoadCompoundSystemDeflection)

    @property
    def power_load_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3026.PowerLoadCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3026,
        )

        return self.__parent__._cast(_3026.PowerLoadCompoundSystemDeflection)

    @property
    def pulley_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3027.PulleyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3027,
        )

        return self.__parent__._cast(_3027.PulleyCompoundSystemDeflection)

    @property
    def ring_pins_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3028.RingPinsCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3028,
        )

        return self.__parent__._cast(_3028.RingPinsCompoundSystemDeflection)

    @property
    def rolling_ring_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3031.RollingRingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3031,
        )

        return self.__parent__._cast(_3031.RollingRingCompoundSystemDeflection)

    @property
    def shaft_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3034.ShaftCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3034,
        )

        return self.__parent__._cast(_3034.ShaftCompoundSystemDeflection)

    @property
    def shaft_hub_connection_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3036.ShaftHubConnectionCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3036,
        )

        return self.__parent__._cast(_3036.ShaftHubConnectionCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3039.SpiralBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3039,
        )

        return self.__parent__._cast(_3039.SpiralBevelGearCompoundSystemDeflection)

    @property
    def spring_damper_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3044.SpringDamperHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3044,
        )

        return self.__parent__._cast(_3044.SpringDamperHalfCompoundSystemDeflection)

    @property
    def straight_bevel_diff_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3045.StraightBevelDiffGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3045,
        )

        return self.__parent__._cast(
            _3045.StraightBevelDiffGearCompoundSystemDeflection
        )

    @property
    def straight_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3048.StraightBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3048,
        )

        return self.__parent__._cast(_3048.StraightBevelGearCompoundSystemDeflection)

    @property
    def straight_bevel_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3051.StraightBevelPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3051,
        )

        return self.__parent__._cast(
            _3051.StraightBevelPlanetGearCompoundSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3052.StraightBevelSunGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3052,
        )

        return self.__parent__._cast(_3052.StraightBevelSunGearCompoundSystemDeflection)

    @property
    def synchroniser_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3054.SynchroniserHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3054,
        )

        return self.__parent__._cast(_3054.SynchroniserHalfCompoundSystemDeflection)

    @property
    def synchroniser_part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3055.SynchroniserPartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3055,
        )

        return self.__parent__._cast(_3055.SynchroniserPartCompoundSystemDeflection)

    @property
    def synchroniser_sleeve_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3056.SynchroniserSleeveCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3056,
        )

        return self.__parent__._cast(_3056.SynchroniserSleeveCompoundSystemDeflection)

    @property
    def torque_converter_pump_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3059.TorqueConverterPumpCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3059,
        )

        return self.__parent__._cast(_3059.TorqueConverterPumpCompoundSystemDeflection)

    @property
    def torque_converter_turbine_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3060.TorqueConverterTurbineCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3060,
        )

        return self.__parent__._cast(
            _3060.TorqueConverterTurbineCompoundSystemDeflection
        )

    @property
    def unbalanced_mass_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3061.UnbalancedMassCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3061,
        )

        return self.__parent__._cast(_3061.UnbalancedMassCompoundSystemDeflection)

    @property
    def virtual_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3062.VirtualComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3062,
        )

        return self.__parent__._cast(_3062.VirtualComponentCompoundSystemDeflection)

    @property
    def worm_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3063.WormGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3063,
        )

        return self.__parent__._cast(_3063.WormGearCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3066.ZerolBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3066,
        )

        return self.__parent__._cast(_3066.ZerolBevelGearCompoundSystemDeflection)

    @property
    def component_compound_system_deflection(
        self: "CastSelf",
    ) -> "ComponentCompoundSystemDeflection":
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
class ComponentCompoundSystemDeflection(_3018.PartCompoundSystemDeflection):
    """ComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_2798.ComponentSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    ) -> "List[_2798.ComponentSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_ComponentCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_ComponentCompoundSystemDeflection
        """
        return _Cast_ComponentCompoundSystemDeflection(self)
