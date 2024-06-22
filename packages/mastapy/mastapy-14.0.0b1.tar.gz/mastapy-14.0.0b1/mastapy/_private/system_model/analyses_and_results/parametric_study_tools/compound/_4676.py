"""VirtualComponentCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4631,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "VirtualComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4545,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4627,
        _4628,
        _4640,
        _4641,
        _4675,
        _4577,
        _4633,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="VirtualComponentCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_VirtualComponentCompoundParametricStudyTool:
    """Special nested class for casting VirtualComponentCompoundParametricStudyTool to subclasses."""

    __parent__: "VirtualComponentCompoundParametricStudyTool"

    @property
    def mountable_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4631.MountableComponentCompoundParametricStudyTool":
        return self.__parent__._cast(
            _4631.MountableComponentCompoundParametricStudyTool
        )

    @property
    def component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4577.ComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4577,
        )

        return self.__parent__._cast(_4577.ComponentCompoundParametricStudyTool)

    @property
    def part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4633.PartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4633,
        )

        return self.__parent__._cast(_4633.PartCompoundParametricStudyTool)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.PartCompoundAnalysis)

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
    def mass_disc_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4627.MassDiscCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4627,
        )

        return self.__parent__._cast(_4627.MassDiscCompoundParametricStudyTool)

    @property
    def measurement_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4628.MeasurementComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4628,
        )

        return self.__parent__._cast(
            _4628.MeasurementComponentCompoundParametricStudyTool
        )

    @property
    def point_load_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4640.PointLoadCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4640,
        )

        return self.__parent__._cast(_4640.PointLoadCompoundParametricStudyTool)

    @property
    def power_load_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4641.PowerLoadCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4641,
        )

        return self.__parent__._cast(_4641.PowerLoadCompoundParametricStudyTool)

    @property
    def unbalanced_mass_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4675.UnbalancedMassCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4675,
        )

        return self.__parent__._cast(_4675.UnbalancedMassCompoundParametricStudyTool)

    @property
    def virtual_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "VirtualComponentCompoundParametricStudyTool":
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
class VirtualComponentCompoundParametricStudyTool(
    _4631.MountableComponentCompoundParametricStudyTool
):
    """VirtualComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _VIRTUAL_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_4545.VirtualComponentParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.VirtualComponentParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4545.VirtualComponentParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.VirtualComponentParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_VirtualComponentCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_VirtualComponentCompoundParametricStudyTool
        """
        return _Cast_VirtualComponentCompoundParametricStudyTool(self)
