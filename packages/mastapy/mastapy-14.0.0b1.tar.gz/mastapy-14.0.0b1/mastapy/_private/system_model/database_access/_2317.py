"""Databases"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DATABASES = python_net_import("SMT.MastaAPI.SystemModel.DatabaseAccess", "Databases")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.materials import _257, _260, _279
    from mastapy._private.gears.materials import (
        _598,
        _600,
        _602,
        _603,
        _606,
        _620,
        _629,
    )
    from mastapy._private.bolts import _1515, _1517, _1522
    from mastapy._private.system_model.optimization import _2281, _2289
    from mastapy._private.gears.manufacturing.cylindrical.cutters import (
        _728,
        _734,
        _739,
        _740,
    )
    from mastapy._private.gears.manufacturing.cylindrical import _638, _649
    from mastapy._private.electric_machines import _1329, _1347, _1360
    from mastapy._private.gears.manufacturing.bevel import _823
    from mastapy._private.gears.gear_set_pareto_optimiser import (
        _944,
        _945,
        _948,
        _949,
        _954,
        _955,
        _957,
        _958,
        _959,
        _960,
    )
    from mastapy._private.bearings import _1945
    from mastapy._private.shafts import _25
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2620,
    )

    Self = TypeVar("Self", bound="Databases")
    CastSelf = TypeVar("CastSelf", bound="Databases._Cast_Databases")


__docformat__ = "restructuredtext en"
__all__ = ("Databases",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Databases:
    """Special nested class for casting Databases to subclasses."""

    __parent__: "Databases"

    @property
    def databases(self: "CastSelf") -> "Databases":
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
class Databases(_0.APIBase):
    """Databases

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DATABASES

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bearing_material_database(self: "Self") -> "_257.BearingMaterialDatabase":
        """mastapy._private.materials.BearingMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_iso_material_database(
        self: "Self",
    ) -> "_598.BevelGearISOMaterialDatabase":
        """mastapy._private.gears.materials.BevelGearISOMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearIsoMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_material_database(self: "Self") -> "_600.BevelGearMaterialDatabase":
        """mastapy._private.gears.materials.BevelGearMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bolt_geometry_database(self: "Self") -> "_1515.BoltGeometryDatabase":
        """mastapy._private.bolts.BoltGeometryDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltGeometryDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bolt_material_database(self: "Self") -> "_1517.BoltMaterialDatabase":
        """mastapy._private.bolts.BoltMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def clamped_section_material_database(
        self: "Self",
    ) -> "_1522.ClampedSectionMaterialDatabase":
        """mastapy._private.bolts.ClampedSectionMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClampedSectionMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_material_database(self: "Self") -> "_260.ComponentMaterialDatabase":
        """mastapy._private.materials.ComponentMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_optimization_strategy_database(
        self: "Self",
    ) -> "_2281.ConicalGearOptimizationStrategyDatabase":
        """mastapy._private.system_model.optimization.ConicalGearOptimizationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearOptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_formed_wheel_grinder_database(
        self: "Self",
    ) -> "_728.CylindricalFormedWheelGrinderDatabase":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.CylindricalFormedWheelGrinderDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_agma_material_database(
        self: "Self",
    ) -> "_602.CylindricalGearAGMAMaterialDatabase":
        """mastapy._private.gears.materials.CylindricalGearAGMAMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAGMAMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_iso_material_database(
        self: "Self",
    ) -> "_603.CylindricalGearISOMaterialDatabase":
        """mastapy._private.gears.materials.CylindricalGearISOMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_plastic_material_database(
        self: "Self",
    ) -> "_606.CylindricalGearPlasticMaterialDatabase":
        """mastapy._private.gears.materials.CylindricalGearPlasticMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearPlasticMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_plunge_shaver_database(
        self: "Self",
    ) -> "_734.CylindricalGearPlungeShaverDatabase":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.CylindricalGearPlungeShaverDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearPlungeShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_shaver_database(
        self: "Self",
    ) -> "_739.CylindricalGearShaverDatabase":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.CylindricalGearShaverDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_hob_database(self: "Self") -> "_638.CylindricalHobDatabase":
        """mastapy._private.gears.manufacturing.cylindrical.CylindricalHobDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalHobDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_shaper_database(self: "Self") -> "_649.CylindricalShaperDatabase":
        """mastapy._private.gears.manufacturing.cylindrical.CylindricalShaperDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalShaperDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_worm_grinder_database(
        self: "Self",
    ) -> "_740.CylindricalWormGrinderDatabase":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.CylindricalWormGrinderDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalWormGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_conical_gear_material_database(
        self: "Self",
    ) -> "_620.KlingelnbergConicalGearMaterialDatabase":
        """mastapy._private.gears.materials.KlingelnbergConicalGearMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lubrication_detail_database(self: "Self") -> "_279.LubricationDetailDatabase":
        """mastapy._private.materials.LubricationDetailDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationDetailDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def magnet_material_database(self: "Self") -> "_1329.MagnetMaterialDatabase":
        """mastapy._private.electric_machines.MagnetMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnetMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def manufacturing_machine_database(
        self: "Self",
    ) -> "_823.ManufacturingMachineDatabase":
        """mastapy._private.gears.manufacturing.bevel.ManufacturingMachineDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingMachineDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(
        self: "Self",
    ) -> "_944.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
        self: "Self",
    ) -> "_945.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def optimization_strategy_database(
        self: "Self",
    ) -> "_2289.OptimizationStrategyDatabase":
        """mastapy._private.system_model.optimization.OptimizationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
        self: "Self",
    ) -> "_948.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(
        self: "Self",
    ) -> "_949.ParetoCylindricalGearSetOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoCylindricalGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
        self: "Self",
    ) -> "_954.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(
        self: "Self",
    ) -> "_955.ParetoHypoidGearSetOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoHypoidGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
        self: "Self",
    ) -> "_957.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
        self: "Self",
    ) -> "_958.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
        self: "Self",
    ) -> "_959.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(
        self: "Self",
    ) -> "_960.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def raw_material_database(self: "Self") -> "_629.RawMaterialDatabase":
        """mastapy._private.gears.materials.RawMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RawMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rolling_bearing_database(self: "Self") -> "_1945.RollingBearingDatabase":
        """mastapy._private.bearings.RollingBearingDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingBearingDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_material_database(self: "Self") -> "_25.ShaftMaterialDatabase":
        """mastapy._private.shafts.ShaftMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_and_rotor_material_database(
        self: "Self",
    ) -> "_1347.StatorRotorMaterialDatabase":
        """mastapy._private.electric_machines.StatorRotorMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorAndRotorMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def supercharger_rotor_set_database(
        self: "Self",
    ) -> "_2620.SuperchargerRotorSetDatabase":
        """mastapy._private.system_model.part_model.gears.supercharger_rotor_set.SuperchargerRotorSetDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerRotorSetDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def winding_material_database(self: "Self") -> "_1360.WindingMaterialDatabase":
        """mastapy._private.electric_machines.WindingMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_Databases":
        """Cast to another type.

        Returns:
            _Cast_Databases
        """
        return _Cast_Databases(self)
