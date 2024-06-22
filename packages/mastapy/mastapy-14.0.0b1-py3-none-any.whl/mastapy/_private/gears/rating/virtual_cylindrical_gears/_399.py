"""VirtualCylindricalGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.rating.virtual_cylindrical_gears import _400
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears", "VirtualCylindricalGear"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.virtual_cylindrical_gears import (
        _395,
        _396,
        _397,
        _401,
    )

    Self = TypeVar("Self", bound="VirtualCylindricalGear")
    CastSelf = TypeVar(
        "CastSelf", bound="VirtualCylindricalGear._Cast_VirtualCylindricalGear"
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_VirtualCylindricalGear:
    """Special nested class for casting VirtualCylindricalGear to subclasses."""

    __parent__: "VirtualCylindricalGear"

    @property
    def virtual_cylindrical_gear_basic(
        self: "CastSelf",
    ) -> "_400.VirtualCylindricalGearBasic":
        return self.__parent__._cast(_400.VirtualCylindricalGearBasic)

    @property
    def klingelnberg_hypoid_virtual_cylindrical_gear(
        self: "CastSelf",
    ) -> "_395.KlingelnbergHypoidVirtualCylindricalGear":
        from mastapy._private.gears.rating.virtual_cylindrical_gears import _395

        return self.__parent__._cast(_395.KlingelnbergHypoidVirtualCylindricalGear)

    @property
    def klingelnberg_spiral_bevel_virtual_cylindrical_gear(
        self: "CastSelf",
    ) -> "_396.KlingelnbergSpiralBevelVirtualCylindricalGear":
        from mastapy._private.gears.rating.virtual_cylindrical_gears import _396

        return self.__parent__._cast(_396.KlingelnbergSpiralBevelVirtualCylindricalGear)

    @property
    def klingelnberg_virtual_cylindrical_gear(
        self: "CastSelf",
    ) -> "_397.KlingelnbergVirtualCylindricalGear":
        from mastapy._private.gears.rating.virtual_cylindrical_gears import _397

        return self.__parent__._cast(_397.KlingelnbergVirtualCylindricalGear)

    @property
    def virtual_cylindrical_gear_iso10300_method_b1(
        self: "CastSelf",
    ) -> "_401.VirtualCylindricalGearISO10300MethodB1":
        from mastapy._private.gears.rating.virtual_cylindrical_gears import _401

        return self.__parent__._cast(_401.VirtualCylindricalGearISO10300MethodB1)

    @property
    def virtual_cylindrical_gear(self: "CastSelf") -> "VirtualCylindricalGear":
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
class VirtualCylindricalGear(_400.VirtualCylindricalGearBasic):
    """VirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _VIRTUAL_CYLINDRICAL_GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def base_diameter_of_virtual_cylindrical_gear(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_normal_for_virtual_cylindrical_gears(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_transverse_for_virtual_cylindrical_gears(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_of_addendum_normal_for_virtual_cylindrical_gears(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioOfAddendumNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_of_addendum_transverse_for_virtual_cylindrical_gears(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioOfAddendumTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_pressure_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectivePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def path_of_addendum_contact_normal(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PathOfAddendumContactNormal

        if temp is None:
            return 0.0

        return temp

    @property
    def path_of_addendum_contact_transverse(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PathOfAddendumContactTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_VirtualCylindricalGear":
        """Cast to another type.

        Returns:
            _Cast_VirtualCylindricalGear
        """
        return _Cast_VirtualCylindricalGear(self)
