"""BoltedJointMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.materials import _280
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BOLTED_JOINT_MATERIAL = python_net_import("SMT.MastaAPI.Bolts", "BoltedJointMaterial")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.math_utility import _1581
    from mastapy._private.bolts import _1516
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="BoltedJointMaterial")
    CastSelf = TypeVar(
        "CastSelf", bound="BoltedJointMaterial._Cast_BoltedJointMaterial"
    )


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointMaterial",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BoltedJointMaterial:
    """Special nested class for casting BoltedJointMaterial to subclasses."""

    __parent__: "BoltedJointMaterial"

    @property
    def material(self: "CastSelf") -> "_280.Material":
        return self.__parent__._cast(_280.Material)

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        from mastapy._private.utility.databases import _1879

        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def bolt_material(self: "CastSelf") -> "_1516.BoltMaterial":
        from mastapy._private.bolts import _1516

        return self.__parent__._cast(_1516.BoltMaterial)

    @property
    def bolted_joint_material(self: "CastSelf") -> "BoltedJointMaterial":
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
class BoltedJointMaterial(_280.Material):
    """BoltedJointMaterial

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BOLTED_JOINT_MATERIAL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def coefficient_of_thermal_expansion_at_20c(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfThermalExpansionAt20C

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_thermal_expansion_at_20c.setter
    @enforce_parameter_types
    def coefficient_of_thermal_expansion_at_20c(self: "Self", value: "float") -> None:
        self.wrapped.CoefficientOfThermalExpansionAt20C = (
            float(value) if value is not None else 0.0
        )

    @property
    def limiting_surface_pressure(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LimitingSurfacePressure

        if temp is None:
            return 0.0

        return temp

    @limiting_surface_pressure.setter
    @enforce_parameter_types
    def limiting_surface_pressure(self: "Self", value: "float") -> None:
        self.wrapped.LimitingSurfacePressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_tensile_strength(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumTensileStrength

        if temp is None:
            return 0.0

        return temp

    @minimum_tensile_strength.setter
    @enforce_parameter_types
    def minimum_tensile_strength(self: "Self", value: "float") -> None:
        self.wrapped.MinimumTensileStrength = float(value) if value is not None else 0.0

    @property
    def modulus_of_elasticity_at_20c(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ModulusOfElasticityAt20C

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity_at_20c.setter
    @enforce_parameter_types
    def modulus_of_elasticity_at_20c(self: "Self", value: "float") -> None:
        self.wrapped.ModulusOfElasticityAt20C = (
            float(value) if value is not None else 0.0
        )

    @property
    def proof_stress(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    @enforce_parameter_types
    def proof_stress(self: "Self", value: "float") -> None:
        self.wrapped.ProofStress = float(value) if value is not None else 0.0

    @property
    def shearing_strength(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShearingStrength

        if temp is None:
            return 0.0

        return temp

    @shearing_strength.setter
    @enforce_parameter_types
    def shearing_strength(self: "Self", value: "float") -> None:
        self.wrapped.ShearingStrength = float(value) if value is not None else 0.0

    @property
    def stress_endurance_limit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StressEnduranceLimit

        if temp is None:
            return 0.0

        return temp

    @stress_endurance_limit.setter
    @enforce_parameter_types
    def stress_endurance_limit(self: "Self", value: "float") -> None:
        self.wrapped.StressEnduranceLimit = float(value) if value is not None else 0.0

    @property
    def temperature_dependent_coefficient_of_thermal_expansion(
        self: "Self",
    ) -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TemperatureDependentCoefficientOfThermalExpansion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @temperature_dependent_coefficient_of_thermal_expansion.setter
    @enforce_parameter_types
    def temperature_dependent_coefficient_of_thermal_expansion(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.TemperatureDependentCoefficientOfThermalExpansion = value.wrapped

    @property
    def temperature_dependent_youngs_moduli(
        self: "Self",
    ) -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TemperatureDependentYoungsModuli

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @temperature_dependent_youngs_moduli.setter
    @enforce_parameter_types
    def temperature_dependent_youngs_moduli(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.TemperatureDependentYoungsModuli = value.wrapped

    @property
    def cast_to(self: "Self") -> "_Cast_BoltedJointMaterial":
        """Cast to another type.

        Returns:
            _Cast_BoltedJointMaterial
        """
        return _Cast_BoltedJointMaterial(self)
