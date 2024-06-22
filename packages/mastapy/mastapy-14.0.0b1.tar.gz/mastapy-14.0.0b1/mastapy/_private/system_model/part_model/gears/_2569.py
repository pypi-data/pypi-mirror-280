"""AGMAGleasonConicalGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.part_model.gears import _2579
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.gears import (
        _2571,
        _2573,
        _2574,
        _2575,
        _2590,
        _2599,
        _2601,
        _2603,
        _2605,
        _2606,
        _2609,
        _2586,
    )
    from mastapy._private.system_model.part_model import _2520, _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="AGMAGleasonConicalGear")
    CastSelf = TypeVar(
        "CastSelf", bound="AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGear:
    """Special nested class for casting AGMAGleasonConicalGear to subclasses."""

    __parent__: "AGMAGleasonConicalGear"

    @property
    def conical_gear(self: "CastSelf") -> "_2579.ConicalGear":
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
    def bevel_differential_gear(self: "CastSelf") -> "_2571.BevelDifferentialGear":
        from mastapy._private.system_model.part_model.gears import _2571

        return self.__parent__._cast(_2571.BevelDifferentialGear)

    @property
    def bevel_differential_planet_gear(
        self: "CastSelf",
    ) -> "_2573.BevelDifferentialPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2573

        return self.__parent__._cast(_2573.BevelDifferentialPlanetGear)

    @property
    def bevel_differential_sun_gear(
        self: "CastSelf",
    ) -> "_2574.BevelDifferentialSunGear":
        from mastapy._private.system_model.part_model.gears import _2574

        return self.__parent__._cast(_2574.BevelDifferentialSunGear)

    @property
    def bevel_gear(self: "CastSelf") -> "_2575.BevelGear":
        from mastapy._private.system_model.part_model.gears import _2575

        return self.__parent__._cast(_2575.BevelGear)

    @property
    def hypoid_gear(self: "CastSelf") -> "_2590.HypoidGear":
        from mastapy._private.system_model.part_model.gears import _2590

        return self.__parent__._cast(_2590.HypoidGear)

    @property
    def spiral_bevel_gear(self: "CastSelf") -> "_2599.SpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2599

        return self.__parent__._cast(_2599.SpiralBevelGear)

    @property
    def straight_bevel_diff_gear(self: "CastSelf") -> "_2601.StraightBevelDiffGear":
        from mastapy._private.system_model.part_model.gears import _2601

        return self.__parent__._cast(_2601.StraightBevelDiffGear)

    @property
    def straight_bevel_gear(self: "CastSelf") -> "_2603.StraightBevelGear":
        from mastapy._private.system_model.part_model.gears import _2603

        return self.__parent__._cast(_2603.StraightBevelGear)

    @property
    def straight_bevel_planet_gear(self: "CastSelf") -> "_2605.StraightBevelPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2605

        return self.__parent__._cast(_2605.StraightBevelPlanetGear)

    @property
    def straight_bevel_sun_gear(self: "CastSelf") -> "_2606.StraightBevelSunGear":
        from mastapy._private.system_model.part_model.gears import _2606

        return self.__parent__._cast(_2606.StraightBevelSunGear)

    @property
    def zerol_bevel_gear(self: "CastSelf") -> "_2609.ZerolBevelGear":
        from mastapy._private.system_model.part_model.gears import _2609

        return self.__parent__._cast(_2609.ZerolBevelGear)

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "AGMAGleasonConicalGear":
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
class AGMAGleasonConicalGear(_2579.ConicalGear):
    """AGMAGleasonConicalGear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _AGMA_GLEASON_CONICAL_GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_AGMAGleasonConicalGear":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGear
        """
        return _Cast_AGMAGleasonConicalGear(self)
