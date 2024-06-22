"""ConicalGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model.gears import _2588
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1194
    from mastapy._private.system_model.part_model.gears import (
        _2579,
        _2570,
        _2572,
        _2576,
        _2591,
        _2593,
        _2595,
        _2597,
        _2600,
        _2602,
        _2604,
        _2610,
    )
    from mastapy._private.system_model.part_model import _2532, _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="ConicalGearSet")
    CastSelf = TypeVar("CastSelf", bound="ConicalGearSet._Cast_ConicalGearSet")


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSet:
    """Special nested class for casting ConicalGearSet to subclasses."""

    __parent__: "ConicalGearSet"

    @property
    def gear_set(self: "CastSelf") -> "_2588.GearSet":
        return self.__parent__._cast(_2588.GearSet)

    @property
    def specialised_assembly(self: "CastSelf") -> "_2532.SpecialisedAssembly":
        from mastapy._private.system_model.part_model import _2532

        return self.__parent__._cast(_2532.SpecialisedAssembly)

    @property
    def abstract_assembly(self: "CastSelf") -> "_2488.AbstractAssembly":
        from mastapy._private.system_model.part_model import _2488

        return self.__parent__._cast(_2488.AbstractAssembly)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def agma_gleason_conical_gear_set(
        self: "CastSelf",
    ) -> "_2570.AGMAGleasonConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2570

        return self.__parent__._cast(_2570.AGMAGleasonConicalGearSet)

    @property
    def bevel_differential_gear_set(
        self: "CastSelf",
    ) -> "_2572.BevelDifferentialGearSet":
        from mastapy._private.system_model.part_model.gears import _2572

        return self.__parent__._cast(_2572.BevelDifferentialGearSet)

    @property
    def bevel_gear_set(self: "CastSelf") -> "_2576.BevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2576

        return self.__parent__._cast(_2576.BevelGearSet)

    @property
    def hypoid_gear_set(self: "CastSelf") -> "_2591.HypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2591

        return self.__parent__._cast(_2591.HypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set(
        self: "CastSelf",
    ) -> "_2593.KlingelnbergCycloPalloidConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2593

        return self.__parent__._cast(_2593.KlingelnbergCycloPalloidConicalGearSet)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "CastSelf",
    ) -> "_2595.KlingelnbergCycloPalloidHypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2595

        return self.__parent__._cast(_2595.KlingelnbergCycloPalloidHypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "CastSelf",
    ) -> "_2597.KlingelnbergCycloPalloidSpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2597

        return self.__parent__._cast(_2597.KlingelnbergCycloPalloidSpiralBevelGearSet)

    @property
    def spiral_bevel_gear_set(self: "CastSelf") -> "_2600.SpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2600

        return self.__parent__._cast(_2600.SpiralBevelGearSet)

    @property
    def straight_bevel_diff_gear_set(
        self: "CastSelf",
    ) -> "_2602.StraightBevelDiffGearSet":
        from mastapy._private.system_model.part_model.gears import _2602

        return self.__parent__._cast(_2602.StraightBevelDiffGearSet)

    @property
    def straight_bevel_gear_set(self: "CastSelf") -> "_2604.StraightBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2604

        return self.__parent__._cast(_2604.StraightBevelGearSet)

    @property
    def zerol_bevel_gear_set(self: "CastSelf") -> "_2610.ZerolBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2610

        return self.__parent__._cast(_2610.ZerolBevelGearSet)

    @property
    def conical_gear_set(self: "CastSelf") -> "ConicalGearSet":
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
class ConicalGearSet(_2588.GearSet):
    """ConicalGearSet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_SET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def active_gear_set_design(self: "Self") -> "_1194.ConicalGearSetDesign":
        """mastapy._private.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_design(self: "Self") -> "_1194.ConicalGearSetDesign":
        """mastapy._private.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears(self: "Self") -> "List[_2579.ConicalGear]":
        """List[mastapy._private.system_model.part_model.gears.ConicalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearSet":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSet
        """
        return _Cast_ConicalGearSet(self)
