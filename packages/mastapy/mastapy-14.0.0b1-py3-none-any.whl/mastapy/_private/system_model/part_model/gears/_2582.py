"""CylindricalGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private.gears import _332
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import (
    overridable_enum_runtime,
    conversion,
    constructor,
    utility,
)
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.part_model.gears import _2588
from mastapy._private._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical import _1058
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2619,
    )
    from mastapy._private.system_model.part_model.gears import _2581, _2598
    from mastapy._private.system_model.connections_and_sockets.gears import _2362
    from mastapy._private.system_model.part_model import _2532, _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="CylindricalGearSet")
    CastSelf = TypeVar("CastSelf", bound="CylindricalGearSet._Cast_CylindricalGearSet")


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSet:
    """Special nested class for casting CylindricalGearSet to subclasses."""

    __parent__: "CylindricalGearSet"

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
    def planetary_gear_set(self: "CastSelf") -> "_2598.PlanetaryGearSet":
        from mastapy._private.system_model.part_model.gears import _2598

        return self.__parent__._cast(_2598.PlanetaryGearSet)

    @property
    def cylindrical_gear_set(self: "CastSelf") -> "CylindricalGearSet":
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
class CylindricalGearSet(_2588.GearSet):
    """CylindricalGearSet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def axial_contact_ratio_requirement(
        self: "Self",
    ) -> "overridable.Overridable_ContactRatioRequirements":
        """Overridable[mastapy._private.gears.ContactRatioRequirements]"""
        temp = self.wrapped.AxialContactRatioRequirement

        if temp is None:
            return None

        value = overridable.Overridable_ContactRatioRequirements.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @axial_contact_ratio_requirement.setter
    @enforce_parameter_types
    def axial_contact_ratio_requirement(
        self: "Self",
        value: "Union[_332.ContactRatioRequirements, Tuple[_332.ContactRatioRequirements, bool]]",
    ) -> None:
        wrapper_type = overridable.Overridable_ContactRatioRequirements.wrapper_type()
        enclosed_type = overridable.Overridable_ContactRatioRequirements.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def is_supercharger_rotor_set(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IsSuperchargerRotorSet

        if temp is None:
            return False

        return temp

    @is_supercharger_rotor_set.setter
    @enforce_parameter_types
    def is_supercharger_rotor_set(self: "Self", value: "bool") -> None:
        self.wrapped.IsSuperchargerRotorSet = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_acceptable_axial_contact_ratio(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_acceptable_axial_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_axial_contact_ratio(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumAcceptableAxialContactRatio = value

    @property
    def maximum_acceptable_transverse_contact_ratio(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_transverse_contact_ratio(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumAcceptableTransverseContactRatio = value

    @property
    def maximum_face_width(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumFaceWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_face_width.setter
    @enforce_parameter_types
    def maximum_face_width(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumFaceWidth = value

    @property
    def maximum_helix_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_helix_angle.setter
    @enforce_parameter_types
    def maximum_helix_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumHelixAngle = value

    @property
    def maximum_normal_module(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_normal_module.setter
    @enforce_parameter_types
    def maximum_normal_module(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumNormalModule = value

    @property
    def maximum_normal_pressure_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_normal_pressure_angle.setter
    @enforce_parameter_types
    def maximum_normal_pressure_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumNormalPressureAngle = value

    @property
    def minimum_acceptable_axial_contact_ratio(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_acceptable_axial_contact_ratio.setter
    @enforce_parameter_types
    def minimum_acceptable_axial_contact_ratio(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumAcceptableAxialContactRatio = value

    @property
    def minimum_acceptable_transverse_contact_ratio(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def minimum_acceptable_transverse_contact_ratio(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumAcceptableTransverseContactRatio = value

    @property
    def minimum_face_width(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumFaceWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_face_width.setter
    @enforce_parameter_types
    def minimum_face_width(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumFaceWidth = value

    @property
    def minimum_helix_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_helix_angle.setter
    @enforce_parameter_types
    def minimum_helix_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumHelixAngle = value

    @property
    def minimum_normal_module(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_normal_module.setter
    @enforce_parameter_types
    def minimum_normal_module(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumNormalModule = value

    @property
    def minimum_normal_pressure_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_normal_pressure_angle.setter
    @enforce_parameter_types
    def minimum_normal_pressure_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumNormalPressureAngle = value

    @property
    def opposite_hand(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.OppositeHand

        if temp is None:
            return False

        return temp

    @opposite_hand.setter
    @enforce_parameter_types
    def opposite_hand(self: "Self", value: "bool") -> None:
        self.wrapped.OppositeHand = bool(value) if value is not None else False

    @property
    def supercharger_rotor_set_database(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.SuperchargerRotorSetDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @supercharger_rotor_set_database.setter
    @enforce_parameter_types
    def supercharger_rotor_set_database(self: "Self", value: "str") -> None:
        self.wrapped.SuperchargerRotorSetDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def transverse_contact_ratio_requirement(
        self: "Self",
    ) -> "overridable.Overridable_ContactRatioRequirements":
        """Overridable[mastapy._private.gears.ContactRatioRequirements]"""
        temp = self.wrapped.TransverseContactRatioRequirement

        if temp is None:
            return None

        value = overridable.Overridable_ContactRatioRequirements.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @transverse_contact_ratio_requirement.setter
    @enforce_parameter_types
    def transverse_contact_ratio_requirement(
        self: "Self",
        value: "Union[_332.ContactRatioRequirements, Tuple[_332.ContactRatioRequirements, bool]]",
    ) -> None:
        wrapper_type = overridable.Overridable_ContactRatioRequirements.wrapper_type()
        enclosed_type = overridable.Overridable_ContactRatioRequirements.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def active_gear_set_design(self: "Self") -> "_1058.CylindricalGearSetDesign":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_design(self: "Self") -> "_1058.CylindricalGearSetDesign":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def supercharger_rotor_set(self: "Self") -> "_2619.SuperchargerRotorSet":
        """mastapy._private.system_model.part_model.gears.supercharger_rotor_set.SuperchargerRotorSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerRotorSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears(self: "Self") -> "List[_2581.CylindricalGear]":
        """List[mastapy._private.system_model.part_model.gears.CylindricalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes(self: "Self") -> "List[_2362.CylindricalGearMesh]":
        """List[mastapy._private.system_model.connections_and_sockets.gears.CylindricalGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set_designs(self: "Self") -> "List[_1058.CylindricalGearSetDesign]":
        """List[mastapy._private.gears.gear_designs.cylindrical.CylindricalGearSetDesign]

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

    def add_gear(self: "Self") -> "_2581.CylindricalGear":
        """mastapy._private.system_model.part_model.gears.CylindricalGear"""
        method_result = self.wrapped.AddGear()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSet":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSet
        """
        return _Cast_CylindricalGearSet(self)
