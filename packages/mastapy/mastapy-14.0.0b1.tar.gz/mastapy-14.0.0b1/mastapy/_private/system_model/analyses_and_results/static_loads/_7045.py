"""HarmonicLoadDataCSVImport"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _7049
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CSV_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataCSVImport",
)

if TYPE_CHECKING:
    from typing import Any, Type, List

    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7015,
        _7027,
        _7047,
        _7050,
        _7048,
    )

    Self = TypeVar("Self", bound="HarmonicLoadDataCSVImport")
    CastSelf = TypeVar(
        "CastSelf", bound="HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport"
    )

T = TypeVar("T", bound="_7027.ElectricMachineHarmonicLoadImportOptionsBase")

__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataCSVImport",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicLoadDataCSVImport:
    """Special nested class for casting HarmonicLoadDataCSVImport to subclasses."""

    __parent__: "HarmonicLoadDataCSVImport"

    @property
    def harmonic_load_data_import_from_motor_packages(
        self: "CastSelf",
    ) -> "_7049.HarmonicLoadDataImportFromMotorPackages":
        return self.__parent__._cast(_7049.HarmonicLoadDataImportFromMotorPackages)

    @property
    def harmonic_load_data_import_base(
        self: "CastSelf",
    ) -> "_7048.HarmonicLoadDataImportBase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7048,
        )

        return self.__parent__._cast(_7048.HarmonicLoadDataImportBase)

    @property
    def harmonic_load_data_flux_import(
        self: "CastSelf",
    ) -> "_7047.HarmonicLoadDataFluxImport":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7047,
        )

        return self.__parent__._cast(_7047.HarmonicLoadDataFluxImport)

    @property
    def harmonic_load_data_jmag_import(
        self: "CastSelf",
    ) -> "_7050.HarmonicLoadDataJMAGImport":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7050,
        )

        return self.__parent__._cast(_7050.HarmonicLoadDataJMAGImport)

    @property
    def harmonic_load_data_csv_import(self: "CastSelf") -> "HarmonicLoadDataCSVImport":
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
class HarmonicLoadDataCSVImport(_7049.HarmonicLoadDataImportFromMotorPackages[T]):
    """HarmonicLoadDataCSVImport

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _HARMONIC_LOAD_DATA_CSV_IMPORT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def electric_machine_data_per_speed(
        self: "Self",
    ) -> "List[_7015.DataFromMotorPackagePerSpeed]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.DataFromMotorPackagePerSpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDataPerSpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_HarmonicLoadDataCSVImport":
        """Cast to another type.

        Returns:
            _Cast_HarmonicLoadDataCSVImport
        """
        return _Cast_HarmonicLoadDataCSVImport(self)
