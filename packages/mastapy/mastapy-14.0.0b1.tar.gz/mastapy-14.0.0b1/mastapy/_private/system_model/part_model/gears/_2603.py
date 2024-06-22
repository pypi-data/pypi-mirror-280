"""StraightBevelGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model.gears import _2575
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.straight_bevel import _985
    from mastapy._private.system_model.part_model.gears import _2569, _2579, _2586
    from mastapy._private.system_model.part_model import _2520, _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="StraightBevelGear")
    CastSelf = TypeVar("CastSelf", bound="StraightBevelGear._Cast_StraightBevelGear")


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelGear:
    """Special nested class for casting StraightBevelGear to subclasses."""

    __parent__: "StraightBevelGear"

    @property
    def bevel_gear(self: "CastSelf") -> "_2575.BevelGear":
        return self.__parent__._cast(_2575.BevelGear)

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2569.AGMAGleasonConicalGear":
        from mastapy._private.system_model.part_model.gears import _2569

        return self.__parent__._cast(_2569.AGMAGleasonConicalGear)

    @property
    def conical_gear(self: "CastSelf") -> "_2579.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2579

        return self.__parent__._cast(_2579.ConicalGear)

    @property
    def gear(self: "CastSelf") -> "_2586.Gear":
        from mastapy._private.system_model.part_model.gears import _2586

        return self.__parent__._cast(_2586.Gear)

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        from mastapy._private.system_model.part_model import _2498

        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def straight_bevel_gear(self: "CastSelf") -> "StraightBevelGear":
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
class StraightBevelGear(_2575.BevelGear):
    """StraightBevelGear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bevel_gear_design(self: "Self") -> "_985.StraightBevelGearDesign":
        """mastapy._private.gears.gear_designs.straight_bevel.StraightBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gear_design(self: "Self") -> "_985.StraightBevelGearDesign":
        """mastapy._private.gears.gear_designs.straight_bevel.StraightBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelGear":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelGear
        """
        return _Cast_StraightBevelGear(self)
