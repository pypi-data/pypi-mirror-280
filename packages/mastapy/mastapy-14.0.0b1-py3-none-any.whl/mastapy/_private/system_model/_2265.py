"""MASTASettings"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MASTA_SETTINGS = python_net_import("SMT.MastaAPI.SystemModel", "MASTASettings")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import _2028
    from mastapy._private.bearings import _1931, _1932, _1945, _1951
    from mastapy._private.bolts import _1515, _1517, _1522
    from mastapy._private.cycloidal import _1503, _1510
    from mastapy._private.electric_machines import _1329, _1347, _1360
    from mastapy._private.gears import _326, _327, _353
    from mastapy._private.gears.gear_designs import _964, _966, _969, _975
    from mastapy._private.gears.gear_designs.cylindrical import (
        _1041,
        _1045,
        _1046,
        _1051,
        _1062,
    )
    from mastapy._private.gears.gear_set_pareto_optimiser import (
        _944,
        _945,
        _948,
        _949,
        _951,
        _952,
        _954,
        _955,
        _957,
        _958,
        _959,
        _960,
    )
    from mastapy._private.gears.ltca.cylindrical import _878
    from mastapy._private.gears.manufacturing.bevel import _823
    from mastapy._private.gears.manufacturing.cylindrical.cutters import (
        _728,
        _734,
        _739,
        _740,
    )
    from mastapy._private.gears.manufacturing.cylindrical import _638, _649
    from mastapy._private.gears.materials import (
        _598,
        _600,
        _602,
        _603,
        _606,
        _610,
        _619,
        _620,
        _629,
    )
    from mastapy._private.gears.rating.cylindrical import _463, _464, _479, _480
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6726,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5892,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5584
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4769
    from mastapy._private.system_model.analyses_and_results.power_flows import _4228
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3972,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3179,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2911,
    )
    from mastapy._private.system_model.drawing import _2305
    from mastapy._private.system_model.optimization import _2281, _2289
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2620,
    )
    from mastapy._private.system_model.part_model import _2526
    from mastapy._private.materials import _257, _260, _279, _282, _283
    from mastapy._private.nodal_analysis import _48, _49, _68
    from mastapy._private.nodal_analysis.geometry_modeller_link import _167
    from mastapy._private.shafts import _25, _38, _39
    from mastapy._private.utility.cad_export import _1882
    from mastapy._private.utility.databases import _1877
    from mastapy._private.utility import _1643, _1644
    from mastapy._private.utility.scripting import _1787
    from mastapy._private.utility.units_and_measurements import _1653

    Self = TypeVar("Self", bound="MASTASettings")
    CastSelf = TypeVar("CastSelf", bound="MASTASettings._Cast_MASTASettings")


__docformat__ = "restructuredtext en"
__all__ = ("MASTASettings",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MASTASettings:
    """Special nested class for casting MASTASettings to subclasses."""

    __parent__: "MASTASettings"

    @property
    def masta_settings(self: "CastSelf") -> "MASTASettings":
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
class MASTASettings(_0.APIBase):
    """MASTASettings

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MASTA_SETTINGS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def iso14179_settings_database(self: "Self") -> "_2028.ISO14179SettingsDatabase":
        """mastapy._private.bearings.bearing_results.rolling.ISO14179SettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179SettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_settings(self: "Self") -> "_1931.BearingSettings":
        """mastapy._private.bearings.BearingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_settings_database(self: "Self") -> "_1932.BearingSettingsDatabase":
        """mastapy._private.bearings.BearingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSettingsDatabase

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
    def skf_settings(self: "Self") -> "_1951.SKFSettings":
        """mastapy._private.bearings.SKFSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFSettings

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
    def cycloidal_disc_material_database(
        self: "Self",
    ) -> "_1503.CycloidalDiscMaterialDatabase":
        """mastapy._private.cycloidal.CycloidalDiscMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins_material_database(self: "Self") -> "_1510.RingPinsMaterialDatabase":
        """mastapy._private.cycloidal.RingPinsMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinsMaterialDatabase

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
    def stator_rotor_material_database(
        self: "Self",
    ) -> "_1347.StatorRotorMaterialDatabase":
        """mastapy._private.electric_machines.StatorRotorMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorRotorMaterialDatabase

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
    def bevel_hypoid_gear_design_settings(
        self: "Self",
    ) -> "_326.BevelHypoidGearDesignSettings":
        """mastapy._private.gears.BevelHypoidGearDesignSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearDesignSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_rating_settings(
        self: "Self",
    ) -> "_327.BevelHypoidGearRatingSettings":
        """mastapy._private.gears.BevelHypoidGearRatingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_design_settings_database(
        self: "Self",
    ) -> "_964.BevelHypoidGearDesignSettingsDatabase":
        """mastapy._private.gears.gear_designs.BevelHypoidGearDesignSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_rating_settings_database(
        self: "Self",
    ) -> "_966.BevelHypoidGearRatingSettingsDatabase":
        """mastapy._private.gears.gear_designs.BevelHypoidGearRatingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_defaults(self: "Self") -> "_1041.CylindricalGearDefaults":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearDefaults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDefaults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_constraints_database(
        self: "Self",
    ) -> "_1045.CylindricalGearDesignConstraintsDatabase":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearDesignConstraintsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignConstraintsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_constraint_settings(
        self: "Self",
    ) -> "_1046.CylindricalGearDesignConstraintSettings":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearDesignConstraintSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignConstraintSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_micro_geometry_settings_database(
        self: "Self",
    ) -> "_1051.CylindricalGearMicroGeometrySettingsDatabase":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometrySettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_micro_geometry_settings(
        self: "Self",
    ) -> "_1062.CylindricalGearSetMicroGeometrySettings":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearSetMicroGeometrySettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_constraint_collection_database(
        self: "Self",
    ) -> "_969.DesignConstraintCollectionDatabase":
        """mastapy._private.gears.gear_designs.DesignConstraintCollectionDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignConstraintCollectionDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_design_constraints_collection(
        self: "Self",
    ) -> "_975.SelectedDesignConstraintsCollection":
        """mastapy._private.gears.gear_designs.SelectedDesignConstraintsCollection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedDesignConstraintsCollection

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
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
        self: "Self",
    ) -> "_951.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_face_gear_set_optimisation_strategy_database(
        self: "Self",
    ) -> "_952.ParetoFaceGearSetOptimisationStrategyDatabase":
        """mastapy._private.gears.gear_set_pareto_optimiser.ParetoFaceGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoFaceGearSetOptimisationStrategyDatabase

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
    def cylindrical_gear_fe_settings(self: "Self") -> "_878.CylindricalGearFESettings":
        """mastapy._private.gears.ltca.cylindrical.CylindricalGearFESettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearFESettings

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
    def bevel_gear_iso_material_database(
        self: "Self",
    ) -> "_598.BevelGearISOMaterialDatabase":
        """mastapy._private.gears.materials.BevelGearISOMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearISOMaterialDatabase

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
    def gear_material_expert_system_factor_settings(
        self: "Self",
    ) -> "_610.GearMaterialExpertSystemFactorSettings":
        """mastapy._private.gears.materials.GearMaterialExpertSystemFactorSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMaterialExpertSystemFactorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isotr1417912001_coefficient_of_friction_constants_database(
        self: "Self",
    ) -> "_619.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
        """mastapy._private.gears.materials.ISOTR1417912001CoefficientOfFrictionConstantsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTR1417912001CoefficientOfFrictionConstantsDatabase

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
    def pocketing_power_loss_coefficients_database(
        self: "Self",
    ) -> "_353.PocketingPowerLossCoefficientsDatabase":
        """mastapy._private.gears.PocketingPowerLossCoefficientsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PocketingPowerLossCoefficientsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_and_rating_settings(
        self: "Self",
    ) -> "_463.CylindricalGearDesignAndRatingSettings":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignAndRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_and_rating_settings_database(
        self: "Self",
    ) -> "_464.CylindricalGearDesignAndRatingSettingsDatabase":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_plastic_gear_rating_settings(
        self: "Self",
    ) -> "_479.CylindricalPlasticGearRatingSettings":
        """mastapy._private.gears.rating.cylindrical.CylindricalPlasticGearRatingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalPlasticGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_plastic_gear_rating_settings_database(
        self: "Self",
    ) -> "_480.CylindricalPlasticGearRatingSettingsDatabase":
        """mastapy._private.gears.rating.cylindrical.CylindricalPlasticGearRatingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalPlasticGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speed_analysis_draw_style(
        self: "Self",
    ) -> "_6726.CriticalSpeedAnalysisDrawStyle":
        """mastapy._private.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_draw_style(self: "Self") -> "_5892.HarmonicAnalysisDrawStyle":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mbd_analysis_draw_style(self: "Self") -> "_5584.MBDAnalysisDrawStyle":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MBDAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MBDAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_draw_style(self: "Self") -> "_4769.ModalAnalysisDrawStyle":
        """mastapy._private.system_model.analyses_and_results.modal_analyses.ModalAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_draw_style(self: "Self") -> "_4228.PowerFlowDrawStyle":
        """mastapy._private.system_model.analyses_and_results.power_flows.PowerFlowDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stability_analysis_draw_style(
        self: "Self",
    ) -> "_3972.StabilityAnalysisDrawStyle":
        """mastapy._private.system_model.analyses_and_results.stability_analyses.StabilityAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_draw_style(
        self: "Self",
    ) -> "_3179.SteadyStateSynchronousResponseDrawStyle":
        """mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponseDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_draw_style(self: "Self") -> "_2911.SystemDeflectionDrawStyle":
        """mastapy._private.system_model.analyses_and_results.system_deflections.SystemDeflectionDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def model_view_options_draw_style(
        self: "Self",
    ) -> "_2305.ModelViewOptionsDrawStyle":
        """mastapy._private.system_model.drawing.ModelViewOptionsDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelViewOptionsDrawStyle

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
    def planet_carrier_settings(self: "Self") -> "_2526.PlanetCarrierSettings":
        """mastapy._private.system_model.part_model.PlanetCarrierSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetCarrierSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def materials_settings(self: "Self") -> "_282.MaterialsSettings":
        """mastapy._private.materials.MaterialsSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def materials_settings_database(self: "Self") -> "_283.MaterialsSettingsDatabase":
        """mastapy._private.materials.MaterialsSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialsSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analysis_settings(self: "Self") -> "_48.AnalysisSettings":
        """mastapy._private.nodal_analysis.AnalysisSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analysis_settings_database(self: "Self") -> "_49.AnalysisSettingsDatabase":
        """mastapy._private.nodal_analysis.AnalysisSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_user_settings(self: "Self") -> "_68.FEUserSettings":
        """mastapy._private.nodal_analysis.FEUserSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEUserSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def geometry_modeller_settings(self: "Self") -> "_167.GeometryModellerSettings":
        """mastapy._private.nodal_analysis.geometry_modeller_link.GeometryModellerSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryModellerSettings

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
    def shaft_settings(self: "Self") -> "_38.ShaftSettings":
        """mastapy._private.shafts.ShaftSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_settings_database(self: "Self") -> "_39.ShaftSettingsDatabase":
        """mastapy._private.shafts.ShaftSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cad_export_settings(self: "Self") -> "_1882.CADExportSettings":
        """mastapy._private.utility.cad_export.CADExportSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CADExportSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def database_settings(self: "Self") -> "_1877.DatabaseSettings":
        """mastapy._private.utility.databases.DatabaseSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DatabaseSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def program_settings(self: "Self") -> "_1643.ProgramSettings":
        """mastapy._private.utility.ProgramSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProgramSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pushbullet_settings(self: "Self") -> "_1644.PushbulletSettings":
        """mastapy._private.utility.PushbulletSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PushbulletSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scripting_setup(self: "Self") -> "_1787.ScriptingSetup":
        """mastapy._private.utility.scripting.ScriptingSetup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScriptingSetup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def measurement_settings(self: "Self") -> "_1653.MeasurementSettings":
        """mastapy._private.utility.units_and_measurements.MeasurementSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_MASTASettings":
        """Cast to another type.

        Returns:
            _Cast_MASTASettings
        """
        return _Cast_MASTASettings(self)
