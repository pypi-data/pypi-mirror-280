"""StraightBevelDiffMeshedGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.gear_designs.bevel import _1221
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff",
    "StraightBevelDiffMeshedGearDesign",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1234
    from mastapy._private.gears.gear_designs.conical import _1197
    from mastapy._private.gears.gear_designs import _972

    Self = TypeVar("Self", bound="StraightBevelDiffMeshedGearDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffMeshedGearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffMeshedGearDesign:
    """Special nested class for casting StraightBevelDiffMeshedGearDesign to subclasses."""

    __parent__: "StraightBevelDiffMeshedGearDesign"

    @property
    def bevel_meshed_gear_design(self: "CastSelf") -> "_1221.BevelMeshedGearDesign":
        return self.__parent__._cast(_1221.BevelMeshedGearDesign)

    @property
    def agma_gleason_conical_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1234.AGMAGleasonConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1234

        return self.__parent__._cast(_1234.AGMAGleasonConicalMeshedGearDesign)

    @property
    def conical_meshed_gear_design(self: "CastSelf") -> "_1197.ConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.conical import _1197

        return self.__parent__._cast(_1197.ConicalMeshedGearDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def straight_bevel_diff_meshed_gear_design(
        self: "CastSelf",
    ) -> "StraightBevelDiffMeshedGearDesign":
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
class StraightBevelDiffMeshedGearDesign(_1221.BevelMeshedGearDesign):
    """StraightBevelDiffMeshedGearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_DIFF_MESHED_GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def geometry_factor_j(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_topland(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelDiffMeshedGearDesign":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffMeshedGearDesign
        """
        return _Cast_StraightBevelDiffMeshedGearDesign(self)
