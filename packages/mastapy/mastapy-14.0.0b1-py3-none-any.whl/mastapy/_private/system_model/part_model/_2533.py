"""UnbalancedMass"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.system_model.part_model import _2535
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model import _2520, _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="UnbalancedMass")
    CastSelf = TypeVar("CastSelf", bound="UnbalancedMass._Cast_UnbalancedMass")


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMass",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_UnbalancedMass:
    """Special nested class for casting UnbalancedMass to subclasses."""

    __parent__: "UnbalancedMass"

    @property
    def virtual_component(self: "CastSelf") -> "_2535.VirtualComponent":
        return self.__parent__._cast(_2535.VirtualComponent)

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        from mastapy._private.system_model.part_model import _2498

        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def unbalanced_mass(self: "CastSelf") -> "UnbalancedMass":
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
class UnbalancedMass(_2535.VirtualComponent):
    """UnbalancedMass

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _UNBALANCED_MASS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: "Self", value: "float") -> None:
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def radius(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: "Self", value: "float") -> None:
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_UnbalancedMass":
        """Cast to another type.

        Returns:
            _Cast_UnbalancedMass
        """
        return _Cast_UnbalancedMass(self)
