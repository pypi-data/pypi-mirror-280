"""SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6293,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2600
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6247,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6376,
        _6377,
        _6281,
        _6309,
        _6335,
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
        "Self", bound="SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"

    @property
    def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6293.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6293.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

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
    def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6309.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6309,
        )

        return self.__parent__._cast(
            _6309.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6335.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6335,
        )

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
    def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
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
class SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6293.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2600.SpiralBevelGearSet":
        """mastapy._private.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2600.SpiralBevelGearSet":
        """mastapy._private.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6247.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    def spiral_bevel_gears_compound_harmonic_analysis_of_single_excitation(
        self: "Self",
    ) -> "List[_6376.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_harmonic_analysis_of_single_excitation(
        self: "Self",
    ) -> "List[_6377.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6247.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
