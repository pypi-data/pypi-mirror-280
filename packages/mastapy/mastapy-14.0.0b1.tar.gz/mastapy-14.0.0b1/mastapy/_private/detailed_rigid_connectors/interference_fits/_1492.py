"""InterferenceFitHalfDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.detailed_rigid_connectors import _1434
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_INTERFERENCE_FIT_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits", "InterferenceFitHalfDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.detailed_rigid_connectors.interference_fits import _1493
    from mastapy._private.bearings.tolerances import _1974
    from mastapy._private.detailed_rigid_connectors.keyed_joints import _1485

    Self = TypeVar("Self", bound="InterferenceFitHalfDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceFitHalfDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterferenceFitHalfDesign:
    """Special nested class for casting InterferenceFitHalfDesign to subclasses."""

    __parent__: "InterferenceFitHalfDesign"

    @property
    def detailed_rigid_connector_half_design(
        self: "CastSelf",
    ) -> "_1434.DetailedRigidConnectorHalfDesign":
        return self.__parent__._cast(_1434.DetailedRigidConnectorHalfDesign)

    @property
    def keyway_joint_half_design(self: "CastSelf") -> "_1485.KeywayJointHalfDesign":
        from mastapy._private.detailed_rigid_connectors.keyed_joints import _1485

        return self.__parent__._cast(_1485.KeywayJointHalfDesign)

    @property
    def interference_fit_half_design(self: "CastSelf") -> "InterferenceFitHalfDesign":
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
class InterferenceFitHalfDesign(_1434.DetailedRigidConnectorHalfDesign):
    """InterferenceFitHalfDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _INTERFERENCE_FIT_HALF_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def average_joint_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageJointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def average_surface_roughness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AverageSurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @average_surface_roughness.setter
    @enforce_parameter_types
    def average_surface_roughness(self: "Self", value: "float") -> None:
        self.wrapped.AverageSurfaceRoughness = (
            float(value) if value is not None else 0.0
        )

    @property
    def designation(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Designation

        if temp is None:
            return ""

        return temp

    @property
    def diameter_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def joint_pressure_for_fully_plastic_part(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JointPressureForFullyPlasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def lower_deviation(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowerDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def nominal_joint_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NominalJointDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @nominal_joint_diameter.setter
    @enforce_parameter_types
    def nominal_joint_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NominalJointDiameter = value

    @property
    def permissible_joint_pressure_for_fully_elastic_part(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleJointPressureForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_relative_interference_for_fully_elastic_part(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleRelativeInterferenceForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_against_plastic_strain(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyAgainstPlasticStrain

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_against_plastic_strain.setter
    @enforce_parameter_types
    def required_safety_against_plastic_strain(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyAgainstPlasticStrain = value

    @property
    def stress_region(self: "Self") -> "_1493.StressRegions":
        """mastapy._private.detailed_rigid_connectors.interference_fits.StressRegions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressRegion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.StressRegions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.detailed_rigid_connectors.interference_fits._1493",
            "StressRegions",
        )(value)

    @property
    def upper_deviation(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpperDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def tolerance(self: "Self") -> "_1974.SupportTolerance":
        """mastapy._private.bearings.tolerances.SupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Tolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_InterferenceFitHalfDesign":
        """Cast to another type.

        Returns:
            _Cast_InterferenceFitHalfDesign
        """
        return _Cast_InterferenceFitHalfDesign(self)
