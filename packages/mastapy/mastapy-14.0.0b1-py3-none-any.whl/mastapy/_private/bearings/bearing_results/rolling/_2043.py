"""LoadedAsymmetricSphericalRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.bearings.bearing_results.rolling import _2083
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAsymmetricSphericalRollerBearingRow",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import _2042, _2087

    Self = TypeVar("Self", bound="LoadedAsymmetricSphericalRollerBearingRow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedAsymmetricSphericalRollerBearingRow._Cast_LoadedAsymmetricSphericalRollerBearingRow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAsymmetricSphericalRollerBearingRow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedAsymmetricSphericalRollerBearingRow:
    """Special nested class for casting LoadedAsymmetricSphericalRollerBearingRow to subclasses."""

    __parent__: "LoadedAsymmetricSphericalRollerBearingRow"

    @property
    def loaded_roller_bearing_row(self: "CastSelf") -> "_2083.LoadedRollerBearingRow":
        return self.__parent__._cast(_2083.LoadedRollerBearingRow)

    @property
    def loaded_rolling_bearing_row(self: "CastSelf") -> "_2087.LoadedRollingBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2087

        return self.__parent__._cast(_2087.LoadedRollingBearingRow)

    @property
    def loaded_asymmetric_spherical_roller_bearing_row(
        self: "CastSelf",
    ) -> "LoadedAsymmetricSphericalRollerBearingRow":
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
class LoadedAsymmetricSphericalRollerBearingRow(_2083.LoadedRollerBearingRow):
    """LoadedAsymmetricSphericalRollerBearingRow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_ROW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def loaded_bearing(
        self: "Self",
    ) -> "_2042.LoadedAsymmetricSphericalRollerBearingResults":
        """mastapy._private.bearings.bearing_results.rolling.LoadedAsymmetricSphericalRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedAsymmetricSphericalRollerBearingRow":
        """Cast to another type.

        Returns:
            _Cast_LoadedAsymmetricSphericalRollerBearingRow
        """
        return _Cast_LoadedAsymmetricSphericalRollerBearingRow(self)
