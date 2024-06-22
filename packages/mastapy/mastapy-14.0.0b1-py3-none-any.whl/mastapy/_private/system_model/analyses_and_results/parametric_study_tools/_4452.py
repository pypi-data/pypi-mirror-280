"""CylindricalGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
    _4470,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CylindricalGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2582
    from mastapy._private.system_model.analyses_and_results.static_loads import _7012
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2825,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4451,
        _4450,
        _4507,
        _4521,
        _4403,
        _4502,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7710
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="CylindricalGearSetParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearSetParametricStudyTool._Cast_CylindricalGearSetParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSetParametricStudyTool:
    """Special nested class for casting CylindricalGearSetParametricStudyTool to subclasses."""

    __parent__: "CylindricalGearSetParametricStudyTool"

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
    def planetary_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4507.PlanetaryGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4507,
        )

        return self.__parent__._cast(_4507.PlanetaryGearSetParametricStudyTool)

    @property
    def cylindrical_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "CylindricalGearSetParametricStudyTool":
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
class CylindricalGearSetParametricStudyTool(_4470.GearSetParametricStudyTool):
    """CylindricalGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2582.CylindricalGearSet":
        """mastapy._private.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7012.CylindricalGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

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
    ) -> "List[_2825.CylindricalGearSetSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflection]

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
    ) -> "List[_4451.CylindricalGearParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool]

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
    def cylindrical_gears_parametric_study_tool(
        self: "Self",
    ) -> "List[_4451.CylindricalGearParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_parametric_study_tool(
        self: "Self",
    ) -> "List[_4450.CylindricalGearMeshParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CylindricalGearMeshParametricStudyTool]

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
    def cylindrical_meshes_parametric_study_tool(
        self: "Self",
    ) -> "List[_4450.CylindricalGearMeshParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.CylindricalGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSetParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSetParametricStudyTool
        """
        return _Cast_CylindricalGearSetParametricStudyTool(self)
