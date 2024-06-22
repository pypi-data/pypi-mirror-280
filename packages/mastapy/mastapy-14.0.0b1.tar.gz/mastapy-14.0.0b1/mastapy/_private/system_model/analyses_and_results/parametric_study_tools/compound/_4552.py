"""AbstractAssemblyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4633,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AbstractAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4403,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4558,
        _4559,
        _4562,
        _4565,
        _4570,
        _4572,
        _4573,
        _4578,
        _4583,
        _4586,
        _4589,
        _4593,
        _4595,
        _4601,
        _4607,
        _4609,
        _4612,
        _4616,
        _4620,
        _4623,
        _4626,
        _4629,
        _4634,
        _4638,
        _4645,
        _4648,
        _4652,
        _4655,
        _4656,
        _4661,
        _4664,
        _4667,
        _4671,
        _4679,
        _4682,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="AbstractAssemblyCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssemblyCompoundParametricStudyTool:
    """Special nested class for casting AbstractAssemblyCompoundParametricStudyTool to subclasses."""

    __parent__: "AbstractAssemblyCompoundParametricStudyTool"

    @property
    def part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4633.PartCompoundParametricStudyTool":
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
    def agma_gleason_conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4558.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4558,
        )

        return self.__parent__._cast(
            _4558.AGMAGleasonConicalGearSetCompoundParametricStudyTool
        )

    @property
    def assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4559.AssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4559,
        )

        return self.__parent__._cast(_4559.AssemblyCompoundParametricStudyTool)

    @property
    def belt_drive_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4562.BeltDriveCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4562,
        )

        return self.__parent__._cast(_4562.BeltDriveCompoundParametricStudyTool)

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
    def bolted_joint_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4572.BoltedJointCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4572,
        )

        return self.__parent__._cast(_4572.BoltedJointCompoundParametricStudyTool)

    @property
    def clutch_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4573.ClutchCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4573,
        )

        return self.__parent__._cast(_4573.ClutchCompoundParametricStudyTool)

    @property
    def concept_coupling_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4578.ConceptCouplingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4578,
        )

        return self.__parent__._cast(_4578.ConceptCouplingCompoundParametricStudyTool)

    @property
    def concept_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4583.ConceptGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4583,
        )

        return self.__parent__._cast(_4583.ConceptGearSetCompoundParametricStudyTool)

    @property
    def conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4586.ConicalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4586,
        )

        return self.__parent__._cast(_4586.ConicalGearSetCompoundParametricStudyTool)

    @property
    def coupling_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4589.CouplingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4589,
        )

        return self.__parent__._cast(_4589.CouplingCompoundParametricStudyTool)

    @property
    def cvt_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4593.CVTCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4593,
        )

        return self.__parent__._cast(_4593.CVTCompoundParametricStudyTool)

    @property
    def cycloidal_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4595.CycloidalAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4595,
        )

        return self.__parent__._cast(_4595.CycloidalAssemblyCompoundParametricStudyTool)

    @property
    def cylindrical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4601.CylindricalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4601,
        )

        return self.__parent__._cast(
            _4601.CylindricalGearSetCompoundParametricStudyTool
        )

    @property
    def face_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4607.FaceGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4607,
        )

        return self.__parent__._cast(_4607.FaceGearSetCompoundParametricStudyTool)

    @property
    def flexible_pin_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4609.FlexiblePinAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4609,
        )

        return self.__parent__._cast(
            _4609.FlexiblePinAssemblyCompoundParametricStudyTool
        )

    @property
    def gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4612.GearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4612,
        )

        return self.__parent__._cast(_4612.GearSetCompoundParametricStudyTool)

    @property
    def hypoid_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4616.HypoidGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4616,
        )

        return self.__parent__._cast(_4616.HypoidGearSetCompoundParametricStudyTool)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4620.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4620,
        )

        return self.__parent__._cast(
            _4620.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4623.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4623,
        )

        return self.__parent__._cast(
            _4623.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4626.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4626,
        )

        return self.__parent__._cast(
            _4626.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
        )

    @property
    def microphone_array_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4629.MicrophoneArrayCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4629,
        )

        return self.__parent__._cast(_4629.MicrophoneArrayCompoundParametricStudyTool)

    @property
    def part_to_part_shear_coupling_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4634.PartToPartShearCouplingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4634,
        )

        return self.__parent__._cast(
            _4634.PartToPartShearCouplingCompoundParametricStudyTool
        )

    @property
    def planetary_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4638.PlanetaryGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4638,
        )

        return self.__parent__._cast(_4638.PlanetaryGearSetCompoundParametricStudyTool)

    @property
    def rolling_ring_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4645.RollingRingAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4645,
        )

        return self.__parent__._cast(
            _4645.RollingRingAssemblyCompoundParametricStudyTool
        )

    @property
    def root_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4648.RootAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4648,
        )

        return self.__parent__._cast(_4648.RootAssemblyCompoundParametricStudyTool)

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
    def spring_damper_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4656.SpringDamperCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4656,
        )

        return self.__parent__._cast(_4656.SpringDamperCompoundParametricStudyTool)

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
    def synchroniser_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4667.SynchroniserCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4667,
        )

        return self.__parent__._cast(_4667.SynchroniserCompoundParametricStudyTool)

    @property
    def torque_converter_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4671.TorqueConverterCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4671,
        )

        return self.__parent__._cast(_4671.TorqueConverterCompoundParametricStudyTool)

    @property
    def worm_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4679.WormGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4679,
        )

        return self.__parent__._cast(_4679.WormGearSetCompoundParametricStudyTool)

    @property
    def zerol_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4682.ZerolBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4682,
        )

        return self.__parent__._cast(_4682.ZerolBevelGearSetCompoundParametricStudyTool)

    @property
    def abstract_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "AbstractAssemblyCompoundParametricStudyTool":
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
class AbstractAssemblyCompoundParametricStudyTool(
    _4633.PartCompoundParametricStudyTool
):
    """AbstractAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_4403.AbstractAssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool]

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
    ) -> "List[_4403.AbstractAssemblyParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_AbstractAssemblyCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssemblyCompoundParametricStudyTool
        """
        return _Cast_AbstractAssemblyCompoundParametricStudyTool(self)
