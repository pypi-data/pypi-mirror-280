"""UserTextRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.report import _1826
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_USER_TEXT_ROW = python_net_import("SMT.MastaAPI.Utility.Report", "UserTextRow")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.report import _1833, _1821

    Self = TypeVar("Self", bound="UserTextRow")
    CastSelf = TypeVar("CastSelf", bound="UserTextRow._Cast_UserTextRow")


__docformat__ = "restructuredtext en"
__all__ = ("UserTextRow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_UserTextRow:
    """Special nested class for casting UserTextRow to subclasses."""

    __parent__: "UserTextRow"

    @property
    def custom_row(self: "CastSelf") -> "_1826.CustomRow":
        return self.__parent__._cast(_1826.CustomRow)

    @property
    def custom_report_property_item(
        self: "CastSelf",
    ) -> "_1821.CustomReportPropertyItem":
        from mastapy._private.utility.report import _1821

        return self.__parent__._cast(_1821.CustomReportPropertyItem)

    @property
    def user_text_row(self: "CastSelf") -> "UserTextRow":
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
class UserTextRow(_1826.CustomRow):
    """UserTextRow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _USER_TEXT_ROW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def additional_text(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.AdditionalText

        if temp is None:
            return ""

        return temp

    @additional_text.setter
    @enforce_parameter_types
    def additional_text(self: "Self", value: "str") -> None:
        self.wrapped.AdditionalText = str(value) if value is not None else ""

    @property
    def heading_size(self: "Self") -> "_1833.HeadingSize":
        """mastapy._private.utility.report.HeadingSize"""
        temp = self.wrapped.HeadingSize

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Report.HeadingSize"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.utility.report._1833", "HeadingSize"
        )(value)

    @heading_size.setter
    @enforce_parameter_types
    def heading_size(self: "Self", value: "_1833.HeadingSize") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Report.HeadingSize"
        )
        self.wrapped.HeadingSize = value

    @property
    def is_heading(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IsHeading

        if temp is None:
            return False

        return temp

    @is_heading.setter
    @enforce_parameter_types
    def is_heading(self: "Self", value: "bool") -> None:
        self.wrapped.IsHeading = bool(value) if value is not None else False

    @property
    def show_additional_text(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ShowAdditionalText

        if temp is None:
            return False

        return temp

    @show_additional_text.setter
    @enforce_parameter_types
    def show_additional_text(self: "Self", value: "bool") -> None:
        self.wrapped.ShowAdditionalText = bool(value) if value is not None else False

    @property
    def text(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Text

        if temp is None:
            return ""

        return temp

    @text.setter
    @enforce_parameter_types
    def text(self: "Self", value: "str") -> None:
        self.wrapped.Text = str(value) if value is not None else ""

    @property
    def cast_to(self: "Self") -> "_Cast_UserTextRow":
        """Cast to another type.

        Returns:
            _Cast_UserTextRow
        """
        return _Cast_UserTextRow(self)
