"""LoadedNonBarrelRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from PIL.Image import Image

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.bearings.bearing_results.rolling import _2083
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNonBarrelRollerBearingRow"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import (
        _2077,
        _2048,
        _2051,
        _2063,
        _2075,
        _2102,
        _2087,
    )

    Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingRow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingRow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedNonBarrelRollerBearingRow:
    """Special nested class for casting LoadedNonBarrelRollerBearingRow to subclasses."""

    __parent__: "LoadedNonBarrelRollerBearingRow"

    @property
    def loaded_roller_bearing_row(self: "CastSelf") -> "_2083.LoadedRollerBearingRow":
        return self.__parent__._cast(_2083.LoadedRollerBearingRow)

    @property
    def loaded_rolling_bearing_row(self: "CastSelf") -> "_2087.LoadedRollingBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2087

        return self.__parent__._cast(_2087.LoadedRollingBearingRow)

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2048.LoadedAxialThrustCylindricalRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2048

        return self.__parent__._cast(_2048.LoadedAxialThrustCylindricalRollerBearingRow)

    @property
    def loaded_axial_thrust_needle_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2051.LoadedAxialThrustNeedleRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2051

        return self.__parent__._cast(_2051.LoadedAxialThrustNeedleRollerBearingRow)

    @property
    def loaded_cylindrical_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2063.LoadedCylindricalRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2063

        return self.__parent__._cast(_2063.LoadedCylindricalRollerBearingRow)

    @property
    def loaded_needle_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2075.LoadedNeedleRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2075

        return self.__parent__._cast(_2075.LoadedNeedleRollerBearingRow)

    @property
    def loaded_taper_roller_bearing_row(
        self: "CastSelf",
    ) -> "_2102.LoadedTaperRollerBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2102

        return self.__parent__._cast(_2102.LoadedTaperRollerBearingRow)

    @property
    def loaded_non_barrel_roller_bearing_row(
        self: "CastSelf",
    ) -> "LoadedNonBarrelRollerBearingRow":
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
class LoadedNonBarrelRollerBearingRow(_2083.LoadedRollerBearingRow):
    """LoadedNonBarrelRollerBearingRow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_NON_BARREL_ROLLER_BEARING_ROW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def rib_normal_contact_stress_inner_left(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressInnerLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_inner_right(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressInnerRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_outer_left(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressOuterLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_outer_right(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressOuterRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def loaded_bearing(self: "Self") -> "_2077.LoadedNonBarrelRollerBearingResults":
        """mastapy._private.bearings.bearing_results.rolling.LoadedNonBarrelRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedNonBarrelRollerBearingRow":
        """Cast to another type.

        Returns:
            _Cast_LoadedNonBarrelRollerBearingRow
        """
        return _Cast_LoadedNonBarrelRollerBearingRow(self)
