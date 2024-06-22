"""ElectricMachineHarmonicLoadDataFromMotorPackages"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.analyses_and_results.static_loads import _7018
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
)

if TYPE_CHECKING:
    from typing import Any, Type

    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7027,
        _7020,
        _7021,
        _7023,
    )
    from mastapy._private.electric_machines.harmonic_load_data import (
        _1424,
        _1429,
        _1426,
    )

    Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromMotorPackages")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
    )

T = TypeVar("T", bound="_7027.ElectricMachineHarmonicLoadImportOptionsBase")

__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromMotorPackages",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ElectricMachineHarmonicLoadDataFromMotorPackages:
    """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorPackages to subclasses."""

    __parent__: "ElectricMachineHarmonicLoadDataFromMotorPackages"

    @property
    def electric_machine_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7018.ElectricMachineHarmonicLoadData":
        return self.__parent__._cast(_7018.ElectricMachineHarmonicLoadData)

    @property
    def electric_machine_harmonic_load_data_base(
        self: "CastSelf",
    ) -> "_1424.ElectricMachineHarmonicLoadDataBase":
        from mastapy._private.electric_machines.harmonic_load_data import _1424

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
    ) -> "ElectricMachineHarmonicLoadDataFromMotorPackages":
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
class ElectricMachineHarmonicLoadDataFromMotorPackages(
    _7018.ElectricMachineHarmonicLoadData, Generic[T]
):
    """ElectricMachineHarmonicLoadDataFromMotorPackages

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_ElectricMachineHarmonicLoadDataFromMotorPackages":
        """Cast to another type.

        Returns:
            _Cast_ElectricMachineHarmonicLoadDataFromMotorPackages
        """
        return _Cast_ElectricMachineHarmonicLoadDataFromMotorPackages(self)
