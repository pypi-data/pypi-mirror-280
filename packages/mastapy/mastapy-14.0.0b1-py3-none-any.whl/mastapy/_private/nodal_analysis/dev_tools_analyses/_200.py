"""FEModelPart"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_MODEL_PART = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelPart"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    Self = TypeVar("Self", bound="FEModelPart")
    CastSelf = TypeVar("CastSelf", bound="FEModelPart._Cast_FEModelPart")


__docformat__ = "restructuredtext en"
__all__ = ("FEModelPart",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEModelPart:
    """Special nested class for casting FEModelPart to subclasses."""

    __parent__: "FEModelPart"

    @property
    def fe_model_part(self: "CastSelf") -> "FEModelPart":
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
class FEModelPart(_0.APIBase):
    """FEModelPart

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_MODEL_PART

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def draw_component(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.DrawComponent

        if temp is None:
            return False

        return temp

    @draw_component.setter
    @enforce_parameter_types
    def draw_component(self: "Self", value: "bool") -> None:
        self.wrapped.DrawComponent = bool(value) if value is not None else False

    @property
    def id(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_FEModelPart":
        """Cast to another type.

        Returns:
            _Cast_FEModelPart
        """
        return _Cast_FEModelPart(self)
