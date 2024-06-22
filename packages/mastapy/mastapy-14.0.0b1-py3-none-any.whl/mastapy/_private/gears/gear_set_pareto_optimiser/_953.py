"""ParetoFaceRatingOptimisationStrategyDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.math_utility.optimisation import _1598
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoFaceRatingOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_set_pareto_optimiser import _951, _952
    from mastapy._private.math_utility.optimisation import _1586
    from mastapy._private.utility.databases import _1878, _1881, _1874

    Self = TypeVar("Self", bound="ParetoFaceRatingOptimisationStrategyDatabase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ParetoFaceRatingOptimisationStrategyDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ParetoFaceRatingOptimisationStrategyDatabase:
    """Special nested class for casting ParetoFaceRatingOptimisationStrategyDatabase to subclasses."""

    __parent__: "ParetoFaceRatingOptimisationStrategyDatabase"

    @property
    def pareto_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_1598.ParetoOptimisationStrategyDatabase":
        return self.__parent__._cast(_1598.ParetoOptimisationStrategyDatabase)

    @property
    def design_space_search_strategy_database(
        self: "CastSelf",
    ) -> "_1586.DesignSpaceSearchStrategyDatabase":
        from mastapy._private.math_utility.optimisation import _1586

        return self.__parent__._cast(_1586.DesignSpaceSearchStrategyDatabase)

    @property
    def named_database(self: "CastSelf") -> "_1878.NamedDatabase":
        pass

        from mastapy._private.utility.databases import _1878

        return self.__parent__._cast(_1878.NamedDatabase)

    @property
    def sql_database(self: "CastSelf") -> "_1881.SQLDatabase":
        pass

        from mastapy._private.utility.databases import _1881

        return self.__parent__._cast(_1881.SQLDatabase)

    @property
    def database(self: "CastSelf") -> "_1874.Database":
        pass

        from mastapy._private.utility.databases import _1874

        return self.__parent__._cast(_1874.Database)

    @property
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_951.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _951

        return self.__parent__._cast(
            _951.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
        )

    @property
    def pareto_face_gear_set_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_952.ParetoFaceGearSetOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _952

        return self.__parent__._cast(_952.ParetoFaceGearSetOptimisationStrategyDatabase)

    @property
    def pareto_face_rating_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "ParetoFaceRatingOptimisationStrategyDatabase":
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
class ParetoFaceRatingOptimisationStrategyDatabase(
    _1598.ParetoOptimisationStrategyDatabase
):
    """ParetoFaceRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_ParetoFaceRatingOptimisationStrategyDatabase":
        """Cast to another type.

        Returns:
            _Cast_ParetoFaceRatingOptimisationStrategyDatabase
        """
        return _Cast_ParetoFaceRatingOptimisationStrategyDatabase(self)
