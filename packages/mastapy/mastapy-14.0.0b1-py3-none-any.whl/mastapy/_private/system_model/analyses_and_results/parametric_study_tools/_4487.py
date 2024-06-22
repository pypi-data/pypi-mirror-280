"""MicrophoneArrayParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
    _4521,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MICROPHONE_ARRAY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "MicrophoneArrayParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2519
    from mastapy._private.system_model.analyses_and_results.static_loads import _7071
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2865,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4403,
        _4502,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7710
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="MicrophoneArrayParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="MicrophoneArrayParametricStudyTool._Cast_MicrophoneArrayParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("MicrophoneArrayParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MicrophoneArrayParametricStudyTool:
    """Special nested class for casting MicrophoneArrayParametricStudyTool to subclasses."""

    __parent__: "MicrophoneArrayParametricStudyTool"

    @property
    def specialised_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4521.SpecialisedAssemblyParametricStudyTool":
        return self.__parent__._cast(_4521.SpecialisedAssemblyParametricStudyTool)

    @property
    def abstract_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4403.AbstractAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4403,
        )

        return self.__parent__._cast(_4403.AbstractAssemblyParametricStudyTool)

    @property
    def part_parametric_study_tool(self: "CastSelf") -> "_4502.PartParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4502,
        )

        return self.__parent__._cast(_4502.PartParametricStudyTool)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

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
    def microphone_array_parametric_study_tool(
        self: "CastSelf",
    ) -> "MicrophoneArrayParametricStudyTool":
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
class MicrophoneArrayParametricStudyTool(_4521.SpecialisedAssemblyParametricStudyTool):
    """MicrophoneArrayParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MICROPHONE_ARRAY_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2519.MicrophoneArray":
        """mastapy._private.system_model.part_model.MicrophoneArray

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7071.MicrophoneArrayLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.MicrophoneArrayLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: "Self",
    ) -> "List[_2865.MicrophoneArraySystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.MicrophoneArraySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_MicrophoneArrayParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_MicrophoneArrayParametricStudyTool
        """
        return _Cast_MicrophoneArrayParametricStudyTool(self)
