"""ConicalGearSetHarmonicLoadData"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _7041
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConicalGearSetHarmonicLoadData",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears import _359
    from mastapy._private.math_utility import _1559
    from mastapy._private.electric_machines.harmonic_load_data import _1426

    Self = TypeVar("Self", bound="ConicalGearSetHarmonicLoadData")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetHarmonicLoadData",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSetHarmonicLoadData:
    """Special nested class for casting ConicalGearSetHarmonicLoadData to subclasses."""

    __parent__: "ConicalGearSetHarmonicLoadData"

    @property
    def gear_set_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7041.GearSetHarmonicLoadData":
        return self.__parent__._cast(_7041.GearSetHarmonicLoadData)

    @property
    def harmonic_load_data_base(self: "CastSelf") -> "_1426.HarmonicLoadDataBase":
        from mastapy._private.electric_machines.harmonic_load_data import _1426

        return self.__parent__._cast(_1426.HarmonicLoadDataBase)

    @property
    def conical_gear_set_harmonic_load_data(
        self: "CastSelf",
    ) -> "ConicalGearSetHarmonicLoadData":
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
class ConicalGearSetHarmonicLoadData(_7041.GearSetHarmonicLoadData):
    """ConicalGearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_SET_HARMONIC_LOAD_DATA

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def te_specification_type(self: "Self") -> "_359.TESpecificationType":
        """mastapy._private.gears.TESpecificationType"""
        temp = self.wrapped.TESpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.TESpecificationType")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears._359", "TESpecificationType"
        )(value)

    @te_specification_type.setter
    @enforce_parameter_types
    def te_specification_type(self: "Self", value: "_359.TESpecificationType") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.TESpecificationType"
        )
        self.wrapped.TESpecificationType = value

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

    def read_data_from_gleason_gemsxml(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ReadDataFromGleasonGEMSXML()

    def read_data_from_ki_mo_sxml(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ReadDataFromKIMoSXML()

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearSetHarmonicLoadData":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSetHarmonicLoadData
        """
        return _Cast_ConicalGearSetHarmonicLoadData(self)
