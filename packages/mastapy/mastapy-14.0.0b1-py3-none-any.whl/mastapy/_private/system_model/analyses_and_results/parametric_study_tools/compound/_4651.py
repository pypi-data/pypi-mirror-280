"""ShaftToMountableComponentConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4555,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4520,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4576,
        _4596,
        _4637,
        _4587,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="ShaftToMountableComponentConnectionCompoundParametricStudyTool"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool:
    """Special nested class for casting ShaftToMountableComponentConnectionCompoundParametricStudyTool to subclasses."""

    __parent__: "ShaftToMountableComponentConnectionCompoundParametricStudyTool"

    @property
    def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4555.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
        return self.__parent__._cast(
            _4555.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
        )

    @property
    def connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4587.ConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4587,
        )

        return self.__parent__._cast(_4587.ConnectionCompoundParametricStudyTool)

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
    def coaxial_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4576.CoaxialConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4576,
        )

        return self.__parent__._cast(_4576.CoaxialConnectionCompoundParametricStudyTool)

    @property
    def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4596.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4596,
        )

        return self.__parent__._cast(
            _4596.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
        )

    @property
    def planetary_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4637.PlanetaryConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4637,
        )

        return self.__parent__._cast(
            _4637.PlanetaryConnectionCompoundParametricStudyTool
        )

    @property
    def shaft_to_mountable_component_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "ShaftToMountableComponentConnectionCompoundParametricStudyTool":
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
class ShaftToMountableComponentConnectionCompoundParametricStudyTool(
    _4555.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
):
    """ShaftToMountableComponentConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_4520.ShaftToMountableComponentConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ShaftToMountableComponentConnectionParametricStudyTool]

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
    ) -> "List[_4520.ShaftToMountableComponentConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.ShaftToMountableComponentConnectionParametricStudyTool]

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
    ) -> "_Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool
        """
        return _Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool(
            self
        )
