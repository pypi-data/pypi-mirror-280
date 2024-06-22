"""RingTolerance"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.bearings.tolerances import _1961
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_RING_TOLERANCE = python_net_import("SMT.MastaAPI.Bearings.Tolerances", "RingTolerance")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.tolerances import _1970, _1958, _1964, _1953

    Self = TypeVar("Self", bound="RingTolerance")
    CastSelf = TypeVar("CastSelf", bound="RingTolerance._Cast_RingTolerance")


__docformat__ = "restructuredtext en"
__all__ = ("RingTolerance",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_RingTolerance:
    """Special nested class for casting RingTolerance to subclasses."""

    __parent__: "RingTolerance"

    @property
    def interference_tolerance(self: "CastSelf") -> "_1961.InterferenceTolerance":
        return self.__parent__._cast(_1961.InterferenceTolerance)

    @property
    def bearing_connection_component(
        self: "CastSelf",
    ) -> "_1953.BearingConnectionComponent":
        from mastapy._private.bearings.tolerances import _1953

        return self.__parent__._cast(_1953.BearingConnectionComponent)

    @property
    def inner_ring_tolerance(self: "CastSelf") -> "_1958.InnerRingTolerance":
        from mastapy._private.bearings.tolerances import _1958

        return self.__parent__._cast(_1958.InnerRingTolerance)

    @property
    def outer_ring_tolerance(self: "CastSelf") -> "_1964.OuterRingTolerance":
        from mastapy._private.bearings.tolerances import _1964

        return self.__parent__._cast(_1964.OuterRingTolerance)

    @property
    def ring_tolerance(self: "CastSelf") -> "RingTolerance":
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
class RingTolerance(_1961.InterferenceTolerance):
    """RingTolerance

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _RING_TOLERANCE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def roundness_specification(self: "Self") -> "_1970.RoundnessSpecification":
        """mastapy._private.bearings.tolerances.RoundnessSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoundnessSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_RingTolerance":
        """Cast to another type.

        Returns:
            _Cast_RingTolerance
        """
        return _Cast_RingTolerance(self)
