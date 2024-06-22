"""ISO4156SplineHalfDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.detailed_rigid_connectors.splines import _1465
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO4156_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "ISO4156SplineHalfDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines import _1442, _1460
    from mastapy._private.detailed_rigid_connectors import _1434

    Self = TypeVar("Self", bound="ISO4156SplineHalfDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO4156SplineHalfDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISO4156SplineHalfDesign:
    """Special nested class for casting ISO4156SplineHalfDesign to subclasses."""

    __parent__: "ISO4156SplineHalfDesign"

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
    def gbt3478_spline_half_design(self: "CastSelf") -> "_1442.GBT3478SplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1442

        return self.__parent__._cast(_1442.GBT3478SplineHalfDesign)

    @property
    def iso4156_spline_half_design(self: "CastSelf") -> "ISO4156SplineHalfDesign":
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
class ISO4156SplineHalfDesign(_1465.StandardSplineHalfDesign):
    """ISO4156SplineHalfDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO4156_SPLINE_HALF_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def minimum_maximum_form_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMaximumFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_addendum_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_dedendum_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackDedendumFactor

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
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

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
    def maximum_minor_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMinorDiameter

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
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

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
    def minimum_minor_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMinorDiameter

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
    def cast_to(self: "Self") -> "_Cast_ISO4156SplineHalfDesign":
        """Cast to another type.

        Returns:
            _Cast_ISO4156SplineHalfDesign
        """
        return _Cast_ISO4156SplineHalfDesign(self)
