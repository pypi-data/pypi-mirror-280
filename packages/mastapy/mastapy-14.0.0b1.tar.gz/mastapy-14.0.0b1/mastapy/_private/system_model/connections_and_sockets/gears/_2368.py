"""HypoidGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.connections_and_sockets.gears import _2352
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.hypoid import _1010
    from mastapy._private.system_model.connections_and_sockets.gears import _2360, _2366
    from mastapy._private.system_model.connections_and_sockets import _2334, _2325
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="HypoidGearMesh")
    CastSelf = TypeVar("CastSelf", bound="HypoidGearMesh._Cast_HypoidGearMesh")


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HypoidGearMesh:
    """Special nested class for casting HypoidGearMesh to subclasses."""

    __parent__: "HypoidGearMesh"

    @property
    def agma_gleason_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2352.AGMAGleasonConicalGearMesh":
        return self.__parent__._cast(_2352.AGMAGleasonConicalGearMesh)

    @property
    def conical_gear_mesh(self: "CastSelf") -> "_2360.ConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2360

        return self.__parent__._cast(_2360.ConicalGearMesh)

    @property
    def gear_mesh(self: "CastSelf") -> "_2366.GearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2366

        return self.__parent__._cast(_2366.GearMesh)

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2334.InterMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2334

        return self.__parent__._cast(_2334.InterMountableComponentConnection)

    @property
    def connection(self: "CastSelf") -> "_2325.Connection":
        from mastapy._private.system_model.connections_and_sockets import _2325

        return self.__parent__._cast(_2325.Connection)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def hypoid_gear_mesh(self: "CastSelf") -> "HypoidGearMesh":
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
class HypoidGearMesh(_2352.AGMAGleasonConicalGearMesh):
    """HypoidGearMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HYPOID_GEAR_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def active_gear_mesh_design(self: "Self") -> "_1010.HypoidGearMeshDesign":
        """mastapy._private.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_mesh_design(self: "Self") -> "_1010.HypoidGearMeshDesign":
        """mastapy._private.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_HypoidGearMesh":
        """Cast to another type.

        Returns:
            _Cast_HypoidGearMesh
        """
        return _Cast_HypoidGearMesh(self)
