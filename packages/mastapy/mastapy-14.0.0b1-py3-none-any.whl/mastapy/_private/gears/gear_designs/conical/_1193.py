"""ConicalGearMeshDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.gear_designs import _973
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearMeshDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.gear_designs.bevel import _1225, _1222, _1226, _1219
    from mastapy._private.gears.gear_designs.zerol_bevel import _977
    from mastapy._private.gears.gear_designs.straight_bevel import _986
    from mastapy._private.gears.gear_designs.straight_bevel_diff import _990
    from mastapy._private.gears.gear_designs.spiral_bevel import _994
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _998
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1002
    from mastapy._private.gears.gear_designs.klingelnberg_conical import _1006
    from mastapy._private.gears.gear_designs.hypoid import _1010
    from mastapy._private.gears.gear_designs.agma_gleason_conical import _1232
    from mastapy._private.gears.gear_designs import _972

    Self = TypeVar("Self", bound="ConicalGearMeshDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="ConicalGearMeshDesign._Cast_ConicalGearMeshDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearMeshDesign:
    """Special nested class for casting ConicalGearMeshDesign to subclasses."""

    __parent__: "ConicalGearMeshDesign"

    @property
    def gear_mesh_design(self: "CastSelf") -> "_973.GearMeshDesign":
        return self.__parent__._cast(_973.GearMeshDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def zerol_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_977.ZerolBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _977

        return self.__parent__._cast(_977.ZerolBevelGearMeshDesign)

    @property
    def straight_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_986.StraightBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _986

        return self.__parent__._cast(_986.StraightBevelGearMeshDesign)

    @property
    def straight_bevel_diff_gear_mesh_design(
        self: "CastSelf",
    ) -> "_990.StraightBevelDiffGearMeshDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _990

        return self.__parent__._cast(_990.StraightBevelDiffGearMeshDesign)

    @property
    def spiral_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_994.SpiralBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _994

        return self.__parent__._cast(_994.SpiralBevelGearMeshDesign)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_998.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _998

        return self.__parent__._cast(
            _998.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1002.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1002

        return self.__parent__._cast(_1002.KlingelnbergCycloPalloidHypoidGearMeshDesign)

    @property
    def klingelnberg_conical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1006.KlingelnbergConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1006

        return self.__parent__._cast(_1006.KlingelnbergConicalGearMeshDesign)

    @property
    def hypoid_gear_mesh_design(self: "CastSelf") -> "_1010.HypoidGearMeshDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1010

        return self.__parent__._cast(_1010.HypoidGearMeshDesign)

    @property
    def bevel_gear_mesh_design(self: "CastSelf") -> "_1219.BevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.bevel import _1219

        return self.__parent__._cast(_1219.BevelGearMeshDesign)

    @property
    def agma_gleason_conical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1232.AGMAGleasonConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1232

        return self.__parent__._cast(_1232.AGMAGleasonConicalGearMeshDesign)

    @property
    def conical_gear_mesh_design(self: "CastSelf") -> "ConicalGearMeshDesign":
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
class ConicalGearMeshDesign(_973.GearMeshDesign):
    """ConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_MESH_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def driven_machine_characteristic(
        self: "Self",
    ) -> "_1225.MachineCharacteristicAGMAKlingelnberg":
        """mastapy._private.gears.gear_designs.bevel.MachineCharacteristicAGMAKlingelnberg"""
        temp = self.wrapped.DrivenMachineCharacteristic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.bevel._1225",
            "MachineCharacteristicAGMAKlingelnberg",
        )(value)

    @driven_machine_characteristic.setter
    @enforce_parameter_types
    def driven_machine_characteristic(
        self: "Self", value: "_1225.MachineCharacteristicAGMAKlingelnberg"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )
        self.wrapped.DrivenMachineCharacteristic = value

    @property
    def driven_machine_characteristic_gleason(
        self: "Self",
    ) -> "_1222.DrivenMachineCharacteristicGleason":
        """mastapy._private.gears.gear_designs.bevel.DrivenMachineCharacteristicGleason"""
        temp = self.wrapped.DrivenMachineCharacteristicGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.DrivenMachineCharacteristicGleason",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.bevel._1222",
            "DrivenMachineCharacteristicGleason",
        )(value)

    @driven_machine_characteristic_gleason.setter
    @enforce_parameter_types
    def driven_machine_characteristic_gleason(
        self: "Self", value: "_1222.DrivenMachineCharacteristicGleason"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.DrivenMachineCharacteristicGleason",
        )
        self.wrapped.DrivenMachineCharacteristicGleason = value

    @property
    def maximum_normal_backlash(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_normal_backlash(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNormalBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OverloadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @overload_factor.setter
    @enforce_parameter_types
    def overload_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OverloadFactor = value

    @property
    def pinion_full_circle_edge_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionFullCircleEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def prime_mover_characteristic(
        self: "Self",
    ) -> "_1225.MachineCharacteristicAGMAKlingelnberg":
        """mastapy._private.gears.gear_designs.bevel.MachineCharacteristicAGMAKlingelnberg"""
        temp = self.wrapped.PrimeMoverCharacteristic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.bevel._1225",
            "MachineCharacteristicAGMAKlingelnberg",
        )(value)

    @prime_mover_characteristic.setter
    @enforce_parameter_types
    def prime_mover_characteristic(
        self: "Self", value: "_1225.MachineCharacteristicAGMAKlingelnberg"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )
        self.wrapped.PrimeMoverCharacteristic = value

    @property
    def prime_mover_characteristic_gleason(
        self: "Self",
    ) -> "_1226.PrimeMoverCharacteristicGleason":
        """mastapy._private.gears.gear_designs.bevel.PrimeMoverCharacteristicGleason"""
        temp = self.wrapped.PrimeMoverCharacteristicGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Bevel.PrimeMoverCharacteristicGleason"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.bevel._1226",
            "PrimeMoverCharacteristicGleason",
        )(value)

    @prime_mover_characteristic_gleason.setter
    @enforce_parameter_types
    def prime_mover_characteristic_gleason(
        self: "Self", value: "_1226.PrimeMoverCharacteristicGleason"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.PrimeMoverCharacteristicGleason",
        )
        self.wrapped.PrimeMoverCharacteristicGleason = value

    @property
    def shaft_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @shaft_angle.setter
    @enforce_parameter_types
    def shaft_angle(self: "Self", value: "float") -> None:
        self.wrapped.ShaftAngle = float(value) if value is not None else 0.0

    @property
    def specified_backlash_range_max(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecifiedBacklashRangeMax

        if temp is None:
            return 0.0

        return temp

    @specified_backlash_range_max.setter
    @enforce_parameter_types
    def specified_backlash_range_max(self: "Self", value: "float") -> None:
        self.wrapped.SpecifiedBacklashRangeMax = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_backlash_range_min(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecifiedBacklashRangeMin

        if temp is None:
            return 0.0

        return temp

    @specified_backlash_range_min.setter
    @enforce_parameter_types
    def specified_backlash_range_min(self: "Self", value: "float") -> None:
        self.wrapped.SpecifiedBacklashRangeMin = (
            float(value) if value is not None else 0.0
        )

    @property
    def specify_backlash(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyBacklash

        if temp is None:
            return False

        return temp

    @specify_backlash.setter
    @enforce_parameter_types
    def specify_backlash(self: "Self", value: "bool") -> None:
        self.wrapped.SpecifyBacklash = bool(value) if value is not None else False

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearMeshDesign":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearMeshDesign
        """
        return _Cast_ConicalGearMeshDesign(self)
