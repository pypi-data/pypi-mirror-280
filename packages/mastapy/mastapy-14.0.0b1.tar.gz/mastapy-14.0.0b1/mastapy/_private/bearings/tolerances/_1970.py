"""RoundnessSpecification"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility import _1633
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ROUNDNESS_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "RoundnessSpecification"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bearings.tolerances import _1971, _1977, _1967
    from mastapy._private.math_utility import _1581

    Self = TypeVar("Self", bound="RoundnessSpecification")
    CastSelf = TypeVar(
        "CastSelf", bound="RoundnessSpecification._Cast_RoundnessSpecification"
    )


__docformat__ = "restructuredtext en"
__all__ = ("RoundnessSpecification",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_RoundnessSpecification:
    """Special nested class for casting RoundnessSpecification to subclasses."""

    __parent__: "RoundnessSpecification"

    @property
    def independent_reportable_properties_base(
        self: "CastSelf",
    ) -> "_1633.IndependentReportablePropertiesBase":
        pass

        return self.__parent__._cast(_1633.IndependentReportablePropertiesBase)

    @property
    def roundness_specification(self: "CastSelf") -> "RoundnessSpecification":
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
class RoundnessSpecification(
    _1633.IndependentReportablePropertiesBase["RoundnessSpecification"]
):
    """RoundnessSpecification

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ROUNDNESS_SPECIFICATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle_of_first_max_deviation_from_round(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AngleOfFirstMaxDeviationFromRound

        if temp is None:
            return 0.0

        return temp

    @angle_of_first_max_deviation_from_round.setter
    @enforce_parameter_types
    def angle_of_first_max_deviation_from_round(self: "Self", value: "float") -> None:
        self.wrapped.AngleOfFirstMaxDeviationFromRound = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_deviation_from_round(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumDeviationFromRound

        if temp is None:
            return 0.0

        return temp

    @maximum_deviation_from_round.setter
    @enforce_parameter_types
    def maximum_deviation_from_round(self: "Self", value: "float") -> None:
        self.wrapped.MaximumDeviationFromRound = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_lobes(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfLobes

        if temp is None:
            return 0

        return temp

    @number_of_lobes.setter
    @enforce_parameter_types
    def number_of_lobes(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfLobes = int(value) if value is not None else 0

    @property
    def specification_type(self: "Self") -> "_1971.RoundnessSpecificationType":
        """mastapy._private.bearings.tolerances.RoundnessSpecificationType"""
        temp = self.wrapped.SpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.RoundnessSpecificationType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.tolerances._1971", "RoundnessSpecificationType"
        )(value)

    @specification_type.setter
    @enforce_parameter_types
    def specification_type(
        self: "Self", value: "_1971.RoundnessSpecificationType"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.RoundnessSpecificationType"
        )
        self.wrapped.SpecificationType = value

    @property
    def type_of_fit(self: "Self") -> "_1977.TypeOfFit":
        """mastapy._private.bearings.tolerances.TypeOfFit"""
        temp = self.wrapped.TypeOfFit

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.TypeOfFit"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.tolerances._1977", "TypeOfFit"
        )(value)

    @type_of_fit.setter
    @enforce_parameter_types
    def type_of_fit(self: "Self", value: "_1977.TypeOfFit") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.TypeOfFit"
        )
        self.wrapped.TypeOfFit = value

    @property
    def user_specified_deviation(self: "Self") -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.UserSpecifiedDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @user_specified_deviation.setter
    @enforce_parameter_types
    def user_specified_deviation(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.UserSpecifiedDeviation = value.wrapped

    @property
    def roundness_distribution(self: "Self") -> "List[_1967.RaceRoundnessAtAngle]":
        """List[mastapy._private.bearings.tolerances.RaceRoundnessAtAngle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoundnessDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_RoundnessSpecification":
        """Cast to another type.

        Returns:
            _Cast_RoundnessSpecification
        """
        return _Cast_RoundnessSpecification(self)
