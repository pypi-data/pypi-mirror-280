"""ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6335,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6176,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6281,
        _6288,
        _6293,
        _6339,
        _6343,
        _6346,
        _6349,
        _6378,
        _6384,
        _6387,
        _6405,
        _6375,
        _6275,
        _6356,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"

    @property
    def gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6335.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6335.GearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6375.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6375,
        )

        return self.__parent__._cast(
            _6375.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6275.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6275,
        )

        return self.__parent__._cast(
            _6275.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6356.PartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6356,
        )

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
    def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6281.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6281,
        )

        return self.__parent__._cast(
            _6281.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6288.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6288,
        )

        return self.__parent__._cast(
            _6288.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6293.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6293,
        )

        return self.__parent__._cast(
            _6293.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6339.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6339,
        )

        return self.__parent__._cast(
            _6339.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6343.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6343,
        )

        return self.__parent__._cast(
            _6343.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6346.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6346,
        )

        return self.__parent__._cast(
            _6346.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6349.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6349,
        )

        return self.__parent__._cast(
            _6349.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6378.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6378,
        )

        return self.__parent__._cast(
            _6378.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6384.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6384,
        )

        return self.__parent__._cast(
            _6384.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6387.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6387,
        )

        return self.__parent__._cast(
            _6387.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6405.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6405,
        )

        return self.__parent__._cast(
            _6405.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
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
class ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6335.GearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6176.ConicalGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConicalGearSetHarmonicAnalysisOfSingleExcitation]

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
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6176.ConicalGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConicalGearSetHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
