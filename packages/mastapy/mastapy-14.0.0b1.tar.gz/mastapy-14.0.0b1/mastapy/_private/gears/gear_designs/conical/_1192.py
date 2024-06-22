"""ConicalGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.gear_designs import _971
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears import _343
    from mastapy._private.gears.manufacturing.bevel import _819
    from mastapy._private.gears.gear_designs.cylindrical import _1110
    from mastapy._private.gears.gear_designs.zerol_bevel import _976
    from mastapy._private.gears.gear_designs.straight_bevel import _985
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _989
    from mastapy._private.gears.gear_designs.spiral_bevel import _993
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _997
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1001
    from mastapy._private.gears.gear_designs.klingelnberg_conical import _1005
    from mastapy._private.gears.gear_designs.hypoid import _1009
    from mastapy._private.gears.gear_designs.bevel import _1218
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1231
    from mastapy._private.gears.gear_designs import _972

    Self = TypeVar("Self", bound="ConicalGearDesign")
    CastSelf = TypeVar("CastSelf", bound="ConicalGearDesign._Cast_ConicalGearDesign")


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearDesign:
    """Special nested class for casting ConicalGearDesign to subclasses."""

    __parent__: "ConicalGearDesign"

    @property
    def gear_design(self: "CastSelf") -> "_971.GearDesign":
        return self.__parent__._cast(_971.GearDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_gear_design(self: "CastSelf") -> "_976.ZerolBevelGearDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _976

        return self.__parent__._cast(_976.ZerolBevelGearDesign)

    @property
    def straight_bevel_gear_design(self: "CastSelf") -> "_985.StraightBevelGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _985

        return self.__parent__._cast(_985.StraightBevelGearDesign)

    @property
    def straight_bevel_diff_gear_design(
        self: "CastSelf",
    ) -> "_989.StraightBevelDiffGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _989

        return self.__parent__._cast(_989.StraightBevelDiffGearDesign)

    @property
    def spiral_bevel_gear_design(self: "CastSelf") -> "_993.SpiralBevelGearDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _993

        return self.__parent__._cast(_993.SpiralBevelGearDesign)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
        self: "CastSelf",
    ) -> "_997.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _997

        return self.__parent__._cast(_997.KlingelnbergCycloPalloidSpiralBevelGearDesign)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_design(
        self: "CastSelf",
    ) -> "_1001.KlingelnbergCycloPalloidHypoidGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1001

        return self.__parent__._cast(_1001.KlingelnbergCycloPalloidHypoidGearDesign)

    @property
    def klingelnberg_conical_gear_design(
        self: "CastSelf",
    ) -> "_1005.KlingelnbergConicalGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1005

        return self.__parent__._cast(_1005.KlingelnbergConicalGearDesign)

    @property
    def hypoid_gear_design(self: "CastSelf") -> "_1009.HypoidGearDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1009

        return self.__parent__._cast(_1009.HypoidGearDesign)

    @property
    def bevel_gear_design(self: "CastSelf") -> "_1218.BevelGearDesign":
        from mastapy._private.gears.gear_designs.bevel import _1218

        return self.__parent__._cast(_1218.BevelGearDesign)

    @property
    def agma_gleason_conical_gear_design(
        self: "CastSelf",
    ) -> "_1231.AGMAGleasonConicalGearDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1231

        return self.__parent__._cast(_1231.AGMAGleasonConicalGearDesign)

    @property
    def conical_gear_design(self: "CastSelf") -> "ConicalGearDesign":
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
class ConicalGearDesign(_971.GearDesign):
    """ConicalGearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cutter_edge_radius_concave(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_edge_radius_convex(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def face_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def hand(self: "Self") -> "_343.Hand":
        """mastapy._private.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy._private.gears._343", "Hand")(
            value
        )

    @hand.setter
    @enforce_parameter_types
    def hand(self: "Self", value: "_343.Hand") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def inner_root_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_tip_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_root_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def straddle_mounted(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.StraddleMounted

        if temp is None:
            return False

        return temp

    @straddle_mounted.setter
    @enforce_parameter_types
    def straddle_mounted(self: "Self", value: "bool") -> None:
        self.wrapped.StraddleMounted = bool(value) if value is not None else False

    @property
    def use_cutter_tilt(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseCutterTilt

        if temp is None:
            return False

        return temp

    @use_cutter_tilt.setter
    @enforce_parameter_types
    def use_cutter_tilt(self: "Self", value: "bool") -> None:
        self.wrapped.UseCutterTilt = bool(value) if value is not None else False

    @property
    def flank_measurement_border(self: "Self") -> "_819.FlankMeasurementBorder":
        """mastapy._private.gears.manufacturing.bevel.FlankMeasurementBorder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def surface_roughness(self: "Self") -> "_1110.SurfaceRoughness":
        """mastapy._private.gears.gear_designs.cylindrical.SurfaceRoughness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearDesign":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearDesign
        """
        return _Cast_ConicalGearDesign(self)
