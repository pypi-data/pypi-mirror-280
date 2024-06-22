"""CylindricalRateableMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.rating import _378
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_CYLINDRICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalRateableMesh"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import (
        _504,
        _509,
        _510,
        _511,
    )
    from mastapy._private.gears.rating.cylindrical.iso6336 import _533, _534
    from mastapy._private.gears.rating.cylindrical.agma import _547

    Self = TypeVar("Self", bound="CylindricalRateableMesh")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalRateableMesh._Cast_CylindricalRateableMesh"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalRateableMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalRateableMesh:
    """Special nested class for casting CylindricalRateableMesh to subclasses."""

    __parent__: "CylindricalRateableMesh"

    @property
    def rateable_mesh(self: "CastSelf") -> "_378.RateableMesh":
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
    def iso6336_rateable_mesh(self: "CastSelf") -> "_534.ISO6336RateableMesh":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _534

        return self.__parent__._cast(_534.ISO6336RateableMesh)

    @property
    def agma2101_rateable_mesh(self: "CastSelf") -> "_547.AGMA2101RateableMesh":
        from mastapy._private.gears.rating.cylindrical.agma import _547

        return self.__parent__._cast(_547.AGMA2101RateableMesh)

    @property
    def cylindrical_rateable_mesh(self: "CastSelf") -> "CylindricalRateableMesh":
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
class CylindricalRateableMesh(_378.RateableMesh):
    """CylindricalRateableMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_RATEABLE_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalRateableMesh":
        """Cast to another type.

        Returns:
            _Cast_CylindricalRateableMesh
        """
        return _Cast_CylindricalRateableMesh(self)
