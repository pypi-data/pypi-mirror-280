"""CouplingConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4617,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CouplingConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4440,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4574,
        _4579,
        _4635,
        _4657,
        _4672,
        _4587,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CouplingConnectionCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingConnectionCompoundParametricStudyTool:
    """Special nested class for casting CouplingConnectionCompoundParametricStudyTool to subclasses."""

    __parent__: "CouplingConnectionCompoundParametricStudyTool"

    @property
    def inter_mountable_component_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4617.InterMountableComponentConnectionCompoundParametricStudyTool":
        return self.__parent__._cast(
            _4617.InterMountableComponentConnectionCompoundParametricStudyTool
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
    def clutch_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4574.ClutchConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4574,
        )

        return self.__parent__._cast(_4574.ClutchConnectionCompoundParametricStudyTool)

    @property
    def concept_coupling_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4579.ConceptCouplingConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4579,
        )

        return self.__parent__._cast(
            _4579.ConceptCouplingConnectionCompoundParametricStudyTool
        )

    @property
    def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4635.PartToPartShearCouplingConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4635,
        )

        return self.__parent__._cast(
            _4635.PartToPartShearCouplingConnectionCompoundParametricStudyTool
        )

    @property
    def spring_damper_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4657.SpringDamperConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4657,
        )

        return self.__parent__._cast(
            _4657.SpringDamperConnectionCompoundParametricStudyTool
        )

    @property
    def torque_converter_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4672.TorqueConverterConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4672,
        )

        return self.__parent__._cast(
            _4672.TorqueConverterConnectionCompoundParametricStudyTool
        )

    @property
    def coupling_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "CouplingConnectionCompoundParametricStudyTool":
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
class CouplingConnectionCompoundParametricStudyTool(
    _4617.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """CouplingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_4440.CouplingConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CouplingConnectionParametricStudyTool]

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
    ) -> "List[_4440.CouplingConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CouplingConnectionParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_CouplingConnectionCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_CouplingConnectionCompoundParametricStudyTool
        """
        return _Cast_CouplingConnectionCompoundParametricStudyTool(self)
