"""DIN5480SplineJointDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.detailed_rigid_connectors.splines import _1466
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DIN5480_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "DIN5480SplineJointDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines import _1461
    from mastapy._private.detailed_rigid_connectors import _1433

    Self = TypeVar("Self", bound="DIN5480SplineJointDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="DIN5480SplineJointDesign._Cast_DIN5480SplineJointDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("DIN5480SplineJointDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DIN5480SplineJointDesign:
    """Special nested class for casting DIN5480SplineJointDesign to subclasses."""

    __parent__: "DIN5480SplineJointDesign"

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
    def din5480_spline_joint_design(self: "CastSelf") -> "DIN5480SplineJointDesign":
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
class DIN5480SplineJointDesign(_1466.StandardSplineJointDesign):
    """DIN5480SplineJointDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DIN5480_SPLINE_JOINT_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def addendum_modification_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AddendumModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @addendum_modification_factor.setter
    @enforce_parameter_types
    def addendum_modification_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AddendumModificationFactor = value

    @property
    def base_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_form_clearance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFormClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_space_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tooth_thickness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_DIN5480SplineJointDesign":
        """Cast to another type.

        Returns:
            _Cast_DIN5480SplineJointDesign
        """
        return _Cast_DIN5480SplineJointDesign(self)
