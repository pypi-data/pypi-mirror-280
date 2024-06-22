"""HarmonicLoadDataJMAGImport"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.system_model.analyses_and_results.static_loads import _7045, _7028
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_JMAG_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataJMAGImport",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7049,
        _7048,
    )

    Self = TypeVar("Self", bound="HarmonicLoadDataJMAGImport")
    CastSelf = TypeVar(
        "CastSelf", bound="HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport"
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataJMAGImport",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicLoadDataJMAGImport:
    """Special nested class for casting HarmonicLoadDataJMAGImport to subclasses."""

    __parent__: "HarmonicLoadDataJMAGImport"

    @property
    def harmonic_load_data_csv_import(
        self: "CastSelf",
    ) -> "_7045.HarmonicLoadDataCSVImport":
        return self.__parent__._cast(_7045.HarmonicLoadDataCSVImport)

    @property
    def harmonic_load_data_import_from_motor_packages(
        self: "CastSelf",
    ) -> "_7049.HarmonicLoadDataImportFromMotorPackages":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7049,
        )

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
    def harmonic_load_data_jmag_import(
        self: "CastSelf",
    ) -> "HarmonicLoadDataJMAGImport":
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
class HarmonicLoadDataJMAGImport(
    _7045.HarmonicLoadDataCSVImport[_7028.ElectricMachineHarmonicLoadJMAGImportOptions]
):
    """HarmonicLoadDataJMAGImport

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HARMONIC_LOAD_DATA_JMAG_IMPORT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    def select_jmag_file(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.SelectJMAGFile()

    @property
    def cast_to(self: "Self") -> "_Cast_HarmonicLoadDataJMAGImport":
        """Cast to another type.

        Returns:
            _Cast_HarmonicLoadDataJMAGImport
        """
        return _Cast_HarmonicLoadDataJMAGImport(self)
