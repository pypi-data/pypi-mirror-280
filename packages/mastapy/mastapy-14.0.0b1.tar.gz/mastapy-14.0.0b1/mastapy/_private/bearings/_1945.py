"""RollingBearingDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.utility.databases import _1881
from mastapy._private.bearings import _1946
from mastapy._private.bearings.bearing_designs.rolling import _2218
from mastapy._private._internal.cast_exception import CastException

_ROLLING_BEARING_TYPE = python_net_import("SMT.MastaAPI.Bearings", "RollingBearingType")
_BEARING_CATALOG = python_net_import("SMT.MastaAPI.Bearings", "BearingCatalog")
_HYBRID_STEEL_ALL = python_net_import("SMT.MastaAPI.Bearings", "HybridSteelAll")
_ROLLING_BEARING_DATABASE = python_net_import(
    "SMT.MastaAPI.Bearings", "RollingBearingDatabase"
)
_STRING = python_net_import("System", "String")
_INT_32 = python_net_import("System", "Int32")
_RANGE = python_net_import("SMT.MastaAPI.MathUtility", "Range")

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility.databases import _1874
    from mastapy._private.bearings import _1948, _1921, _1937
    from mastapy._private.math_utility import _1535

    Self = TypeVar("Self", bound="RollingBearingDatabase")
    CastSelf = TypeVar(
        "CastSelf", bound="RollingBearingDatabase._Cast_RollingBearingDatabase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_RollingBearingDatabase:
    """Special nested class for casting RollingBearingDatabase to subclasses."""

    __parent__: "RollingBearingDatabase"

    @property
    def sql_database(self: "CastSelf") -> "_1881.SQLDatabase":
        return self.__parent__._cast(_1881.SQLDatabase)

    @property
    def database(self: "CastSelf") -> "_1874.Database":
        from mastapy._private.utility.databases import _1874

        return self.__parent__._cast(_1874.Database)

    @property
    def rolling_bearing_database(self: "CastSelf") -> "RollingBearingDatabase":
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
class RollingBearingDatabase(
    _1881.SQLDatabase[_1946.RollingBearingKey, _2218.RollingBearing]
):
    """RollingBearingDatabase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ROLLING_BEARING_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @enforce_parameter_types
    def add_to_database(self: "Self", bearing: "_2218.RollingBearing") -> None:
        """Method does not return.

        Args:
            bearing (mastapy._private.bearings.bearing_designs.rolling.RollingBearing)
        """
        self.wrapped.AddToDatabase(bearing.wrapped if bearing else None)

    @enforce_parameter_types
    def create_bearing(
        self: "Self", type_: "_1948.RollingBearingType", designation: "str" = "None"
    ) -> "_2218.RollingBearing":
        """mastapy._private.bearings.bearing_designs.rolling.RollingBearing

        Args:
            type_ (mastapy._private.bearings.RollingBearingType)
            designation (str, optional)
        """
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        designation = str(designation)
        method_result = self.wrapped.CreateBearing.Overloads[
            _ROLLING_BEARING_TYPE, _STRING
        ](type_, designation if designation else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_bearing_with_type_name(
        self: "Self", type_: "str", designation: "str" = "None"
    ) -> "_2218.RollingBearing":
        """mastapy._private.bearings.bearing_designs.rolling.RollingBearing

        Args:
            type_ (str)
            designation (str, optional)
        """
        type_ = str(type_)
        designation = str(designation)
        method_result = self.wrapped.CreateBearing.Overloads[_STRING, _STRING](
            type_ if type_ else "", designation if designation else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_key(
        self: "Self", type_: "_1948.RollingBearingType", designation: "str" = "None"
    ) -> "_1946.RollingBearingKey":
        """mastapy._private.bearings.RollingBearingKey

        Args:
            type_ (mastapy._private.bearings.RollingBearingType)
            designation (str, optional)
        """
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        designation = str(designation)
        method_result = self.wrapped.CreateKey.Overloads[
            _ROLLING_BEARING_TYPE, _STRING
        ](type_, designation if designation else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_key_with_type_name(
        self: "Self", type_: "str", designation: "str" = "None"
    ) -> "_1946.RollingBearingKey":
        """mastapy._private.bearings.RollingBearingKey

        Args:
            type_ (str)
            designation (str, optional)
        """
        type_ = str(type_)
        designation = str(designation)
        method_result = self.wrapped.CreateKey.Overloads[_STRING, _STRING](
            type_ if type_ else "", designation if designation else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_from_database(self: "Self", bearing: "_2218.RollingBearing") -> None:
        """Method does not return.

        Args:
            bearing (mastapy._private.bearings.bearing_designs.rolling.RollingBearing)
        """
        self.wrapped.RemoveFromDatabase(bearing.wrapped if bearing else None)

    @enforce_parameter_types
    def search_for_rolling_bearing_with_catalog(
        self: "Self", catalog: "_1921.BearingCatalog"
    ) -> "List[_2218.RollingBearing]":
        """List[mastapy._private.bearings.bearing_designs.rolling.RollingBearing]

        Args:
            catalog (mastapy._private.bearings.BearingCatalog)
        """
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.SearchForRollingBearing.Overloads[_BEARING_CATALOG](catalog)
        )

    @enforce_parameter_types
    def search_for_rolling_bearing_with_name_and_catalog(
        self: "Self", designation: "str", catalog: "_1921.BearingCatalog"
    ) -> "_2218.RollingBearing":
        """mastapy._private.bearings.bearing_designs.rolling.RollingBearing

        Args:
            designation (str)
            catalog (mastapy._private.bearings.BearingCatalog)
        """
        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        method_result = self.wrapped.SearchForRollingBearing.Overloads[
            _STRING, _BEARING_CATALOG
        ](designation if designation else "", catalog)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def search_for_rolling_bearing_with_name_catalog_and_type(
        self: "Self",
        designation: "str",
        catalog: "_1921.BearingCatalog",
        type_: "_1948.RollingBearingType",
    ) -> "List[_2218.RollingBearing]":
        """List[mastapy._private.bearings.bearing_designs.rolling.RollingBearing]

        Args:
            designation (str)
            catalog (mastapy._private.bearings.BearingCatalog)
            type_ (mastapy._private.bearings.RollingBearingType)
        """
        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.SearchForRollingBearing.Overloads[
                _STRING, _BEARING_CATALOG, _ROLLING_BEARING_TYPE
            ](designation if designation else "", catalog, type_)
        )

    @enforce_parameter_types
    def search_for_rolling_bearing(
        self: "Self",
        designation: "str",
        catalog: "_1921.BearingCatalog",
        type_: "_1948.RollingBearingType",
        bore_range: "_1535.Range",
        outer_diameter_range: "_1535.Range",
        width_range: "_1535.Range",
        dynamic_capacity_range: "_1535.Range",
        number_of_rows: "int",
        material_type: "_1937.HybridSteelAll",
    ) -> "List[_2218.RollingBearing]":
        """List[mastapy._private.bearings.bearing_designs.rolling.RollingBearing]

        Args:
            designation (str)
            catalog (mastapy._private.bearings.BearingCatalog)
            type_ (mastapy._private.bearings.RollingBearingType)
            bore_range (mastapy._private.math_utility.Range)
            outer_diameter_range (mastapy._private.math_utility.Range)
            width_range (mastapy._private.math_utility.Range)
            dynamic_capacity_range (mastapy._private.math_utility.Range)
            number_of_rows (int)
            material_type (mastapy._private.bearings.HybridSteelAll)
        """
        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        number_of_rows = int(number_of_rows)
        material_type = conversion.mp_to_pn_enum(
            material_type, "SMT.MastaAPI.Bearings.HybridSteelAll"
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.SearchForRollingBearing.Overloads[
                _STRING,
                _BEARING_CATALOG,
                _ROLLING_BEARING_TYPE,
                _RANGE,
                _RANGE,
                _RANGE,
                _RANGE,
                _INT_32,
                _HYBRID_STEEL_ALL,
            ](
                designation if designation else "",
                catalog,
                type_,
                bore_range.wrapped if bore_range else None,
                outer_diameter_range.wrapped if outer_diameter_range else None,
                width_range.wrapped if width_range else None,
                dynamic_capacity_range.wrapped if dynamic_capacity_range else None,
                number_of_rows if number_of_rows else 0,
                material_type,
            )
        )

    @property
    def cast_to(self: "Self") -> "_Cast_RollingBearingDatabase":
        """Cast to another type.

        Returns:
            _Cast_RollingBearingDatabase
        """
        return _Cast_RollingBearingDatabase(self)
