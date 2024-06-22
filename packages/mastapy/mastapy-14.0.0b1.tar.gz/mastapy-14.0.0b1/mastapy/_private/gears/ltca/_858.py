"""GearContactStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.ltca import _870
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_GEAR_CONTACT_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearContactStiffness"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.ltca.cylindrical import _876
    from mastapy._private.gears.ltca.conical import _888
    from mastapy._private.nodal_analysis import _66

    Self = TypeVar("Self", bound="GearContactStiffness")
    CastSelf = TypeVar(
        "CastSelf", bound="GearContactStiffness._Cast_GearContactStiffness"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearContactStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearContactStiffness:
    """Special nested class for casting GearContactStiffness to subclasses."""

    __parent__: "GearContactStiffness"

    @property
    def gear_stiffness(self: "CastSelf") -> "_870.GearStiffness":
        return self.__parent__._cast(_870.GearStiffness)

    @property
    def fe_stiffness(self: "CastSelf") -> "_66.FEStiffness":
        from mastapy._private.nodal_analysis import _66

        return self.__parent__._cast(_66.FEStiffness)

    @property
    def cylindrical_gear_contact_stiffness(
        self: "CastSelf",
    ) -> "_876.CylindricalGearContactStiffness":
        from mastapy._private.gears.ltca.cylindrical import _876

        return self.__parent__._cast(_876.CylindricalGearContactStiffness)

    @property
    def conical_gear_contact_stiffness(
        self: "CastSelf",
    ) -> "_888.ConicalGearContactStiffness":
        from mastapy._private.gears.ltca.conical import _888

        return self.__parent__._cast(_888.ConicalGearContactStiffness)

    @property
    def gear_contact_stiffness(self: "CastSelf") -> "GearContactStiffness":
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
class GearContactStiffness(_870.GearStiffness):
    """GearContactStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_CONTACT_STIFFNESS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_GearContactStiffness":
        """Cast to another type.

        Returns:
            _Cast_GearContactStiffness
        """
        return _Cast_GearContactStiffness(self)
