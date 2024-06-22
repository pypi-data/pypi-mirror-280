"""LoadedRollerBearingElement"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private.bearings.bearing_results.rolling import _2067
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerBearingElement"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import (
        _2120,
        _2041,
        _2046,
        _2049,
        _2057,
        _2061,
        _2073,
        _2080,
        _2091,
        _2092,
        _2098,
        _2100,
        _2109,
    )

    Self = TypeVar("Self", bound="LoadedRollerBearingElement")
    CastSelf = TypeVar(
        "CastSelf", bound="LoadedRollerBearingElement._Cast_LoadedRollerBearingElement"
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerBearingElement",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedRollerBearingElement:
    """Special nested class for casting LoadedRollerBearingElement to subclasses."""

    __parent__: "LoadedRollerBearingElement"

    @property
    def loaded_element(self: "CastSelf") -> "_2067.LoadedElement":
        return self.__parent__._cast(_2067.LoadedElement)

    @property
    def loaded_asymmetric_spherical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2041.LoadedAsymmetricSphericalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2041

        return self.__parent__._cast(
            _2041.LoadedAsymmetricSphericalRollerBearingElement
        )

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2046.LoadedAxialThrustCylindricalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2046

        return self.__parent__._cast(
            _2046.LoadedAxialThrustCylindricalRollerBearingElement
        )

    @property
    def loaded_axial_thrust_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2049.LoadedAxialThrustNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2049

        return self.__parent__._cast(_2049.LoadedAxialThrustNeedleRollerBearingElement)

    @property
    def loaded_crossed_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2057.LoadedCrossedRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2057

        return self.__parent__._cast(_2057.LoadedCrossedRollerBearingElement)

    @property
    def loaded_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2061.LoadedCylindricalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2061

        return self.__parent__._cast(_2061.LoadedCylindricalRollerBearingElement)

    @property
    def loaded_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2073.LoadedNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2073

        return self.__parent__._cast(_2073.LoadedNeedleRollerBearingElement)

    @property
    def loaded_non_barrel_roller_element(
        self: "CastSelf",
    ) -> "_2080.LoadedNonBarrelRollerElement":
        from mastapy._private.bearings.bearing_results.rolling import _2080

        return self.__parent__._cast(_2080.LoadedNonBarrelRollerElement)

    @property
    def loaded_spherical_radial_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2091.LoadedSphericalRadialRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2091

        return self.__parent__._cast(_2091.LoadedSphericalRadialRollerBearingElement)

    @property
    def loaded_spherical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2092.LoadedSphericalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2092

        return self.__parent__._cast(_2092.LoadedSphericalRollerBearingElement)

    @property
    def loaded_spherical_thrust_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2098.LoadedSphericalThrustRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2098

        return self.__parent__._cast(_2098.LoadedSphericalThrustRollerBearingElement)

    @property
    def loaded_taper_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2100.LoadedTaperRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2100

        return self.__parent__._cast(_2100.LoadedTaperRollerBearingElement)

    @property
    def loaded_toroidal_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2109.LoadedToroidalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2109

        return self.__parent__._cast(_2109.LoadedToroidalRollerBearingElement)

    @property
    def loaded_roller_bearing_element(self: "CastSelf") -> "LoadedRollerBearingElement":
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
class LoadedRollerBearingElement(_2067.LoadedElement):
    """LoadedRollerBearingElement

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_ROLLER_BEARING_ELEMENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def contact_length_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLengthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_length_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLengthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_tilt(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ElementTilt

        if temp is None:
            return 0.0

        return temp

    @element_tilt.setter
    @enforce_parameter_types
    def element_tilt(self: "Self", value: "float") -> None:
        self.wrapped.ElementTilt = float(value) if value is not None else 0.0

    @property
    def maximum_contact_width_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_width_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_depth_of_maximum_shear_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDepthOfMaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_depth_of_maximum_shear_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDepthOfMaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalEdgeStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalEdgeStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def rib_load(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def results_at_roller_offsets(self: "Self") -> "List[_2120.ResultsAtRollerOffset]":
        """List[mastapy._private.bearings.bearing_results.rolling.ResultsAtRollerOffset]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsAtRollerOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedRollerBearingElement":
        """Cast to another type.

        Returns:
            _Cast_LoadedRollerBearingElement
        """
        return _Cast_LoadedRollerBearingElement(self)
