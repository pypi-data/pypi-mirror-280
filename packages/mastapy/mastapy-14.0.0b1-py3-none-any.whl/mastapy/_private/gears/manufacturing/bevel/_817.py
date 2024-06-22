"""ConicalWheelManufacturingConfig"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.gears.manufacturing.bevel import _799
from mastapy._private._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CONICAL_WHEEL_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalWheelManufacturingConfig"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.bevel.basic_machine_settings import (
        _847,
        _844,
    )
    from mastapy._private.gears.manufacturing.bevel.cutters import _838, _839
    from mastapy._private.gears.manufacturing.bevel import _801
    from mastapy._private.gears.analysis import _1259, _1256, _1253

    Self = TypeVar("Self", bound="ConicalWheelManufacturingConfig")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalWheelManufacturingConfig",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalWheelManufacturingConfig:
    """Special nested class for casting ConicalWheelManufacturingConfig to subclasses."""

    __parent__: "ConicalWheelManufacturingConfig"

    @property
    def conical_gear_manufacturing_config(
        self: "CastSelf",
    ) -> "_799.ConicalGearManufacturingConfig":
        return self.__parent__._cast(_799.ConicalGearManufacturingConfig)

    @property
    def conical_gear_micro_geometry_config_base(
        self: "CastSelf",
    ) -> "_801.ConicalGearMicroGeometryConfigBase":
        from mastapy._private.gears.manufacturing.bevel import _801

        return self.__parent__._cast(_801.ConicalGearMicroGeometryConfigBase)

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        from mastapy._private.gears.analysis import _1259

        return self.__parent__._cast(_1259.GearImplementationDetail)

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def conical_wheel_manufacturing_config(
        self: "CastSelf",
    ) -> "ConicalWheelManufacturingConfig":
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
class ConicalWheelManufacturingConfig(_799.ConicalGearManufacturingConfig):
    """ConicalWheelManufacturingConfig

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_WHEEL_MANUFACTURING_CONFIG

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def use_cutter_tilt(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseCutterTilt

        if temp is None:
            return False

        return temp

    @use_cutter_tilt.setter
    @enforce_parameter_types
    def use_cutter_tilt(self: "Self", value: "bool") -> None:
        self.wrapped.UseCutterTilt = bool(value) if value is not None else False

    @property
    def wheel_finish_manufacturing_machine(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.WheelFinishManufacturingMachine.SelectedItemName

        if temp is None:
            return ""

        return temp

    @wheel_finish_manufacturing_machine.setter
    @enforce_parameter_types
    def wheel_finish_manufacturing_machine(self: "Self", value: "str") -> None:
        self.wrapped.WheelFinishManufacturingMachine.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def wheel_rough_manufacturing_machine(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.WheelRoughManufacturingMachine.SelectedItemName

        if temp is None:
            return ""

        return temp

    @wheel_rough_manufacturing_machine.setter
    @enforce_parameter_types
    def wheel_rough_manufacturing_machine(self: "Self", value: "str") -> None:
        self.wrapped.WheelRoughManufacturingMachine.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def specified_cradle_style_machine_settings(
        self: "Self",
    ) -> "_847.CradleStyleConicalMachineSettingsGenerated":
        """mastapy._private.gears.manufacturing.bevel.basic_machine_settings.CradleStyleConicalMachineSettingsGenerated

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedCradleStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specified_machine_settings(
        self: "Self",
    ) -> "_844.BasicConicalGearMachineSettings":
        """mastapy._private.gears.manufacturing.bevel.basic_machine_settings.BasicConicalGearMachineSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_finish_cutter(self: "Self") -> "_838.WheelFinishCutter":
        """mastapy._private.gears.manufacturing.bevel.cutters.WheelFinishCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_rough_cutter(self: "Self") -> "_839.WheelRoughCutter":
        """mastapy._private.gears.manufacturing.bevel.cutters.WheelRoughCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalWheelManufacturingConfig":
        """Cast to another type.

        Returns:
            _Cast_ConicalWheelManufacturingConfig
        """
        return _Cast_ConicalWheelManufacturingConfig(self)
