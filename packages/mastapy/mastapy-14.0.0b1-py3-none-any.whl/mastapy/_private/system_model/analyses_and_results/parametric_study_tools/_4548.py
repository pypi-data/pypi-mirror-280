"""WormGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
    _4470,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_WORM_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "WormGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2608
    from mastapy._private.system_model.analyses_and_results.static_loads import _7133
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2922,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4547,
        _4546,
        _4521,
        _4403,
        _4502,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7710
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="WormGearSetParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="WormGearSetParametricStudyTool._Cast_WormGearSetParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGearSetParametricStudyTool:
    """Special nested class for casting WormGearSetParametricStudyTool to subclasses."""

    __parent__: "WormGearSetParametricStudyTool"

    @property
    def gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4470.GearSetParametricStudyTool":
        return self.__parent__._cast(_4470.GearSetParametricStudyTool)

    @property
    def specialised_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4521.SpecialisedAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4521,
        )

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
    def worm_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "WormGearSetParametricStudyTool":
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
class WormGearSetParametricStudyTool(_4470.GearSetParametricStudyTool):
    """WormGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GEAR_SET_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2608.WormGearSet":
        """mastapy._private.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7133.WormGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

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
    ) -> "List[_2922.WormGearSetSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection]

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
    def gears_parametric_study_tool(
        self: "Self",
    ) -> "List[_4547.WormGearParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.WormGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gears_parametric_study_tool(
        self: "Self",
    ) -> "List[_4547.WormGearParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.WormGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_parametric_study_tool(
        self: "Self",
    ) -> "List[_4546.WormGearMeshParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.WormGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_parametric_study_tool(
        self: "Self",
    ) -> "List[_4546.WormGearMeshParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.WormGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_WormGearSetParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_WormGearSetParametricStudyTool
        """
        return _Cast_WormGearSetParametricStudyTool(self)
