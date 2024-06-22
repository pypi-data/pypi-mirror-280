"""BevelDifferentialPlanetGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.system_model.part_model.gears import _2571
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.gears import (
        _2575,
        _2569,
        _2579,
        _2586,
    )
    from mastapy._private.system_model.part_model import _2520, _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="BevelDifferentialPlanetGear")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelDifferentialPlanetGear:
    """Special nested class for casting BevelDifferentialPlanetGear to subclasses."""

    __parent__: "BevelDifferentialPlanetGear"

    @property
    def bevel_differential_gear(self: "CastSelf") -> "_2571.BevelDifferentialGear":
        return self.__parent__._cast(_2571.BevelDifferentialGear)

    @property
    def bevel_gear(self: "CastSelf") -> "_2575.BevelGear":
        from mastapy._private.system_model.part_model.gears import _2575

        return self.__parent__._cast(_2575.BevelGear)

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2569.AGMAGleasonConicalGear":
        from mastapy._private.system_model.part_model.gears import _2569

        return self.__parent__._cast(_2569.AGMAGleasonConicalGear)

    @property
    def conical_gear(self: "CastSelf") -> "_2579.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2579

        return self.__parent__._cast(_2579.ConicalGear)

    @property
    def gear(self: "CastSelf") -> "_2586.Gear":
        from mastapy._private.system_model.part_model.gears import _2586

        return self.__parent__._cast(_2586.Gear)

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        from mastapy._private.system_model.part_model import _2498

        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def bevel_differential_planet_gear(
        self: "CastSelf",
    ) -> "BevelDifferentialPlanetGear":
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
class BevelDifferentialPlanetGear(_2571.BevelDifferentialGear):
    """BevelDifferentialPlanetGear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_DIFFERENTIAL_PLANET_GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def number_of_planets(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfPlanets

        if temp is None:
            return 0

        return temp

    @number_of_planets.setter
    @enforce_parameter_types
    def number_of_planets(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfPlanets = int(value) if value is not None else 0

    @property
    def cast_to(self: "Self") -> "_Cast_BevelDifferentialPlanetGear":
        """Cast to another type.

        Returns:
            _Cast_BevelDifferentialPlanetGear
        """
        return _Cast_BevelDifferentialPlanetGear(self)
