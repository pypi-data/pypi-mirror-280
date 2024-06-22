"""StraightBevelDiffGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model.gears import _2576
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.straight_bevel_diff import _991
    from mastapy._private.system_model.part_model.gears import (
        _2601,
        _2570,
        _2580,
        _2588,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2378
    from mastapy._private.system_model.part_model import _2532, _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="StraightBevelDiffGearSet")
    CastSelf = TypeVar(
        "CastSelf", bound="StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet"
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffGearSet:
    """Special nested class for casting StraightBevelDiffGearSet to subclasses."""

    __parent__: "StraightBevelDiffGearSet"

    @property
    def bevel_gear_set(self: "CastSelf") -> "_2576.BevelGearSet":
        return self.__parent__._cast(_2576.BevelGearSet)

    @property
    def agma_gleason_conical_gear_set(
        self: "CastSelf",
    ) -> "_2570.AGMAGleasonConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2570

        return self.__parent__._cast(_2570.AGMAGleasonConicalGearSet)

    @property
    def conical_gear_set(self: "CastSelf") -> "_2580.ConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2580

        return self.__parent__._cast(_2580.ConicalGearSet)

    @property
    def gear_set(self: "CastSelf") -> "_2588.GearSet":
        from mastapy._private.system_model.part_model.gears import _2588

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
    def straight_bevel_diff_gear_set(self: "CastSelf") -> "StraightBevelDiffGearSet":
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
class StraightBevelDiffGearSet(_2576.BevelGearSet):
    """StraightBevelDiffGearSet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_DIFF_GEAR_SET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def conical_gear_set_design(self: "Self") -> "_991.StraightBevelDiffGearSetDesign":
        """mastapy._private.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_set_design(
        self: "Self",
    ) -> "_991.StraightBevelDiffGearSetDesign":
        """mastapy._private.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears(self: "Self") -> "List[_2601.StraightBevelDiffGear]":
        """List[mastapy._private.system_model.part_model.gears.StraightBevelDiffGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes(
        self: "Self",
    ) -> "List[_2378.StraightBevelDiffGearMesh]":
        """List[mastapy._private.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelDiffGearSet":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffGearSet
        """
        return _Cast_StraightBevelDiffGearSet(self)
