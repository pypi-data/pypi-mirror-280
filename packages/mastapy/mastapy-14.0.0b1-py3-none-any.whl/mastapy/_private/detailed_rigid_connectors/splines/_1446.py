"""ISO4156SplineJointDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.detailed_rigid_connectors.splines import _1466
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO4156_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "ISO4156SplineJointDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines import _1443, _1447, _1461
    from mastapy._private.detailed_rigid_connectors import _1433

    Self = TypeVar("Self", bound="ISO4156SplineJointDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO4156SplineJointDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISO4156SplineJointDesign:
    """Special nested class for casting ISO4156SplineJointDesign to subclasses."""

    __parent__: "ISO4156SplineJointDesign"

    @property
    def standard_spline_joint_design(
        self: "CastSelf",
    ) -> "_1466.StandardSplineJointDesign":
        return self.__parent__._cast(_1466.StandardSplineJointDesign)

    @property
    def spline_joint_design(self: "CastSelf") -> "_1461.SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1461

        return self.__parent__._cast(_1461.SplineJointDesign)

    @property
    def detailed_rigid_connector_design(
        self: "CastSelf",
    ) -> "_1433.DetailedRigidConnectorDesign":
        from mastapy._private.detailed_rigid_connectors import _1433

        return self.__parent__._cast(_1433.DetailedRigidConnectorDesign)

    @property
    def gbt3478_spline_joint_design(
        self: "CastSelf",
    ) -> "_1443.GBT3478SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1443

        return self.__parent__._cast(_1443.GBT3478SplineJointDesign)

    @property
    def jisb1603_spline_joint_design(
        self: "CastSelf",
    ) -> "_1447.JISB1603SplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1447

        return self.__parent__._cast(_1447.JISB1603SplineJointDesign)

    @property
    def iso4156_spline_joint_design(self: "CastSelf") -> "ISO4156SplineJointDesign":
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
class ISO4156SplineJointDesign(_1466.StandardSplineJointDesign):
    """ISO4156SplineJointDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO4156_SPLINE_JOINT_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def form_clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_effective_clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_ISO4156SplineJointDesign":
        """Cast to another type.

        Returns:
            _Cast_ISO4156SplineJointDesign
        """
        return _Cast_ISO4156SplineJointDesign(self)
