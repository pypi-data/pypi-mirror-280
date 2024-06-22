"""PartCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7711
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PART_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PartCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2870,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2936,
        _2937,
        _2938,
        _2940,
        _2942,
        _2943,
        _2944,
        _2946,
        _2947,
        _2949,
        _2950,
        _2951,
        _2952,
        _2954,
        _2955,
        _2956,
        _2957,
        _2959,
        _2961,
        _2962,
        _2964,
        _2965,
        _2967,
        _2968,
        _2970,
        _2972,
        _2973,
        _2975,
        _2977,
        _2978,
        _2979,
        _2981,
        _2983,
        _2985,
        _2986,
        _2987,
        _2989,
        _2990,
        _2992,
        _2993,
        _2994,
        _2995,
        _2997,
        _2998,
        _2999,
        _3001,
        _3003,
        _3005,
        _3006,
        _3008,
        _3009,
        _3011,
        _3012,
        _3013,
        _3014,
        _3015,
        _3016,
        _3017,
        _3019,
        _3021,
        _3023,
        _3024,
        _3025,
        _3026,
        _3027,
        _3028,
        _3030,
        _3031,
        _3033,
        _3034,
        _3036,
        _3038,
        _3039,
        _3041,
        _3042,
        _3044,
        _3045,
        _3047,
        _3048,
        _3050,
        _3051,
        _3052,
        _3053,
        _3054,
        _3055,
        _3056,
        _3057,
        _3059,
        _3060,
        _3061,
        _3062,
        _3063,
        _3065,
        _3066,
        _3068,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="PartCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundSystemDeflection:
    """Special nested class for casting PartCompoundSystemDeflection to subclasses."""

    __parent__: "PartCompoundSystemDeflection"

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
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2936.AbstractAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2936,
        )

        return self.__parent__._cast(_2936.AbstractAssemblyCompoundSystemDeflection)

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
    def agma_gleason_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2942.AGMAGleasonConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2942,
        )

        return self.__parent__._cast(
            _2942.AGMAGleasonConicalGearSetCompoundSystemDeflection
        )

    @property
    def assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2943.AssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2943,
        )

        return self.__parent__._cast(_2943.AssemblyCompoundSystemDeflection)

    @property
    def bearing_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2944.BearingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2944,
        )

        return self.__parent__._cast(_2944.BearingCompoundSystemDeflection)

    @property
    def belt_drive_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2946.BeltDriveCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2946,
        )

        return self.__parent__._cast(_2946.BeltDriveCompoundSystemDeflection)

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
    def bevel_differential_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2949.BevelDifferentialGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2949,
        )

        return self.__parent__._cast(
            _2949.BevelDifferentialGearSetCompoundSystemDeflection
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
    def bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2954.BevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2954,
        )

        return self.__parent__._cast(_2954.BevelGearSetCompoundSystemDeflection)

    @property
    def bolt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2955.BoltCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2955,
        )

        return self.__parent__._cast(_2955.BoltCompoundSystemDeflection)

    @property
    def bolted_joint_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2956.BoltedJointCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2956,
        )

        return self.__parent__._cast(_2956.BoltedJointCompoundSystemDeflection)

    @property
    def clutch_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2957.ClutchCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2957,
        )

        return self.__parent__._cast(_2957.ClutchCompoundSystemDeflection)

    @property
    def clutch_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2959.ClutchHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2959,
        )

        return self.__parent__._cast(_2959.ClutchHalfCompoundSystemDeflection)

    @property
    def component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2961.ComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2961,
        )

        return self.__parent__._cast(_2961.ComponentCompoundSystemDeflection)

    @property
    def concept_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2962.ConceptCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2962,
        )

        return self.__parent__._cast(_2962.ConceptCouplingCompoundSystemDeflection)

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
    def concept_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2967.ConceptGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2967,
        )

        return self.__parent__._cast(_2967.ConceptGearSetCompoundSystemDeflection)

    @property
    def conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2968.ConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2968,
        )

        return self.__parent__._cast(_2968.ConicalGearCompoundSystemDeflection)

    @property
    def conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2970.ConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2970,
        )

        return self.__parent__._cast(_2970.ConicalGearSetCompoundSystemDeflection)

    @property
    def connector_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2972.ConnectorCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2972,
        )

        return self.__parent__._cast(_2972.ConnectorCompoundSystemDeflection)

    @property
    def coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2973.CouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2973,
        )

        return self.__parent__._cast(_2973.CouplingCompoundSystemDeflection)

    @property
    def coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2975.CouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2975,
        )

        return self.__parent__._cast(_2975.CouplingHalfCompoundSystemDeflection)

    @property
    def cvt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2977.CVTCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2977,
        )

        return self.__parent__._cast(_2977.CVTCompoundSystemDeflection)

    @property
    def cvt_pulley_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2978.CVTPulleyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2978,
        )

        return self.__parent__._cast(_2978.CVTPulleyCompoundSystemDeflection)

    @property
    def cycloidal_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2979.CycloidalAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2979,
        )

        return self.__parent__._cast(_2979.CycloidalAssemblyCompoundSystemDeflection)

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
    def cylindrical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2985.CylindricalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2985,
        )

        return self.__parent__._cast(_2985.CylindricalGearSetCompoundSystemDeflection)

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
    def face_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2992.FaceGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2992,
        )

        return self.__parent__._cast(_2992.FaceGearSetCompoundSystemDeflection)

    @property
    def fe_part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2993.FEPartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2993,
        )

        return self.__parent__._cast(_2993.FEPartCompoundSystemDeflection)

    @property
    def flexible_pin_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2994.FlexiblePinAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2994,
        )

        return self.__parent__._cast(_2994.FlexiblePinAssemblyCompoundSystemDeflection)

    @property
    def gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2995.GearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2995,
        )

        return self.__parent__._cast(_2995.GearCompoundSystemDeflection)

    @property
    def gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2997.GearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2997,
        )

        return self.__parent__._cast(_2997.GearSetCompoundSystemDeflection)

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
    def hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3001.HypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3001,
        )

        return self.__parent__._cast(_3001.HypoidGearSetCompoundSystemDeflection)

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
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3005.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3005,
        )

        return self.__parent__._cast(
            _3005.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
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
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3008.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3008,
        )

        return self.__parent__._cast(
            _3008.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3011.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3011,
        )

        return self.__parent__._cast(
            _3011.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
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
    def microphone_array_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3014.MicrophoneArrayCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3014,
        )

        return self.__parent__._cast(_3014.MicrophoneArrayCompoundSystemDeflection)

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
    def part_to_part_shear_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3019.PartToPartShearCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3019,
        )

        return self.__parent__._cast(
            _3019.PartToPartShearCouplingCompoundSystemDeflection
        )

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
    def planetary_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3023.PlanetaryGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3023,
        )

        return self.__parent__._cast(_3023.PlanetaryGearSetCompoundSystemDeflection)

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
    def rolling_ring_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3030.RollingRingAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3030,
        )

        return self.__parent__._cast(_3030.RollingRingAssemblyCompoundSystemDeflection)

    @property
    def rolling_ring_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3031.RollingRingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3031,
        )

        return self.__parent__._cast(_3031.RollingRingCompoundSystemDeflection)

    @property
    def root_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3033.RootAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3033,
        )

        return self.__parent__._cast(_3033.RootAssemblyCompoundSystemDeflection)

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
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3038.SpecialisedAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3038,
        )

        return self.__parent__._cast(_3038.SpecialisedAssemblyCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3039.SpiralBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3039,
        )

        return self.__parent__._cast(_3039.SpiralBevelGearCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3041.SpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3041,
        )

        return self.__parent__._cast(_3041.SpiralBevelGearSetCompoundSystemDeflection)

    @property
    def spring_damper_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3042.SpringDamperCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3042,
        )

        return self.__parent__._cast(_3042.SpringDamperCompoundSystemDeflection)

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
    def straight_bevel_diff_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3047.StraightBevelDiffGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3047,
        )

        return self.__parent__._cast(
            _3047.StraightBevelDiffGearSetCompoundSystemDeflection
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
    def straight_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3050.StraightBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3050,
        )

        return self.__parent__._cast(_3050.StraightBevelGearSetCompoundSystemDeflection)

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
    def synchroniser_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3053.SynchroniserCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3053,
        )

        return self.__parent__._cast(_3053.SynchroniserCompoundSystemDeflection)

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
    def torque_converter_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3057.TorqueConverterCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3057,
        )

        return self.__parent__._cast(_3057.TorqueConverterCompoundSystemDeflection)

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
    def worm_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3065.WormGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3065,
        )

        return self.__parent__._cast(_3065.WormGearSetCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3066.ZerolBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3066,
        )

        return self.__parent__._cast(_3066.ZerolBevelGearCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3068.ZerolBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3068,
        )

        return self.__parent__._cast(_3068.ZerolBevelGearSetCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "PartCompoundSystemDeflection":
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
class PartCompoundSystemDeflection(_7711.PartCompoundAnalysis):
    """PartCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(self: "Self") -> "List[_2870.PartSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.PartSystemDeflection]

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
    ) -> "List[_2870.PartSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.PartSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_PartCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundSystemDeflection
        """
        return _Cast_PartCompoundSystemDeflection(self)
