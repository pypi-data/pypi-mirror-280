"""StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6160,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2602
    from mastapy._private.system_model.analyses_and_results.static_loads import _7110
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6251,
        _6252,
        _6148,
        _6176,
        _6202,
        _6244,
        _6142,
        _6225,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar(
        "Self", bound="StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation"

    @property
    def bevel_gear_set_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6160.BevelGearSetHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6160.BevelGearSetHarmonicAnalysisOfSingleExcitation
        )

    @property
    def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6148.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6148,
        )

        return self.__parent__._cast(
            _6148.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_set_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6176.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6176,
        )

        return self.__parent__._cast(
            _6176.ConicalGearSetHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_set_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6202.GearSetHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6202,
        )

        return self.__parent__._cast(_6202.GearSetHarmonicAnalysisOfSingleExcitation)

    @property
    def specialised_assembly_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6244.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6244,
        )

        return self.__parent__._cast(
            _6244.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_assembly_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6142.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6142,
        )

        return self.__parent__._cast(
            _6142.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6225.PartHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6225,
        )

        return self.__parent__._cast(_6225.PartHarmonicAnalysisOfSingleExcitation)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
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
class StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation(
    _6160.BevelGearSetHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _STRAIGHT_BEVEL_DIFF_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2602.StraightBevelDiffGearSet":
        """mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7110.StraightBevelDiffGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_harmonic_analysis_of_single_excitation(
        self: "Self",
    ) -> "List[_6251.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gears_harmonic_analysis_of_single_excitation(
        self: "Self",
    ) -> "List[_6251.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_harmonic_analysis_of_single_excitation(
        self: "Self",
    ) -> "List[_6252.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_harmonic_analysis_of_single_excitation(
        self: "Self",
    ) -> "List[_6252.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation(self)
