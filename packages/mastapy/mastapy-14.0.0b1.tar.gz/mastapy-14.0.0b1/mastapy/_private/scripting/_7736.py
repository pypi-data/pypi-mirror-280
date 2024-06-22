"""ApiVersioning"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion
from mastapy._private._internal.python_net import python_net_import

_API_VERSIONING = python_net_import("SMT.MastaAPIUtility.Scripting", "ApiVersioning")

if TYPE_CHECKING:
    from typing import Any, Type, Iterable, NoReturn

    from mastapy._private.scripting import _7728


__docformat__ = "restructuredtext en"
__all__ = ("ApiVersioning",)


class ApiVersioning:
    """ApiVersioning

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _API_VERSIONING

    def __new__(
        cls: "Type[ApiVersioning]", *args: "Any", **kwargs: "Any"
    ) -> "NoReturn":
        """Override of the new magic method.

        Note:
            This class cannot be instantiated and this method will always throw an
            exception.

        Args:
            cls (Type[ApiVersioning]: The class to instantiate.
            *args (Any): Arguments.
            **kwargs (Any): Keyword arguments.

        Returns:
            NoReturn
        """
        raise TypeError("Class cannot be instantiated. Please use statically.")

    @staticmethod
    @enforce_parameter_types
    def get_available_api_versions(folder: "str") -> "Iterable[_7728.ApiVersion]":
        """Iterable[mastapy._private.scripting.ApiVersion]

        Args:
            folder (str)
        """
        folder = str(folder)
        return conversion.pn_to_mp_objects_in_iterable(
            ApiVersioning.TYPE.GetAvailableApiVersions(folder if folder else "")
        )

    @staticmethod
    @enforce_parameter_types
    def get_available_api_utility_versions(
        folder: "str",
    ) -> "Iterable[_7728.ApiVersion]":
        """Iterable[mastapy._private.scripting.ApiVersion]

        Args:
            folder (str)
        """
        folder = str(folder)
        return conversion.pn_to_mp_objects_in_iterable(
            ApiVersioning.TYPE.GetAvailableApiUtilityVersions(folder if folder else "")
        )

    @staticmethod
    @enforce_parameter_types
    def get_api_version_for_assembly(
        api_library_search_folder: "str", assembly_path: "str"
    ) -> "_7728.ApiVersion":
        """mastapy._private.scripting.ApiVersion

        Args:
            api_library_search_folder (str)
            assembly_path (str)
        """
        api_library_search_folder = str(api_library_search_folder)
        assembly_path = str(assembly_path)
        method_result = ApiVersioning.TYPE.GetApiVersionForAssembly(
            api_library_search_folder if api_library_search_folder else "",
            assembly_path if assembly_path else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )
