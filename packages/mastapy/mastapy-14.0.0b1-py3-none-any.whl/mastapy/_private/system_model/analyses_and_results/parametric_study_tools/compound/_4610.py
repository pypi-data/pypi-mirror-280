"""GearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4631,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.rating import _368
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4469,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4556,
        _4563,
        _4566,
        _4567,
        _4568,
        _4581,
        _4584,
        _4599,
        _4602,
        _4605,
        _4614,
        _4618,
        _4621,
        _4624,
        _4653,
        _4659,
        _4662,
        _4665,
        _4666,
        _4677,
        _4680,
        _4577,
        _4633,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="GearCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearCompoundParametricStudyTool:
    """Special nested class for casting GearCompoundParametricStudyTool to subclasses."""

    __parent__: "GearCompoundParametricStudyTool"

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
    def agma_gleason_conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4556.AGMAGleasonConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4556,
        )

        return self.__parent__._cast(
            _4556.AGMAGleasonConicalGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4563.BevelDifferentialGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4563,
        )

        return self.__parent__._cast(
            _4563.BevelDifferentialGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4566.BevelDifferentialPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4566,
        )

        return self.__parent__._cast(
            _4566.BevelDifferentialPlanetGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_sun_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4567.BevelDifferentialSunGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4567,
        )

        return self.__parent__._cast(
            _4567.BevelDifferentialSunGearCompoundParametricStudyTool
        )

    @property
    def bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4568.BevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4568,
        )

        return self.__parent__._cast(_4568.BevelGearCompoundParametricStudyTool)

    @property
    def concept_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4581.ConceptGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4581,
        )

        return self.__parent__._cast(_4581.ConceptGearCompoundParametricStudyTool)

    @property
    def conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4584.ConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4584,
        )

        return self.__parent__._cast(_4584.ConicalGearCompoundParametricStudyTool)

    @property
    def cylindrical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4599.CylindricalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4599,
        )

        return self.__parent__._cast(_4599.CylindricalGearCompoundParametricStudyTool)

    @property
    def cylindrical_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4602.CylindricalPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4602,
        )

        return self.__parent__._cast(
            _4602.CylindricalPlanetGearCompoundParametricStudyTool
        )

    @property
    def face_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4605.FaceGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4605,
        )

        return self.__parent__._cast(_4605.FaceGearCompoundParametricStudyTool)

    @property
    def hypoid_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4614.HypoidGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4614,
        )

        return self.__parent__._cast(_4614.HypoidGearCompoundParametricStudyTool)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4618.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4618,
        )

        return self.__parent__._cast(
            _4618.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4621.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4621,
        )

        return self.__parent__._cast(
            _4621.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4624.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4624,
        )

        return self.__parent__._cast(
            _4624.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
        )

    @property
    def spiral_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4653.SpiralBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4653,
        )

        return self.__parent__._cast(_4653.SpiralBevelGearCompoundParametricStudyTool)

    @property
    def straight_bevel_diff_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4659.StraightBevelDiffGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4659,
        )

        return self.__parent__._cast(
            _4659.StraightBevelDiffGearCompoundParametricStudyTool
        )

    @property
    def straight_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4662.StraightBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4662,
        )

        return self.__parent__._cast(_4662.StraightBevelGearCompoundParametricStudyTool)

    @property
    def straight_bevel_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4665.StraightBevelPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4665,
        )

        return self.__parent__._cast(
            _4665.StraightBevelPlanetGearCompoundParametricStudyTool
        )

    @property
    def straight_bevel_sun_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4666.StraightBevelSunGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4666,
        )

        return self.__parent__._cast(
            _4666.StraightBevelSunGearCompoundParametricStudyTool
        )

    @property
    def worm_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4677.WormGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4677,
        )

        return self.__parent__._cast(_4677.WormGearCompoundParametricStudyTool)

    @property
    def zerol_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4680.ZerolBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4680,
        )

        return self.__parent__._cast(_4680.ZerolBevelGearCompoundParametricStudyTool)

    @property
    def gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "GearCompoundParametricStudyTool":
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
class GearCompoundParametricStudyTool(
    _4631.MountableComponentCompoundParametricStudyTool
):
    """GearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def gear_duty_cycle_results(self: "Self") -> "_368.GearDutyCycleRating":
        """mastapy._private.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: "Self") -> "List[_4469.GearParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

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
    ) -> "List[_4469.GearParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_GearCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_GearCompoundParametricStudyTool
        """
        return _Cast_GearCompoundParametricStudyTool(self)
