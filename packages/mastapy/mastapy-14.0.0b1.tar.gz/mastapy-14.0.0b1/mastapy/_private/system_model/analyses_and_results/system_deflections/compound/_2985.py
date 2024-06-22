"""CylindricalGearSetCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _2997,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CylindricalGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1140
    from mastapy._private.system_model.part_model.gears import _2582
    from mastapy._private.gears.rating.cylindrical import _474, _475
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2827,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2983,
        _2984,
        _3023,
        _3038,
        _2936,
        _3018,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CylindricalGearSetCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearSetCompoundSystemDeflection._Cast_CylindricalGearSetCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSetCompoundSystemDeflection:
    """Special nested class for casting CylindricalGearSetCompoundSystemDeflection to subclasses."""

    __parent__: "CylindricalGearSetCompoundSystemDeflection"

    @property
    def gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2997.GearSetCompoundSystemDeflection":
        return self.__parent__._cast(_2997.GearSetCompoundSystemDeflection)

    @property
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3038.SpecialisedAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3038,
        )

        return self.__parent__._cast(_3038.SpecialisedAssemblyCompoundSystemDeflection)

    @property
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2936.AbstractAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2936,
        )

        return self.__parent__._cast(_2936.AbstractAssemblyCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3018.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3018,
        )

        return self.__parent__._cast(_3018.PartCompoundSystemDeflection)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7708.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def planetary_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3023.PlanetaryGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3023,
        )

        return self.__parent__._cast(_3023.PlanetaryGearSetCompoundSystemDeflection)

    @property
    def cylindrical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "CylindricalGearSetCompoundSystemDeflection":
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
class CylindricalGearSetCompoundSystemDeflection(_2997.GearSetCompoundSystemDeflection):
    """CylindricalGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def advanced_ltca_results(
        self: "Self",
    ) -> "_1140.CylindricalGearSetMicroGeometryDutyCycle":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometryDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def advanced_ltca_results_only_first_planetary_mesh(
        self: "Self",
    ) -> "_1140.CylindricalGearSetMicroGeometryDutyCycle":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometryDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: "Self") -> "_2582.CylindricalGearSet":
        """mastapy._private.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def basic_ltca_results(
        self: "Self",
    ) -> "_1140.CylindricalGearSetMicroGeometryDutyCycle":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometryDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def basic_ltca_results_only_first_planetary_mesh(
        self: "Self",
    ) -> "_1140.CylindricalGearSetMicroGeometryDutyCycle":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometryDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_rating(
        self: "Self",
    ) -> "_474.CylindricalGearSetDutyCycleRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_rating_using_basic_ltca(
        self: "Self",
    ) -> "_474.CylindricalGearSetDutyCycleRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetRatingUsingBasicLTCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case_rating_with_lowest_safety_factor_for_scuffing(
        self: "Self",
    ) -> "_475.CylindricalGearSetRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseRatingWithLowestSafetyFactorForScuffing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_2827.CylindricalGearSetSystemDeflectionWithLTCAResults]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gears_compound_system_deflection(
        self: "Self",
    ) -> "List[_2983.CylindricalGearCompoundSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalGearCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_system_deflection(
        self: "Self",
    ) -> "List[_2984.CylindricalGearMeshCompoundSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalGearMeshCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_2827.CylindricalGearSetSystemDeflectionWithLTCAResults]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSetCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSetCompoundSystemDeflection
        """
        return _Cast_CylindricalGearSetCompoundSystemDeflection(self)
