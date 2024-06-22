"""NamedDatabaseItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_NAMED_DATABASE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Databases", "NamedDatabaseItem"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility import _1629
    from mastapy._private.utility.databases import _1880
    from mastapy._private.shafts import _24, _40, _43
    from mastapy._private.nodal_analysis import _50
    from mastapy._private.materials import _256, _278, _280, _284
    from mastapy._private.gears import _352
    from mastapy._private.gears.rating.cylindrical import _465, _481
    from mastapy._private.gears.materials import (
        _594,
        _597,
        _599,
        _604,
        _608,
        _616,
        _618,
        _621,
        _625,
        _628,
    )
    from mastapy._private.gears.manufacturing.cylindrical.cutters import (
        _729,
        _730,
        _731,
        _732,
        _733,
        _735,
        _736,
        _737,
        _738,
        _741,
    )
    from mastapy._private.gears.manufacturing.bevel import _822
    from mastapy._private.gears.gear_designs import _965, _967, _970
    from mastapy._private.gears.gear_designs.cylindrical import _1044, _1052
    from mastapy._private.electric_machines import _1328, _1346, _1359
    from mastapy._private.detailed_rigid_connectors.splines import _1462
    from mastapy._private.cycloidal import _1502, _1509
    from mastapy._private.bolts import _1512, _1514, _1516
    from mastapy._private.math_utility.optimisation import _1595
    from mastapy._private.bearings import _1933
    from mastapy._private.bearings.bearing_results.rolling import _2027
    from mastapy._private.system_model.optimization import _2279, _2282, _2287, _2288
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2619,
    )

    Self = TypeVar("Self", bound="NamedDatabaseItem")
    CastSelf = TypeVar("CastSelf", bound="NamedDatabaseItem._Cast_NamedDatabaseItem")


__docformat__ = "restructuredtext en"
__all__ = ("NamedDatabaseItem",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_NamedDatabaseItem:
    """Special nested class for casting NamedDatabaseItem to subclasses."""

    __parent__: "NamedDatabaseItem"

    @property
    def shaft_material(self: "CastSelf") -> "_24.ShaftMaterial":
        from mastapy._private.shafts import _24

        return self.__parent__._cast(_24.ShaftMaterial)

    @property
    def shaft_settings_item(self: "CastSelf") -> "_40.ShaftSettingsItem":
        from mastapy._private.shafts import _40

        return self.__parent__._cast(_40.ShaftSettingsItem)

    @property
    def simple_shaft_definition(self: "CastSelf") -> "_43.SimpleShaftDefinition":
        from mastapy._private.shafts import _43

        return self.__parent__._cast(_43.SimpleShaftDefinition)

    @property
    def analysis_settings_item(self: "CastSelf") -> "_50.AnalysisSettingsItem":
        from mastapy._private.nodal_analysis import _50

        return self.__parent__._cast(_50.AnalysisSettingsItem)

    @property
    def bearing_material(self: "CastSelf") -> "_256.BearingMaterial":
        from mastapy._private.materials import _256

        return self.__parent__._cast(_256.BearingMaterial)

    @property
    def lubrication_detail(self: "CastSelf") -> "_278.LubricationDetail":
        from mastapy._private.materials import _278

        return self.__parent__._cast(_278.LubricationDetail)

    @property
    def material(self: "CastSelf") -> "_280.Material":
        from mastapy._private.materials import _280

        return self.__parent__._cast(_280.Material)

    @property
    def materials_settings_item(self: "CastSelf") -> "_284.MaterialsSettingsItem":
        from mastapy._private.materials import _284

        return self.__parent__._cast(_284.MaterialsSettingsItem)

    @property
    def pocketing_power_loss_coefficients(
        self: "CastSelf",
    ) -> "_352.PocketingPowerLossCoefficients":
        from mastapy._private.gears import _352

        return self.__parent__._cast(_352.PocketingPowerLossCoefficients)

    @property
    def cylindrical_gear_design_and_rating_settings_item(
        self: "CastSelf",
    ) -> "_465.CylindricalGearDesignAndRatingSettingsItem":
        from mastapy._private.gears.rating.cylindrical import _465

        return self.__parent__._cast(_465.CylindricalGearDesignAndRatingSettingsItem)

    @property
    def cylindrical_plastic_gear_rating_settings_item(
        self: "CastSelf",
    ) -> "_481.CylindricalPlasticGearRatingSettingsItem":
        from mastapy._private.gears.rating.cylindrical import _481

        return self.__parent__._cast(_481.CylindricalPlasticGearRatingSettingsItem)

    @property
    def agma_cylindrical_gear_material(
        self: "CastSelf",
    ) -> "_594.AGMACylindricalGearMaterial":
        from mastapy._private.gears.materials import _594

        return self.__parent__._cast(_594.AGMACylindricalGearMaterial)

    @property
    def bevel_gear_iso_material(self: "CastSelf") -> "_597.BevelGearISOMaterial":
        from mastapy._private.gears.materials import _597

        return self.__parent__._cast(_597.BevelGearISOMaterial)

    @property
    def bevel_gear_material(self: "CastSelf") -> "_599.BevelGearMaterial":
        from mastapy._private.gears.materials import _599

        return self.__parent__._cast(_599.BevelGearMaterial)

    @property
    def cylindrical_gear_material(self: "CastSelf") -> "_604.CylindricalGearMaterial":
        from mastapy._private.gears.materials import _604

        return self.__parent__._cast(_604.CylindricalGearMaterial)

    @property
    def gear_material(self: "CastSelf") -> "_608.GearMaterial":
        from mastapy._private.gears.materials import _608

        return self.__parent__._cast(_608.GearMaterial)

    @property
    def iso_cylindrical_gear_material(
        self: "CastSelf",
    ) -> "_616.ISOCylindricalGearMaterial":
        from mastapy._private.gears.materials import _616

        return self.__parent__._cast(_616.ISOCylindricalGearMaterial)

    @property
    def isotr1417912001_coefficient_of_friction_constants(
        self: "CastSelf",
    ) -> "_618.ISOTR1417912001CoefficientOfFrictionConstants":
        from mastapy._private.gears.materials import _618

        return self.__parent__._cast(_618.ISOTR1417912001CoefficientOfFrictionConstants)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_material(
        self: "CastSelf",
    ) -> "_621.KlingelnbergCycloPalloidConicalGearMaterial":
        from mastapy._private.gears.materials import _621

        return self.__parent__._cast(_621.KlingelnbergCycloPalloidConicalGearMaterial)

    @property
    def plastic_cylindrical_gear_material(
        self: "CastSelf",
    ) -> "_625.PlasticCylindricalGearMaterial":
        from mastapy._private.gears.materials import _625

        return self.__parent__._cast(_625.PlasticCylindricalGearMaterial)

    @property
    def raw_material(self: "CastSelf") -> "_628.RawMaterial":
        from mastapy._private.gears.materials import _628

        return self.__parent__._cast(_628.RawMaterial)

    @property
    def cylindrical_gear_abstract_cutter_design(
        self: "CastSelf",
    ) -> "_729.CylindricalGearAbstractCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _729

        return self.__parent__._cast(_729.CylindricalGearAbstractCutterDesign)

    @property
    def cylindrical_gear_form_grinding_wheel(
        self: "CastSelf",
    ) -> "_730.CylindricalGearFormGrindingWheel":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _730

        return self.__parent__._cast(_730.CylindricalGearFormGrindingWheel)

    @property
    def cylindrical_gear_grinding_worm(
        self: "CastSelf",
    ) -> "_731.CylindricalGearGrindingWorm":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _731

        return self.__parent__._cast(_731.CylindricalGearGrindingWorm)

    @property
    def cylindrical_gear_hob_design(
        self: "CastSelf",
    ) -> "_732.CylindricalGearHobDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _732

        return self.__parent__._cast(_732.CylindricalGearHobDesign)

    @property
    def cylindrical_gear_plunge_shaver(
        self: "CastSelf",
    ) -> "_733.CylindricalGearPlungeShaver":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _733

        return self.__parent__._cast(_733.CylindricalGearPlungeShaver)

    @property
    def cylindrical_gear_rack_design(
        self: "CastSelf",
    ) -> "_735.CylindricalGearRackDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _735

        return self.__parent__._cast(_735.CylindricalGearRackDesign)

    @property
    def cylindrical_gear_real_cutter_design(
        self: "CastSelf",
    ) -> "_736.CylindricalGearRealCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _736

        return self.__parent__._cast(_736.CylindricalGearRealCutterDesign)

    @property
    def cylindrical_gear_shaper(self: "CastSelf") -> "_737.CylindricalGearShaper":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _737

        return self.__parent__._cast(_737.CylindricalGearShaper)

    @property
    def cylindrical_gear_shaver(self: "CastSelf") -> "_738.CylindricalGearShaver":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _738

        return self.__parent__._cast(_738.CylindricalGearShaver)

    @property
    def involute_cutter_design(self: "CastSelf") -> "_741.InvoluteCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _741

        return self.__parent__._cast(_741.InvoluteCutterDesign)

    @property
    def manufacturing_machine(self: "CastSelf") -> "_822.ManufacturingMachine":
        from mastapy._private.gears.manufacturing.bevel import _822

        return self.__parent__._cast(_822.ManufacturingMachine)

    @property
    def bevel_hypoid_gear_design_settings_item(
        self: "CastSelf",
    ) -> "_965.BevelHypoidGearDesignSettingsItem":
        from mastapy._private.gears.gear_designs import _965

        return self.__parent__._cast(_965.BevelHypoidGearDesignSettingsItem)

    @property
    def bevel_hypoid_gear_rating_settings_item(
        self: "CastSelf",
    ) -> "_967.BevelHypoidGearRatingSettingsItem":
        from mastapy._private.gears.gear_designs import _967

        return self.__parent__._cast(_967.BevelHypoidGearRatingSettingsItem)

    @property
    def design_constraints_collection(
        self: "CastSelf",
    ) -> "_970.DesignConstraintsCollection":
        from mastapy._private.gears.gear_designs import _970

        return self.__parent__._cast(_970.DesignConstraintsCollection)

    @property
    def cylindrical_gear_design_constraints(
        self: "CastSelf",
    ) -> "_1044.CylindricalGearDesignConstraints":
        from mastapy._private.gears.gear_designs.cylindrical import _1044

        return self.__parent__._cast(_1044.CylindricalGearDesignConstraints)

    @property
    def cylindrical_gear_micro_geometry_settings_item(
        self: "CastSelf",
    ) -> "_1052.CylindricalGearMicroGeometrySettingsItem":
        from mastapy._private.gears.gear_designs.cylindrical import _1052

        return self.__parent__._cast(_1052.CylindricalGearMicroGeometrySettingsItem)

    @property
    def magnet_material(self: "CastSelf") -> "_1328.MagnetMaterial":
        from mastapy._private.electric_machines import _1328

        return self.__parent__._cast(_1328.MagnetMaterial)

    @property
    def stator_rotor_material(self: "CastSelf") -> "_1346.StatorRotorMaterial":
        from mastapy._private.electric_machines import _1346

        return self.__parent__._cast(_1346.StatorRotorMaterial)

    @property
    def winding_material(self: "CastSelf") -> "_1359.WindingMaterial":
        from mastapy._private.electric_machines import _1359

        return self.__parent__._cast(_1359.WindingMaterial)

    @property
    def spline_material(self: "CastSelf") -> "_1462.SplineMaterial":
        from mastapy._private.detailed_rigid_connectors.splines import _1462

        return self.__parent__._cast(_1462.SplineMaterial)

    @property
    def cycloidal_disc_material(self: "CastSelf") -> "_1502.CycloidalDiscMaterial":
        from mastapy._private.cycloidal import _1502

        return self.__parent__._cast(_1502.CycloidalDiscMaterial)

    @property
    def ring_pins_material(self: "CastSelf") -> "_1509.RingPinsMaterial":
        from mastapy._private.cycloidal import _1509

        return self.__parent__._cast(_1509.RingPinsMaterial)

    @property
    def bolted_joint_material(self: "CastSelf") -> "_1512.BoltedJointMaterial":
        from mastapy._private.bolts import _1512

        return self.__parent__._cast(_1512.BoltedJointMaterial)

    @property
    def bolt_geometry(self: "CastSelf") -> "_1514.BoltGeometry":
        from mastapy._private.bolts import _1514

        return self.__parent__._cast(_1514.BoltGeometry)

    @property
    def bolt_material(self: "CastSelf") -> "_1516.BoltMaterial":
        from mastapy._private.bolts import _1516

        return self.__parent__._cast(_1516.BoltMaterial)

    @property
    def pareto_optimisation_strategy(
        self: "CastSelf",
    ) -> "_1595.ParetoOptimisationStrategy":
        from mastapy._private.math_utility.optimisation import _1595

        return self.__parent__._cast(_1595.ParetoOptimisationStrategy)

    @property
    def bearing_settings_item(self: "CastSelf") -> "_1933.BearingSettingsItem":
        from mastapy._private.bearings import _1933

        return self.__parent__._cast(_1933.BearingSettingsItem)

    @property
    def iso14179_settings(self: "CastSelf") -> "_2027.ISO14179Settings":
        from mastapy._private.bearings.bearing_results.rolling import _2027

        return self.__parent__._cast(_2027.ISO14179Settings)

    @property
    def conical_gear_optimisation_strategy(
        self: "CastSelf",
    ) -> "_2279.ConicalGearOptimisationStrategy":
        from mastapy._private.system_model.optimization import _2279

        return self.__parent__._cast(_2279.ConicalGearOptimisationStrategy)

    @property
    def cylindrical_gear_optimisation_strategy(
        self: "CastSelf",
    ) -> "_2282.CylindricalGearOptimisationStrategy":
        from mastapy._private.system_model.optimization import _2282

        return self.__parent__._cast(_2282.CylindricalGearOptimisationStrategy)

    @property
    def optimization_strategy(self: "CastSelf") -> "_2287.OptimizationStrategy":
        from mastapy._private.system_model.optimization import _2287

        return self.__parent__._cast(_2287.OptimizationStrategy)

    @property
    def optimization_strategy_base(
        self: "CastSelf",
    ) -> "_2288.OptimizationStrategyBase":
        from mastapy._private.system_model.optimization import _2288

        return self.__parent__._cast(_2288.OptimizationStrategyBase)

    @property
    def supercharger_rotor_set(self: "CastSelf") -> "_2619.SuperchargerRotorSet":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2619,
        )

        return self.__parent__._cast(_2619.SuperchargerRotorSet)

    @property
    def named_database_item(self: "CastSelf") -> "NamedDatabaseItem":
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
class NamedDatabaseItem(_0.APIBase):
    """NamedDatabaseItem

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _NAMED_DATABASE_ITEM

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def comment(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: "Self", value: "str") -> None:
        self.wrapped.Comment = str(value) if value is not None else ""

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
    def no_history(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoHistory

        if temp is None:
            return ""

        return temp

    @property
    def history(self: "Self") -> "_1629.FileHistory":
        """mastapy._private.utility.FileHistory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def database_key(self: "Self") -> "_1880.NamedKey":
        """mastapy._private.utility.databases.NamedKey"""
        temp = self.wrapped.DatabaseKey

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @database_key.setter
    @enforce_parameter_types
    def database_key(self: "Self", value: "_1880.NamedKey") -> None:
        self.wrapped.DatabaseKey = value.wrapped

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_NamedDatabaseItem":
        """Cast to another type.

        Returns:
            _Cast_NamedDatabaseItem
        """
        return _Cast_NamedDatabaseItem(self)
