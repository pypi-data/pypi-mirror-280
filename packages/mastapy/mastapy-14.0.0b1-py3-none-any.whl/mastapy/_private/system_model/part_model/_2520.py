"""MountableComponent"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model import _2498
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model import (
        _2489,
        _2499,
        _2493,
        _2501,
        _2516,
        _2517,
        _2522,
        _2525,
        _2527,
        _2528,
        _2533,
        _2535,
        _2524,
    )
    from mastapy._private.system_model.connections_and_sockets import (
        _2325,
        _2329,
        _2322,
    )
    from mastapy._private.system_model.part_model.gears import (
        _2569,
        _2571,
        _2573,
        _2574,
        _2575,
        _2577,
        _2579,
        _2581,
        _2583,
        _2584,
        _2586,
        _2590,
        _2592,
        _2594,
        _2596,
        _2599,
        _2601,
        _2603,
        _2605,
        _2606,
        _2607,
        _2609,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2626
    from mastapy._private.system_model.part_model.couplings import (
        _2636,
        _2639,
        _2642,
        _2645,
        _2647,
        _2649,
        _2655,
        _2657,
        _2663,
        _2666,
        _2667,
        _2668,
        _2670,
        _2672,
    )
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="MountableComponent")
    CastSelf = TypeVar("CastSelf", bound="MountableComponent._Cast_MountableComponent")


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponent:
    """Special nested class for casting MountableComponent to subclasses."""

    __parent__: "MountableComponent"

    @property
    def component(self: "CastSelf") -> "_2498.Component":
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
    def bearing(self: "CastSelf") -> "_2493.Bearing":
        from mastapy._private.system_model.part_model import _2493

        return self.__parent__._cast(_2493.Bearing)

    @property
    def connector(self: "CastSelf") -> "_2501.Connector":
        from mastapy._private.system_model.part_model import _2501

        return self.__parent__._cast(_2501.Connector)

    @property
    def mass_disc(self: "CastSelf") -> "_2516.MassDisc":
        from mastapy._private.system_model.part_model import _2516

        return self.__parent__._cast(_2516.MassDisc)

    @property
    def measurement_component(self: "CastSelf") -> "_2517.MeasurementComponent":
        from mastapy._private.system_model.part_model import _2517

        return self.__parent__._cast(_2517.MeasurementComponent)

    @property
    def oil_seal(self: "CastSelf") -> "_2522.OilSeal":
        from mastapy._private.system_model.part_model import _2522

        return self.__parent__._cast(_2522.OilSeal)

    @property
    def planet_carrier(self: "CastSelf") -> "_2525.PlanetCarrier":
        from mastapy._private.system_model.part_model import _2525

        return self.__parent__._cast(_2525.PlanetCarrier)

    @property
    def point_load(self: "CastSelf") -> "_2527.PointLoad":
        from mastapy._private.system_model.part_model import _2527

        return self.__parent__._cast(_2527.PointLoad)

    @property
    def power_load(self: "CastSelf") -> "_2528.PowerLoad":
        from mastapy._private.system_model.part_model import _2528

        return self.__parent__._cast(_2528.PowerLoad)

    @property
    def unbalanced_mass(self: "CastSelf") -> "_2533.UnbalancedMass":
        from mastapy._private.system_model.part_model import _2533

        return self.__parent__._cast(_2533.UnbalancedMass)

    @property
    def virtual_component(self: "CastSelf") -> "_2535.VirtualComponent":
        from mastapy._private.system_model.part_model import _2535

        return self.__parent__._cast(_2535.VirtualComponent)

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2569.AGMAGleasonConicalGear":
        from mastapy._private.system_model.part_model.gears import _2569

        return self.__parent__._cast(_2569.AGMAGleasonConicalGear)

    @property
    def bevel_differential_gear(self: "CastSelf") -> "_2571.BevelDifferentialGear":
        from mastapy._private.system_model.part_model.gears import _2571

        return self.__parent__._cast(_2571.BevelDifferentialGear)

    @property
    def bevel_differential_planet_gear(
        self: "CastSelf",
    ) -> "_2573.BevelDifferentialPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2573

        return self.__parent__._cast(_2573.BevelDifferentialPlanetGear)

    @property
    def bevel_differential_sun_gear(
        self: "CastSelf",
    ) -> "_2574.BevelDifferentialSunGear":
        from mastapy._private.system_model.part_model.gears import _2574

        return self.__parent__._cast(_2574.BevelDifferentialSunGear)

    @property
    def bevel_gear(self: "CastSelf") -> "_2575.BevelGear":
        from mastapy._private.system_model.part_model.gears import _2575

        return self.__parent__._cast(_2575.BevelGear)

    @property
    def concept_gear(self: "CastSelf") -> "_2577.ConceptGear":
        from mastapy._private.system_model.part_model.gears import _2577

        return self.__parent__._cast(_2577.ConceptGear)

    @property
    def conical_gear(self: "CastSelf") -> "_2579.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2579

        return self.__parent__._cast(_2579.ConicalGear)

    @property
    def cylindrical_gear(self: "CastSelf") -> "_2581.CylindricalGear":
        from mastapy._private.system_model.part_model.gears import _2581

        return self.__parent__._cast(_2581.CylindricalGear)

    @property
    def cylindrical_planet_gear(self: "CastSelf") -> "_2583.CylindricalPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2583

        return self.__parent__._cast(_2583.CylindricalPlanetGear)

    @property
    def face_gear(self: "CastSelf") -> "_2584.FaceGear":
        from mastapy._private.system_model.part_model.gears import _2584

        return self.__parent__._cast(_2584.FaceGear)

    @property
    def gear(self: "CastSelf") -> "_2586.Gear":
        from mastapy._private.system_model.part_model.gears import _2586

        return self.__parent__._cast(_2586.Gear)

    @property
    def hypoid_gear(self: "CastSelf") -> "_2590.HypoidGear":
        from mastapy._private.system_model.part_model.gears import _2590

        return self.__parent__._cast(_2590.HypoidGear)

    @property
    def klingelnberg_cyclo_palloid_conical_gear(
        self: "CastSelf",
    ) -> "_2592.KlingelnbergCycloPalloidConicalGear":
        from mastapy._private.system_model.part_model.gears import _2592

        return self.__parent__._cast(_2592.KlingelnbergCycloPalloidConicalGear)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(
        self: "CastSelf",
    ) -> "_2594.KlingelnbergCycloPalloidHypoidGear":
        from mastapy._private.system_model.part_model.gears import _2594

        return self.__parent__._cast(_2594.KlingelnbergCycloPalloidHypoidGear)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "CastSelf",
    ) -> "_2596.KlingelnbergCycloPalloidSpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2596

        return self.__parent__._cast(_2596.KlingelnbergCycloPalloidSpiralBevelGear)

    @property
    def spiral_bevel_gear(self: "CastSelf") -> "_2599.SpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2599

        return self.__parent__._cast(_2599.SpiralBevelGear)

    @property
    def straight_bevel_diff_gear(self: "CastSelf") -> "_2601.StraightBevelDiffGear":
        from mastapy._private.system_model.part_model.gears import _2601

        return self.__parent__._cast(_2601.StraightBevelDiffGear)

    @property
    def straight_bevel_gear(self: "CastSelf") -> "_2603.StraightBevelGear":
        from mastapy._private.system_model.part_model.gears import _2603

        return self.__parent__._cast(_2603.StraightBevelGear)

    @property
    def straight_bevel_planet_gear(self: "CastSelf") -> "_2605.StraightBevelPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2605

        return self.__parent__._cast(_2605.StraightBevelPlanetGear)

    @property
    def straight_bevel_sun_gear(self: "CastSelf") -> "_2606.StraightBevelSunGear":
        from mastapy._private.system_model.part_model.gears import _2606

        return self.__parent__._cast(_2606.StraightBevelSunGear)

    @property
    def worm_gear(self: "CastSelf") -> "_2607.WormGear":
        from mastapy._private.system_model.part_model.gears import _2607

        return self.__parent__._cast(_2607.WormGear)

    @property
    def zerol_bevel_gear(self: "CastSelf") -> "_2609.ZerolBevelGear":
        from mastapy._private.system_model.part_model.gears import _2609

        return self.__parent__._cast(_2609.ZerolBevelGear)

    @property
    def ring_pins(self: "CastSelf") -> "_2626.RingPins":
        from mastapy._private.system_model.part_model.cycloidal import _2626

        return self.__parent__._cast(_2626.RingPins)

    @property
    def clutch_half(self: "CastSelf") -> "_2636.ClutchHalf":
        from mastapy._private.system_model.part_model.couplings import _2636

        return self.__parent__._cast(_2636.ClutchHalf)

    @property
    def concept_coupling_half(self: "CastSelf") -> "_2639.ConceptCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2639

        return self.__parent__._cast(_2639.ConceptCouplingHalf)

    @property
    def coupling_half(self: "CastSelf") -> "_2642.CouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2642

        return self.__parent__._cast(_2642.CouplingHalf)

    @property
    def cvt_pulley(self: "CastSelf") -> "_2645.CVTPulley":
        from mastapy._private.system_model.part_model.couplings import _2645

        return self.__parent__._cast(_2645.CVTPulley)

    @property
    def part_to_part_shear_coupling_half(
        self: "CastSelf",
    ) -> "_2647.PartToPartShearCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2647

        return self.__parent__._cast(_2647.PartToPartShearCouplingHalf)

    @property
    def pulley(self: "CastSelf") -> "_2649.Pulley":
        from mastapy._private.system_model.part_model.couplings import _2649

        return self.__parent__._cast(_2649.Pulley)

    @property
    def rolling_ring(self: "CastSelf") -> "_2655.RollingRing":
        from mastapy._private.system_model.part_model.couplings import _2655

        return self.__parent__._cast(_2655.RollingRing)

    @property
    def shaft_hub_connection(self: "CastSelf") -> "_2657.ShaftHubConnection":
        from mastapy._private.system_model.part_model.couplings import _2657

        return self.__parent__._cast(_2657.ShaftHubConnection)

    @property
    def spring_damper_half(self: "CastSelf") -> "_2663.SpringDamperHalf":
        from mastapy._private.system_model.part_model.couplings import _2663

        return self.__parent__._cast(_2663.SpringDamperHalf)

    @property
    def synchroniser_half(self: "CastSelf") -> "_2666.SynchroniserHalf":
        from mastapy._private.system_model.part_model.couplings import _2666

        return self.__parent__._cast(_2666.SynchroniserHalf)

    @property
    def synchroniser_part(self: "CastSelf") -> "_2667.SynchroniserPart":
        from mastapy._private.system_model.part_model.couplings import _2667

        return self.__parent__._cast(_2667.SynchroniserPart)

    @property
    def synchroniser_sleeve(self: "CastSelf") -> "_2668.SynchroniserSleeve":
        from mastapy._private.system_model.part_model.couplings import _2668

        return self.__parent__._cast(_2668.SynchroniserSleeve)

    @property
    def torque_converter_pump(self: "CastSelf") -> "_2670.TorqueConverterPump":
        from mastapy._private.system_model.part_model.couplings import _2670

        return self.__parent__._cast(_2670.TorqueConverterPump)

    @property
    def torque_converter_turbine(self: "CastSelf") -> "_2672.TorqueConverterTurbine":
        from mastapy._private.system_model.part_model.couplings import _2672

        return self.__parent__._cast(_2672.TorqueConverterTurbine)

    @property
    def mountable_component(self: "CastSelf") -> "MountableComponent":
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
class MountableComponent(_2498.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def rotation_about_axis(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: "Self", value: "float") -> None:
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: "Self") -> "_2489.AbstractShaft":
        """mastapy._private.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: "Self") -> "_2325.Connection":
        """mastapy._private.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: "Self") -> "_2329.CylindricalSocket":
        """mastapy._private.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: "Self", shaft: "_2489.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2322.CoaxialConnection":
        """mastapy._private.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy._private.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: "Self", shaft: "_2489.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy._private.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_MountableComponent":
        """Cast to another type.

        Returns:
            _Cast_MountableComponent
        """
        return _Cast_MountableComponent(self)
