"""ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5108,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5073,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5129,
        _5149,
        _5190,
        _5140,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self",
        bound="ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness:
    """Special nested class for casting ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

    __parent__: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"

    @property
    def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5108.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
        return self.__parent__._cast(
            _5108.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
        )

    @property
    def connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5140.ConnectionCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5140,
        )

        return self.__parent__._cast(_5140.ConnectionCompoundModalAnalysisAtAStiffness)

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
    def coaxial_connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5129.CoaxialConnectionCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5129,
        )

        return self.__parent__._cast(
            _5129.CoaxialConnectionCompoundModalAnalysisAtAStiffness
        )

    @property
    def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5149.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5149,
        )

        return self.__parent__._cast(
            _5149.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
        )

    @property
    def planetary_connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5190.PlanetaryConnectionCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5190,
        )

        return self.__parent__._cast(
            _5190.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
        )

    @property
    def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
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
class ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
    _5108.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_5073.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_5073.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]

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
    ) -> "_Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
        """
        return (
            _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
                self
            )
        )
