"""OuterRingTolerance"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.bearings.tolerances import _1969
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_OUTER_RING_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "OuterRingTolerance"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.tolerances import _1961, _1953

    Self = TypeVar("Self", bound="OuterRingTolerance")
    CastSelf = TypeVar("CastSelf", bound="OuterRingTolerance._Cast_OuterRingTolerance")


__docformat__ = "restructuredtext en"
__all__ = ("OuterRingTolerance",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_OuterRingTolerance:
    """Special nested class for casting OuterRingTolerance to subclasses."""

    __parent__: "OuterRingTolerance"

    @property
    def ring_tolerance(self: "CastSelf") -> "_1969.RingTolerance":
        return self.__parent__._cast(_1969.RingTolerance)

    @property
    def interference_tolerance(self: "CastSelf") -> "_1961.InterferenceTolerance":
        from mastapy._private.bearings.tolerances import _1961

        return self.__parent__._cast(_1961.InterferenceTolerance)

    @property
    def bearing_connection_component(
        self: "CastSelf",
    ) -> "_1953.BearingConnectionComponent":
        from mastapy._private.bearings.tolerances import _1953

        return self.__parent__._cast(_1953.BearingConnectionComponent)

    @property
    def outer_ring_tolerance(self: "CastSelf") -> "OuterRingTolerance":
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
class OuterRingTolerance(_1969.RingTolerance):
    """OuterRingTolerance

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _OUTER_RING_TOLERANCE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_OuterRingTolerance":
        """Cast to another type.

        Returns:
            _Cast_OuterRingTolerance
        """
        return _Cast_OuterRingTolerance(self)
