"""ParetoOptimisationVariable"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.math_utility.optimisation import _1600
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PARETO_OPTIMISATION_VARIABLE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationVariable"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.math_utility.optimisation import _1601, _1593, _1594

    Self = TypeVar("Self", bound="ParetoOptimisationVariable")
    CastSelf = TypeVar(
        "CastSelf", bound="ParetoOptimisationVariable._Cast_ParetoOptimisationVariable"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationVariable",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ParetoOptimisationVariable:
    """Special nested class for casting ParetoOptimisationVariable to subclasses."""

    __parent__: "ParetoOptimisationVariable"

    @property
    def pareto_optimisation_variable_base(
        self: "CastSelf",
    ) -> "_1600.ParetoOptimisationVariableBase":
        return self.__parent__._cast(_1600.ParetoOptimisationVariableBase)

    @property
    def pareto_optimisation_input(self: "CastSelf") -> "_1593.ParetoOptimisationInput":
        from mastapy._private.math_utility.optimisation import _1593

        return self.__parent__._cast(_1593.ParetoOptimisationInput)

    @property
    def pareto_optimisation_output(
        self: "CastSelf",
    ) -> "_1594.ParetoOptimisationOutput":
        from mastapy._private.math_utility.optimisation import _1594

        return self.__parent__._cast(_1594.ParetoOptimisationOutput)

    @property
    def pareto_optimisation_variable(self: "CastSelf") -> "ParetoOptimisationVariable":
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
class ParetoOptimisationVariable(_1600.ParetoOptimisationVariableBase):
    """ParetoOptimisationVariable

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PARETO_OPTIMISATION_VARIABLE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def property_target_for_dominant_candidate_search(
        self: "Self",
    ) -> "_1601.PropertyTargetForDominantCandidateSearch":
        """mastapy._private.math_utility.optimisation.PropertyTargetForDominantCandidateSearch"""
        temp = self.wrapped.PropertyTargetForDominantCandidateSearch

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.math_utility.optimisation._1601",
            "PropertyTargetForDominantCandidateSearch",
        )(value)

    @property_target_for_dominant_candidate_search.setter
    @enforce_parameter_types
    def property_target_for_dominant_candidate_search(
        self: "Self", value: "_1601.PropertyTargetForDominantCandidateSearch"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch",
        )
        self.wrapped.PropertyTargetForDominantCandidateSearch = value

    @property
    def cast_to(self: "Self") -> "_Cast_ParetoOptimisationVariable":
        """Cast to another type.

        Returns:
            _Cast_ParetoOptimisationVariable
        """
        return _Cast_ParetoOptimisationVariable(self)
