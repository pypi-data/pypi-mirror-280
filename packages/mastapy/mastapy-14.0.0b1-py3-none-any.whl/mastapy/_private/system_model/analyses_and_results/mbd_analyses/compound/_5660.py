"""AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5692,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5502
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5681,
        _5701,
        _5703,
        _5742,
        _5756,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self",
        bound="AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"

    @property
    def connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5692.ConnectionCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5692.ConnectionCompoundMultibodyDynamicsAnalysis)

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
    def coaxial_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5681.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5681,
        )

        return self.__parent__._cast(
            _5681.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5701.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5701,
        )

        return self.__parent__._cast(
            _5701.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> (
        "_5703.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5703,
        )

        return self.__parent__._cast(
            _5703.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def planetary_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5742.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5742,
        )

        return self.__parent__._cast(
            _5742.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5756.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5756,
        )

        return self.__parent__._cast(
            _5756.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
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
class AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5692.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_5502.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5502.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "_Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
