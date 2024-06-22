"""RateableMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_RATEABLE_MESH = python_net_import("SMT.MastaAPI.Gears.Rating", "RateableMesh")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.klingelnberg_conical.kn3030 import _426
    from mastapy._private.gears.rating.iso_10300 import _438
    from mastapy._private.gears.rating.hypoid.standards import _455
    from mastapy._private.gears.rating.cylindrical import _482
    from mastapy._private.gears.rating.cylindrical.plastic_vdi2736 import (
        _504,
        _509,
        _510,
        _511,
    )
    from mastapy._private.gears.rating.cylindrical.iso6336 import _533, _534
    from mastapy._private.gears.rating.cylindrical.agma import _547
    from mastapy._private.gears.rating.conical import _558
    from mastapy._private.gears.rating.bevel.standards import _575
    from mastapy._private.gears.rating.agma_gleason_conical import _579

    Self = TypeVar("Self", bound="RateableMesh")
    CastSelf = TypeVar("CastSelf", bound="RateableMesh._Cast_RateableMesh")


__docformat__ = "restructuredtext en"
__all__ = ("RateableMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_RateableMesh:
    """Special nested class for casting RateableMesh to subclasses."""

    __parent__: "RateableMesh"

    @property
    def klingelnberg_conical_rateable_mesh(
        self: "CastSelf",
    ) -> "_426.KlingelnbergConicalRateableMesh":
        from mastapy._private.gears.rating.klingelnberg_conical.kn3030 import _426

        return self.__parent__._cast(_426.KlingelnbergConicalRateableMesh)

    @property
    def iso10300_rateable_mesh(self: "CastSelf") -> "_438.ISO10300RateableMesh":
        from mastapy._private.gears.rating.iso_10300 import _438

        return self.__parent__._cast(_438.ISO10300RateableMesh)

    @property
    def hypoid_rateable_mesh(self: "CastSelf") -> "_455.HypoidRateableMesh":
        from mastapy._private.gears.rating.hypoid.standards import _455

        return self.__parent__._cast(_455.HypoidRateableMesh)

    @property
    def cylindrical_rateable_mesh(self: "CastSelf") -> "_482.CylindricalRateableMesh":
        from mastapy._private.gears.rating.cylindrical import _482

        return self.__parent__._cast(_482.CylindricalRateableMesh)

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
    def conical_rateable_mesh(self: "CastSelf") -> "_558.ConicalRateableMesh":
        from mastapy._private.gears.rating.conical import _558

        return self.__parent__._cast(_558.ConicalRateableMesh)

    @property
    def spiral_bevel_rateable_mesh(self: "CastSelf") -> "_575.SpiralBevelRateableMesh":
        from mastapy._private.gears.rating.bevel.standards import _575

        return self.__parent__._cast(_575.SpiralBevelRateableMesh)

    @property
    def agma_gleason_conical_rateable_mesh(
        self: "CastSelf",
    ) -> "_579.AGMAGleasonConicalRateableMesh":
        from mastapy._private.gears.rating.agma_gleason_conical import _579

        return self.__parent__._cast(_579.AGMAGleasonConicalRateableMesh)

    @property
    def rateable_mesh(self: "CastSelf") -> "RateableMesh":
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
class RateableMesh(_0.APIBase):
    """RateableMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _RATEABLE_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_RateableMesh":
        """Cast to another type.

        Returns:
            _Cast_RateableMesh
        """
        return _Cast_RateableMesh(self)
