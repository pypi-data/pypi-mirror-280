"""Component"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._math.vector_3d import Vector3D
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.part_model import _2524
from mastapy._private._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.math_utility import _1545, _1546
    from mastapy._private.system_model.connections_and_sockets import (
        _2323,
        _2325,
        _2349,
        _2344,
    )
    from mastapy._private.system_model.part_model import (
        _2499,
        _2489,
        _2490,
        _2493,
        _2496,
        _2501,
        _2502,
        _2506,
        _2507,
        _2509,
        _2516,
        _2517,
        _2518,
        _2520,
        _2522,
        _2525,
        _2527,
        _2528,
        _2533,
        _2535,
    )
    from mastapy._private.system_model.part_model.shaft_model import _2538
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
    from mastapy._private.system_model.part_model.cycloidal import _2625, _2626
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

    Self = TypeVar("Self", bound="Component")
    CastSelf = TypeVar("CastSelf", bound="Component._Cast_Component")


__docformat__ = "restructuredtext en"
__all__ = ("Component",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Component:
    """Special nested class for casting Component to subclasses."""

    __parent__: "Component"

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def abstract_shaft(self: "CastSelf") -> "_2489.AbstractShaft":
        from mastapy._private.system_model.part_model import _2489

        return self.__parent__._cast(_2489.AbstractShaft)

    @property
    def abstract_shaft_or_housing(self: "CastSelf") -> "_2490.AbstractShaftOrHousing":
        from mastapy._private.system_model.part_model import _2490

        return self.__parent__._cast(_2490.AbstractShaftOrHousing)

    @property
    def bearing(self: "CastSelf") -> "_2493.Bearing":
        from mastapy._private.system_model.part_model import _2493

        return self.__parent__._cast(_2493.Bearing)

    @property
    def bolt(self: "CastSelf") -> "_2496.Bolt":
        from mastapy._private.system_model.part_model import _2496

        return self.__parent__._cast(_2496.Bolt)

    @property
    def connector(self: "CastSelf") -> "_2501.Connector":
        from mastapy._private.system_model.part_model import _2501

        return self.__parent__._cast(_2501.Connector)

    @property
    def datum(self: "CastSelf") -> "_2502.Datum":
        from mastapy._private.system_model.part_model import _2502

        return self.__parent__._cast(_2502.Datum)

    @property
    def external_cad_model(self: "CastSelf") -> "_2506.ExternalCADModel":
        from mastapy._private.system_model.part_model import _2506

        return self.__parent__._cast(_2506.ExternalCADModel)

    @property
    def fe_part(self: "CastSelf") -> "_2507.FEPart":
        from mastapy._private.system_model.part_model import _2507

        return self.__parent__._cast(_2507.FEPart)

    @property
    def guide_dxf_model(self: "CastSelf") -> "_2509.GuideDxfModel":
        from mastapy._private.system_model.part_model import _2509

        return self.__parent__._cast(_2509.GuideDxfModel)

    @property
    def mass_disc(self: "CastSelf") -> "_2516.MassDisc":
        from mastapy._private.system_model.part_model import _2516

        return self.__parent__._cast(_2516.MassDisc)

    @property
    def measurement_component(self: "CastSelf") -> "_2517.MeasurementComponent":
        from mastapy._private.system_model.part_model import _2517

        return self.__parent__._cast(_2517.MeasurementComponent)

    @property
    def microphone(self: "CastSelf") -> "_2518.Microphone":
        from mastapy._private.system_model.part_model import _2518

        return self.__parent__._cast(_2518.Microphone)

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.MountableComponent)

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
    def shaft(self: "CastSelf") -> "_2538.Shaft":
        from mastapy._private.system_model.part_model.shaft_model import _2538

        return self.__parent__._cast(_2538.Shaft)

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
    def cycloidal_disc(self: "CastSelf") -> "_2625.CycloidalDisc":
        from mastapy._private.system_model.part_model.cycloidal import _2625

        return self.__parent__._cast(_2625.CycloidalDisc)

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
    def component(self: "CastSelf") -> "Component":
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
class Component(_2524.Part):
    """Component

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def additional_modal_damping_ratio(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: "Self", value: "float") -> None:
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: "Self", value: "float") -> None:
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def polar_inertia(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia.setter
    @enforce_parameter_types
    def polar_inertia(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PolarInertia = value

    @property
    def polar_inertia_for_synchroniser_sizing_only(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PolarInertiaForSynchroniserSizingOnly

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia_for_synchroniser_sizing_only.setter
    @enforce_parameter_types
    def polar_inertia_for_synchroniser_sizing_only(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PolarInertiaForSynchroniserSizingOnly = value

    @property
    def reason_mass_properties_are_unknown(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_zero(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ""

        return temp

    @property
    def translation(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Translation

        if temp is None:
            return ""

        return temp

    @property
    def transverse_inertia(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TransverseInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @transverse_inertia.setter
    @enforce_parameter_types
    def transverse_inertia(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TransverseInertia = value

    @property
    def x_axis(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxis

        if temp is None:
            return ""

        return temp

    @property
    def y_axis(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxis

        if temp is None:
            return ""

        return temp

    @property
    def z_axis(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxis

        if temp is None:
            return ""

        return temp

    @property
    def coordinate_system_euler_angles(self: "Self") -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.CoordinateSystemEulerAngles

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @coordinate_system_euler_angles.setter
    @enforce_parameter_types
    def coordinate_system_euler_angles(self: "Self", value: "Vector3D") -> None:
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.CoordinateSystemEulerAngles = value

    @property
    def local_coordinate_system(self: "Self") -> "_1545.CoordinateSystem3D":
        """mastapy._private.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def position(self: "Self") -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @position.setter
    @enforce_parameter_types
    def position(self: "Self", value: "Vector3D") -> None:
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Position = value

    @property
    def component_connections(self: "Self") -> "List[_2323.ComponentConnection]":
        """List[mastapy._private.system_model.connections_and_sockets.ComponentConnection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def available_socket_offsets(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableSocketOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def centre_offset(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOffset

        if temp is None:
            return 0.0

        return temp

    @property
    def translation_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TranslationVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def x_axis_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def y_axis_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def z_axis_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def can_connect_to(self: "Self", component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.CanConnectTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def can_delete_connection(self: "Self", connection: "_2325.Connection") -> "bool":
        """bool

        Args:
            connection (mastapy._private.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.CanDeleteConnection(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def connect_to(
        self: "Self", component: "Component"
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: "Self", socket: "_2349.Socket"
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy._private.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_coordinate_system_editor(self: "Self") -> "_1546.CoordinateSystemEditor":
        """mastapy._private.math_utility.CoordinateSystemEditor"""
        method_result = self.wrapped.CreateCoordinateSystemEditor()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def diameter_at_middle_of_connection(
        self: "Self", connection: "_2325.Connection"
    ) -> "float":
        """float

        Args:
            connection (mastapy._private.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.DiameterAtMiddleOfConnection(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def diameter_of_socket_for(self: "Self", connection: "_2325.Connection") -> "float":
        """float

        Args:
            connection (mastapy._private.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.DiameterOfSocketFor(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def is_coaxially_connected_to(self: "Self", component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsCoaxiallyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def is_directly_connected_to(self: "Self", component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsDirectlyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def is_directly_or_indirectly_connected_to(
        self: "Self", component: "Component"
    ) -> "bool":
        """bool

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsDirectlyOrIndirectlyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def move_all_concentric_parts_radially(
        self: "Self", delta_x: "float", delta_y: "float"
    ) -> "bool":
        """bool

        Args:
            delta_x (float)
            delta_y (float)
        """
        delta_x = float(delta_x)
        delta_y = float(delta_y)
        method_result = self.wrapped.MoveAllConcentricPartsRadially(
            delta_x if delta_x else 0.0, delta_y if delta_y else 0.0
        )
        return method_result

    @enforce_parameter_types
    def move_along_axis(self: "Self", delta: "float") -> None:
        """Method does not return.

        Args:
            delta (float)
        """
        delta = float(delta)
        self.wrapped.MoveAlongAxis(delta if delta else 0.0)

    @enforce_parameter_types
    def move_with_concentric_parts_to_new_origin(
        self: "Self", target_origin: "Vector3D"
    ) -> "bool":
        """bool

        Args:
            target_origin (Vector3D)
        """
        target_origin = conversion.mp_to_pn_vector3d(target_origin)
        method_result = self.wrapped.MoveWithConcentricPartsToNewOrigin(target_origin)
        return method_result

    @enforce_parameter_types
    def possible_sockets_to_connect_with_component(
        self: "Self", component: "Component"
    ) -> "List[_2349.Socket]":
        """List[mastapy._private.system_model.connections_and_sockets.Socket]

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.PossibleSocketsToConnectWith.Overloads[_COMPONENT](
                component.wrapped if component else None
            )
        )

    @enforce_parameter_types
    def possible_sockets_to_connect_with(
        self: "Self", socket: "_2349.Socket"
    ) -> "List[_2349.Socket]":
        """List[mastapy._private.system_model.connections_and_sockets.Socket]

        Args:
            socket (mastapy._private.system_model.connections_and_sockets.Socket)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.PossibleSocketsToConnectWith.Overloads[_SOCKET](
                socket.wrapped if socket else None
            )
        )

    @enforce_parameter_types
    def set_position_and_axis_of_component_and_connected_components(
        self: "Self", origin: "Vector3D", z_axis: "Vector3D"
    ) -> "_2344.RealignmentResult":
        """mastapy._private.system_model.connections_and_sockets.RealignmentResult

        Args:
            origin (Vector3D)
            z_axis (Vector3D)
        """
        origin = conversion.mp_to_pn_vector3d(origin)
        z_axis = conversion.mp_to_pn_vector3d(z_axis)
        method_result = (
            self.wrapped.SetPositionAndAxisOfComponentAndConnectedComponents(
                origin, z_axis
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_and_rotation_of_component_and_connected_components(
        self: "Self", new_coordinate_system: "_1545.CoordinateSystem3D"
    ) -> "_2344.RealignmentResult":
        """mastapy._private.system_model.connections_and_sockets.RealignmentResult

        Args:
            new_coordinate_system (mastapy._private.math_utility.CoordinateSystem3D)
        """
        method_result = (
            self.wrapped.SetPositionAndRotationOfComponentAndConnectedComponents(
                new_coordinate_system.wrapped if new_coordinate_system else None
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_of_component_and_connected_components(
        self: "Self", position: "Vector3D"
    ) -> "_2344.RealignmentResult":
        """mastapy._private.system_model.connections_and_sockets.RealignmentResult

        Args:
            position (Vector3D)
        """
        position = conversion.mp_to_pn_vector3d(position)
        method_result = self.wrapped.SetPositionOfComponentAndConnectedComponents(
            position
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_named(self: "Self", socket_name: "str") -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Args:
            socket_name (str)
        """
        socket_name = str(socket_name)
        method_result = self.wrapped.SocketNamed(socket_name if socket_name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_connect_to(
        self: "Self", component: "Component", hint_offset: "float" = float("nan")
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy._private.system_model.part_model.Component)
            hint_offset (float, optional)
        """
        hint_offset = float(hint_offset)
        method_result = self.wrapped.TryConnectTo(
            component.wrapped if component else None,
            hint_offset if hint_offset else 0.0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_Component":
        """Cast to another type.

        Returns:
            _Cast_Component
        """
        return _Cast_Component(self)
