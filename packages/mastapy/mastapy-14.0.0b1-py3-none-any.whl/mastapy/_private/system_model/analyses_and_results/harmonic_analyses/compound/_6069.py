"""GearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
    _6090,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "GearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5883,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6015,
        _6022,
        _6025,
        _6026,
        _6027,
        _6040,
        _6043,
        _6058,
        _6061,
        _6064,
        _6073,
        _6077,
        _6080,
        _6083,
        _6112,
        _6118,
        _6121,
        _6124,
        _6125,
        _6136,
        _6139,
        _6036,
        _6092,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="GearCompoundHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearCompoundHarmonicAnalysis:
    """Special nested class for casting GearCompoundHarmonicAnalysis to subclasses."""

    __parent__: "GearCompoundHarmonicAnalysis"

    @property
    def mountable_component_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6090.MountableComponentCompoundHarmonicAnalysis":
        return self.__parent__._cast(_6090.MountableComponentCompoundHarmonicAnalysis)

    @property
    def component_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6036.ComponentCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6036,
        )

        return self.__parent__._cast(_6036.ComponentCompoundHarmonicAnalysis)

    @property
    def part_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6092.PartCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6092,
        )

        return self.__parent__._cast(_6092.PartCompoundHarmonicAnalysis)

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
    def agma_gleason_conical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6015.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6015,
        )

        return self.__parent__._cast(
            _6015.AGMAGleasonConicalGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_differential_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6022.BevelDifferentialGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6022,
        )

        return self.__parent__._cast(
            _6022.BevelDifferentialGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6025.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6025,
        )

        return self.__parent__._cast(
            _6025.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6026.BevelDifferentialSunGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6026,
        )

        return self.__parent__._cast(
            _6026.BevelDifferentialSunGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6027.BevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6027,
        )

        return self.__parent__._cast(_6027.BevelGearCompoundHarmonicAnalysis)

    @property
    def concept_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6040.ConceptGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6040,
        )

        return self.__parent__._cast(_6040.ConceptGearCompoundHarmonicAnalysis)

    @property
    def conical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6043.ConicalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6043,
        )

        return self.__parent__._cast(_6043.ConicalGearCompoundHarmonicAnalysis)

    @property
    def cylindrical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6058.CylindricalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6058,
        )

        return self.__parent__._cast(_6058.CylindricalGearCompoundHarmonicAnalysis)

    @property
    def cylindrical_planet_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6061.CylindricalPlanetGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6061,
        )

        return self.__parent__._cast(
            _6061.CylindricalPlanetGearCompoundHarmonicAnalysis
        )

    @property
    def face_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6064.FaceGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6064,
        )

        return self.__parent__._cast(_6064.FaceGearCompoundHarmonicAnalysis)

    @property
    def hypoid_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6073.HypoidGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6073,
        )

        return self.__parent__._cast(_6073.HypoidGearCompoundHarmonicAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6077.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6077,
        )

        return self.__parent__._cast(
            _6077.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6080.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6080,
        )

        return self.__parent__._cast(
            _6080.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6083.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6083,
        )

        return self.__parent__._cast(
            _6083.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
        )

    @property
    def spiral_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6112.SpiralBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6112,
        )

        return self.__parent__._cast(_6112.SpiralBevelGearCompoundHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6118.StraightBevelDiffGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6118,
        )

        return self.__parent__._cast(
            _6118.StraightBevelDiffGearCompoundHarmonicAnalysis
        )

    @property
    def straight_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6121.StraightBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6121,
        )

        return self.__parent__._cast(_6121.StraightBevelGearCompoundHarmonicAnalysis)

    @property
    def straight_bevel_planet_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6124.StraightBevelPlanetGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6124,
        )

        return self.__parent__._cast(
            _6124.StraightBevelPlanetGearCompoundHarmonicAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6125.StraightBevelSunGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6125,
        )

        return self.__parent__._cast(_6125.StraightBevelSunGearCompoundHarmonicAnalysis)

    @property
    def worm_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6136.WormGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6136,
        )

        return self.__parent__._cast(_6136.WormGearCompoundHarmonicAnalysis)

    @property
    def zerol_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6139.ZerolBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6139,
        )

        return self.__parent__._cast(_6139.ZerolBevelGearCompoundHarmonicAnalysis)

    @property
    def gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "GearCompoundHarmonicAnalysis":
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
class GearCompoundHarmonicAnalysis(_6090.MountableComponentCompoundHarmonicAnalysis):
    """GearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_COMPOUND_HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(self: "Self") -> "List[_5883.GearHarmonicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis]

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
    ) -> "List[_5883.GearHarmonicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_GearCompoundHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_GearCompoundHarmonicAnalysis
        """
        return _Cast_GearCompoundHarmonicAnalysis(self)
