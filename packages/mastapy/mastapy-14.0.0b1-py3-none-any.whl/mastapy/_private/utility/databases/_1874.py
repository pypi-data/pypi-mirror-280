"""Database"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "Database")

if TYPE_CHECKING:
    from typing import Any, Type, List

    from mastapy._private.utility.databases import _1876, _1878, _1881
    from mastapy._private.shafts import _25, _39
    from mastapy._private.nodal_analysis import _49
    from mastapy._private.materials import _257, _260, _279, _281, _283
    from mastapy._private.gears import _353
    from mastapy._private.gears.rating.cylindrical import _464, _480
    from mastapy._private.gears.materials import (
        _596,
        _598,
        _600,
        _602,
        _603,
        _605,
        _606,
        _609,
        _619,
        _620,
        _629,
    )
    from mastapy._private.gears.manufacturing.cylindrical import _633, _638, _649
    from mastapy._private.gears.manufacturing.cylindrical.cutters import (
        _728,
        _734,
        _739,
        _740,
    )
    from mastapy._private.gears.manufacturing.bevel import _823
    from mastapy._private.gears.gear_set_pareto_optimiser import (
        _942,
        _944,
        _945,
        _947,
        _948,
        _949,
        _950,
        _951,
        _952,
        _953,
        _954,
        _955,
        _957,
        _958,
        _959,
        _960,
    )
    from mastapy._private.gears.gear_designs import _964, _966, _969
    from mastapy._private.gears.gear_designs.cylindrical import _1045, _1051
    from mastapy._private.electric_machines import _1329, _1347, _1360
    from mastapy._private.cycloidal import _1503, _1510
    from mastapy._private.bolts import _1513, _1515, _1517, _1522
    from mastapy._private.math_utility.optimisation import _1586, _1598
    from mastapy._private.bearings import _1932, _1945
    from mastapy._private.bearings.bearing_results.rolling import _2028
    from mastapy._private.system_model.optimization import _2281, _2289
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2620,
    )

    Self = TypeVar("Self", bound="Database")
    CastSelf = TypeVar("CastSelf", bound="Database._Cast_Database")

TKey = TypeVar("TKey", bound="_1876.DatabaseKey")
TValue = TypeVar("TValue", bound="_0.APIBase")

__docformat__ = "restructuredtext en"
__all__ = ("Database",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Database:
    """Special nested class for casting Database to subclasses."""

    __parent__: "Database"

    @property
    def shaft_material_database(self: "CastSelf") -> "_25.ShaftMaterialDatabase":
        from mastapy._private.shafts import _25

        return self.__parent__._cast(_25.ShaftMaterialDatabase)

    @property
    def shaft_settings_database(self: "CastSelf") -> "_39.ShaftSettingsDatabase":
        from mastapy._private.shafts import _39

        return self.__parent__._cast(_39.ShaftSettingsDatabase)

    @property
    def analysis_settings_database(self: "CastSelf") -> "_49.AnalysisSettingsDatabase":
        from mastapy._private.nodal_analysis import _49

        return self.__parent__._cast(_49.AnalysisSettingsDatabase)

    @property
    def bearing_material_database(self: "CastSelf") -> "_257.BearingMaterialDatabase":
        from mastapy._private.materials import _257

        return self.__parent__._cast(_257.BearingMaterialDatabase)

    @property
    def component_material_database(
        self: "CastSelf",
    ) -> "_260.ComponentMaterialDatabase":
        from mastapy._private.materials import _260

        return self.__parent__._cast(_260.ComponentMaterialDatabase)

    @property
    def lubrication_detail_database(
        self: "CastSelf",
    ) -> "_279.LubricationDetailDatabase":
        from mastapy._private.materials import _279

        return self.__parent__._cast(_279.LubricationDetailDatabase)

    @property
    def material_database(self: "CastSelf") -> "_281.MaterialDatabase":
        from mastapy._private.materials import _281

        return self.__parent__._cast(_281.MaterialDatabase)

    @property
    def materials_settings_database(
        self: "CastSelf",
    ) -> "_283.MaterialsSettingsDatabase":
        from mastapy._private.materials import _283

        return self.__parent__._cast(_283.MaterialsSettingsDatabase)

    @property
    def pocketing_power_loss_coefficients_database(
        self: "CastSelf",
    ) -> "_353.PocketingPowerLossCoefficientsDatabase":
        from mastapy._private.gears import _353

        return self.__parent__._cast(_353.PocketingPowerLossCoefficientsDatabase)

    @property
    def cylindrical_gear_design_and_rating_settings_database(
        self: "CastSelf",
    ) -> "_464.CylindricalGearDesignAndRatingSettingsDatabase":
        from mastapy._private.gears.rating.cylindrical import _464

        return self.__parent__._cast(
            _464.CylindricalGearDesignAndRatingSettingsDatabase
        )

    @property
    def cylindrical_plastic_gear_rating_settings_database(
        self: "CastSelf",
    ) -> "_480.CylindricalPlasticGearRatingSettingsDatabase":
        from mastapy._private.gears.rating.cylindrical import _480

        return self.__parent__._cast(_480.CylindricalPlasticGearRatingSettingsDatabase)

    @property
    def bevel_gear_abstract_material_database(
        self: "CastSelf",
    ) -> "_596.BevelGearAbstractMaterialDatabase":
        from mastapy._private.gears.materials import _596

        return self.__parent__._cast(_596.BevelGearAbstractMaterialDatabase)

    @property
    def bevel_gear_iso_material_database(
        self: "CastSelf",
    ) -> "_598.BevelGearISOMaterialDatabase":
        from mastapy._private.gears.materials import _598

        return self.__parent__._cast(_598.BevelGearISOMaterialDatabase)

    @property
    def bevel_gear_material_database(
        self: "CastSelf",
    ) -> "_600.BevelGearMaterialDatabase":
        from mastapy._private.gears.materials import _600

        return self.__parent__._cast(_600.BevelGearMaterialDatabase)

    @property
    def cylindrical_gear_agma_material_database(
        self: "CastSelf",
    ) -> "_602.CylindricalGearAGMAMaterialDatabase":
        from mastapy._private.gears.materials import _602

        return self.__parent__._cast(_602.CylindricalGearAGMAMaterialDatabase)

    @property
    def cylindrical_gear_iso_material_database(
        self: "CastSelf",
    ) -> "_603.CylindricalGearISOMaterialDatabase":
        from mastapy._private.gears.materials import _603

        return self.__parent__._cast(_603.CylindricalGearISOMaterialDatabase)

    @property
    def cylindrical_gear_material_database(
        self: "CastSelf",
    ) -> "_605.CylindricalGearMaterialDatabase":
        from mastapy._private.gears.materials import _605

        return self.__parent__._cast(_605.CylindricalGearMaterialDatabase)

    @property
    def cylindrical_gear_plastic_material_database(
        self: "CastSelf",
    ) -> "_606.CylindricalGearPlasticMaterialDatabase":
        from mastapy._private.gears.materials import _606

        return self.__parent__._cast(_606.CylindricalGearPlasticMaterialDatabase)

    @property
    def gear_material_database(self: "CastSelf") -> "_609.GearMaterialDatabase":
        from mastapy._private.gears.materials import _609

        return self.__parent__._cast(_609.GearMaterialDatabase)

    @property
    def isotr1417912001_coefficient_of_friction_constants_database(
        self: "CastSelf",
    ) -> "_619.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
        from mastapy._private.gears.materials import _619

        return self.__parent__._cast(
            _619.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
        )

    @property
    def klingelnberg_conical_gear_material_database(
        self: "CastSelf",
    ) -> "_620.KlingelnbergConicalGearMaterialDatabase":
        from mastapy._private.gears.materials import _620

        return self.__parent__._cast(_620.KlingelnbergConicalGearMaterialDatabase)

    @property
    def raw_material_database(self: "CastSelf") -> "_629.RawMaterialDatabase":
        from mastapy._private.gears.materials import _629

        return self.__parent__._cast(_629.RawMaterialDatabase)

    @property
    def cylindrical_cutter_database(
        self: "CastSelf",
    ) -> "_633.CylindricalCutterDatabase":
        from mastapy._private.gears.manufacturing.cylindrical import _633

        return self.__parent__._cast(_633.CylindricalCutterDatabase)

    @property
    def cylindrical_hob_database(self: "CastSelf") -> "_638.CylindricalHobDatabase":
        from mastapy._private.gears.manufacturing.cylindrical import _638

        return self.__parent__._cast(_638.CylindricalHobDatabase)

    @property
    def cylindrical_shaper_database(
        self: "CastSelf",
    ) -> "_649.CylindricalShaperDatabase":
        from mastapy._private.gears.manufacturing.cylindrical import _649

        return self.__parent__._cast(_649.CylindricalShaperDatabase)

    @property
    def cylindrical_formed_wheel_grinder_database(
        self: "CastSelf",
    ) -> "_728.CylindricalFormedWheelGrinderDatabase":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _728

        return self.__parent__._cast(_728.CylindricalFormedWheelGrinderDatabase)

    @property
    def cylindrical_gear_plunge_shaver_database(
        self: "CastSelf",
    ) -> "_734.CylindricalGearPlungeShaverDatabase":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _734

        return self.__parent__._cast(_734.CylindricalGearPlungeShaverDatabase)

    @property
    def cylindrical_gear_shaver_database(
        self: "CastSelf",
    ) -> "_739.CylindricalGearShaverDatabase":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _739

        return self.__parent__._cast(_739.CylindricalGearShaverDatabase)

    @property
    def cylindrical_worm_grinder_database(
        self: "CastSelf",
    ) -> "_740.CylindricalWormGrinderDatabase":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _740

        return self.__parent__._cast(_740.CylindricalWormGrinderDatabase)

    @property
    def manufacturing_machine_database(
        self: "CastSelf",
    ) -> "_823.ManufacturingMachineDatabase":
        from mastapy._private.gears.manufacturing.bevel import _823

        return self.__parent__._cast(_823.ManufacturingMachineDatabase)

    @property
    def micro_geometry_design_space_search_strategy_database(
        self: "CastSelf",
    ) -> "_942.MicroGeometryDesignSpaceSearchStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _942

        return self.__parent__._cast(
            _942.MicroGeometryDesignSpaceSearchStrategyDatabase
        )

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(
        self: "CastSelf",
    ) -> "_944.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _944

        return self.__parent__._cast(
            _944.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
        )

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
        self: "CastSelf",
    ) -> "_945.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _945

        return self.__parent__._cast(
            _945.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
        )

    @property
    def pareto_conical_rating_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_947.ParetoConicalRatingOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _947

        return self.__parent__._cast(
            _947.ParetoConicalRatingOptimisationStrategyDatabase
        )

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_948.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _948

        return self.__parent__._cast(
            _948.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
        )

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_949.ParetoCylindricalGearSetOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _949

        return self.__parent__._cast(
            _949.ParetoCylindricalGearSetOptimisationStrategyDatabase
        )

    @property
    def pareto_cylindrical_rating_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_950.ParetoCylindricalRatingOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _950

        return self.__parent__._cast(
            _950.ParetoCylindricalRatingOptimisationStrategyDatabase
        )

    @property
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_951.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _951

        return self.__parent__._cast(
            _951.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
        )

    @property
    def pareto_face_gear_set_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_952.ParetoFaceGearSetOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _952

        return self.__parent__._cast(_952.ParetoFaceGearSetOptimisationStrategyDatabase)

    @property
    def pareto_face_rating_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_953.ParetoFaceRatingOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _953

        return self.__parent__._cast(_953.ParetoFaceRatingOptimisationStrategyDatabase)

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_954.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _954

        return self.__parent__._cast(
            _954.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
        )

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_955.ParetoHypoidGearSetOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _955

        return self.__parent__._cast(
            _955.ParetoHypoidGearSetOptimisationStrategyDatabase
        )

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_957.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _957

        return self.__parent__._cast(
            _957.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
        )

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_958.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _958

        return self.__parent__._cast(
            _958.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
        )

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_959.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _959

        return self.__parent__._cast(
            _959.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
        )

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_960.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
        from mastapy._private.gears.gear_set_pareto_optimiser import _960

        return self.__parent__._cast(
            _960.ParetoStraightBevelGearSetOptimisationStrategyDatabase
        )

    @property
    def bevel_hypoid_gear_design_settings_database(
        self: "CastSelf",
    ) -> "_964.BevelHypoidGearDesignSettingsDatabase":
        from mastapy._private.gears.gear_designs import _964

        return self.__parent__._cast(_964.BevelHypoidGearDesignSettingsDatabase)

    @property
    def bevel_hypoid_gear_rating_settings_database(
        self: "CastSelf",
    ) -> "_966.BevelHypoidGearRatingSettingsDatabase":
        from mastapy._private.gears.gear_designs import _966

        return self.__parent__._cast(_966.BevelHypoidGearRatingSettingsDatabase)

    @property
    def design_constraint_collection_database(
        self: "CastSelf",
    ) -> "_969.DesignConstraintCollectionDatabase":
        from mastapy._private.gears.gear_designs import _969

        return self.__parent__._cast(_969.DesignConstraintCollectionDatabase)

    @property
    def cylindrical_gear_design_constraints_database(
        self: "CastSelf",
    ) -> "_1045.CylindricalGearDesignConstraintsDatabase":
        from mastapy._private.gears.gear_designs.cylindrical import _1045

        return self.__parent__._cast(_1045.CylindricalGearDesignConstraintsDatabase)

    @property
    def cylindrical_gear_micro_geometry_settings_database(
        self: "CastSelf",
    ) -> "_1051.CylindricalGearMicroGeometrySettingsDatabase":
        from mastapy._private.gears.gear_designs.cylindrical import _1051

        return self.__parent__._cast(_1051.CylindricalGearMicroGeometrySettingsDatabase)

    @property
    def magnet_material_database(self: "CastSelf") -> "_1329.MagnetMaterialDatabase":
        from mastapy._private.electric_machines import _1329

        return self.__parent__._cast(_1329.MagnetMaterialDatabase)

    @property
    def stator_rotor_material_database(
        self: "CastSelf",
    ) -> "_1347.StatorRotorMaterialDatabase":
        from mastapy._private.electric_machines import _1347

        return self.__parent__._cast(_1347.StatorRotorMaterialDatabase)

    @property
    def winding_material_database(self: "CastSelf") -> "_1360.WindingMaterialDatabase":
        from mastapy._private.electric_machines import _1360

        return self.__parent__._cast(_1360.WindingMaterialDatabase)

    @property
    def cycloidal_disc_material_database(
        self: "CastSelf",
    ) -> "_1503.CycloidalDiscMaterialDatabase":
        from mastapy._private.cycloidal import _1503

        return self.__parent__._cast(_1503.CycloidalDiscMaterialDatabase)

    @property
    def ring_pins_material_database(
        self: "CastSelf",
    ) -> "_1510.RingPinsMaterialDatabase":
        from mastapy._private.cycloidal import _1510

        return self.__parent__._cast(_1510.RingPinsMaterialDatabase)

    @property
    def bolted_joint_material_database(
        self: "CastSelf",
    ) -> "_1513.BoltedJointMaterialDatabase":
        from mastapy._private.bolts import _1513

        return self.__parent__._cast(_1513.BoltedJointMaterialDatabase)

    @property
    def bolt_geometry_database(self: "CastSelf") -> "_1515.BoltGeometryDatabase":
        from mastapy._private.bolts import _1515

        return self.__parent__._cast(_1515.BoltGeometryDatabase)

    @property
    def bolt_material_database(self: "CastSelf") -> "_1517.BoltMaterialDatabase":
        from mastapy._private.bolts import _1517

        return self.__parent__._cast(_1517.BoltMaterialDatabase)

    @property
    def clamped_section_material_database(
        self: "CastSelf",
    ) -> "_1522.ClampedSectionMaterialDatabase":
        from mastapy._private.bolts import _1522

        return self.__parent__._cast(_1522.ClampedSectionMaterialDatabase)

    @property
    def design_space_search_strategy_database(
        self: "CastSelf",
    ) -> "_1586.DesignSpaceSearchStrategyDatabase":
        from mastapy._private.math_utility.optimisation import _1586

        return self.__parent__._cast(_1586.DesignSpaceSearchStrategyDatabase)

    @property
    def pareto_optimisation_strategy_database(
        self: "CastSelf",
    ) -> "_1598.ParetoOptimisationStrategyDatabase":
        from mastapy._private.math_utility.optimisation import _1598

        return self.__parent__._cast(_1598.ParetoOptimisationStrategyDatabase)

    @property
    def named_database(self: "CastSelf") -> "_1878.NamedDatabase":
        from mastapy._private.utility.databases import _1878

        return self.__parent__._cast(_1878.NamedDatabase)

    @property
    def sql_database(self: "CastSelf") -> "_1881.SQLDatabase":
        from mastapy._private.utility.databases import _1881

        return self.__parent__._cast(_1881.SQLDatabase)

    @property
    def bearing_settings_database(self: "CastSelf") -> "_1932.BearingSettingsDatabase":
        from mastapy._private.bearings import _1932

        return self.__parent__._cast(_1932.BearingSettingsDatabase)

    @property
    def rolling_bearing_database(self: "CastSelf") -> "_1945.RollingBearingDatabase":
        from mastapy._private.bearings import _1945

        return self.__parent__._cast(_1945.RollingBearingDatabase)

    @property
    def iso14179_settings_database(
        self: "CastSelf",
    ) -> "_2028.ISO14179SettingsDatabase":
        from mastapy._private.bearings.bearing_results.rolling import _2028

        return self.__parent__._cast(_2028.ISO14179SettingsDatabase)

    @property
    def conical_gear_optimization_strategy_database(
        self: "CastSelf",
    ) -> "_2281.ConicalGearOptimizationStrategyDatabase":
        from mastapy._private.system_model.optimization import _2281

        return self.__parent__._cast(_2281.ConicalGearOptimizationStrategyDatabase)

    @property
    def optimization_strategy_database(
        self: "CastSelf",
    ) -> "_2289.OptimizationStrategyDatabase":
        from mastapy._private.system_model.optimization import _2289

        return self.__parent__._cast(_2289.OptimizationStrategyDatabase)

    @property
    def supercharger_rotor_set_database(
        self: "CastSelf",
    ) -> "_2620.SuperchargerRotorSetDatabase":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2620,
        )

        return self.__parent__._cast(_2620.SuperchargerRotorSetDatabase)

    @property
    def database(self: "CastSelf") -> "Database":
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
class Database(_0.APIBase, Generic[TKey, TValue]):
    """Database

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE: ClassVar["Type"] = _DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def count(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Count

        if temp is None:
            return 0

        return temp

    @enforce_parameter_types
    def can_be_removed(self: "Self", item: "TValue") -> "bool":
        """bool

        Args:
            item (TValue)
        """
        method_result = self.wrapped.CanBeRemoved(item)
        return method_result

    def get_all_items(self: "Self") -> "List[TValue]":
        """List[TValue]"""
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetAllItems())

    @property
    def cast_to(self: "Self") -> "_Cast_Database":
        """Cast to another type.

        Returns:
            _Cast_Database
        """
        return _Cast_Database(self)
