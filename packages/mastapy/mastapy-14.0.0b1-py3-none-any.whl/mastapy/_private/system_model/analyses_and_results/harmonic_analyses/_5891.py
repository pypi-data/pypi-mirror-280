"""HarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7702
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses", "HarmonicAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.acoustic_analyses import (
        _7692,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6204,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5895,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7715,
        _7700,
    )
    from mastapy._private.system_model.analyses_and_results import _2733

    Self = TypeVar("Self", bound="HarmonicAnalysis")
    CastSelf = TypeVar("CastSelf", bound="HarmonicAnalysis._Cast_HarmonicAnalysis")


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicAnalysis:
    """Special nested class for casting HarmonicAnalysis to subclasses."""

    __parent__: "HarmonicAnalysis"

    @property
    def compound_analysis_case(self: "CastSelf") -> "_7702.CompoundAnalysisCase":
        return self.__parent__._cast(_7702.CompoundAnalysisCase)

    @property
    def static_load_analysis_case(self: "CastSelf") -> "_7715.StaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7715,
        )

        return self.__parent__._cast(_7715.StaticLoadAnalysisCase)

    @property
    def analysis_case(self: "CastSelf") -> "_7700.AnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7700,
        )

        return self.__parent__._cast(_7700.AnalysisCase)

    @property
    def context(self: "CastSelf") -> "_2733.Context":
        from mastapy._private.system_model.analyses_and_results import _2733

        return self.__parent__._cast(_2733.Context)

    @property
    def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_5895.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5895,
        )

        return self.__parent__._cast(
            _5895.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def harmonic_analysis(self: "CastSelf") -> "HarmonicAnalysis":
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
class HarmonicAnalysis(_7702.CompoundAnalysisCase):
    """HarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def time_for_modal_analysis(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeForModalAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def time_for_single_excitations_post_analysis(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeForSingleExcitationsPostAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_run_single_excitations(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToRunSingleExcitations

        if temp is None:
            return 0.0

        return temp

    @property
    def acoustic_analysis(self: "Self") -> "_7692.HarmonicAcousticAnalysis":
        """mastapy._private.system_model.analyses_and_results.acoustic_analyses.HarmonicAcousticAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AcousticAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: "Self",
    ) -> "List[_6204.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_HarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_HarmonicAnalysis
        """
        return _Cast_HarmonicAnalysis(self)
