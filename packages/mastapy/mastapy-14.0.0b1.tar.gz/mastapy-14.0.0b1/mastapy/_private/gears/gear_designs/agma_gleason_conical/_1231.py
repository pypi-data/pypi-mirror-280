"""AGMAGleasonConicalGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.gears.gear_designs.conical import _1195, _1196, _1192
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_AGMA_GLEASON_CONICAL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical", "AGMAGleasonConicalGearDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1202, _1191
    from mastapy._private.gears import _324
    from mastapy._private.gears.materials import _608
    from mastapy._private.gears.gear_designs.zerol_bevel import _976
    from mastapy._private.gears.gear_designs.straight_bevel import _985
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _989
    from mastapy._private.gears.gear_designs.spiral_bevel import _993
    from mastapy._private.gears.gear_designs.hypoid import _1009
    from mastapy._private.gears.gear_designs.bevel import _1218
    from mastapy._private.gears.gear_designs import _971, _972

    Self = TypeVar("Self", bound="AGMAGleasonConicalGearDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearDesign:
    """Special nested class for casting AGMAGleasonConicalGearDesign to subclasses."""

    __parent__: "AGMAGleasonConicalGearDesign"

    @property
    def conical_gear_design(self: "CastSelf") -> "_1192.ConicalGearDesign":
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
    def zerol_bevel_gear_design(self: "CastSelf") -> "_976.ZerolBevelGearDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _976

        return self.__parent__._cast(_976.ZerolBevelGearDesign)

    @property
    def straight_bevel_gear_design(self: "CastSelf") -> "_985.StraightBevelGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _985

        return self.__parent__._cast(_985.StraightBevelGearDesign)

    @property
    def straight_bevel_diff_gear_design(
        self: "CastSelf",
    ) -> "_989.StraightBevelDiffGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _989

        return self.__parent__._cast(_989.StraightBevelDiffGearDesign)

    @property
    def spiral_bevel_gear_design(self: "CastSelf") -> "_993.SpiralBevelGearDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _993

        return self.__parent__._cast(_993.SpiralBevelGearDesign)

    @property
    def hypoid_gear_design(self: "CastSelf") -> "_1009.HypoidGearDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1009

        return self.__parent__._cast(_1009.HypoidGearDesign)

    @property
    def bevel_gear_design(self: "CastSelf") -> "_1218.BevelGearDesign":
        from mastapy._private.gears.gear_designs.bevel import _1218

        return self.__parent__._cast(_1218.BevelGearDesign)

    @property
    def agma_gleason_conical_gear_design(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearDesign":
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
class AGMAGleasonConicalGearDesign(_1192.ConicalGearDesign):
    """AGMAGleasonConicalGearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _AGMA_GLEASON_CONICAL_GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def allowable_bending_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

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
    def front_end_type(self: "Self") -> "_1202.FrontEndTypes":
        """mastapy._private.gears.gear_designs.conical.FrontEndTypes"""
        temp = self.wrapped.FrontEndType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.FrontEndTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.conical._1202", "FrontEndTypes"
        )(value)

    @front_end_type.setter
    @enforce_parameter_types
    def front_end_type(self: "Self", value: "_1202.FrontEndTypes") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.FrontEndTypes"
        )
        self.wrapped.FrontEndType = value

    @property
    def machine_setting_calculation_method(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods":
        """EnumWithSelectedValue[mastapy._private.gears.gear_designs.conical.ConicalMachineSettingCalculationMethods]"""
        temp = self.wrapped.MachineSettingCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @machine_setting_calculation_method.setter
    @enforce_parameter_types
    def machine_setting_calculation_method(
        self: "Self", value: "_1195.ConicalMachineSettingCalculationMethods"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MachineSettingCalculationMethod = value

    @property
    def manufacture_method(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods":
        """EnumWithSelectedValue[mastapy._private.gears.gear_designs.conical.ConicalManufactureMethods]"""
        temp = self.wrapped.ManufactureMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @manufacture_method.setter
    @enforce_parameter_types
    def manufacture_method(
        self: "Self", value: "_1196.ConicalManufactureMethods"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ManufactureMethod = value

    @property
    def material(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Material.SelectedItemName

        if temp is None:
            return ""

        return temp

    @material.setter
    @enforce_parameter_types
    def material(self: "Self", value: "str") -> None:
        self.wrapped.Material.SetSelectedItem(str(value) if value is not None else "")

    @property
    def accuracy_grades(self: "Self") -> "_324.AccuracyGrades":
        """mastapy._private.gears.AccuracyGrades

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_material(self: "Self") -> "_608.GearMaterial":
        """mastapy._private.gears.materials.GearMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cutter(self: "Self") -> "_1191.ConicalGearCutter":
        """mastapy._private.gears.gear_designs.conical.ConicalGearCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AGMAGleasonConicalGearDesign":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearDesign
        """
        return _Cast_AGMAGleasonConicalGearDesign(self)
