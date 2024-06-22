"""IndependentReportablePropertiesBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.Utility", "IndependentReportablePropertiesBase"
)

if TYPE_CHECKING:
    from typing import Any, Type

    from mastapy._private.materials.efficiency import _308
    from mastapy._private.geometry import _319
    from mastapy._private.gears import _356
    from mastapy._private.gears.gear_designs.cylindrical import (
        _1050,
        _1081,
        _1089,
        _1090,
        _1093,
        _1094,
        _1102,
        _1110,
        _1112,
        _1116,
        _1120,
    )
    from mastapy._private.electric_machines import _1301
    from mastapy._private.electric_machines.load_cases_and_analyses import _1423
    from mastapy._private.math_utility.measured_data import _1612, _1613, _1614
    from mastapy._private.bearings.tolerances import _1970
    from mastapy._private.bearings.bearing_results import _1998
    from mastapy._private.bearings.bearing_results.rolling import _2029, _2123
    from mastapy._private.system_model.analyses_and_results.static_loads import _6957

    Self = TypeVar("Self", bound="IndependentReportablePropertiesBase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
    )

T = TypeVar("T", bound="IndependentReportablePropertiesBase")

__docformat__ = "restructuredtext en"
__all__ = ("IndependentReportablePropertiesBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_IndependentReportablePropertiesBase:
    """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

    __parent__: "IndependentReportablePropertiesBase"

    @property
    def oil_pump_detail(self: "CastSelf") -> "_308.OilPumpDetail":
        from mastapy._private.materials.efficiency import _308

        return self.__parent__._cast(_308.OilPumpDetail)

    @property
    def packaging_limits(self: "CastSelf") -> "_319.PackagingLimits":
        from mastapy._private.geometry import _319

        return self.__parent__._cast(_319.PackagingLimits)

    @property
    def specification_for_the_effect_of_oil_kinematic_viscosity(
        self: "CastSelf",
    ) -> "_356.SpecificationForTheEffectOfOilKinematicViscosity":
        from mastapy._private.gears import _356

        return self.__parent__._cast(
            _356.SpecificationForTheEffectOfOilKinematicViscosity
        )

    @property
    def cylindrical_gear_micro_geometry_settings(
        self: "CastSelf",
    ) -> "_1050.CylindricalGearMicroGeometrySettings":
        from mastapy._private.gears.gear_designs.cylindrical import _1050

        return self.__parent__._cast(_1050.CylindricalGearMicroGeometrySettings)

    @property
    def hardened_material_properties(
        self: "CastSelf",
    ) -> "_1081.HardenedMaterialProperties":
        from mastapy._private.gears.gear_designs.cylindrical import _1081

        return self.__parent__._cast(_1081.HardenedMaterialProperties)

    @property
    def ltca_load_case_modifiable_settings(
        self: "CastSelf",
    ) -> "_1089.LTCALoadCaseModifiableSettings":
        from mastapy._private.gears.gear_designs.cylindrical import _1089

        return self.__parent__._cast(_1089.LTCALoadCaseModifiableSettings)

    @property
    def ltca_settings(self: "CastSelf") -> "_1090.LTCASettings":
        from mastapy._private.gears.gear_designs.cylindrical import _1090

        return self.__parent__._cast(_1090.LTCASettings)

    @property
    def micropitting(self: "CastSelf") -> "_1093.Micropitting":
        from mastapy._private.gears.gear_designs.cylindrical import _1093

        return self.__parent__._cast(_1093.Micropitting)

    @property
    def muller_residual_stress_definition(
        self: "CastSelf",
    ) -> "_1094.MullerResidualStressDefinition":
        from mastapy._private.gears.gear_designs.cylindrical import _1094

        return self.__parent__._cast(_1094.MullerResidualStressDefinition)

    @property
    def scuffing(self: "CastSelf") -> "_1102.Scuffing":
        from mastapy._private.gears.gear_designs.cylindrical import _1102

        return self.__parent__._cast(_1102.Scuffing)

    @property
    def surface_roughness(self: "CastSelf") -> "_1110.SurfaceRoughness":
        from mastapy._private.gears.gear_designs.cylindrical import _1110

        return self.__parent__._cast(_1110.SurfaceRoughness)

    @property
    def tiff_analysis_settings(self: "CastSelf") -> "_1112.TiffAnalysisSettings":
        from mastapy._private.gears.gear_designs.cylindrical import _1112

        return self.__parent__._cast(_1112.TiffAnalysisSettings)

    @property
    def tooth_flank_fracture_analysis_settings(
        self: "CastSelf",
    ) -> "_1116.ToothFlankFractureAnalysisSettings":
        from mastapy._private.gears.gear_designs.cylindrical import _1116

        return self.__parent__._cast(_1116.ToothFlankFractureAnalysisSettings)

    @property
    def usage(self: "CastSelf") -> "_1120.Usage":
        from mastapy._private.gears.gear_designs.cylindrical import _1120

        return self.__parent__._cast(_1120.Usage)

    @property
    def eccentricity(self: "CastSelf") -> "_1301.Eccentricity":
        from mastapy._private.electric_machines import _1301

        return self.__parent__._cast(_1301.Eccentricity)

    @property
    def temperatures(self: "CastSelf") -> "_1423.Temperatures":
        from mastapy._private.electric_machines.load_cases_and_analyses import _1423

        return self.__parent__._cast(_1423.Temperatures)

    @property
    def lookup_table_base(self: "CastSelf") -> "_1612.LookupTableBase":
        from mastapy._private.math_utility.measured_data import _1612

        return self.__parent__._cast(_1612.LookupTableBase)

    @property
    def onedimensional_function_lookup_table(
        self: "CastSelf",
    ) -> "_1613.OnedimensionalFunctionLookupTable":
        from mastapy._private.math_utility.measured_data import _1613

        return self.__parent__._cast(_1613.OnedimensionalFunctionLookupTable)

    @property
    def twodimensional_function_lookup_table(
        self: "CastSelf",
    ) -> "_1614.TwodimensionalFunctionLookupTable":
        from mastapy._private.math_utility.measured_data import _1614

        return self.__parent__._cast(_1614.TwodimensionalFunctionLookupTable)

    @property
    def roundness_specification(self: "CastSelf") -> "_1970.RoundnessSpecification":
        from mastapy._private.bearings.tolerances import _1970

        return self.__parent__._cast(_1970.RoundnessSpecification)

    @property
    def equivalent_load_factors(self: "CastSelf") -> "_1998.EquivalentLoadFactors":
        from mastapy._private.bearings.bearing_results import _1998

        return self.__parent__._cast(_1998.EquivalentLoadFactors)

    @property
    def iso14179_settings_per_bearing_type(
        self: "CastSelf",
    ) -> "_2029.ISO14179SettingsPerBearingType":
        from mastapy._private.bearings.bearing_results.rolling import _2029

        return self.__parent__._cast(_2029.ISO14179SettingsPerBearingType)

    @property
    def rolling_bearing_friction_coefficients(
        self: "CastSelf",
    ) -> "_2123.RollingBearingFrictionCoefficients":
        from mastapy._private.bearings.bearing_results.rolling import _2123

        return self.__parent__._cast(_2123.RollingBearingFrictionCoefficients)

    @property
    def additional_acceleration_options(
        self: "CastSelf",
    ) -> "_6957.AdditionalAccelerationOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6957,
        )

        return self.__parent__._cast(_6957.AdditionalAccelerationOptions)

    @property
    def independent_reportable_properties_base(
        self: "CastSelf",
    ) -> "IndependentReportablePropertiesBase":
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
class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_IndependentReportablePropertiesBase":
        """Cast to another type.

        Returns:
            _Cast_IndependentReportablePropertiesBase
        """
        return _Cast_IndependentReportablePropertiesBase(self)
