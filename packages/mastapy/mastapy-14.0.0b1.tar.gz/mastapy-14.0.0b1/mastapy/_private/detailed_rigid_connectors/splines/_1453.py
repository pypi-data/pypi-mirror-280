"""SAESplineHalfDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.detailed_rigid_connectors.splines import _1465
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SAE_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SAESplineHalfDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines.tolerances_and_deviations import (
        _1468,
    )
    from mastapy._private.detailed_rigid_connectors.splines import _1460
    from mastapy._private.detailed_rigid_connectors import _1434

    Self = TypeVar("Self", bound="SAESplineHalfDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="SAESplineHalfDesign._Cast_SAESplineHalfDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("SAESplineHalfDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SAESplineHalfDesign:
    """Special nested class for casting SAESplineHalfDesign to subclasses."""

    __parent__: "SAESplineHalfDesign"

    @property
    def standard_spline_half_design(
        self: "CastSelf",
    ) -> "_1465.StandardSplineHalfDesign":
        return self.__parent__._cast(_1465.StandardSplineHalfDesign)

    @property
    def spline_half_design(self: "CastSelf") -> "_1460.SplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1460

        return self.__parent__._cast(_1460.SplineHalfDesign)

    @property
    def detailed_rigid_connector_half_design(
        self: "CastSelf",
    ) -> "_1434.DetailedRigidConnectorHalfDesign":
        from mastapy._private.detailed_rigid_connectors import _1434

        return self.__parent__._cast(_1434.DetailedRigidConnectorHalfDesign)

    @property
    def sae_spline_half_design(self: "CastSelf") -> "SAESplineHalfDesign":
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
class SAESplineHalfDesign(_1465.StandardSplineHalfDesign):
    """SAESplineHalfDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SAE_SPLINE_HALF_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def change_in_root_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def form_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_actual_space_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumActualSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @maximum_actual_space_width.setter
    @enforce_parameter_types
    def maximum_actual_space_width(self: "Self", value: "float") -> None:
        self.wrapped.MaximumActualSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_actual_tooth_thickness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumActualToothThickness

        if temp is None:
            return 0.0

        return temp

    @maximum_actual_tooth_thickness.setter
    @enforce_parameter_types
    def maximum_actual_tooth_thickness(self: "Self", value: "float") -> None:
        self.wrapped.MaximumActualToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_dimension_over_balls(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

    @maximum_dimension_over_balls.setter
    @enforce_parameter_types
    def maximum_dimension_over_balls(self: "Self", value: "float") -> None:
        self.wrapped.MaximumDimensionOverBalls = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_effective_space_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_tooth_thickness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumEffectiveToothThickness

        if temp is None:
            return 0.0

        return temp

    @maximum_effective_tooth_thickness.setter
    @enforce_parameter_types
    def maximum_effective_tooth_thickness(self: "Self", value: "float") -> None:
        self.wrapped.MaximumEffectiveToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_major_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_actual_space_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumActualSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @minimum_actual_space_width.setter
    @enforce_parameter_types
    def minimum_actual_space_width(self: "Self", value: "float") -> None:
        self.wrapped.MinimumActualSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_actual_tooth_thickness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumActualToothThickness

        if temp is None:
            return 0.0

        return temp

    @minimum_actual_tooth_thickness.setter
    @enforce_parameter_types
    def minimum_actual_tooth_thickness(self: "Self", value: "float") -> None:
        self.wrapped.MinimumActualToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_dimension_over_balls(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

    @minimum_dimension_over_balls.setter
    @enforce_parameter_types
    def minimum_dimension_over_balls(self: "Self", value: "float") -> None:
        self.wrapped.MinimumDimensionOverBalls = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_effective_space_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumEffectiveSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @minimum_effective_space_width.setter
    @enforce_parameter_types
    def minimum_effective_space_width(self: "Self", value: "float") -> None:
        self.wrapped.MinimumEffectiveSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_effective_tooth_thickness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_major_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RootFilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @root_fillet_radius_factor.setter
    @enforce_parameter_types
    def root_fillet_radius_factor(self: "Self", value: "float") -> None:
        self.wrapped.RootFilletRadiusFactor = float(value) if value is not None else 0.0

    @property
    def sae_accuracy_and_tolerance(self: "Self") -> "_1468.SAESplineTolerances":
        """mastapy._private.detailed_rigid_connectors.splines.tolerances_and_deviations.SAESplineTolerances

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SAEAccuracyAndTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SAESplineHalfDesign":
        """Cast to another type.

        Returns:
            _Cast_SAESplineHalfDesign
        """
        return _Cast_SAESplineHalfDesign(self)
