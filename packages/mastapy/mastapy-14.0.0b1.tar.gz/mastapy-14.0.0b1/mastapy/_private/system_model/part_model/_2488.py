"""AbstractAssembly"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.part_model import _2524
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import (
        _2498,
        _2487,
        _2497,
        _2508,
        _2519,
        _2530,
        _2532,
    )
    from mastapy._private.system_model.part_model.gears import (
        _2570,
        _2572,
        _2576,
        _2578,
        _2580,
        _2582,
        _2585,
        _2588,
        _2591,
        _2593,
        _2595,
        _2597,
        _2598,
        _2600,
        _2602,
        _2604,
        _2608,
        _2610,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2624
    from mastapy._private.system_model.part_model.couplings import (
        _2633,
        _2635,
        _2638,
        _2641,
        _2644,
        _2646,
        _2656,
        _2662,
        _2664,
        _2669,
    )
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="AbstractAssembly")
    CastSelf = TypeVar("CastSelf", bound="AbstractAssembly._Cast_AbstractAssembly")


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssembly",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssembly:
    """Special nested class for casting AbstractAssembly to subclasses."""

    __parent__: "AbstractAssembly"

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def assembly(self: "CastSelf") -> "_2487.Assembly":
        from mastapy._private.system_model.part_model import _2487

        return self.__parent__._cast(_2487.Assembly)

    @property
    def bolted_joint(self: "CastSelf") -> "_2497.BoltedJoint":
        from mastapy._private.system_model.part_model import _2497

        return self.__parent__._cast(_2497.BoltedJoint)

    @property
    def flexible_pin_assembly(self: "CastSelf") -> "_2508.FlexiblePinAssembly":
        from mastapy._private.system_model.part_model import _2508

        return self.__parent__._cast(_2508.FlexiblePinAssembly)

    @property
    def microphone_array(self: "CastSelf") -> "_2519.MicrophoneArray":
        from mastapy._private.system_model.part_model import _2519

        return self.__parent__._cast(_2519.MicrophoneArray)

    @property
    def root_assembly(self: "CastSelf") -> "_2530.RootAssembly":
        from mastapy._private.system_model.part_model import _2530

        return self.__parent__._cast(_2530.RootAssembly)

    @property
    def specialised_assembly(self: "CastSelf") -> "_2532.SpecialisedAssembly":
        from mastapy._private.system_model.part_model import _2532

        return self.__parent__._cast(_2532.SpecialisedAssembly)

    @property
    def agma_gleason_conical_gear_set(
        self: "CastSelf",
    ) -> "_2570.AGMAGleasonConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2570

        return self.__parent__._cast(_2570.AGMAGleasonConicalGearSet)

    @property
    def bevel_differential_gear_set(
        self: "CastSelf",
    ) -> "_2572.BevelDifferentialGearSet":
        from mastapy._private.system_model.part_model.gears import _2572

        return self.__parent__._cast(_2572.BevelDifferentialGearSet)

    @property
    def bevel_gear_set(self: "CastSelf") -> "_2576.BevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2576

        return self.__parent__._cast(_2576.BevelGearSet)

    @property
    def concept_gear_set(self: "CastSelf") -> "_2578.ConceptGearSet":
        from mastapy._private.system_model.part_model.gears import _2578

        return self.__parent__._cast(_2578.ConceptGearSet)

    @property
    def conical_gear_set(self: "CastSelf") -> "_2580.ConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2580

        return self.__parent__._cast(_2580.ConicalGearSet)

    @property
    def cylindrical_gear_set(self: "CastSelf") -> "_2582.CylindricalGearSet":
        from mastapy._private.system_model.part_model.gears import _2582

        return self.__parent__._cast(_2582.CylindricalGearSet)

    @property
    def face_gear_set(self: "CastSelf") -> "_2585.FaceGearSet":
        from mastapy._private.system_model.part_model.gears import _2585

        return self.__parent__._cast(_2585.FaceGearSet)

    @property
    def gear_set(self: "CastSelf") -> "_2588.GearSet":
        from mastapy._private.system_model.part_model.gears import _2588

        return self.__parent__._cast(_2588.GearSet)

    @property
    def hypoid_gear_set(self: "CastSelf") -> "_2591.HypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2591

        return self.__parent__._cast(_2591.HypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set(
        self: "CastSelf",
    ) -> "_2593.KlingelnbergCycloPalloidConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2593

        return self.__parent__._cast(_2593.KlingelnbergCycloPalloidConicalGearSet)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "CastSelf",
    ) -> "_2595.KlingelnbergCycloPalloidHypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2595

        return self.__parent__._cast(_2595.KlingelnbergCycloPalloidHypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "CastSelf",
    ) -> "_2597.KlingelnbergCycloPalloidSpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2597

        return self.__parent__._cast(_2597.KlingelnbergCycloPalloidSpiralBevelGearSet)

    @property
    def planetary_gear_set(self: "CastSelf") -> "_2598.PlanetaryGearSet":
        from mastapy._private.system_model.part_model.gears import _2598

        return self.__parent__._cast(_2598.PlanetaryGearSet)

    @property
    def spiral_bevel_gear_set(self: "CastSelf") -> "_2600.SpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2600

        return self.__parent__._cast(_2600.SpiralBevelGearSet)

    @property
    def straight_bevel_diff_gear_set(
        self: "CastSelf",
    ) -> "_2602.StraightBevelDiffGearSet":
        from mastapy._private.system_model.part_model.gears import _2602

        return self.__parent__._cast(_2602.StraightBevelDiffGearSet)

    @property
    def straight_bevel_gear_set(self: "CastSelf") -> "_2604.StraightBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2604

        return self.__parent__._cast(_2604.StraightBevelGearSet)

    @property
    def worm_gear_set(self: "CastSelf") -> "_2608.WormGearSet":
        from mastapy._private.system_model.part_model.gears import _2608

        return self.__parent__._cast(_2608.WormGearSet)

    @property
    def zerol_bevel_gear_set(self: "CastSelf") -> "_2610.ZerolBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2610

        return self.__parent__._cast(_2610.ZerolBevelGearSet)

    @property
    def cycloidal_assembly(self: "CastSelf") -> "_2624.CycloidalAssembly":
        from mastapy._private.system_model.part_model.cycloidal import _2624

        return self.__parent__._cast(_2624.CycloidalAssembly)

    @property
    def belt_drive(self: "CastSelf") -> "_2633.BeltDrive":
        from mastapy._private.system_model.part_model.couplings import _2633

        return self.__parent__._cast(_2633.BeltDrive)

    @property
    def clutch(self: "CastSelf") -> "_2635.Clutch":
        from mastapy._private.system_model.part_model.couplings import _2635

        return self.__parent__._cast(_2635.Clutch)

    @property
    def concept_coupling(self: "CastSelf") -> "_2638.ConceptCoupling":
        from mastapy._private.system_model.part_model.couplings import _2638

        return self.__parent__._cast(_2638.ConceptCoupling)

    @property
    def coupling(self: "CastSelf") -> "_2641.Coupling":
        from mastapy._private.system_model.part_model.couplings import _2641

        return self.__parent__._cast(_2641.Coupling)

    @property
    def cvt(self: "CastSelf") -> "_2644.CVT":
        from mastapy._private.system_model.part_model.couplings import _2644

        return self.__parent__._cast(_2644.CVT)

    @property
    def part_to_part_shear_coupling(
        self: "CastSelf",
    ) -> "_2646.PartToPartShearCoupling":
        from mastapy._private.system_model.part_model.couplings import _2646

        return self.__parent__._cast(_2646.PartToPartShearCoupling)

    @property
    def rolling_ring_assembly(self: "CastSelf") -> "_2656.RollingRingAssembly":
        from mastapy._private.system_model.part_model.couplings import _2656

        return self.__parent__._cast(_2656.RollingRingAssembly)

    @property
    def spring_damper(self: "CastSelf") -> "_2662.SpringDamper":
        from mastapy._private.system_model.part_model.couplings import _2662

        return self.__parent__._cast(_2662.SpringDamper)

    @property
    def synchroniser(self: "CastSelf") -> "_2664.Synchroniser":
        from mastapy._private.system_model.part_model.couplings import _2664

        return self.__parent__._cast(_2664.Synchroniser)

    @property
    def torque_converter(self: "CastSelf") -> "_2669.TorqueConverter":
        from mastapy._private.system_model.part_model.couplings import _2669

        return self.__parent__._cast(_2669.TorqueConverter)

    @property
    def abstract_assembly(self: "CastSelf") -> "AbstractAssembly":
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
class AbstractAssembly(_2524.Part):
    """AbstractAssembly

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def mass_of_assembly(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassOfAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def components_with_unknown_mass_properties(
        self: "Self",
    ) -> "List[_2498.Component]":
        """List[mastapy._private.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(self: "Self") -> "List[_2498.Component]":
        """List[mastapy._private.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractAssembly":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssembly
        """
        return _Cast_AbstractAssembly(self)
