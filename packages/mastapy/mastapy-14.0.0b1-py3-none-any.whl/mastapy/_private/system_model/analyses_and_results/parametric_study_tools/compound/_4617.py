"""InterMountableComponentConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4587,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "InterMountableComponentConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4475,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4557,
        _4561,
        _4564,
        _4569,
        _4574,
        _4579,
        _4582,
        _4585,
        _4590,
        _4592,
        _4600,
        _4606,
        _4611,
        _4615,
        _4619,
        _4622,
        _4625,
        _4635,
        _4644,
        _4647,
        _4654,
        _4657,
        _4660,
        _4663,
        _4672,
        _4678,
        _4681,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="InterMountableComponentConnectionCompoundParametricStudyTool"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnectionCompoundParametricStudyTool._Cast_InterMountableComponentConnectionCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnectionCompoundParametricStudyTool:
    """Special nested class for casting InterMountableComponentConnectionCompoundParametricStudyTool to subclasses."""

    __parent__: "InterMountableComponentConnectionCompoundParametricStudyTool"

    @property
    def connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4587.ConnectionCompoundParametricStudyTool":
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
    def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4557.AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4557,
        )

        return self.__parent__._cast(
            _4557.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
        )

    @property
    def belt_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4561.BeltConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4561,
        )

        return self.__parent__._cast(_4561.BeltConnectionCompoundParametricStudyTool)

    @property
    def bevel_differential_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4564.BevelDifferentialGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4564,
        )

        return self.__parent__._cast(
            _4564.BevelDifferentialGearMeshCompoundParametricStudyTool
        )

    @property
    def bevel_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4569.BevelGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4569,
        )

        return self.__parent__._cast(_4569.BevelGearMeshCompoundParametricStudyTool)

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
    def concept_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4582.ConceptGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4582,
        )

        return self.__parent__._cast(_4582.ConceptGearMeshCompoundParametricStudyTool)

    @property
    def conical_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4585.ConicalGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4585,
        )

        return self.__parent__._cast(_4585.ConicalGearMeshCompoundParametricStudyTool)

    @property
    def coupling_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4590.CouplingConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4590,
        )

        return self.__parent__._cast(
            _4590.CouplingConnectionCompoundParametricStudyTool
        )

    @property
    def cvt_belt_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4592.CVTBeltConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4592,
        )

        return self.__parent__._cast(_4592.CVTBeltConnectionCompoundParametricStudyTool)

    @property
    def cylindrical_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4600.CylindricalGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4600,
        )

        return self.__parent__._cast(
            _4600.CylindricalGearMeshCompoundParametricStudyTool
        )

    @property
    def face_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4606.FaceGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4606,
        )

        return self.__parent__._cast(_4606.FaceGearMeshCompoundParametricStudyTool)

    @property
    def gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4611.GearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4611,
        )

        return self.__parent__._cast(_4611.GearMeshCompoundParametricStudyTool)

    @property
    def hypoid_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4615.HypoidGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4615,
        )

        return self.__parent__._cast(_4615.HypoidGearMeshCompoundParametricStudyTool)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4619.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4619,
        )

        return self.__parent__._cast(
            _4619.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4622.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4622,
        )

        return self.__parent__._cast(
            _4622.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4625.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4625,
        )

        return self.__parent__._cast(
            _4625.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
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
    def ring_pins_to_disc_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4644.RingPinsToDiscConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4644,
        )

        return self.__parent__._cast(
            _4644.RingPinsToDiscConnectionCompoundParametricStudyTool
        )

    @property
    def rolling_ring_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4647.RollingRingConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4647,
        )

        return self.__parent__._cast(
            _4647.RollingRingConnectionCompoundParametricStudyTool
        )

    @property
    def spiral_bevel_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4654.SpiralBevelGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4654,
        )

        return self.__parent__._cast(
            _4654.SpiralBevelGearMeshCompoundParametricStudyTool
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
    def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4660.StraightBevelDiffGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4660,
        )

        return self.__parent__._cast(
            _4660.StraightBevelDiffGearMeshCompoundParametricStudyTool
        )

    @property
    def straight_bevel_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4663.StraightBevelGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4663,
        )

        return self.__parent__._cast(
            _4663.StraightBevelGearMeshCompoundParametricStudyTool
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
    def worm_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4678.WormGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4678,
        )

        return self.__parent__._cast(_4678.WormGearMeshCompoundParametricStudyTool)

    @property
    def zerol_bevel_gear_mesh_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4681.ZerolBevelGearMeshCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4681,
        )

        return self.__parent__._cast(
            _4681.ZerolBevelGearMeshCompoundParametricStudyTool
        )

    @property
    def inter_mountable_component_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "InterMountableComponentConnectionCompoundParametricStudyTool":
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
class InterMountableComponentConnectionCompoundParametricStudyTool(
    _4587.ConnectionCompoundParametricStudyTool
):
    """InterMountableComponentConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_4475.InterMountableComponentConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.InterMountableComponentConnectionParametricStudyTool]

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
    ) -> "List[_4475.InterMountableComponentConnectionParametricStudyTool]":
        """List[mastapy._private.system_model.analyses_and_results.parametric_study_tools.InterMountableComponentConnectionParametricStudyTool]

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
    ) -> "_Cast_InterMountableComponentConnectionCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnectionCompoundParametricStudyTool
        """
        return _Cast_InterMountableComponentConnectionCompoundParametricStudyTool(self)
