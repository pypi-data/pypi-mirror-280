"""LubricationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    utility,
)
from mastapy._private._internal.implicit import overridable, enum_with_selected_value
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.materials import _272, _276
from mastapy._private.utility.databases import _1879
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LUBRICATION_DETAIL = python_net_import("SMT.MastaAPI.Materials", "LubricationDetail")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.materials import (
        _250,
        _273,
        _263,
        _268,
        _271,
        _274,
        _277,
        _255,
        _275,
        _287,
        _288,
    )
    from mastapy._private.math_utility import _1581

    Self = TypeVar("Self", bound="LubricationDetail")
    CastSelf = TypeVar("CastSelf", bound="LubricationDetail._Cast_LubricationDetail")


__docformat__ = "restructuredtext en"
__all__ = ("LubricationDetail",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LubricationDetail:
    """Special nested class for casting LubricationDetail to subclasses."""

    __parent__: "LubricationDetail"

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def lubrication_detail(self: "CastSelf") -> "LubricationDetail":
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
class LubricationDetail(_1879.NamedDatabaseItem):
    """LubricationDetail

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LUBRICATION_DETAIL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def agma925a03_lubricant_type(self: "Self") -> "_250.AGMALubricantType":
        """mastapy._private.materials.AGMALubricantType"""
        temp = self.wrapped.AGMA925A03LubricantType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.AGMALubricantType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._250", "AGMALubricantType"
        )(value)

    @agma925a03_lubricant_type.setter
    @enforce_parameter_types
    def agma925a03_lubricant_type(
        self: "Self", value: "_250.AGMALubricantType"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.AGMALubricantType"
        )
        self.wrapped.AGMA925A03LubricantType = value

    @property
    def air_flow_velocity(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AirFlowVelocity

        if temp is None:
            return 0.0

        return temp

    @air_flow_velocity.setter
    @enforce_parameter_types
    def air_flow_velocity(self: "Self", value: "float") -> None:
        self.wrapped.AirFlowVelocity = float(value) if value is not None else 0.0

    @property
    def contamination_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ContaminationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @contamination_factor.setter
    @enforce_parameter_types
    def contamination_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ContaminationFactor = value

    @property
    def delivery(self: "Self") -> "_273.LubricantDelivery":
        """mastapy._private.materials.LubricantDelivery

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Delivery

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.LubricantDelivery"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._273", "LubricantDelivery"
        )(value)

    @property
    def density(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    @enforce_parameter_types
    def density(self: "Self", value: "float") -> None:
        self.wrapped.Density = float(value) if value is not None else 0.0

    @property
    def density_specification_method(self: "Self") -> "_263.DensitySpecificationMethod":
        """mastapy._private.materials.DensitySpecificationMethod"""
        temp = self.wrapped.DensitySpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.DensitySpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._263", "DensitySpecificationMethod"
        )(value)

    @density_specification_method.setter
    @enforce_parameter_types
    def density_specification_method(
        self: "Self", value: "_263.DensitySpecificationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.DensitySpecificationMethod"
        )
        self.wrapped.DensitySpecificationMethod = value

    @property
    def density_vs_temperature(self: "Self") -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.DensityVsTemperature

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @density_vs_temperature.setter
    @enforce_parameter_types
    def density_vs_temperature(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.DensityVsTemperature = value.wrapped

    @property
    def dynamic_viscosity_at_38c(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicViscosityAt38C

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_viscosity_of_the_lubricant_at_100_degrees_c(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DynamicViscosityOfTheLubricantAt100DegreesC

        if temp is None:
            return 0.0

        return temp

    @dynamic_viscosity_of_the_lubricant_at_100_degrees_c.setter
    @enforce_parameter_types
    def dynamic_viscosity_of_the_lubricant_at_100_degrees_c(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.DynamicViscosityOfTheLubricantAt100DegreesC = (
            float(value) if value is not None else 0.0
        )

    @property
    def dynamic_viscosity_of_the_lubricant_at_40_degrees_c(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DynamicViscosityOfTheLubricantAt40DegreesC

        if temp is None:
            return 0.0

        return temp

    @dynamic_viscosity_of_the_lubricant_at_40_degrees_c.setter
    @enforce_parameter_types
    def dynamic_viscosity_of_the_lubricant_at_40_degrees_c(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.DynamicViscosityOfTheLubricantAt40DegreesC = (
            float(value) if value is not None else 0.0
        )

    @property
    def ep_additives_proven_with_severe_contamination(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.EPAdditivesProvenWithSevereContamination

        if temp is None:
            return False

        return temp

    @ep_additives_proven_with_severe_contamination.setter
    @enforce_parameter_types
    def ep_additives_proven_with_severe_contamination(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.EPAdditivesProvenWithSevereContamination = (
            bool(value) if value is not None else False
        )

    @property
    def ep_and_aw_additives_present(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.EPAndAWAdditivesPresent

        if temp is None:
            return False

        return temp

    @ep_and_aw_additives_present.setter
    @enforce_parameter_types
    def ep_and_aw_additives_present(self: "Self", value: "bool") -> None:
        self.wrapped.EPAndAWAdditivesPresent = (
            bool(value) if value is not None else False
        )

    @property
    def factor_for_newly_greased_bearings(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.FactorForNewlyGreasedBearings

        if temp is None:
            return 0.0

        return temp

    @factor_for_newly_greased_bearings.setter
    @enforce_parameter_types
    def factor_for_newly_greased_bearings(self: "Self", value: "float") -> None:
        self.wrapped.FactorForNewlyGreasedBearings = (
            float(value) if value is not None else 0.0
        )

    @property
    def grease_contamination_level(self: "Self") -> "_268.GreaseContaminationOptions":
        """mastapy._private.materials.GreaseContaminationOptions"""
        temp = self.wrapped.GreaseContaminationLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.GreaseContaminationOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._268", "GreaseContaminationOptions"
        )(value)

    @grease_contamination_level.setter
    @enforce_parameter_types
    def grease_contamination_level(
        self: "Self", value: "_268.GreaseContaminationOptions"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.GreaseContaminationOptions"
        )
        self.wrapped.GreaseContaminationLevel = value

    @property
    def heat_transfer_coefficient(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HeatTransferCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @heat_transfer_coefficient.setter
    @enforce_parameter_types
    def heat_transfer_coefficient(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HeatTransferCoefficient = value

    @property
    def iso_lubricant_type(self: "Self") -> "_271.ISOLubricantType":
        """mastapy._private.materials.ISOLubricantType"""
        temp = self.wrapped.ISOLubricantType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.ISOLubricantType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._271", "ISOLubricantType"
        )(value)

    @iso_lubricant_type.setter
    @enforce_parameter_types
    def iso_lubricant_type(self: "Self", value: "_271.ISOLubricantType") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.ISOLubricantType"
        )
        self.wrapped.ISOLubricantType = value

    @property
    def kinematic_viscosity_at_38c(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KinematicViscosityAt38C

        if temp is None:
            return 0.0

        return temp

    @property
    def kinematic_viscosity_of_the_lubricant_at_100_degrees_c(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.KinematicViscosityOfTheLubricantAt100DegreesC

        if temp is None:
            return 0.0

        return temp

    @kinematic_viscosity_of_the_lubricant_at_100_degrees_c.setter
    @enforce_parameter_types
    def kinematic_viscosity_of_the_lubricant_at_100_degrees_c(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.KinematicViscosityOfTheLubricantAt100DegreesC = (
            float(value) if value is not None else 0.0
        )

    @property
    def kinematic_viscosity_of_the_lubricant_at_40_degrees_c(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.KinematicViscosityOfTheLubricantAt40DegreesC

        if temp is None:
            return 0.0

        return temp

    @kinematic_viscosity_of_the_lubricant_at_40_degrees_c.setter
    @enforce_parameter_types
    def kinematic_viscosity_of_the_lubricant_at_40_degrees_c(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.KinematicViscosityOfTheLubricantAt40DegreesC = (
            float(value) if value is not None else 0.0
        )

    @property
    def lubricant_definition(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition":
        """EnumWithSelectedValue[mastapy._private.materials.LubricantDefinition]"""
        temp = self.wrapped.LubricantDefinition

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lubricant_definition.setter
    @enforce_parameter_types
    def lubricant_definition(self: "Self", value: "_272.LubricantDefinition") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantDefinition = value

    @property
    def lubricant_grade_agma(self: "Self") -> "_274.LubricantViscosityClassAGMA":
        """mastapy._private.materials.LubricantViscosityClassAGMA"""
        temp = self.wrapped.LubricantGradeAGMA

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.LubricantViscosityClassAGMA"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._274", "LubricantViscosityClassAGMA"
        )(value)

    @lubricant_grade_agma.setter
    @enforce_parameter_types
    def lubricant_grade_agma(
        self: "Self", value: "_274.LubricantViscosityClassAGMA"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.LubricantViscosityClassAGMA"
        )
        self.wrapped.LubricantGradeAGMA = value

    @property
    def lubricant_grade_iso(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO":
        """EnumWithSelectedValue[mastapy._private.materials.LubricantViscosityClassISO]"""
        temp = self.wrapped.LubricantGradeISO

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lubricant_grade_iso.setter
    @enforce_parameter_types
    def lubricant_grade_iso(
        self: "Self", value: "_276.LubricantViscosityClassISO"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantGradeISO = value

    @property
    def lubricant_grade_sae(self: "Self") -> "_277.LubricantViscosityClassSAE":
        """mastapy._private.materials.LubricantViscosityClassSAE"""
        temp = self.wrapped.LubricantGradeSAE

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.LubricantViscosityClassSAE"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._277", "LubricantViscosityClassSAE"
        )(value)

    @lubricant_grade_sae.setter
    @enforce_parameter_types
    def lubricant_grade_sae(
        self: "Self", value: "_277.LubricantViscosityClassSAE"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.LubricantViscosityClassSAE"
        )
        self.wrapped.LubricantGradeSAE = value

    @property
    def lubricant_shear_modulus(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LubricantShearModulus

        if temp is None:
            return 0.0

        return temp

    @lubricant_shear_modulus.setter
    @enforce_parameter_types
    def lubricant_shear_modulus(self: "Self", value: "float") -> None:
        self.wrapped.LubricantShearModulus = float(value) if value is not None else 0.0

    @property
    def lubricant_type_ampersand_supply(
        self: "Self",
    ) -> "_255.BearingLubricationCondition":
        """mastapy._private.materials.BearingLubricationCondition"""
        temp = self.wrapped.LubricantTypeAmpersandSupply

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.BearingLubricationCondition"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._255", "BearingLubricationCondition"
        )(value)

    @lubricant_type_ampersand_supply.setter
    @enforce_parameter_types
    def lubricant_type_ampersand_supply(
        self: "Self", value: "_255.BearingLubricationCondition"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.BearingLubricationCondition"
        )
        self.wrapped.LubricantTypeAmpersandSupply = value

    @property
    def lubricant_viscosity_classification(
        self: "Self",
    ) -> "_275.LubricantViscosityClassification":
        """mastapy._private.materials.LubricantViscosityClassification"""
        temp = self.wrapped.LubricantViscosityClassification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.LubricantViscosityClassification"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._275", "LubricantViscosityClassification"
        )(value)

    @lubricant_viscosity_classification.setter
    @enforce_parameter_types
    def lubricant_viscosity_classification(
        self: "Self", value: "_275.LubricantViscosityClassification"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.LubricantViscosityClassification"
        )
        self.wrapped.LubricantViscosityClassification = value

    @property
    def micropitting_failure_load_stage(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.MicropittingFailureLoadStage

        if temp is None:
            return 0

        return temp

    @micropitting_failure_load_stage.setter
    @enforce_parameter_types
    def micropitting_failure_load_stage(self: "Self", value: "int") -> None:
        self.wrapped.MicropittingFailureLoadStage = (
            int(value) if value is not None else 0
        )

    @property
    def micropitting_failure_load_stage_test_temperature(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MicropittingFailureLoadStageTestTemperature

        if temp is None:
            return 0.0

        return temp

    @micropitting_failure_load_stage_test_temperature.setter
    @enforce_parameter_types
    def micropitting_failure_load_stage_test_temperature(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.MicropittingFailureLoadStageTestTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def oil_filtration_and_contamination(self: "Self") -> "_287.OilFiltrationOptions":
        """mastapy._private.materials.OilFiltrationOptions"""
        temp = self.wrapped.OilFiltrationAndContamination

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.OilFiltrationOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._287", "OilFiltrationOptions"
        )(value)

    @oil_filtration_and_contamination.setter
    @enforce_parameter_types
    def oil_filtration_and_contamination(
        self: "Self", value: "_287.OilFiltrationOptions"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.OilFiltrationOptions"
        )
        self.wrapped.OilFiltrationAndContamination = value

    @property
    def oil_to_air_heat_transfer_area(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OilToAirHeatTransferArea

        if temp is None:
            return 0.0

        return temp

    @oil_to_air_heat_transfer_area.setter
    @enforce_parameter_types
    def oil_to_air_heat_transfer_area(self: "Self", value: "float") -> None:
        self.wrapped.OilToAirHeatTransferArea = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_viscosity_coefficient(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PressureViscosityCoefficient

        if temp is None:
            return 0.0

        return temp

    @pressure_viscosity_coefficient.setter
    @enforce_parameter_types
    def pressure_viscosity_coefficient(self: "Self", value: "float") -> None:
        self.wrapped.PressureViscosityCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_viscosity_coefficient_method(
        self: "Self",
    ) -> "_288.PressureViscosityCoefficientMethod":
        """mastapy._private.materials.PressureViscosityCoefficientMethod"""
        temp = self.wrapped.PressureViscosityCoefficientMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.PressureViscosityCoefficientMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._288", "PressureViscosityCoefficientMethod"
        )(value)

    @pressure_viscosity_coefficient_method.setter
    @enforce_parameter_types
    def pressure_viscosity_coefficient_method(
        self: "Self", value: "_288.PressureViscosityCoefficientMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.PressureViscosityCoefficientMethod"
        )
        self.wrapped.PressureViscosityCoefficientMethod = value

    @property
    def scuffing_failure_load_stage(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.ScuffingFailureLoadStage

        if temp is None:
            return 0

        return temp

    @scuffing_failure_load_stage.setter
    @enforce_parameter_types
    def scuffing_failure_load_stage(self: "Self", value: "int") -> None:
        self.wrapped.ScuffingFailureLoadStage = int(value) if value is not None else 0

    @property
    def specific_heat_capacity(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecificHeatCapacity

        if temp is None:
            return 0.0

        return temp

    @specific_heat_capacity.setter
    @enforce_parameter_types
    def specific_heat_capacity(self: "Self", value: "float") -> None:
        self.wrapped.SpecificHeatCapacity = float(value) if value is not None else 0.0

    @property
    def specified_parameter_k(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecifiedParameterK

        if temp is None:
            return 0.0

        return temp

    @specified_parameter_k.setter
    @enforce_parameter_types
    def specified_parameter_k(self: "Self", value: "float") -> None:
        self.wrapped.SpecifiedParameterK = float(value) if value is not None else 0.0

    @property
    def specified_parameter_s(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SpecifiedParameterS

        if temp is None:
            return 0.0

        return temp

    @specified_parameter_s.setter
    @enforce_parameter_types
    def specified_parameter_s(self: "Self", value: "float") -> None:
        self.wrapped.SpecifiedParameterS = float(value) if value is not None else 0.0

    @property
    def temperature_at_which_density_is_specified(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TemperatureAtWhichDensityIsSpecified

        if temp is None:
            return 0.0

        return temp

    @temperature_at_which_density_is_specified.setter
    @enforce_parameter_types
    def temperature_at_which_density_is_specified(self: "Self", value: "float") -> None:
        self.wrapped.TemperatureAtWhichDensityIsSpecified = (
            float(value) if value is not None else 0.0
        )

    @property
    def temperature_at_which_pressure_viscosity_coefficient_is_specified(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.TemperatureAtWhichPressureViscosityCoefficientIsSpecified

        if temp is None:
            return 0.0

        return temp

    @temperature_at_which_pressure_viscosity_coefficient_is_specified.setter
    @enforce_parameter_types
    def temperature_at_which_pressure_viscosity_coefficient_is_specified(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.TemperatureAtWhichPressureViscosityCoefficientIsSpecified = (
            float(value) if value is not None else 0.0
        )

    @property
    def thermal_conductivity(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ThermalConductivity

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @thermal_conductivity.setter
    @enforce_parameter_types
    def thermal_conductivity(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ThermalConductivity = value

    @enforce_parameter_types
    def dynamic_viscosity_at(self: "Self", temperature: "float") -> "float":
        """float

        Args:
            temperature (float)
        """
        temperature = float(temperature)
        method_result = self.wrapped.DynamicViscosityAt(
            temperature if temperature else 0.0
        )
        return method_result

    @enforce_parameter_types
    def kinematic_viscosity_at(self: "Self", temperature: "float") -> "float":
        """float

        Args:
            temperature (float)
        """
        temperature = float(temperature)
        method_result = self.wrapped.KinematicViscosityAt(
            temperature if temperature else 0.0
        )
        return method_result

    @enforce_parameter_types
    def lubricant_density_at(self: "Self", temperature: "float") -> "float":
        """float

        Args:
            temperature (float)
        """
        temperature = float(temperature)
        method_result = self.wrapped.LubricantDensityAt(
            temperature if temperature else 0.0
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_LubricationDetail":
        """Cast to another type.

        Returns:
            _Cast_LubricationDetail
        """
        return _Cast_LubricationDetail(self)
