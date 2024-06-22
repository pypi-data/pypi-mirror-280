"""ParetoOptimisationOutput"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.math_utility.optimisation import _1599
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PARETO_OPTIMISATION_OUTPUT = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationOutput"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.math_utility.optimisation import _1600

    Self = TypeVar("Self", bound="ParetoOptimisationOutput")
    CastSelf = TypeVar(
        "CastSelf", bound="ParetoOptimisationOutput._Cast_ParetoOptimisationOutput"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationOutput",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ParetoOptimisationOutput:
    """Special nested class for casting ParetoOptimisationOutput to subclasses."""

    __parent__: "ParetoOptimisationOutput"

    @property
    def pareto_optimisation_variable(
        self: "CastSelf",
    ) -> "_1599.ParetoOptimisationVariable":
        return self.__parent__._cast(_1599.ParetoOptimisationVariable)

    @property
    def pareto_optimisation_variable_base(
        self: "CastSelf",
    ) -> "_1600.ParetoOptimisationVariableBase":
        from mastapy._private.math_utility.optimisation import _1600

        return self.__parent__._cast(_1600.ParetoOptimisationVariableBase)

    @property
    def pareto_optimisation_output(self: "CastSelf") -> "ParetoOptimisationOutput":
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
class ParetoOptimisationOutput(_1599.ParetoOptimisationVariable):
    """ParetoOptimisationOutput

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PARETO_OPTIMISATION_OUTPUT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def percent(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Percent

        if temp is None:
            return 0.0

        return temp

    @percent.setter
    @enforce_parameter_types
    def percent(self: "Self", value: "float") -> None:
        self.wrapped.Percent = float(value) if value is not None else 0.0

    @property
    def exclude_from_dominant_candidates_search(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ExcludeFromDominantCandidatesSearch

        if temp is None:
            return False

        return temp

    @exclude_from_dominant_candidates_search.setter
    @enforce_parameter_types
    def exclude_from_dominant_candidates_search(self: "Self", value: "bool") -> None:
        self.wrapped.ExcludeFromDominantCandidatesSearch = (
            bool(value) if value is not None else False
        )

    @property
    def use_original_design_value(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseOriginalDesignValue

        if temp is None:
            return False

        return temp

    @use_original_design_value.setter
    @enforce_parameter_types
    def use_original_design_value(self: "Self", value: "bool") -> None:
        self.wrapped.UseOriginalDesignValue = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: "Self") -> "_Cast_ParetoOptimisationOutput":
        """Cast to another type.

        Returns:
            _Cast_ParetoOptimisationOutput
        """
        return _Cast_ParetoOptimisationOutput(self)
