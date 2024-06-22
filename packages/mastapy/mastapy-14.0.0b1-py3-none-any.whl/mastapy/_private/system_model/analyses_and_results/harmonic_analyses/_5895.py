"""HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5891
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
        "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7702,
        _7715,
        _7700,
    )
    from mastapy._private.system_model.analyses_and_results import _2733

    Self = TypeVar(
        "Self", bound="HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
    """Special nested class for casting HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

    __parent__: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"

    @property
    def harmonic_analysis(self: "CastSelf") -> "_5891.HarmonicAnalysis":
        return self.__parent__._cast(_5891.HarmonicAnalysis)

    @property
    def compound_analysis_case(self: "CastSelf") -> "_7702.CompoundAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7702,
        )

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
    ) -> "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
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
class HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
    _5891.HarmonicAnalysis
):
    """HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        """Cast to another type.

        Returns:
            _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
        """
        return _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(self)
