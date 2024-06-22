"""Usage"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility import _1633
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_USAGE = python_net_import("SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Usage")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears import _355
    from mastapy._private.gears.gear_designs.cylindrical import _1107

    Self = TypeVar("Self", bound="Usage")
    CastSelf = TypeVar("CastSelf", bound="Usage._Cast_Usage")


__docformat__ = "restructuredtext en"
__all__ = ("Usage",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Usage:
    """Special nested class for casting Usage to subclasses."""

    __parent__: "Usage"

    @property
    def independent_reportable_properties_base(
        self: "CastSelf",
    ) -> "_1633.IndependentReportablePropertiesBase":
        pass

        return self.__parent__._cast(_1633.IndependentReportablePropertiesBase)

    @property
    def usage(self: "CastSelf") -> "Usage":
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
class Usage(_1633.IndependentReportablePropertiesBase["Usage"]):
    """Usage

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _USAGE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def gearing_is_runin(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.GearingIsRunin

        if temp is None:
            return False

        return temp

    @gearing_is_runin.setter
    @enforce_parameter_types
    def gearing_is_runin(self: "Self", value: "bool") -> None:
        self.wrapped.GearingIsRunin = bool(value) if value is not None else False

    @property
    def improved_gearing(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ImprovedGearing

        if temp is None:
            return False

        return temp

    @improved_gearing.setter
    @enforce_parameter_types
    def improved_gearing(self: "Self", value: "bool") -> None:
        self.wrapped.ImprovedGearing = bool(value) if value is not None else False

    @property
    def leads_modified(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.LeadsModified

        if temp is None:
            return False

        return temp

    @leads_modified.setter
    @enforce_parameter_types
    def leads_modified(self: "Self", value: "bool") -> None:
        self.wrapped.LeadsModified = bool(value) if value is not None else False

    @property
    def safety_requirement(self: "Self") -> "_355.SafetyRequirementsAGMA":
        """mastapy._private.gears.SafetyRequirementsAGMA"""
        temp = self.wrapped.SafetyRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.SafetyRequirementsAGMA"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears._355", "SafetyRequirementsAGMA"
        )(value)

    @safety_requirement.setter
    @enforce_parameter_types
    def safety_requirement(self: "Self", value: "_355.SafetyRequirementsAGMA") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.SafetyRequirementsAGMA"
        )
        self.wrapped.SafetyRequirement = value

    @property
    def spur_gear_load_sharing_code(self: "Self") -> "_1107.SpurGearLoadSharingCodes":
        """mastapy._private.gears.gear_designs.cylindrical.SpurGearLoadSharingCodes"""
        temp = self.wrapped.SpurGearLoadSharingCode

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.SpurGearLoadSharingCodes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1107",
            "SpurGearLoadSharingCodes",
        )(value)

    @spur_gear_load_sharing_code.setter
    @enforce_parameter_types
    def spur_gear_load_sharing_code(
        self: "Self", value: "_1107.SpurGearLoadSharingCodes"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.SpurGearLoadSharingCodes"
        )
        self.wrapped.SpurGearLoadSharingCode = value

    @property
    def cast_to(self: "Self") -> "_Cast_Usage":
        """Cast to another type.

        Returns:
            _Cast_Usage
        """
        return _Cast_Usage(self)
