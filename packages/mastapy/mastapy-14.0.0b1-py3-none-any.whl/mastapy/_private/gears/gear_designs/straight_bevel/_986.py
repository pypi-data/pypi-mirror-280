"""StraightBevelGearMeshDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.gear_designs.bevel import _1219
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearMeshDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.straight_bevel import _987, _985, _988
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1232
    from mastapy._private.gears.gear_designs.conical import _1193
    from mastapy._private.gears.gear_designs import _973, _972

    Self = TypeVar("Self", bound="StraightBevelGearMeshDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelGearMeshDesign:
    """Special nested class for casting StraightBevelGearMeshDesign to subclasses."""

    __parent__: "StraightBevelGearMeshDesign"

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
    def straight_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "StraightBevelGearMeshDesign":
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
class StraightBevelGearMeshDesign(_1219.BevelGearMeshDesign):
    """StraightBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_GEAR_MESH_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def straight_bevel_gear_set(self: "Self") -> "_987.StraightBevelGearSetDesign":
        """mastapy._private.gears.gear_designs.straight_bevel.StraightBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gears(self: "Self") -> "List[_985.StraightBevelGearDesign]":
        """List[mastapy._private.gears.gear_designs.straight_bevel.StraightBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshed_gears(
        self: "Self",
    ) -> "List[_988.StraightBevelMeshedGearDesign]":
        """List[mastapy._private.gears.gear_designs.straight_bevel.StraightBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelGearMeshDesign":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelGearMeshDesign
        """
        return _Cast_StraightBevelGearMeshDesign(self)
