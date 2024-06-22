"""AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5690,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5503
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5669,
        _5674,
        _5720,
        _5759,
        _5765,
        _5768,
        _5786,
        _5716,
        _5722,
        _5692,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"

    @property
    def conical_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5690.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(
            _5690.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5716.GearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5716,
        )

        return self.__parent__._cast(_5716.GearMeshCompoundMultibodyDynamicsAnalysis)

    @property
    def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5722.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5722,
        )

        return self.__parent__._cast(
            _5722.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5692.ConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5692,
        )

        return self.__parent__._cast(_5692.ConnectionCompoundMultibodyDynamicsAnalysis)

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
    def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5669.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5669,
        )

        return self.__parent__._cast(
            _5669.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5674.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5674,
        )

        return self.__parent__._cast(
            _5674.BevelGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5720.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5720,
        )

        return self.__parent__._cast(
            _5720.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5759.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5759,
        )

        return self.__parent__._cast(
            _5759.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5765.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5765,
        )

        return self.__parent__._cast(
            _5765.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5768.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5768,
        )

        return self.__parent__._cast(
            _5768.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5786.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5786,
        )

        return self.__parent__._cast(
            _5786.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
        )

    @property
    def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
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
class AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis(
    _5690.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_5503.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5503.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "_Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis(self)
