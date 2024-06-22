"""ElectricMachineHarmonicLoadDataFromMotorCAD"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.analyses_and_results.static_loads import _7024, _7029
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.static_loads import _7018
    from mastapy._private.electric_machines.harmonic_load_data import (
        _1424,
        _1429,
        _1426,
    )

    Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromMotorCAD")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromMotorCAD",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ElectricMachineHarmonicLoadDataFromMotorCAD:
    """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorCAD to subclasses."""

    __parent__: "ElectricMachineHarmonicLoadDataFromMotorCAD"

    @property
    def electric_machine_harmonic_load_data_from_motor_packages(
        self: "CastSelf",
    ) -> "_7024.ElectricMachineHarmonicLoadDataFromMotorPackages":
        return self.__parent__._cast(
            _7024.ElectricMachineHarmonicLoadDataFromMotorPackages
        )

    @property
    def electric_machine_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7018.ElectricMachineHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7018,
        )

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
    def electric_machine_harmonic_load_data_from_motor_cad(
        self: "CastSelf",
    ) -> "ElectricMachineHarmonicLoadDataFromMotorCAD":
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
class ElectricMachineHarmonicLoadDataFromMotorCAD(
    _7024.ElectricMachineHarmonicLoadDataFromMotorPackages[
        _7029.ElectricMachineHarmonicLoadMotorCADImportOptions
    ]
):
    """ElectricMachineHarmonicLoadDataFromMotorCAD

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_CAD

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_ElectricMachineHarmonicLoadDataFromMotorCAD":
        """Cast to another type.

        Returns:
            _Cast_ElectricMachineHarmonicLoadDataFromMotorCAD
        """
        return _Cast_ElectricMachineHarmonicLoadDataFromMotorCAD(self)
