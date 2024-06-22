"""ISO6336RateableMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.rating.cylindrical import _482
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO6336_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO6336RateableMesh"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.cylindrical import _489
    from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import (
        _504,
        _509,
        _510,
        _511,
    )
    from mastapy._private.gears.rating.cylindrical.iso6336 import _533
    from mastapy._private.gears.rating import _378

    Self = TypeVar("Self", bound="ISO6336RateableMesh")
    CastSelf = TypeVar(
        "CastSelf", bound="ISO6336RateableMesh._Cast_ISO6336RateableMesh"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336RateableMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISO6336RateableMesh:
    """Special nested class for casting ISO6336RateableMesh to subclasses."""

    __parent__: "ISO6336RateableMesh"

    @property
    def cylindrical_rateable_mesh(self: "CastSelf") -> "_482.CylindricalRateableMesh":
        return self.__parent__._cast(_482.CylindricalRateableMesh)

    @property
    def rateable_mesh(self: "CastSelf") -> "_378.RateableMesh":
        from mastapy._private.gears.rating import _378

        return self.__parent__._cast(_378.RateableMesh)

    @property
    def plastic_gear_vdi2736_abstract_rateable_mesh(
        self: "CastSelf",
    ) -> "_504.PlasticGearVDI2736AbstractRateableMesh":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _504

        return self.__parent__._cast(_504.PlasticGearVDI2736AbstractRateableMesh)

    @property
    def vdi2736_metal_plastic_rateable_mesh(
        self: "CastSelf",
    ) -> "_509.VDI2736MetalPlasticRateableMesh":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _509

        return self.__parent__._cast(_509.VDI2736MetalPlasticRateableMesh)

    @property
    def vdi2736_plastic_metal_rateable_mesh(
        self: "CastSelf",
    ) -> "_510.VDI2736PlasticMetalRateableMesh":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _510

        return self.__parent__._cast(_510.VDI2736PlasticMetalRateableMesh)

    @property
    def vdi2736_plastic_plastic_rateable_mesh(
        self: "CastSelf",
    ) -> "_511.VDI2736PlasticPlasticRateableMesh":
        from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import _511

        return self.__parent__._cast(_511.VDI2736PlasticPlasticRateableMesh)

    @property
    def iso6336_metal_rateable_mesh(
        self: "CastSelf",
    ) -> "_533.ISO6336MetalRateableMesh":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _533

        return self.__parent__._cast(_533.ISO6336MetalRateableMesh)

    @property
    def iso6336_rateable_mesh(self: "CastSelf") -> "ISO6336RateableMesh":
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
class ISO6336RateableMesh(_482.CylindricalRateableMesh):
    """ISO6336RateableMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO6336_RATEABLE_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def misalignment_contact_pattern_enhancement(
        self: "Self",
    ) -> "_489.MisalignmentContactPatternEnhancements":
        """mastapy._private.gears.rating.cylindrical.MisalignmentContactPatternEnhancements"""
        temp = self.wrapped.MisalignmentContactPatternEnhancement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating.cylindrical._489",
            "MisalignmentContactPatternEnhancements",
        )(value)

    @misalignment_contact_pattern_enhancement.setter
    @enforce_parameter_types
    def misalignment_contact_pattern_enhancement(
        self: "Self", value: "_489.MisalignmentContactPatternEnhancements"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )
        self.wrapped.MisalignmentContactPatternEnhancement = value

    @property
    def cast_to(self: "Self") -> "_Cast_ISO6336RateableMesh":
        """Cast to another type.

        Returns:
            _Cast_ISO6336RateableMesh
        """
        return _Cast_ISO6336RateableMesh(self)
