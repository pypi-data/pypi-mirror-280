"""ConicalGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private.gears.gear_designs import _974
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearSetDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1193
    from mastapy._private.gears.gear_designs.zerol_bevel import _978
    from mastapy._private.gears.gear_designs.straight_bevel import _987
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _991
    from mastapy._private.gears.gear_designs.spiral_bevel import _995
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _999
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1003
    from mastapy._private.gears.gear_designs.klingelnberg_conical import _1007
    from mastapy._private.gears.gear_designs.hypoid import _1011
    from mastapy._private.gears.gear_designs.bevel import _1220
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1233
    from mastapy._private.gears.gear_designs import _972

    Self = TypeVar("Self", bound="ConicalGearSetDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="ConicalGearSetDesign._Cast_ConicalGearSetDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSetDesign:
    """Special nested class for casting ConicalGearSetDesign to subclasses."""

    __parent__: "ConicalGearSetDesign"

    @property
    def gear_set_design(self: "CastSelf") -> "_974.GearSetDesign":
        return self.__parent__._cast(_974.GearSetDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_gear_set_design(self: "CastSelf") -> "_978.ZerolBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _978

        return self.__parent__._cast(_978.ZerolBevelGearSetDesign)

    @property
    def straight_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_987.StraightBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _987

        return self.__parent__._cast(_987.StraightBevelGearSetDesign)

    @property
    def straight_bevel_diff_gear_set_design(
        self: "CastSelf",
    ) -> "_991.StraightBevelDiffGearSetDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _991

        return self.__parent__._cast(_991.StraightBevelDiffGearSetDesign)

    @property
    def spiral_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_995.SpiralBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _995

        return self.__parent__._cast(_995.SpiralBevelGearSetDesign)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _999

        return self.__parent__._cast(
            _999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
        self: "CastSelf",
    ) -> "_1003.KlingelnbergCycloPalloidHypoidGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1003

        return self.__parent__._cast(_1003.KlingelnbergCycloPalloidHypoidGearSetDesign)

    @property
    def klingelnberg_conical_gear_set_design(
        self: "CastSelf",
    ) -> "_1007.KlingelnbergConicalGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1007

        return self.__parent__._cast(_1007.KlingelnbergConicalGearSetDesign)

    @property
    def hypoid_gear_set_design(self: "CastSelf") -> "_1011.HypoidGearSetDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1011

        return self.__parent__._cast(_1011.HypoidGearSetDesign)

    @property
    def bevel_gear_set_design(self: "CastSelf") -> "_1220.BevelGearSetDesign":
        from mastapy._private.gears.gear_designs.bevel import _1220

        return self.__parent__._cast(_1220.BevelGearSetDesign)

    @property
    def agma_gleason_conical_gear_set_design(
        self: "CastSelf",
    ) -> "_1233.AGMAGleasonConicalGearSetDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1233

        return self.__parent__._cast(_1233.AGMAGleasonConicalGearSetDesign)

    @property
    def conical_gear_set_design(self: "CastSelf") -> "ConicalGearSetDesign":
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
class ConicalGearSetDesign(_974.GearSetDesign):
    """ConicalGearSetDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_SET_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def circular_pitch(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def dominant_pinion(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DominantPinion

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @dominant_pinion.setter
    @enforce_parameter_types
    def dominant_pinion(self: "Self", value: "str") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DominantPinion = value

    @property
    def imported_xml_file_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImportedXMLFileName

        if temp is None:
            return ""

        return temp

    @property
    def mean_normal_module(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanNormalModule

        if temp is None:
            return 0.0

        return temp

    @mean_normal_module.setter
    @enforce_parameter_types
    def mean_normal_module(self: "Self", value: "float") -> None:
        self.wrapped.MeanNormalModule = float(value) if value is not None else 0.0

    @property
    def module(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    @enforce_parameter_types
    def module(self: "Self", value: "float") -> None:
        self.wrapped.Module = float(value) if value is not None else 0.0

    @property
    def wheel_finish_cutter_point_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def wheel_finish_cutter_point_width(self: "Self", value: "float") -> None:
        self.wrapped.WheelFinishCutterPointWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_mean_cone_distance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelMeanConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_cone_distance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @wheel_pitch_diameter.setter
    @enforce_parameter_types
    def wheel_pitch_diameter(self: "Self", value: "float") -> None:
        self.wrapped.WheelPitchDiameter = float(value) if value is not None else 0.0

    @property
    def conical_meshes(self: "Self") -> "List[_1193.ConicalGearMeshDesign]":
        """List[mastapy._private.gears.gear_designs.conical.ConicalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearSetDesign":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSetDesign
        """
        return _Cast_ConicalGearSetDesign(self)
