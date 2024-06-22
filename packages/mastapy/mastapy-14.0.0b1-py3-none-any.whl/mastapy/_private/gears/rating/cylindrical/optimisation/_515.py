"""SafetyFactorOptimisationStepResult"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "SafetyFactorOptimisationStepResult",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating import _379
    from mastapy._private.gears.rating.cylindrical.optimisation import _516, _517, _518

    Self = TypeVar("Self", bound="SafetyFactorOptimisationStepResult")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorOptimisationStepResult",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SafetyFactorOptimisationStepResult:
    """Special nested class for casting SafetyFactorOptimisationStepResult to subclasses."""

    __parent__: "SafetyFactorOptimisationStepResult"

    @property
    def safety_factor_optimisation_step_result_angle(
        self: "CastSelf",
    ) -> "_516.SafetyFactorOptimisationStepResultAngle":
        from mastapy._private.gears.rating.cylindrical.optimisation import _516

        return self.__parent__._cast(_516.SafetyFactorOptimisationStepResultAngle)

    @property
    def safety_factor_optimisation_step_result_number(
        self: "CastSelf",
    ) -> "_517.SafetyFactorOptimisationStepResultNumber":
        from mastapy._private.gears.rating.cylindrical.optimisation import _517

        return self.__parent__._cast(_517.SafetyFactorOptimisationStepResultNumber)

    @property
    def safety_factor_optimisation_step_result_short_length(
        self: "CastSelf",
    ) -> "_518.SafetyFactorOptimisationStepResultShortLength":
        from mastapy._private.gears.rating.cylindrical.optimisation import _518

        return self.__parent__._cast(_518.SafetyFactorOptimisationStepResultShortLength)

    @property
    def safety_factor_optimisation_step_result(
        self: "CastSelf",
    ) -> "SafetyFactorOptimisationStepResult":
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
class SafetyFactorOptimisationStepResult(_0.APIBase):
    """SafetyFactorOptimisationStepResult

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def normalised_safety_factors(self: "Self") -> "_379.SafetyFactorResults":
        """mastapy._private.gears.rating.SafetyFactorResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def safety_factors(self: "Self") -> "_379.SafetyFactorResults":
        """mastapy._private.gears.rating.SafetyFactorResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SafetyFactorOptimisationStepResult":
        """Cast to another type.

        Returns:
            _Cast_SafetyFactorOptimisationStepResult
        """
        return _Cast_SafetyFactorOptimisationStepResult(self)
