"""ShaftToMountableComponentConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
    _4001,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3963,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
        _4022,
        _4042,
        _4083,
        _4033,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="ShaftToMountableComponentConnectionCompoundStabilityAnalysis"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundStabilityAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis:
    """Special nested class for casting ShaftToMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

    __parent__: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis"

    @property
    def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4001.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis":
        return self.__parent__._cast(
            _4001.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
        )

    @property
    def connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4033.ConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4033,
        )

        return self.__parent__._cast(_4033.ConnectionCompoundStabilityAnalysis)

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
    def coaxial_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4022.CoaxialConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4022,
        )

        return self.__parent__._cast(_4022.CoaxialConnectionCompoundStabilityAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4042.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4042,
        )

        return self.__parent__._cast(
            _4042.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
        )

    @property
    def planetary_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4083.PlanetaryConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4083,
        )

        return self.__parent__._cast(_4083.PlanetaryConnectionCompoundStabilityAnalysis)

    @property
    def shaft_to_mountable_component_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
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
class ShaftToMountableComponentConnectionCompoundStabilityAnalysis(
    _4001.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
):
    """ShaftToMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_3963.ShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ShaftToMountableComponentConnectionStabilityAnalysis]

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
    ) -> "List[_3963.ShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.ShaftToMountableComponentConnectionStabilityAnalysis]

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
    ) -> "_Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis
        """
        return _Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis(self)
