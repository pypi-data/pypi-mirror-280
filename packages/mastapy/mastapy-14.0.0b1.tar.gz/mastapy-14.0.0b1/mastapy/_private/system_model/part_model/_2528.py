"""PowerLoad"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    utility,
)
from mastapy._private._internal.implicit import (
    list_with_selected_item,
    enum_with_selected_value,
    overridable,
)
from mastapy._private.electric_machines import _1302
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.system_model import _2272
from mastapy._private.system_model.part_model import _2535
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.system_model.part_model import (
        _2503,
        _2537,
        _2520,
        _2498,
        _2524,
    )
    from mastapy._private.math_utility.measured_data import _1611
    from mastapy._private.materials.efficiency import _308
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="PowerLoad")
    CastSelf = TypeVar("CastSelf", bound="PowerLoad._Cast_PowerLoad")


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoad",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PowerLoad:
    """Special nested class for casting PowerLoad to subclasses."""

    __parent__: "PowerLoad"

    @property
    def virtual_component(self: "CastSelf") -> "_2535.VirtualComponent":
        return self.__parent__._cast(_2535.VirtualComponent)

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
    def power_load(self: "CastSelf") -> "PowerLoad":
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
class PowerLoad(_2535.VirtualComponent):
    """PowerLoad

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _POWER_LOAD

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def effective_length_of_stator(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EffectiveLengthOfStator

        if temp is None:
            return 0.0

        return temp

    @effective_length_of_stator.setter
    @enforce_parameter_types
    def effective_length_of_stator(self: "Self", value: "float") -> None:
        self.wrapped.EffectiveLengthOfStator = (
            float(value) if value is not None else 0.0
        )

    @property
    def electric_machine_detail_selector(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail":
        """ListWithSelectedItem[mastapy._private.electric_machines.ElectricMachineDetail]"""
        temp = self.wrapped.ElectricMachineDetailSelector

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ElectricMachineDetail",
        )(temp)

    @electric_machine_detail_selector.setter
    @enforce_parameter_types
    def electric_machine_detail_selector(
        self: "Self", value: "_1302.ElectricMachineDetail"
    ) -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ElectricMachineDetailSelector = value

    @property
    def electric_machine_search_region_specification_method(
        self: "Self",
    ) -> "_2503.ElectricMachineSearchRegionSpecificationMethod":
        """mastapy._private.system_model.part_model.ElectricMachineSearchRegionSpecificationMethod"""
        temp = self.wrapped.ElectricMachineSearchRegionSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PartModel.ElectricMachineSearchRegionSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.part_model._2503",
            "ElectricMachineSearchRegionSpecificationMethod",
        )(value)

    @electric_machine_search_region_specification_method.setter
    @enforce_parameter_types
    def electric_machine_search_region_specification_method(
        self: "Self", value: "_2503.ElectricMachineSearchRegionSpecificationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PartModel.ElectricMachineSearchRegionSpecificationMethod",
        )
        self.wrapped.ElectricMachineSearchRegionSpecificationMethod = value

    @property
    def engine_fuel_consumption_grid(self: "Self") -> "_1611.GriddedSurfaceAccessor":
        """mastapy._private.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.EngineFuelConsumptionGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @engine_fuel_consumption_grid.setter
    @enforce_parameter_types
    def engine_fuel_consumption_grid(
        self: "Self", value: "_1611.GriddedSurfaceAccessor"
    ) -> None:
        self.wrapped.EngineFuelConsumptionGrid = value.wrapped

    @property
    def engine_torque_grid(self: "Self") -> "_1611.GriddedSurfaceAccessor":
        """mastapy._private.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.EngineTorqueGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @engine_torque_grid.setter
    @enforce_parameter_types
    def engine_torque_grid(self: "Self", value: "_1611.GriddedSurfaceAccessor") -> None:
        self.wrapped.EngineTorqueGrid = value.wrapped

    @property
    def include_in_torsional_stiffness_calculation(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeInTorsionalStiffnessCalculation

        if temp is None:
            return False

        return temp

    @include_in_torsional_stiffness_calculation.setter
    @enforce_parameter_types
    def include_in_torsional_stiffness_calculation(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeInTorsionalStiffnessCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def inner_diameter_of_stator_teeth(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    @enforce_parameter_types
    def inner_diameter_of_stator_teeth(self: "Self", value: "float") -> None:
        self.wrapped.InnerDiameterOfStatorTeeth = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_wheels(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfWheels

        if temp is None:
            return 0

        return temp

    @number_of_wheels.setter
    @enforce_parameter_types
    def number_of_wheels(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfWheels = int(value) if value is not None else 0

    @property
    def number_of_blades(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfBlades

        if temp is None:
            return 0

        return temp

    @number_of_blades.setter
    @enforce_parameter_types
    def number_of_blades(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfBlades = int(value) if value is not None else 0

    @property
    def number_of_slots(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    @enforce_parameter_types
    def number_of_slots(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfSlots = int(value) if value is not None else 0

    @property
    def positive_is_forwards(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.PositiveIsForwards

        if temp is None:
            return False

        return temp

    @positive_is_forwards.setter
    @enforce_parameter_types
    def positive_is_forwards(self: "Self", value: "bool") -> None:
        self.wrapped.PositiveIsForwards = bool(value) if value is not None else False

    @property
    def power_load_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PowerLoadType":
        """EnumWithSelectedValue[mastapy._private.system_model.PowerLoadType]"""
        temp = self.wrapped.PowerLoadType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @power_load_type.setter
    @enforce_parameter_types
    def power_load_type(self: "Self", value: "_2272.PowerLoadType") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PowerLoadType = value

    @property
    def torsional_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def tyre_rolling_radius(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TyreRollingRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tyre_rolling_radius.setter
    @enforce_parameter_types
    def tyre_rolling_radius(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TyreRollingRadius = value

    @property
    def width_for_drawing(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WidthForDrawing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @width_for_drawing.setter
    @enforce_parameter_types
    def width_for_drawing(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WidthForDrawing = value

    @property
    def electric_machine_detail(self: "Self") -> "_1302.ElectricMachineDetail":
        """mastapy._private.electric_machines.ElectricMachineDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def oil_pump_detail(self: "Self") -> "_308.OilPumpDetail":
        """mastapy._private.materials.efficiency.OilPumpDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilPumpDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_blade_details(self: "Self") -> "_2537.WindTurbineSingleBladeDetails":
        """mastapy._private.system_model.part_model.WindTurbineSingleBladeDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleBladeDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_PowerLoad":
        """Cast to another type.

        Returns:
            _Cast_PowerLoad
        """
        return _Cast_PowerLoad(self)
