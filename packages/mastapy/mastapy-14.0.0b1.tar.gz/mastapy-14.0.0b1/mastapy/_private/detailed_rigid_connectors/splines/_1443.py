"""GBT3478SplineJointDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.bearings.tolerances import _1962
from mastapy._private.detailed_rigid_connectors.splines import _1446
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GBT3478_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "GBT3478SplineJointDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines import _1466, _1461
    from mastapy._private.detailed_rigid_connectors import _1433

    Self = TypeVar("Self", bound="GBT3478SplineJointDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GBT3478SplineJointDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GBT3478SplineJointDesign:
    """Special nested class for casting GBT3478SplineJointDesign to subclasses."""

    __parent__: "GBT3478SplineJointDesign"

    @property
    def iso4156_spline_joint_design(
        self: "CastSelf",
    ) -> "_1446.ISO4156SplineJointDesign":
        return self.__parent__._cast(_1446.ISO4156SplineJointDesign)

    @property
    def standard_spline_joint_design(
        self: "CastSelf",
    ) -> "_1466.StandardSplineJointDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1466

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
    def gbt3478_spline_joint_design(self: "CastSelf") -> "GBT3478SplineJointDesign":
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
class GBT3478SplineJointDesign(_1446.ISO4156SplineJointDesign):
    """GBT3478SplineJointDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GBT3478_SPLINE_JOINT_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def external_minimum_major_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalMinimumMajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_standard_tolerance_grade(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ITDesignation":
        """EnumWithSelectedValue[mastapy._private.bearings.tolerances.ITDesignation]"""
        temp = self.wrapped.MajorDiameterStandardToleranceGrade

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @major_diameter_standard_tolerance_grade.setter
    @enforce_parameter_types
    def major_diameter_standard_tolerance_grade(
        self: "Self", value: "_1962.ITDesignation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MajorDiameterStandardToleranceGrade = value

    @property
    def minor_diameter_standard_tolerance_grade(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ITDesignation":
        """EnumWithSelectedValue[mastapy._private.bearings.tolerances.ITDesignation]"""
        temp = self.wrapped.MinorDiameterStandardToleranceGrade

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @minor_diameter_standard_tolerance_grade.setter
    @enforce_parameter_types
    def minor_diameter_standard_tolerance_grade(
        self: "Self", value: "_1962.ITDesignation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MinorDiameterStandardToleranceGrade = value

    @property
    def cast_to(self: "Self") -> "_Cast_GBT3478SplineJointDesign":
        """Cast to another type.

        Returns:
            _Cast_GBT3478SplineJointDesign
        """
        return _Cast_GBT3478SplineJointDesign(self)
