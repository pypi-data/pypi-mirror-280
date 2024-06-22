"""ElectricMachineHarmonicLoadData"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.electric_machines.harmonic_load_data import _1428, _1424
from mastapy._private.system_model.analyses_and_results.static_loads import _7125
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadData",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.math_utility import _1559
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7019,
        _7020,
        _7021,
        _7022,
        _7023,
        _7024,
    )
    from mastapy._private.electric_machines.harmonic_load_data import _1429, _1426

    Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadData")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ElectricMachineHarmonicLoadData._Cast_ElectricMachineHarmonicLoadData",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadData",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ElectricMachineHarmonicLoadData:
    """Special nested class for casting ElectricMachineHarmonicLoadData to subclasses."""

    __parent__: "ElectricMachineHarmonicLoadData"

    @property
    def electric_machine_harmonic_load_data_base(
        self: "CastSelf",
    ) -> "_1424.ElectricMachineHarmonicLoadDataBase":
        return self.__parent__._cast(_1424.ElectricMachineHarmonicLoadDataBase)

    @property
    def speed_dependent_harmonic_load_data(
        self: "CastSelf",
    ) -> "_1429.SpeedDependentHarmonicLoadData":
        from mastapy._private.electric_machines.harmonic_load_data import _1429

        return self.__parent__._cast(_1429.SpeedDependentHarmonicLoadData)

    @property
    def harmonic_load_data_base(self: "CastSelf") -> "_1426.HarmonicLoadDataBase":
        from mastapy._private.electric_machines.harmonic_load_data import _1426

        return self.__parent__._cast(_1426.HarmonicLoadDataBase)

    @property
    def electric_machine_harmonic_load_data_from_excel(
        self: "CastSelf",
    ) -> "_7019.ElectricMachineHarmonicLoadDataFromExcel":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7019,
        )

        return self.__parent__._cast(_7019.ElectricMachineHarmonicLoadDataFromExcel)

    @property
    def electric_machine_harmonic_load_data_from_flux(
        self: "CastSelf",
    ) -> "_7020.ElectricMachineHarmonicLoadDataFromFlux":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7020,
        )

        return self.__parent__._cast(_7020.ElectricMachineHarmonicLoadDataFromFlux)

    @property
    def electric_machine_harmonic_load_data_from_jmag(
        self: "CastSelf",
    ) -> "_7021.ElectricMachineHarmonicLoadDataFromJMAG":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7021,
        )

        return self.__parent__._cast(_7021.ElectricMachineHarmonicLoadDataFromJMAG)

    @property
    def electric_machine_harmonic_load_data_from_masta(
        self: "CastSelf",
    ) -> "_7022.ElectricMachineHarmonicLoadDataFromMASTA":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7022,
        )

        return self.__parent__._cast(_7022.ElectricMachineHarmonicLoadDataFromMASTA)

    @property
    def electric_machine_harmonic_load_data_from_motor_cad(
        self: "CastSelf",
    ) -> "_7023.ElectricMachineHarmonicLoadDataFromMotorCAD":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7023,
        )

        return self.__parent__._cast(_7023.ElectricMachineHarmonicLoadDataFromMotorCAD)

    @property
    def electric_machine_harmonic_load_data_from_motor_packages(
        self: "CastSelf",
    ) -> "_7024.ElectricMachineHarmonicLoadDataFromMotorPackages":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7024,
        )

        return self.__parent__._cast(
            _7024.ElectricMachineHarmonicLoadDataFromMotorPackages
        )

    @property
    def electric_machine_harmonic_load_data(
        self: "CastSelf",
    ) -> "ElectricMachineHarmonicLoadData":
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
class ElectricMachineHarmonicLoadData(_1424.ElectricMachineHarmonicLoadDataBase):
    """ElectricMachineHarmonicLoadData

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def apply_to_all_data_types(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ApplyToAllDataTypes

        if temp is None:
            return False

        return temp

    @apply_to_all_data_types.setter
    @enforce_parameter_types
    def apply_to_all_data_types(self: "Self", value: "bool") -> None:
        self.wrapped.ApplyToAllDataTypes = bool(value) if value is not None else False

    @property
    def apply_to_all_speeds_for_selected_data_type(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ApplyToAllSpeedsForSelectedDataType

        if temp is None:
            return False

        return temp

    @apply_to_all_speeds_for_selected_data_type.setter
    @enforce_parameter_types
    def apply_to_all_speeds_for_selected_data_type(self: "Self", value: "bool") -> None:
        self.wrapped.ApplyToAllSpeedsForSelectedDataType = (
            bool(value) if value is not None else False
        )

    @property
    def constant_torque(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ConstantTorque

        if temp is None:
            return 0.0

        return temp

    @constant_torque.setter
    @enforce_parameter_types
    def constant_torque(self: "Self", value: "float") -> None:
        self.wrapped.ConstantTorque = float(value) if value is not None else 0.0

    @property
    def data_type_for_scaling(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType":
        """EnumWithSelectedValue[mastapy._private.electric_machines.harmonic_load_data.HarmonicLoadDataType]"""
        temp = self.wrapped.DataTypeForScaling

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @data_type_for_scaling.setter
    @enforce_parameter_types
    def data_type_for_scaling(
        self: "Self", value: "_1428.HarmonicLoadDataType"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataTypeForScaling = value

    @property
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def rotor_z_force_amplitude_cut_off(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RotorZForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_z_force_amplitude_cut_off.setter
    @enforce_parameter_types
    def rotor_z_force_amplitude_cut_off(self: "Self", value: "float") -> None:
        self.wrapped.RotorZForceAmplitudeCutOff = (
            float(value) if value is not None else 0.0
        )

    @property
    def scale(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    @enforce_parameter_types
    def scale(self: "Self", value: "float") -> None:
        self.wrapped.Scale = float(value) if value is not None else 0.0

    @property
    def torque_ripple_input_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType":
        """EnumWithSelectedValue[mastapy._private.system_model.analyses_and_results.static_loads.TorqueRippleInputType]"""
        temp = self.wrapped.TorqueRippleInputType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @torque_ripple_input_type.setter
    @enforce_parameter_types
    def torque_ripple_input_type(
        self: "Self", value: "_7125.TorqueRippleInputType"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueRippleInputType = value

    @property
    def use_stator_radius_from_masta_model(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseStatorRadiusFromMASTAModel

        if temp is None:
            return False

        return temp

    @use_stator_radius_from_masta_model.setter
    @enforce_parameter_types
    def use_stator_radius_from_masta_model(self: "Self", value: "bool") -> None:
        self.wrapped.UseStatorRadiusFromMASTAModel = (
            bool(value) if value is not None else False
        )

    @property
    def excitations(self: "Self") -> "List[_1559.FourierSeries]":
        """List[mastapy._private.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ElectricMachineHarmonicLoadData":
        """Cast to another type.

        Returns:
            _Cast_ElectricMachineHarmonicLoadData
        """
        return _Cast_ElectricMachineHarmonicLoadData(self)
