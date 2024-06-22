"""BiasModification"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.gears.micro_geometry import _590
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BIAS_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "BiasModification"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1125
    from mastapy._private.gears.gear_designs.conical.micro_geometry import _1210

    Self = TypeVar("Self", bound="BiasModification")
    CastSelf = TypeVar("CastSelf", bound="BiasModification._Cast_BiasModification")


__docformat__ = "restructuredtext en"
__all__ = ("BiasModification",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BiasModification:
    """Special nested class for casting BiasModification to subclasses."""

    __parent__: "BiasModification"

    @property
    def modification(self: "CastSelf") -> "_590.Modification":
        return self.__parent__._cast(_590.Modification)

    @property
    def cylindrical_gear_bias_modification(
        self: "CastSelf",
    ) -> "_1125.CylindricalGearBiasModification":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1125

        return self.__parent__._cast(_1125.CylindricalGearBiasModification)

    @property
    def conical_gear_bias_modification(
        self: "CastSelf",
    ) -> "_1210.ConicalGearBiasModification":
        from mastapy._private.gears.gear_designs.conical.micro_geometry import _1210

        return self.__parent__._cast(_1210.ConicalGearBiasModification)

    @property
    def bias_modification(self: "CastSelf") -> "BiasModification":
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
class BiasModification(_590.Modification):
    """BiasModification

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BIAS_MODIFICATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def lead_evaluation_left_limit_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LeadEvaluationLeftLimitFactor

        if temp is None:
            return 0.0

        return temp

    @lead_evaluation_left_limit_factor.setter
    @enforce_parameter_types
    def lead_evaluation_left_limit_factor(self: "Self", value: "float") -> None:
        self.wrapped.LeadEvaluationLeftLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def lead_evaluation_right_limit_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LeadEvaluationRightLimitFactor

        if temp is None:
            return 0.0

        return temp

    @lead_evaluation_right_limit_factor.setter
    @enforce_parameter_types
    def lead_evaluation_right_limit_factor(self: "Self", value: "float") -> None:
        self.wrapped.LeadEvaluationRightLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimitFactor

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit_factor.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit_factor(self: "Self", value: "float") -> None:
        self.wrapped.ProfileEvaluationLowerLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimitFactor

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit_factor.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit_factor(self: "Self", value: "float") -> None:
        self.wrapped.ProfileEvaluationUpperLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_factor_for_0_bias_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProfileFactorFor0BiasRelief

        if temp is None:
            return 0.0

        return temp

    @profile_factor_for_0_bias_relief.setter
    @enforce_parameter_types
    def profile_factor_for_0_bias_relief(self: "Self", value: "float") -> None:
        self.wrapped.ProfileFactorFor0BiasRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def relief_at_left_limit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ReliefAtLeftLimit

        if temp is None:
            return 0.0

        return temp

    @relief_at_left_limit.setter
    @enforce_parameter_types
    def relief_at_left_limit(self: "Self", value: "float") -> None:
        self.wrapped.ReliefAtLeftLimit = float(value) if value is not None else 0.0

    @property
    def relief_at_right_limit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ReliefAtRightLimit

        if temp is None:
            return 0.0

        return temp

    @relief_at_right_limit.setter
    @enforce_parameter_types
    def relief_at_right_limit(self: "Self", value: "float") -> None:
        self.wrapped.ReliefAtRightLimit = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_BiasModification":
        """Cast to another type.

        Returns:
            _Cast_BiasModification
        """
        return _Cast_BiasModification(self)
