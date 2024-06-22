"""ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6822,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6787,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6843,
        _6863,
        _6904,
        _6854,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis:
    """Special nested class for casting ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"

    @property
    def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> (
        "_6822.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
    ):
        return self.__parent__._cast(
            _6822.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6854.ConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6854,
        )

        return self.__parent__._cast(_6854.ConnectionCompoundCriticalSpeedAnalysis)

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.ConnectionCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.ConnectionCompoundAnalysis)

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
    def coaxial_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6843.CoaxialConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6843,
        )

        return self.__parent__._cast(
            _6843.CoaxialConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6863.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6863,
        )

        return self.__parent__._cast(
            _6863.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def planetary_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6904.PlanetaryConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6904,
        )

        return self.__parent__._cast(
            _6904.PlanetaryConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
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
class ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(
    _6822.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_6787.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6787.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
        """
        return _Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(
            self
        )
