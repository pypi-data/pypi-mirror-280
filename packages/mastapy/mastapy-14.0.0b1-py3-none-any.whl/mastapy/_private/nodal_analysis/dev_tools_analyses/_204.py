"""FEModelTransparencyDrawStyle"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_MODEL_TRANSPARENCY_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelTransparencyDrawStyle"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    Self = TypeVar("Self", bound="FEModelTransparencyDrawStyle")
    CastSelf = TypeVar(
        "CastSelf",
        bound="FEModelTransparencyDrawStyle._Cast_FEModelTransparencyDrawStyle",
    )


__docformat__ = "restructuredtext en"
__all__ = ("FEModelTransparencyDrawStyle",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEModelTransparencyDrawStyle:
    """Special nested class for casting FEModelTransparencyDrawStyle to subclasses."""

    __parent__: "FEModelTransparencyDrawStyle"

    @property
    def fe_model_transparency_draw_style(
        self: "CastSelf",
    ) -> "FEModelTransparencyDrawStyle":
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
class FEModelTransparencyDrawStyle(_0.APIBase):
    """FEModelTransparencyDrawStyle

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_MODEL_TRANSPARENCY_DRAW_STYLE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def show_fe3d_axes(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ShowFE3DAxes

        if temp is None:
            return False

        return temp

    @show_fe3d_axes.setter
    @enforce_parameter_types
    def show_fe3d_axes(self: "Self", value: "bool") -> None:
        self.wrapped.ShowFE3DAxes = bool(value) if value is not None else False

    @property
    def cast_to(self: "Self") -> "_Cast_FEModelTransparencyDrawStyle":
        """Cast to another type.

        Returns:
            _Cast_FEModelTransparencyDrawStyle
        """
        return _Cast_FEModelTransparencyDrawStyle(self)
