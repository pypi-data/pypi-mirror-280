"""KlingelnbergCycloPalloidHypoidMeshedGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.gear_designs.klingelnberg_conical import _1008
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1197
    from mastapy._private.gears.gear_designs import _972

    Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidMeshedGearDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidMeshedGearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign:
    """Special nested class for casting KlingelnbergCycloPalloidHypoidMeshedGearDesign to subclasses."""

    __parent__: "KlingelnbergCycloPalloidHypoidMeshedGearDesign"

    @property
    def klingelnberg_conical_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1008.KlingelnbergConicalMeshedGearDesign":
        return self.__parent__._cast(_1008.KlingelnbergConicalMeshedGearDesign)

    @property
    def conical_meshed_gear_design(self: "CastSelf") -> "_1197.ConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.conical import _1197

        return self.__parent__._cast(_1197.ConicalMeshedGearDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
        self: "CastSelf",
    ) -> "KlingelnbergCycloPalloidHypoidMeshedGearDesign":
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
class KlingelnbergCycloPalloidHypoidMeshedGearDesign(
    _1008.KlingelnbergConicalMeshedGearDesign
):
    """KlingelnbergCycloPalloidHypoidMeshedGearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_MESHED_GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign
        """
        return _Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign(self)
