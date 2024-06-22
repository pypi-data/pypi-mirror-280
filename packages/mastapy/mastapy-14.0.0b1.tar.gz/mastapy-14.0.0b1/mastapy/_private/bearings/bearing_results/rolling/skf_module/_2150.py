"""SKFCredentials"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SKF_CREDENTIALS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "SKFCredentials"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bearings.bearing_results.rolling.skf_module import _2148

    Self = TypeVar("Self", bound="SKFCredentials")
    CastSelf = TypeVar("CastSelf", bound="SKFCredentials._Cast_SKFCredentials")


__docformat__ = "restructuredtext en"
__all__ = ("SKFCredentials",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SKFCredentials:
    """Special nested class for casting SKFCredentials to subclasses."""

    __parent__: "SKFCredentials"

    @property
    def skf_credentials(self: "CastSelf") -> "SKFCredentials":
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
class SKFCredentials(_0.APIBase):
    """SKFCredentials

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SKF_CREDENTIALS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def email_address(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.EmailAddress

        if temp is None:
            return ""

        return temp

    @email_address.setter
    @enforce_parameter_types
    def email_address(self: "Self", value: "str") -> None:
        self.wrapped.EmailAddress = str(value) if value is not None else ""

    @property
    def password(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Password

        if temp is None:
            return ""

        return temp

    @password.setter
    @enforce_parameter_types
    def password(self: "Self", value: "str") -> None:
        self.wrapped.Password = str(value) if value is not None else ""

    @property
    def read_ampersand_accept_terms_of_use(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ReadAmpersandAcceptTermsOfUse

        if temp is None:
            return False

        return temp

    @read_ampersand_accept_terms_of_use.setter
    @enforce_parameter_types
    def read_ampersand_accept_terms_of_use(self: "Self", value: "bool") -> None:
        self.wrapped.ReadAmpersandAcceptTermsOfUse = (
            bool(value) if value is not None else False
        )

    @property
    def skf_authentication(self: "Self") -> "_2148.SKFAuthentication":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.SKFAuthentication

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFAuthentication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def authenticate(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Authenticate()

    def create_skf_account(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CreateSKFAccount()

    def skf_privacy_notice(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.SKFPrivacyNotice()

    def skf_terms_of_use(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.SKFTermsOfUse()

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_SKFCredentials":
        """Cast to another type.

        Returns:
            _Cast_SKFCredentials
        """
        return _Cast_SKFCredentials(self)
