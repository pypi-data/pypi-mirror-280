"""WormGearMeshCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
    _4331,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "WormGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.connections_and_sockets.gears import _2382
    from mastapy._private.system_model.analyses_and_results.power_flows import _4266
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4337,
        _4307,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="WormGearMeshCompoundPowerFlow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="WormGearMeshCompoundPowerFlow._Cast_WormGearMeshCompoundPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGearMeshCompoundPowerFlow:
    """Special nested class for casting WormGearMeshCompoundPowerFlow to subclasses."""

    __parent__: "WormGearMeshCompoundPowerFlow"

    @property
    def gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4331.GearMeshCompoundPowerFlow":
        return self.__parent__._cast(_4331.GearMeshCompoundPowerFlow)

    @property
    def inter_mountable_component_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4337.InterMountableComponentConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4337,
        )

        return self.__parent__._cast(
            _4337.InterMountableComponentConnectionCompoundPowerFlow
        )

    @property
    def connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4307.ConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4307,
        )

        return self.__parent__._cast(_4307.ConnectionCompoundPowerFlow)

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
    def worm_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "WormGearMeshCompoundPowerFlow":
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
class WormGearMeshCompoundPowerFlow(_4331.GearMeshCompoundPowerFlow):
    """WormGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GEAR_MESH_COMPOUND_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2382.WormGearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2382.WormGearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.WormGearMesh

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
    ) -> "List[_4266.WormGearMeshPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.WormGearMeshPowerFlow]

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
    def connection_analysis_cases(self: "Self") -> "List[_4266.WormGearMeshPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.WormGearMeshPowerFlow]

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
    def cast_to(self: "Self") -> "_Cast_WormGearMeshCompoundPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_WormGearMeshCompoundPowerFlow
        """
        return _Cast_WormGearMeshCompoundPowerFlow(self)
