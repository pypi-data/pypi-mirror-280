"""UnbalancedMassHarmonicLoadData"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.math_utility import _1550
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private.electric_machines.harmonic_load_data import _1429
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_UNBALANCED_MASS_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "UnbalancedMassHarmonicLoadData",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.math_utility import _1559
    from mastapy._private.electric_machines.harmonic_load_data import _1426

    Self = TypeVar("Self", bound="UnbalancedMassHarmonicLoadData")
    CastSelf = TypeVar(
        "CastSelf",
        bound="UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData",
    )


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassHarmonicLoadData",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_UnbalancedMassHarmonicLoadData:
    """Special nested class for casting UnbalancedMassHarmonicLoadData to subclasses."""

    __parent__: "UnbalancedMassHarmonicLoadData"

    @property
    def speed_dependent_harmonic_load_data(
        self: "CastSelf",
    ) -> "_1429.SpeedDependentHarmonicLoadData":
        return self.__parent__._cast(_1429.SpeedDependentHarmonicLoadData)

    @property
    def harmonic_load_data_base(self: "CastSelf") -> "_1426.HarmonicLoadDataBase":
        from mastapy._private.electric_machines.harmonic_load_data import _1426

        return self.__parent__._cast(_1426.HarmonicLoadDataBase)

    @property
    def unbalanced_mass_harmonic_load_data(
        self: "CastSelf",
    ) -> "UnbalancedMassHarmonicLoadData":
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
class UnbalancedMassHarmonicLoadData(_1429.SpeedDependentHarmonicLoadData):
    """UnbalancedMassHarmonicLoadData

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _UNBALANCED_MASS_HARMONIC_LOAD_DATA

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def degree_of_freedom(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DegreeOfFreedom":
        """EnumWithSelectedValue[mastapy._private.math_utility.DegreeOfFreedom]"""
        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DegreeOfFreedom.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @degree_of_freedom.setter
    @enforce_parameter_types
    def degree_of_freedom(self: "Self", value: "_1550.DegreeOfFreedom") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DegreeOfFreedom.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DegreeOfFreedom = value

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
    def cast_to(self: "Self") -> "_Cast_UnbalancedMassHarmonicLoadData":
        """Cast to another type.

        Returns:
            _Cast_UnbalancedMassHarmonicLoadData
        """
        return _Cast_UnbalancedMassHarmonicLoadData(self)
