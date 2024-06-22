"""KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.gear_designs.klingelnberg_conical import _1006
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import (
        _999,
        _997,
        _1000,
    )
    from mastapy._private.gears.gear_designs.conical import _1193
    from mastapy._private.gears.gear_designs import _973, _972

    Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergCycloPalloidSpiralBevelGearMeshDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshDesign:
    """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshDesign to subclasses."""

    __parent__: "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"

    @property
    def klingelnberg_conical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1006.KlingelnbergConicalGearMeshDesign":
        return self.__parent__._cast(_1006.KlingelnbergConicalGearMeshDesign)

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
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
class KlingelnbergCycloPalloidSpiralBevelGearMeshDesign(
    _1006.KlingelnbergConicalGearMeshDesign
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "Self",
    ) -> "_999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        """mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears(
        self: "Self",
    ) -> "List[_997.KlingelnbergCycloPalloidSpiralBevelGearDesign]":
        """List[mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gears(
        self: "Self",
    ) -> "List[_1000.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign]":
        """List[mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
        """
        return _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshDesign(self)
