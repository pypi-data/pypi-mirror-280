"""ZerolBevelGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.gear_designs.bevel import _1218
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.ZerolBevel", "ZerolBevelGearDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1231
    from mastapy._private.gears.gear_designs.conical import _1192
    from mastapy._private.gears.gear_designs import _971, _972

    Self = TypeVar("Self", bound="ZerolBevelGearDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="ZerolBevelGearDesign._Cast_ZerolBevelGearDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ZerolBevelGearDesign:
    """Special nested class for casting ZerolBevelGearDesign to subclasses."""

    __parent__: "ZerolBevelGearDesign"

    @property
    def bevel_gear_design(self: "CastSelf") -> "_1218.BevelGearDesign":
        return self.__parent__._cast(_1218.BevelGearDesign)

    @property
    def agma_gleason_conical_gear_design(
        self: "CastSelf",
    ) -> "_1231.AGMAGleasonConicalGearDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1231

        return self.__parent__._cast(_1231.AGMAGleasonConicalGearDesign)

    @property
    def conical_gear_design(self: "CastSelf") -> "_1192.ConicalGearDesign":
        from mastapy._private.gears.gear_designs.conical import _1192

        return self.__parent__._cast(_1192.ConicalGearDesign)

    @property
    def gear_design(self: "CastSelf") -> "_971.GearDesign":
        from mastapy._private.gears.gear_designs import _971

        return self.__parent__._cast(_971.GearDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_gear_design(self: "CastSelf") -> "ZerolBevelGearDesign":
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
class ZerolBevelGearDesign(_1218.BevelGearDesign):
    """ZerolBevelGearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ZEROL_BEVEL_GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def mean_spiral_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_ZerolBevelGearDesign":
        """Cast to another type.

        Returns:
            _Cast_ZerolBevelGearDesign
        """
        return _Cast_ZerolBevelGearDesign(self)
