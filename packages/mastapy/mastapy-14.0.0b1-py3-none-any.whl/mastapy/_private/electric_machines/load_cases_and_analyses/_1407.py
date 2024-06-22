"""ElectricMachineMechanicalLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.electric_machines.load_cases_and_analyses import _1405
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MECHANICAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "ElectricMachineMechanicalLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    Self = TypeVar("Self", bound="ElectricMachineMechanicalLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineMechanicalLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ElectricMachineMechanicalLoadCase:
    """Special nested class for casting ElectricMachineMechanicalLoadCase to subclasses."""

    __parent__: "ElectricMachineMechanicalLoadCase"

    @property
    def electric_machine_load_case_base(
        self: "CastSelf",
    ) -> "_1405.ElectricMachineLoadCaseBase":
        return self.__parent__._cast(_1405.ElectricMachineLoadCaseBase)

    @property
    def electric_machine_mechanical_load_case(
        self: "CastSelf",
    ) -> "ElectricMachineMechanicalLoadCase":
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
class ElectricMachineMechanicalLoadCase(_1405.ElectricMachineLoadCaseBase):
    """ElectricMachineMechanicalLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ELECTRIC_MACHINE_MECHANICAL_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def speed(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    @enforce_parameter_types
    def speed(self: "Self", value: "float") -> None:
        self.wrapped.Speed = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_ElectricMachineMechanicalLoadCase":
        """Cast to another type.

        Returns:
            _Cast_ElectricMachineMechanicalLoadCase
        """
        return _Cast_ElectricMachineMechanicalLoadCase(self)
