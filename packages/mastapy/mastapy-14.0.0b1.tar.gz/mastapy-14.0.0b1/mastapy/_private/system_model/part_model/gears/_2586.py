"""Gear"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model import _2520
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")

if TYPE_CHECKING:
    from typing import Any, Type, Optional, TypeVar

    from mastapy._private.gears.gear_designs import _971
    from mastapy._private.system_model.part_model.gears import (
        _2588,
        _2569,
        _2571,
        _2573,
        _2574,
        _2575,
        _2577,
        _2579,
        _2581,
        _2583,
        _2584,
        _2590,
        _2592,
        _2594,
        _2596,
        _2599,
        _2601,
        _2603,
        _2605,
        _2606,
        _2607,
        _2609,
    )
    from mastapy._private.system_model.part_model.shaft_model import _2538
    from mastapy._private.system_model.part_model import _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="Gear")
    CastSelf = TypeVar("CastSelf", bound="Gear._Cast_Gear")


__docformat__ = "restructuredtext en"
__all__ = ("Gear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Gear:
    """Special nested class for casting Gear to subclasses."""

    __parent__: "Gear"

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
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
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2569.AGMAGleasonConicalGear":
        from mastapy._private.system_model.part_model.gears import _2569

        return self.__parent__._cast(_2569.AGMAGleasonConicalGear)

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
    def concept_gear(self: "CastSelf") -> "_2577.ConceptGear":
        from mastapy._private.system_model.part_model.gears import _2577

        return self.__parent__._cast(_2577.ConceptGear)

    @property
    def conical_gear(self: "CastSelf") -> "_2579.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2579

        return self.__parent__._cast(_2579.ConicalGear)

    @property
    def cylindrical_gear(self: "CastSelf") -> "_2581.CylindricalGear":
        from mastapy._private.system_model.part_model.gears import _2581

        return self.__parent__._cast(_2581.CylindricalGear)

    @property
    def cylindrical_planet_gear(self: "CastSelf") -> "_2583.CylindricalPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2583

        return self.__parent__._cast(_2583.CylindricalPlanetGear)

    @property
    def face_gear(self: "CastSelf") -> "_2584.FaceGear":
        from mastapy._private.system_model.part_model.gears import _2584

        return self.__parent__._cast(_2584.FaceGear)

    @property
    def hypoid_gear(self: "CastSelf") -> "_2590.HypoidGear":
        from mastapy._private.system_model.part_model.gears import _2590

        return self.__parent__._cast(_2590.HypoidGear)

    @property
    def klingelnberg_cyclo_palloid_conical_gear(
        self: "CastSelf",
    ) -> "_2592.KlingelnbergCycloPalloidConicalGear":
        from mastapy._private.system_model.part_model.gears import _2592

        return self.__parent__._cast(_2592.KlingelnbergCycloPalloidConicalGear)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(
        self: "CastSelf",
    ) -> "_2594.KlingelnbergCycloPalloidHypoidGear":
        from mastapy._private.system_model.part_model.gears import _2594

        return self.__parent__._cast(_2594.KlingelnbergCycloPalloidHypoidGear)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "CastSelf",
    ) -> "_2596.KlingelnbergCycloPalloidSpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2596

        return self.__parent__._cast(_2596.KlingelnbergCycloPalloidSpiralBevelGear)

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
    def worm_gear(self: "CastSelf") -> "_2607.WormGear":
        from mastapy._private.system_model.part_model.gears import _2607

        return self.__parent__._cast(_2607.WormGear)

    @property
    def zerol_bevel_gear(self: "CastSelf") -> "_2609.ZerolBevelGear":
        from mastapy._private.system_model.part_model.gears import _2609

        return self.__parent__._cast(_2609.ZerolBevelGear)

    @property
    def gear(self: "CastSelf") -> "Gear":
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
class Gear(_2520.MountableComponent):
    """Gear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cloned_from(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClonedFrom

        if temp is None:
            return ""

        return temp

    @property
    def even_number_of_teeth_required(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.EvenNumberOfTeethRequired

        if temp is None:
            return False

        return temp

    @even_number_of_teeth_required.setter
    @enforce_parameter_types
    def even_number_of_teeth_required(self: "Self", value: "bool") -> None:
        self.wrapped.EvenNumberOfTeethRequired = (
            bool(value) if value is not None else False
        )

    @property
    def is_clone_gear(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsCloneGear

        if temp is None:
            return False

        return temp

    @property
    def length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: "Self", value: "float") -> None:
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def maximum_number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @maximum_number_of_teeth.setter
    @enforce_parameter_types
    def maximum_number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.MaximumNumberOfTeeth = int(value) if value is not None else 0

    @property
    def maximum_and_minimum_number_of_teeth_deviation(self: "Self") -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MaximumAndMinimumNumberOfTeethDeviation

        if temp is None:
            return None

        return temp

    @maximum_and_minimum_number_of_teeth_deviation.setter
    @enforce_parameter_types
    def maximum_and_minimum_number_of_teeth_deviation(
        self: "Self", value: "Optional[int]"
    ) -> None:
        self.wrapped.MaximumAndMinimumNumberOfTeethDeviation = value

    @property
    def minimum_number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @minimum_number_of_teeth.setter
    @enforce_parameter_types
    def minimum_number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.MinimumNumberOfTeeth = int(value) if value is not None else 0

    @property
    def active_gear_design(self: "Self") -> "_971.GearDesign":
        """mastapy._private.gears.gear_designs.GearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: "Self", value: "float") -> None:
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def gear_set(self: "Self") -> "_2588.GearSet":
        """mastapy._private.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def shaft(self: "Self") -> "_2538.Shaft":
        """mastapy._private.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def connect_to(self: "Self", other_gear: "Gear") -> None:
        """Method does not return.

        Args:
            other_gear (mastapy._private.system_model.part_model.gears.Gear)
        """
        self.wrapped.ConnectTo(other_gear.wrapped if other_gear else None)

    @property
    def cast_to(self: "Self") -> "_Cast_Gear":
        """Cast to another type.

        Returns:
            _Cast_Gear
        """
        return _Cast_Gear(self)
