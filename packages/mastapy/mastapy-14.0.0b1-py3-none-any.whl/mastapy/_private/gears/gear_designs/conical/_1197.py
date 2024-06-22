"""ConicalMeshedGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.gears.gear_designs import _972
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalMeshedGearDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.zerol_bevel import _979
    from mastapy._private.gears.gear_designs.straight_bevel import _988
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _992
    from mastapy._private.gears.gear_designs.spiral_bevel import _996
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _1000
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1004
    from mastapy._private.gears.gear_designs.klingelnberg_conical import _1008
    from mastapy._private.gears.gear_designs.hypoid import _1012
    from mastapy._private.gears.gear_designs.bevel import _1221
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1234

    Self = TypeVar("Self", bound="ConicalMeshedGearDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshedGearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalMeshedGearDesign:
    """Special nested class for casting ConicalMeshedGearDesign to subclasses."""

    __parent__: "ConicalMeshedGearDesign"

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_979.ZerolBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _979

        return self.__parent__._cast(_979.ZerolBevelMeshedGearDesign)

    @property
    def straight_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_988.StraightBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _988

        return self.__parent__._cast(_988.StraightBevelMeshedGearDesign)

    @property
    def straight_bevel_diff_meshed_gear_design(
        self: "CastSelf",
    ) -> "_992.StraightBevelDiffMeshedGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _992

        return self.__parent__._cast(_992.StraightBevelDiffMeshedGearDesign)

    @property
    def spiral_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_996.SpiralBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _996

        return self.__parent__._cast(_996.SpiralBevelMeshedGearDesign)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1000.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _1000

        return self.__parent__._cast(
            _1000.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1004.KlingelnbergCycloPalloidHypoidMeshedGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1004

        return self.__parent__._cast(
            _1004.KlingelnbergCycloPalloidHypoidMeshedGearDesign
        )

    @property
    def klingelnberg_conical_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1008.KlingelnbergConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1008

        return self.__parent__._cast(_1008.KlingelnbergConicalMeshedGearDesign)

    @property
    def hypoid_meshed_gear_design(self: "CastSelf") -> "_1012.HypoidMeshedGearDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1012

        return self.__parent__._cast(_1012.HypoidMeshedGearDesign)

    @property
    def bevel_meshed_gear_design(self: "CastSelf") -> "_1221.BevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.bevel import _1221

        return self.__parent__._cast(_1221.BevelMeshedGearDesign)

    @property
    def agma_gleason_conical_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1234.AGMAGleasonConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1234

        return self.__parent__._cast(_1234.AGMAGleasonConicalMeshedGearDesign)

    @property
    def conical_meshed_gear_design(self: "CastSelf") -> "ConicalMeshedGearDesign":
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
class ConicalMeshedGearDesign(_972.GearDesignComponent):
    """ConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_MESHED_GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def axial_force_type(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForceType

        if temp is None:
            return ""

        return temp

    @property
    def axial_force_type_convex(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForceTypeConvex

        if temp is None:
            return ""

        return temp

    @property
    def gleason_axial_factor_concave(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonAxialFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_axial_factor_convex(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonAxialFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor_concave(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonSeparatingFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor_convex(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonSeparatingFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def module(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def pitch_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force_type_concave(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForceTypeConcave

        if temp is None:
            return ""

        return temp

    @property
    def radial_force_type_convex(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForceTypeConvex

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalMeshedGearDesign":
        """Cast to another type.

        Returns:
            _Cast_ConicalMeshedGearDesign
        """
        return _Cast_ConicalMeshedGearDesign(self)
