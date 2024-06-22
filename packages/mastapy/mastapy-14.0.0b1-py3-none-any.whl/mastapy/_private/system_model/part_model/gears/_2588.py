"""GearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.implicit import list_with_selected_item, overridable
from mastapy._private.gears.gear_designs import _974
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model import _2532
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.system_model.part_model.gears import (
        _2570,
        _2572,
        _2576,
        _2578,
        _2580,
        _2582,
        _2585,
        _2591,
        _2593,
        _2595,
        _2597,
        _2598,
        _2600,
        _2602,
        _2604,
        _2608,
        _2610,
    )
    from mastapy._private.system_model.part_model import _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="GearSet")
    CastSelf = TypeVar("CastSelf", bound="GearSet._Cast_GearSet")


__docformat__ = "restructuredtext en"
__all__ = ("GearSet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSet:
    """Special nested class for casting GearSet to subclasses."""

    __parent__: "GearSet"

    @property
    def specialised_assembly(self: "CastSelf") -> "_2532.SpecialisedAssembly":
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
    def concept_gear_set(self: "CastSelf") -> "_2578.ConceptGearSet":
        from mastapy._private.system_model.part_model.gears import _2578

        return self.__parent__._cast(_2578.ConceptGearSet)

    @property
    def conical_gear_set(self: "CastSelf") -> "_2580.ConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2580

        return self.__parent__._cast(_2580.ConicalGearSet)

    @property
    def cylindrical_gear_set(self: "CastSelf") -> "_2582.CylindricalGearSet":
        from mastapy._private.system_model.part_model.gears import _2582

        return self.__parent__._cast(_2582.CylindricalGearSet)

    @property
    def face_gear_set(self: "CastSelf") -> "_2585.FaceGearSet":
        from mastapy._private.system_model.part_model.gears import _2585

        return self.__parent__._cast(_2585.FaceGearSet)

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
    def planetary_gear_set(self: "CastSelf") -> "_2598.PlanetaryGearSet":
        from mastapy._private.system_model.part_model.gears import _2598

        return self.__parent__._cast(_2598.PlanetaryGearSet)

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
    def worm_gear_set(self: "CastSelf") -> "_2608.WormGearSet":
        from mastapy._private.system_model.part_model.gears import _2608

        return self.__parent__._cast(_2608.WormGearSet)

    @property
    def zerol_bevel_gear_set(self: "CastSelf") -> "_2610.ZerolBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2610

        return self.__parent__._cast(_2610.ZerolBevelGearSet)

    @property
    def gear_set(self: "CastSelf") -> "GearSet":
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
class GearSet(_2532.SpecialisedAssembly):
    """GearSet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def active_design(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_GearSetDesign":
        """ListWithSelectedItem[mastapy._private.gears.gear_designs.GearSetDesign]"""
        temp = self.wrapped.ActiveDesign

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GearSetDesign",
        )(temp)

    @active_design.setter
    @enforce_parameter_types
    def active_design(self: "Self", value: "_974.GearSetDesign") -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GearSetDesign.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GearSetDesign.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ActiveDesign = value

    @property
    def maximum_number_of_teeth_in_mesh(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfTeethInMesh

        if temp is None:
            return 0

        return temp

    @maximum_number_of_teeth_in_mesh.setter
    @enforce_parameter_types
    def maximum_number_of_teeth_in_mesh(self: "Self", value: "int") -> None:
        self.wrapped.MaximumNumberOfTeethInMesh = int(value) if value is not None else 0

    @property
    def mesh_ratio_limit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeshRatioLimit

        if temp is None:
            return 0.0

        return temp

    @mesh_ratio_limit.setter
    @enforce_parameter_types
    def mesh_ratio_limit(self: "Self", value: "float") -> None:
        self.wrapped.MeshRatioLimit = float(value) if value is not None else 0.0

    @property
    def minimum_number_of_teeth_in_mesh(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfTeethInMesh

        if temp is None:
            return 0

        return temp

    @minimum_number_of_teeth_in_mesh.setter
    @enforce_parameter_types
    def minimum_number_of_teeth_in_mesh(self: "Self", value: "int") -> None:
        self.wrapped.MinimumNumberOfTeethInMesh = int(value) if value is not None else 0

    @property
    def required_safety_factor_for_bending(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_bending.setter
    @enforce_parameter_types
    def required_safety_factor_for_bending(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForBending = value

    @property
    def required_safety_factor_for_contact(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_contact.setter
    @enforce_parameter_types
    def required_safety_factor_for_contact(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForContact = value

    @property
    def required_safety_factor_for_static_bending(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForStaticBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_static_bending.setter
    @enforce_parameter_types
    def required_safety_factor_for_static_bending(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForStaticBending = value

    @property
    def required_safety_factor_for_static_contact(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyFactorForStaticContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_factor_for_static_contact.setter
    @enforce_parameter_types
    def required_safety_factor_for_static_contact(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyFactorForStaticContact = value

    @property
    def active_gear_set_design(self: "Self") -> "_974.GearSetDesign":
        """mastapy._private.gears.gear_designs.GearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_designs(self: "Self") -> "List[_974.GearSetDesign]":
        """List[mastapy._private.gears.gear_designs.GearSetDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def add_gear_set_design(self: "Self", design: "_974.GearSetDesign") -> None:
        """Method does not return.

        Args:
            design (mastapy._private.gears.gear_designs.GearSetDesign)
        """
        self.wrapped.AddGearSetDesign(design.wrapped if design else None)

    @enforce_parameter_types
    def remove_design(self: "Self", design: "_974.GearSetDesign") -> None:
        """Method does not return.

        Args:
            design (mastapy._private.gears.gear_designs.GearSetDesign)
        """
        self.wrapped.RemoveDesign(design.wrapped if design else None)

    @enforce_parameter_types
    def set_active_gear_set_design(
        self: "Self", gear_set_design: "_974.GearSetDesign"
    ) -> None:
        """Method does not return.

        Args:
            gear_set_design (mastapy._private.gears.gear_designs.GearSetDesign)
        """
        self.wrapped.SetActiveGearSetDesign(
            gear_set_design.wrapped if gear_set_design else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_GearSet":
        """Cast to another type.

        Returns:
            _Cast_GearSet
        """
        return _Cast_GearSet(self)
