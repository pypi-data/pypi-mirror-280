"""TimeSeriesLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _6950
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_TIME_SERIES_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TimeSeriesLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2722, _2703, _2733
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5585
    from mastapy._private.system_model.analyses_and_results.load_case_groups import (
        _5801,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import _6964

    Self = TypeVar("Self", bound="TimeSeriesLoadCase")
    CastSelf = TypeVar("CastSelf", bound="TimeSeriesLoadCase._Cast_TimeSeriesLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("TimeSeriesLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_TimeSeriesLoadCase:
    """Special nested class for casting TimeSeriesLoadCase to subclasses."""

    __parent__: "TimeSeriesLoadCase"

    @property
    def load_case(self: "CastSelf") -> "_6950.LoadCase":
        return self.__parent__._cast(_6950.LoadCase)

    @property
    def context(self: "CastSelf") -> "_2733.Context":
        from mastapy._private.system_model.analyses_and_results import _2733

        return self.__parent__._cast(_2733.Context)

    @property
    def time_series_load_case(self: "CastSelf") -> "TimeSeriesLoadCase":
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
class TimeSeriesLoadCase(_6950.LoadCase):
    """TimeSeriesLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _TIME_SERIES_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def multibody_dynamics_analysis(self: "Self") -> "_2722.MultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def duration_for_rating(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DurationForRating

        if temp is None:
            return 0.0

        return temp

    @duration_for_rating.setter
    @enforce_parameter_types
    def duration_for_rating(self: "Self", value: "float") -> None:
        self.wrapped.DurationForRating = float(value) if value is not None else 0.0

    @property
    def driva_analysis_options(self: "Self") -> "_5585.MBDAnalysisOptions":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MBDAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DRIVAAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case_group(self: "Self") -> "_5801.TimeSeriesLoadCaseGroup":
        """mastapy._private.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCaseGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_of(
        self: "Self", analysis_type: "_6964.AnalysisType"
    ) -> "_2703.SingleAnalysis":
        """mastapy._private.system_model.analyses_and_results.SingleAnalysis

        Args:
            analysis_type (mastapy._private.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate(
        self: "Self",
        new_load_case_group: "_5801.TimeSeriesLoadCaseGroup",
        name: "str" = "None",
    ) -> "TimeSeriesLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Args:
            new_load_case_group (mastapy._private.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup)
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.Duplicate(
            new_load_case_group.wrapped if new_load_case_group else None,
            name if name else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_TimeSeriesLoadCase":
        """Cast to another type.

        Returns:
            _Cast_TimeSeriesLoadCase
        """
        return _Cast_TimeSeriesLoadCase(self)
