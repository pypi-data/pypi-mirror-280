"""CylindricalGearFEModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.fe_model import _1235
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Cylindrical", "CylindricalGearFEModel"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.analysis import _1259, _1256, _1253

    Self = TypeVar("Self", bound="CylindricalGearFEModel")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearFEModel._Cast_CylindricalGearFEModel"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFEModel",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearFEModel:
    """Special nested class for casting CylindricalGearFEModel to subclasses."""

    __parent__: "CylindricalGearFEModel"

    @property
    def gear_fe_model(self: "CastSelf") -> "_1235.GearFEModel":
        return self.__parent__._cast(_1235.GearFEModel)

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        from mastapy._private.gears.analysis import _1259

        return self.__parent__._cast(_1259.GearImplementationDetail)

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def cylindrical_gear_fe_model(self: "CastSelf") -> "CylindricalGearFEModel":
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
class CylindricalGearFEModel(_1235.GearFEModel):
    """CylindricalGearFEModel

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_FE_MODEL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def thickness_for_analyses(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ThicknessForAnalyses

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @thickness_for_analyses.setter
    @enforce_parameter_types
    def thickness_for_analyses(self: "Self", value: "str") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ThicknessForAnalyses = value

    @property
    def use_specified_web(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSpecifiedWeb

        if temp is None:
            return False

        return temp

    @use_specified_web.setter
    @enforce_parameter_types
    def use_specified_web(self: "Self", value: "bool") -> None:
        self.wrapped.UseSpecifiedWeb = bool(value) if value is not None else False

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearFEModel":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearFEModel
        """
        return _Cast_CylindricalGearFEModel(self)
