"""ZerolBevelGearMeshCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
    _6565,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ZerolBevelGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.connections_and_sockets.gears import _2384
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6546,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6553,
        _6581,
        _6607,
        _6613,
        _6583,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundDynamicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundDynamicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ZerolBevelGearMeshCompoundDynamicAnalysis:
    """Special nested class for casting ZerolBevelGearMeshCompoundDynamicAnalysis to subclasses."""

    __parent__: "ZerolBevelGearMeshCompoundDynamicAnalysis"

    @property
    def bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6565.BevelGearMeshCompoundDynamicAnalysis":
        return self.__parent__._cast(_6565.BevelGearMeshCompoundDynamicAnalysis)

    @property
    def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6553.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6553,
        )

        return self.__parent__._cast(
            _6553.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
        )

    @property
    def conical_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6581.ConicalGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6581,
        )

        return self.__parent__._cast(_6581.ConicalGearMeshCompoundDynamicAnalysis)

    @property
    def gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6607.GearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6607,
        )

        return self.__parent__._cast(_6607.GearMeshCompoundDynamicAnalysis)

    @property
    def inter_mountable_component_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6613.InterMountableComponentConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6613,
        )

        return self.__parent__._cast(
            _6613.InterMountableComponentConnectionCompoundDynamicAnalysis
        )

    @property
    def connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6583.ConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6583,
        )

        return self.__parent__._cast(_6583.ConnectionCompoundDynamicAnalysis)

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
    def zerol_bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "ZerolBevelGearMeshCompoundDynamicAnalysis":
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
class ZerolBevelGearMeshCompoundDynamicAnalysis(
    _6565.BevelGearMeshCompoundDynamicAnalysis
):
    """ZerolBevelGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2384.ZerolBevelGearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2384.ZerolBevelGearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6546.ZerolBevelGearMeshDynamicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis]

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
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_6546.ZerolBevelGearMeshDynamicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_ZerolBevelGearMeshCompoundDynamicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ZerolBevelGearMeshCompoundDynamicAnalysis
        """
        return _Cast_ZerolBevelGearMeshCompoundDynamicAnalysis(self)
