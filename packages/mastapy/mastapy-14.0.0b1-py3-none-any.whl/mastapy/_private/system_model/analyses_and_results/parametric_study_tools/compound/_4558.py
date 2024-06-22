"""AGMAGleasonConicalGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4586,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4409,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4565,
        _4570,
        _4616,
        _4655,
        _4661,
        _4664,
        _4682,
        _4612,
        _4652,
        _4552,
        _4633,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool:
    """Special nested class for casting AGMAGleasonConicalGearSetCompoundParametricStudyTool to subclasses."""

    __parent__: "AGMAGleasonConicalGearSetCompoundParametricStudyTool"

    @property
    def conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4586.ConicalGearSetCompoundParametricStudyTool":
        return self.__parent__._cast(_4586.ConicalGearSetCompoundParametricStudyTool)

    @property
    def gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4612.GearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4612,
        )

        return self.__parent__._cast(_4612.GearSetCompoundParametricStudyTool)

    @property
    def specialised_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4652.SpecialisedAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4652,
        )

        return self.__parent__._cast(
            _4652.SpecialisedAssemblyCompoundParametricStudyTool
        )

    @property
    def abstract_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4552.AbstractAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4552,
        )

        return self.__parent__._cast(_4552.AbstractAssemblyCompoundParametricStudyTool)

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
    def bevel_differential_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4565.BevelDifferentialGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4565,
        )

        return self.__parent__._cast(
            _4565.BevelDifferentialGearSetCompoundParametricStudyTool
        )

    @property
    def bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4570.BevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4570,
        )

        return self.__parent__._cast(_4570.BevelGearSetCompoundParametricStudyTool)

    @property
    def hypoid_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4616.HypoidGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4616,
        )

        return self.__parent__._cast(_4616.HypoidGearSetCompoundParametricStudyTool)

    @property
    def spiral_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4655.SpiralBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4655,
        )

        return self.__parent__._cast(
            _4655.SpiralBevelGearSetCompoundParametricStudyTool
        )

    @property
    def straight_bevel_diff_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4661.StraightBevelDiffGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4661,
        )

        return self.__parent__._cast(
            _4661.StraightBevelDiffGearSetCompoundParametricStudyTool
        )

    @property
    def straight_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4664.StraightBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4664,
        )

        return self.__parent__._cast(
            _4664.StraightBevelGearSetCompoundParametricStudyTool
        )

    @property
    def zerol_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4682.ZerolBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4682,
        )

        return self.__parent__._cast(_4682.ZerolBevelGearSetCompoundParametricStudyTool)

    @property
    def agma_gleason_conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearSetCompoundParametricStudyTool":
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
class AGMAGleasonConicalGearSetCompoundParametricStudyTool(
    _4586.ConicalGearSetCompoundParametricStudyTool
):
    """AGMAGleasonConicalGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_4409.AGMAGleasonConicalGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4409.AGMAGleasonConicalGearSetParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool
        """
        return _Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool(self)
