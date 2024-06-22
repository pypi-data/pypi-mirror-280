"""CylindricalGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    conversion,
    overridable_enum_runtime,
    utility,
)
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.rating import _370
from mastapy._private.system_model.analyses_and_results.static_loads import _7042
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.gears import _329
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7090,
        _7008,
        _7010,
        _7011,
        _7082,
        _7101,
        _6953,
        _7077,
    )
    from mastapy._private.system_model.part_model.gears import _2582
    from mastapy._private.gears.gear_designs.cylindrical import _1089
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1139
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="CylindricalGearSetLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSetLoadCase:
    """Special nested class for casting CylindricalGearSetLoadCase to subclasses."""

    __parent__: "CylindricalGearSetLoadCase"

    @property
    def gear_set_load_case(self: "CastSelf") -> "_7042.GearSetLoadCase":
        return self.__parent__._cast(_7042.GearSetLoadCase)

    @property
    def specialised_assembly_load_case(
        self: "CastSelf",
    ) -> "_7101.SpecialisedAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7101,
        )

        return self.__parent__._cast(_7101.SpecialisedAssemblyLoadCase)

    @property
    def abstract_assembly_load_case(
        self: "CastSelf",
    ) -> "_6953.AbstractAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6953,
        )

        return self.__parent__._cast(_6953.AbstractAssemblyLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7077.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7077,
        )

        return self.__parent__._cast(_7077.PartLoadCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def planetary_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7082.PlanetaryGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7082,
        )

        return self.__parent__._cast(_7082.PlanetaryGearSetLoadCase)

    @property
    def cylindrical_gear_set_load_case(
        self: "CastSelf",
    ) -> "CylindricalGearSetLoadCase":
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
class CylindricalGearSetLoadCase(_7042.GearSetLoadCase):
    """CylindricalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SET_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def boost_pressure(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BoostPressure

        if temp is None:
            return 0.0

        return temp

    @boost_pressure.setter
    @enforce_parameter_types
    def boost_pressure(self: "Self", value: "float") -> None:
        self.wrapped.BoostPressure = float(value) if value is not None else 0.0

    @property
    def coefficient_of_friction_calculation_method(
        self: "Self",
    ) -> "_329.CoefficientOfFrictionCalculationMethod":
        """mastapy._private.gears.CoefficientOfFrictionCalculationMethod"""
        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears._329", "CoefficientOfFrictionCalculationMethod"
        )(value)

    @coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def coefficient_of_friction_calculation_method(
        self: "Self", value: "_329.CoefficientOfFrictionCalculationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def dynamic_load_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_load_factor.setter
    @enforce_parameter_types
    def dynamic_load_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicLoadFactor = value

    @property
    def efficiency_rating_method(
        self: "Self",
    ) -> "overridable.Overridable_GearMeshEfficiencyRatingMethod":
        """Overridable[mastapy._private.gears.rating.GearMeshEfficiencyRatingMethod]"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = overridable.Overridable_GearMeshEfficiencyRatingMethod.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(
        self: "Self",
        value: "Union[_370.GearMeshEfficiencyRatingMethod, Tuple[_370.GearMeshEfficiencyRatingMethod, bool]]",
    ) -> None:
        wrapper_type = (
            overridable.Overridable_GearMeshEfficiencyRatingMethod.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_GearMeshEfficiencyRatingMethod.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def override_efficiency_rating_method_script(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.OverrideEfficiencyRatingMethodScript

        if temp is None:
            return False

        return temp

    @override_efficiency_rating_method_script.setter
    @enforce_parameter_types
    def override_efficiency_rating_method_script(self: "Self", value: "bool") -> None:
        self.wrapped.OverrideEfficiencyRatingMethodScript = (
            bool(value) if value is not None else False
        )

    @property
    def override_micro_geometry(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.OverrideMicroGeometry

        if temp is None:
            return False

        return temp

    @override_micro_geometry.setter
    @enforce_parameter_types
    def override_micro_geometry(self: "Self", value: "bool") -> None:
        self.wrapped.OverrideMicroGeometry = bool(value) if value is not None else False

    @property
    def reset_micro_geometry(self: "Self") -> "_7090.ResetMicroGeometryOptions":
        """mastapy._private.system_model.analyses_and_results.static_loads.ResetMicroGeometryOptions"""
        temp = self.wrapped.ResetMicroGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ResetMicroGeometryOptions",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.analyses_and_results.static_loads._7090",
            "ResetMicroGeometryOptions",
        )(value)

    @reset_micro_geometry.setter
    @enforce_parameter_types
    def reset_micro_geometry(
        self: "Self", value: "_7090.ResetMicroGeometryOptions"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ResetMicroGeometryOptions",
        )
        self.wrapped.ResetMicroGeometry = value

    @property
    def use_design_coefficient_of_friction_calculation_method(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod

        if temp is None:
            return False

        return temp

    @use_design_coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def use_design_coefficient_of_friction_calculation_method(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod = (
            bool(value) if value is not None else False
        )

    @property
    def use_design_default_ltca_settings(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignDefaultLTCASettings

        if temp is None:
            return False

        return temp

    @use_design_default_ltca_settings.setter
    @enforce_parameter_types
    def use_design_default_ltca_settings(self: "Self", value: "bool") -> None:
        self.wrapped.UseDesignDefaultLTCASettings = (
            bool(value) if value is not None else False
        )

    @property
    def assembly_design(self: "Self") -> "_2582.CylindricalGearSet":
        """mastapy._private.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ltca(self: "Self") -> "_1089.LTCALoadCaseModifiableSettings":
        """mastapy._private.gears.gear_designs.cylindrical.LTCALoadCaseModifiableSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LTCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overridden_micro_geometry(
        self: "Self",
    ) -> "_1139.CylindricalGearSetMicroGeometry":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverriddenMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_load_case(self: "Self") -> "List[_7008.CylindricalGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gears_load_case(
        self: "Self",
    ) -> "List[_7008.CylindricalGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_load_case(self: "Self") -> "List[_7010.CylindricalGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_load_case(
        self: "Self",
    ) -> "List[_7010.CylindricalGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def get_harmonic_load_data_for_import(
        self: "Self",
    ) -> "_7011.CylindricalGearSetHarmonicLoadData":
        """mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSetLoadCase":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSetLoadCase
        """
        return _Cast_CylindricalGearSetLoadCase(self)
