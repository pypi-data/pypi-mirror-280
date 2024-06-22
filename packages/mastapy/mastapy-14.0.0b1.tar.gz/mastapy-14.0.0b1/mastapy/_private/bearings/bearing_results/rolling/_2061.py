"""LoadedCylindricalRollerBearingElement"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.bearings.bearing_results.rolling import _2080
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedCylindricalRollerBearingElement",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import _2073, _2081, _2067

    Self = TypeVar("Self", bound="LoadedCylindricalRollerBearingElement")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCylindricalRollerBearingElement",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedCylindricalRollerBearingElement:
    """Special nested class for casting LoadedCylindricalRollerBearingElement to subclasses."""

    __parent__: "LoadedCylindricalRollerBearingElement"

    @property
    def loaded_non_barrel_roller_element(
        self: "CastSelf",
    ) -> "_2080.LoadedNonBarrelRollerElement":
        return self.__parent__._cast(_2080.LoadedNonBarrelRollerElement)

    @property
    def loaded_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2081.LoadedRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2081

        return self.__parent__._cast(_2081.LoadedRollerBearingElement)

    @property
    def loaded_element(self: "CastSelf") -> "_2067.LoadedElement":
        from mastapy._private.bearings.bearing_results.rolling import _2067

        return self.__parent__._cast(_2067.LoadedElement)

    @property
    def loaded_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2073.LoadedNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2073

        return self.__parent__._cast(_2073.LoadedNeedleRollerBearingElement)

    @property
    def loaded_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "LoadedCylindricalRollerBearingElement":
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
class LoadedCylindricalRollerBearingElement(_2080.LoadedNonBarrelRollerElement):
    """LoadedCylindricalRollerBearingElement

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_CYLINDRICAL_ROLLER_BEARING_ELEMENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def height_of_rib_roller_contact_above_race_inner_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_inner_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_outer_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_outer_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_inner_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_inner_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_outer_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_outer_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedCylindricalRollerBearingElement":
        """Cast to another type.

        Returns:
            _Cast_LoadedCylindricalRollerBearingElement
        """
        return _Cast_LoadedCylindricalRollerBearingElement(self)
