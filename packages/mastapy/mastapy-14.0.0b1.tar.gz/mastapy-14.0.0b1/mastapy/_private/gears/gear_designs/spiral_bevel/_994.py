"""SpiralBevelGearMeshDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.gear_designs.bevel import _1219
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.SpiralBevel", "SpiralBevelGearMeshDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.spiral_bevel import _995, _993, _996
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1232
    from mastapy._private.gears.gear_designs.conical import _1193
    from mastapy._private.gears.gear_designs import _973, _972

    Self = TypeVar("Self", bound="SpiralBevelGearMeshDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpiralBevelGearMeshDesign:
    """Special nested class for casting SpiralBevelGearMeshDesign to subclasses."""

    __parent__: "SpiralBevelGearMeshDesign"

    @property
    def bevel_gear_mesh_design(self: "CastSelf") -> "_1219.BevelGearMeshDesign":
        return self.__parent__._cast(_1219.BevelGearMeshDesign)

    @property
    def agma_gleason_conical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1232.AGMAGleasonConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1232

        return self.__parent__._cast(_1232.AGMAGleasonConicalGearMeshDesign)

    @property
    def conical_gear_mesh_design(self: "CastSelf") -> "_1193.ConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.conical import _1193

        return self.__parent__._cast(_1193.ConicalGearMeshDesign)

    @property
    def gear_mesh_design(self: "CastSelf") -> "_973.GearMeshDesign":
        from mastapy._private.gears.gear_designs import _973

        return self.__parent__._cast(_973.GearMeshDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def spiral_bevel_gear_mesh_design(self: "CastSelf") -> "SpiralBevelGearMeshDesign":
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
class SpiralBevelGearMeshDesign(_1219.BevelGearMeshDesign):
    """SpiralBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPIRAL_BEVEL_GEAR_MESH_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def wheel_inner_blade_angle_convex(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_blade_angle_concave(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def spiral_bevel_gear_set(self: "Self") -> "_995.SpiralBevelGearSetDesign":
        """mastapy._private.gears.gear_designs.spiral_bevel.SpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears(self: "Self") -> "List[_993.SpiralBevelGearDesign]":
        """List[mastapy._private.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshed_gears(
        self: "Self",
    ) -> "List[_996.SpiralBevelMeshedGearDesign]":
        """List[mastapy._private.gears.gear_designs.spiral_bevel.SpiralBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_SpiralBevelGearMeshDesign":
        """Cast to another type.

        Returns:
            _Cast_SpiralBevelGearMeshDesign
        """
        return _Cast_SpiralBevelGearMeshDesign(self)
