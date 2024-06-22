"""AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
    _6720,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import _2318
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6709,
        _6732,
        _6734,
        _6773,
        _6787,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar(
        "Self", bound="AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis:
    """Special nested class for casting AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis to subclasses."""

    __parent__: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"

    @property
    def connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6720.ConnectionCriticalSpeedAnalysis":
        return self.__parent__._cast(_6720.ConnectionCriticalSpeedAnalysis)

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7706.ConnectionStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

        return self.__parent__._cast(_7706.ConnectionStaticLoadAnalysisCase)

    @property
    def connection_analysis_case(self: "CastSelf") -> "_7703.ConnectionAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7703,
        )

        return self.__parent__._cast(_7703.ConnectionAnalysisCase)

    @property
    def connection_analysis(self: "CastSelf") -> "_2732.ConnectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.ConnectionAnalysis)

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
    def coaxial_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6709.CoaxialConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6709,
        )

        return self.__parent__._cast(_6709.CoaxialConnectionCriticalSpeedAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6732.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6732,
        )

        return self.__parent__._cast(
            _6732.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6734.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6734,
        )

        return self.__parent__._cast(
            _6734.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
        )

    @property
    def planetary_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6773.PlanetaryConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6773,
        )

        return self.__parent__._cast(_6773.PlanetaryConnectionCriticalSpeedAnalysis)

    @property
    def shaft_to_mountable_component_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6787.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6787,
        )

        return self.__parent__._cast(
            _6787.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
        )

    @property
    def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
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
class AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis(
    _6720.ConnectionCriticalSpeedAnalysis
):
    """AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(
        self: "Self",
    ) -> "_2318.AbstractShaftToMountableComponentConnection":
        """mastapy._private.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
        """
        return _Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis(
            self
        )
