"""GearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.connections_and_sockets import _2334
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.gear_designs import _973
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2352,
        _2354,
        _2356,
        _2358,
        _2360,
        _2362,
        _2364,
        _2368,
        _2371,
        _2372,
        _2373,
        _2376,
        _2378,
        _2380,
        _2382,
        _2384,
    )
    from mastapy._private.system_model.connections_and_sockets import _2325
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="GearMesh")
    CastSelf = TypeVar("CastSelf", bound="GearMesh._Cast_GearMesh")


__docformat__ = "restructuredtext en"
__all__ = ("GearMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearMesh:
    """Special nested class for casting GearMesh to subclasses."""

    __parent__: "GearMesh"

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2334.InterMountableComponentConnection":
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
    def agma_gleason_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2352.AGMAGleasonConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2352

        return self.__parent__._cast(_2352.AGMAGleasonConicalGearMesh)

    @property
    def bevel_differential_gear_mesh(
        self: "CastSelf",
    ) -> "_2354.BevelDifferentialGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2354

        return self.__parent__._cast(_2354.BevelDifferentialGearMesh)

    @property
    def bevel_gear_mesh(self: "CastSelf") -> "_2356.BevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2356

        return self.__parent__._cast(_2356.BevelGearMesh)

    @property
    def concept_gear_mesh(self: "CastSelf") -> "_2358.ConceptGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2358

        return self.__parent__._cast(_2358.ConceptGearMesh)

    @property
    def conical_gear_mesh(self: "CastSelf") -> "_2360.ConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2360

        return self.__parent__._cast(_2360.ConicalGearMesh)

    @property
    def cylindrical_gear_mesh(self: "CastSelf") -> "_2362.CylindricalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2362

        return self.__parent__._cast(_2362.CylindricalGearMesh)

    @property
    def face_gear_mesh(self: "CastSelf") -> "_2364.FaceGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2364

        return self.__parent__._cast(_2364.FaceGearMesh)

    @property
    def hypoid_gear_mesh(self: "CastSelf") -> "_2368.HypoidGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2368

        return self.__parent__._cast(_2368.HypoidGearMesh)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2371.KlingelnbergCycloPalloidConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2371

        return self.__parent__._cast(_2371.KlingelnbergCycloPalloidConicalGearMesh)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "CastSelf",
    ) -> "_2372.KlingelnbergCycloPalloidHypoidGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2372

        return self.__parent__._cast(_2372.KlingelnbergCycloPalloidHypoidGearMesh)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "CastSelf",
    ) -> "_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2373

        return self.__parent__._cast(_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh)

    @property
    def spiral_bevel_gear_mesh(self: "CastSelf") -> "_2376.SpiralBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2376

        return self.__parent__._cast(_2376.SpiralBevelGearMesh)

    @property
    def straight_bevel_diff_gear_mesh(
        self: "CastSelf",
    ) -> "_2378.StraightBevelDiffGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2378

        return self.__parent__._cast(_2378.StraightBevelDiffGearMesh)

    @property
    def straight_bevel_gear_mesh(self: "CastSelf") -> "_2380.StraightBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2380

        return self.__parent__._cast(_2380.StraightBevelGearMesh)

    @property
    def worm_gear_mesh(self: "CastSelf") -> "_2382.WormGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2382

        return self.__parent__._cast(_2382.WormGearMesh)

    @property
    def zerol_bevel_gear_mesh(self: "CastSelf") -> "_2384.ZerolBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2384

        return self.__parent__._cast(_2384.ZerolBevelGearMesh)

    @property
    def gear_mesh(self: "CastSelf") -> "GearMesh":
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
class GearMesh(_2334.InterMountableComponentConnection):
    """GearMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def mesh_efficiency(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mesh_efficiency.setter
    @enforce_parameter_types
    def mesh_efficiency(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MeshEfficiency = value

    @property
    def use_specified_mesh_stiffness(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSpecifiedMeshStiffness

        if temp is None:
            return False

        return temp

    @use_specified_mesh_stiffness.setter
    @enforce_parameter_types
    def use_specified_mesh_stiffness(self: "Self", value: "bool") -> None:
        self.wrapped.UseSpecifiedMeshStiffness = (
            bool(value) if value is not None else False
        )

    @property
    def user_specified_mesh_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedMeshStiffness

        if temp is None:
            return 0.0

        return temp

    @user_specified_mesh_stiffness.setter
    @enforce_parameter_types
    def user_specified_mesh_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.UserSpecifiedMeshStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def active_gear_mesh_design(self: "Self") -> "_973.GearMeshDesign":
        """mastapy._private.gears.gear_designs.GearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearMesh":
        """Cast to another type.

        Returns:
            _Cast_GearMesh
        """
        return _Cast_GearMesh(self)
