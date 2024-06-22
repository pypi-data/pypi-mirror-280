"""SynchroniserSleeveCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4669,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SynchroniserSleeveCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.couplings import _2668
    from mastapy._private.system_model.analyses_and_results.static_loads import _7119
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4539,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4591,
        _4631,
        _4577,
        _4633,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="SynchroniserSleeveCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SynchroniserSleeveCompoundParametricStudyTool._Cast_SynchroniserSleeveCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SynchroniserSleeveCompoundParametricStudyTool:
    """Special nested class for casting SynchroniserSleeveCompoundParametricStudyTool to subclasses."""

    __parent__: "SynchroniserSleeveCompoundParametricStudyTool"

    @property
    def synchroniser_part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4669.SynchroniserPartCompoundParametricStudyTool":
        return self.__parent__._cast(_4669.SynchroniserPartCompoundParametricStudyTool)

    @property
    def coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4591.CouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4591,
        )

        return self.__parent__._cast(_4591.CouplingHalfCompoundParametricStudyTool)

    @property
    def mountable_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4631.MountableComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4631,
        )

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
    def synchroniser_sleeve_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "SynchroniserSleeveCompoundParametricStudyTool":
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
class SynchroniserSleeveCompoundParametricStudyTool(
    _4669.SynchroniserPartCompoundParametricStudyTool
):
    """SynchroniserSleeveCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SYNCHRONISER_SLEEVE_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2668.SynchroniserSleeve":
        """mastapy._private.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: "Self",
    ) -> "_7119.SynchroniserSleeveLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4539.SynchroniserSleeveParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.SynchroniserSleeveParametricStudyTool]

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
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_4539.SynchroniserSleeveParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.SynchroniserSleeveParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_SynchroniserSleeveCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_SynchroniserSleeveCompoundParametricStudyTool
        """
        return _Cast_SynchroniserSleeveCompoundParametricStudyTool(self)
