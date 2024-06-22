"""GearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.gear_designs import _972
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_DESIGN = python_net_import("SMT.MastaAPI.Gears.GearDesigns", "GearDesign")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.fe_model import _1235
    from mastapy._private.gears.gear_designs.zerol_bevel import _976
    from mastapy._private.gears.gear_designs.worm import _980, _981, _984
    from mastapy._private.gears.gear_designs.straight_bevel import _985
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _989
    from mastapy._private.gears.gear_designs.spiral_bevel import _993
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _997
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1001
    from mastapy._private.gears.gear_designs.klingelnberg_conical import _1005
    from mastapy._private.gears.gear_designs.hypoid import _1009
    from mastapy._private.gears.gear_designs.face import _1013, _1018, _1021
    from mastapy._private.gears.gear_designs.cylindrical import _1042, _1072
    from mastapy._private.gears.gear_designs.conical import _1192
    from mastapy._private.gears.gear_designs.concept import _1214
    from mastapy._private.gears.gear_designs.bevel import _1218
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1231

    Self = TypeVar("Self", bound="GearDesign")
    CastSelf = TypeVar("CastSelf", bound="GearDesign._Cast_GearDesign")


__docformat__ = "restructuredtext en"
__all__ = ("GearDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearDesign:
    """Special nested class for casting GearDesign to subclasses."""

    __parent__: "GearDesign"

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_gear_design(self: "CastSelf") -> "_976.ZerolBevelGearDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _976

        return self.__parent__._cast(_976.ZerolBevelGearDesign)

    @property
    def worm_design(self: "CastSelf") -> "_980.WormDesign":
        from mastapy._private.gears.gear_designs.worm import _980

        return self.__parent__._cast(_980.WormDesign)

    @property
    def worm_gear_design(self: "CastSelf") -> "_981.WormGearDesign":
        from mastapy._private.gears.gear_designs.worm import _981

        return self.__parent__._cast(_981.WormGearDesign)

    @property
    def worm_wheel_design(self: "CastSelf") -> "_984.WormWheelDesign":
        from mastapy._private.gears.gear_designs.worm import _984

        return self.__parent__._cast(_984.WormWheelDesign)

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
    def face_gear_design(self: "CastSelf") -> "_1013.FaceGearDesign":
        from mastapy._private.gears.gear_designs.face import _1013

        return self.__parent__._cast(_1013.FaceGearDesign)

    @property
    def face_gear_pinion_design(self: "CastSelf") -> "_1018.FaceGearPinionDesign":
        from mastapy._private.gears.gear_designs.face import _1018

        return self.__parent__._cast(_1018.FaceGearPinionDesign)

    @property
    def face_gear_wheel_design(self: "CastSelf") -> "_1021.FaceGearWheelDesign":
        from mastapy._private.gears.gear_designs.face import _1021

        return self.__parent__._cast(_1021.FaceGearWheelDesign)

    @property
    def cylindrical_gear_design(self: "CastSelf") -> "_1042.CylindricalGearDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1042

        return self.__parent__._cast(_1042.CylindricalGearDesign)

    @property
    def cylindrical_planet_gear_design(
        self: "CastSelf",
    ) -> "_1072.CylindricalPlanetGearDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1072

        return self.__parent__._cast(_1072.CylindricalPlanetGearDesign)

    @property
    def conical_gear_design(self: "CastSelf") -> "_1192.ConicalGearDesign":
        from mastapy._private.gears.gear_designs.conical import _1192

        return self.__parent__._cast(_1192.ConicalGearDesign)

    @property
    def concept_gear_design(self: "CastSelf") -> "_1214.ConceptGearDesign":
        from mastapy._private.gears.gear_designs.concept import _1214

        return self.__parent__._cast(_1214.ConceptGearDesign)

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
    def gear_design(self: "CastSelf") -> "GearDesign":
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
class GearDesign(_972.GearDesignComponent):
    """GearDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def absolute_shaft_inner_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: "Self", value: "float") -> None:
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def mass(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def names_of_meshing_gears(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NamesOfMeshingGears

        if temp is None:
            return ""

        return temp

    @property
    def number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def number_of_teeth_maintaining_ratio(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethMaintainingRatio

        if temp is None:
            return 0

        return temp

    @number_of_teeth_maintaining_ratio.setter
    @enforce_parameter_types
    def number_of_teeth_maintaining_ratio(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfTeethMaintainingRatio = (
            int(value) if value is not None else 0
        )

    @property
    def shaft_inner_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_outer_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tifffe_model(self: "Self") -> "_1235.GearFEModel":
        """mastapy._private.gears.fe_model.GearFEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearDesign":
        """Cast to another type.

        Returns:
            _Cast_GearDesign
        """
        return _Cast_GearDesign(self)
