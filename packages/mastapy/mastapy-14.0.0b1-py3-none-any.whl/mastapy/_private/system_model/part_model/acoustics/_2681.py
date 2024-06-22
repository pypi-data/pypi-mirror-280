"""AcousticAnalysisOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ACOUSTIC_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Acoustics", "AcousticAnalysisOptions"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.acoustic_analyses import (
        _7693,
        _7694,
        _7696,
        _7695,
        _7691,
    )

    Self = TypeVar("Self", bound="AcousticAnalysisOptions")
    CastSelf = TypeVar(
        "CastSelf", bound="AcousticAnalysisOptions._Cast_AcousticAnalysisOptions"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AcousticAnalysisOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AcousticAnalysisOptions:
    """Special nested class for casting AcousticAnalysisOptions to subclasses."""

    __parent__: "AcousticAnalysisOptions"

    @property
    def acoustic_analysis_options(self: "CastSelf") -> "AcousticAnalysisOptions":
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
class AcousticAnalysisOptions(_0.APIBase):
    """AcousticAnalysisOptions

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ACOUSTIC_ANALYSIS_OPTIONS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def force_unit_velocity(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ForceUnitVelocity

        if temp is None:
            return False

        return temp

    @force_unit_velocity.setter
    @enforce_parameter_types
    def force_unit_velocity(self: "Self", value: "bool") -> None:
        self.wrapped.ForceUnitVelocity = bool(value) if value is not None else False

    @property
    def high_frequency_multiplier(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.HighFrequencyMultiplier

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @high_frequency_multiplier.setter
    @enforce_parameter_types
    def high_frequency_multiplier(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.HighFrequencyMultiplier = value

    @property
    def initial_guess(self: "Self") -> "_7693.InitialGuessOption":
        """mastapy._private.system_model.analyses_and_results.acoustic_analyses.InitialGuessOption"""
        temp = self.wrapped.InitialGuess

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.InitialGuessOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.analyses_and_results.acoustic_analyses._7693",
            "InitialGuessOption",
        )(value)

    @initial_guess.setter
    @enforce_parameter_types
    def initial_guess(self: "Self", value: "_7693.InitialGuessOption") -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.InitialGuessOption",
        )
        self.wrapped.InitialGuess = value

    @property
    def low_frequency_multiplier(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.LowFrequencyMultiplier

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @low_frequency_multiplier.setter
    @enforce_parameter_types
    def low_frequency_multiplier(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.LowFrequencyMultiplier = value

    @property
    def low_frequency_to_high_frequency_multiplier(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LowFrequencyToHighFrequencyMultiplier

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @low_frequency_to_high_frequency_multiplier.setter
    @enforce_parameter_types
    def low_frequency_to_high_frequency_multiplier(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LowFrequencyToHighFrequencyMultiplier = value

    @property
    def m2l_cache_type(self: "Self") -> "_7694.M2LHfCacheType":
        """mastapy._private.system_model.analyses_and_results.acoustic_analyses.M2LHfCacheType"""
        temp = self.wrapped.M2LCacheType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.M2LHfCacheType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.analyses_and_results.acoustic_analyses._7694",
            "M2LHfCacheType",
        )(value)

    @m2l_cache_type.setter
    @enforce_parameter_types
    def m2l_cache_type(self: "Self", value: "_7694.M2LHfCacheType") -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.M2LHfCacheType",
        )
        self.wrapped.M2LCacheType = value

    @property
    def maximum_level(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaximumLevel

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_level.setter
    @enforce_parameter_types
    def maximum_level(self: "Self", value: "Union[int, Tuple[int, bool]]") -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumLevel = value

    @property
    def maximum_number_of_elements(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaximumNumberOfElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_number_of_elements.setter
    @enforce_parameter_types
    def maximum_number_of_elements(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumNumberOfElements = value

    @property
    def octree_creation_method(self: "Self") -> "_7696.OctreeCreationMethod":
        """mastapy._private.system_model.analyses_and_results.acoustic_analyses.OctreeCreationMethod"""
        temp = self.wrapped.OctreeCreationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.OctreeCreationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.analyses_and_results.acoustic_analyses._7696",
            "OctreeCreationMethod",
        )(value)

    @octree_creation_method.setter
    @enforce_parameter_types
    def octree_creation_method(
        self: "Self", value: "_7696.OctreeCreationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.OctreeCreationMethod",
        )
        self.wrapped.OctreeCreationMethod = value

    @property
    def optimise_maximum_number_of_elements(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.OptimiseMaximumNumberOfElements

        if temp is None:
            return False

        return temp

    @optimise_maximum_number_of_elements.setter
    @enforce_parameter_types
    def optimise_maximum_number_of_elements(self: "Self", value: "bool") -> None:
        self.wrapped.OptimiseMaximumNumberOfElements = (
            bool(value) if value is not None else False
        )

    @property
    def perform_iterative_solver_logging(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.PerformIterativeSolverLogging

        if temp is None:
            return False

        return temp

    @perform_iterative_solver_logging.setter
    @enforce_parameter_types
    def perform_iterative_solver_logging(self: "Self", value: "bool") -> None:
        self.wrapped.PerformIterativeSolverLogging = (
            bool(value) if value is not None else False
        )

    @property
    def pre_calculate_near_field_integrals(
        self: "Self",
    ) -> "_7695.NearFieldIntegralsCacheType":
        """mastapy._private.system_model.analyses_and_results.acoustic_analyses.NearFieldIntegralsCacheType"""
        temp = self.wrapped.PreCalculateNearFieldIntegrals

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.NearFieldIntegralsCacheType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.analyses_and_results.acoustic_analyses._7695",
            "NearFieldIntegralsCacheType",
        )(value)

    @pre_calculate_near_field_integrals.setter
    @enforce_parameter_types
    def pre_calculate_near_field_integrals(
        self: "Self", value: "_7695.NearFieldIntegralsCacheType"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.NearFieldIntegralsCacheType",
        )
        self.wrapped.PreCalculateNearFieldIntegrals = value

    @property
    def preconditioner(self: "Self") -> "_7691.AcousticPreconditionerType":
        """mastapy._private.system_model.analyses_and_results.acoustic_analyses.AcousticPreconditionerType"""
        temp = self.wrapped.Preconditioner

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.AcousticPreconditionerType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.analyses_and_results.acoustic_analyses._7691",
            "AcousticPreconditionerType",
        )(value)

    @preconditioner.setter
    @enforce_parameter_types
    def preconditioner(self: "Self", value: "_7691.AcousticPreconditionerType") -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AcousticAnalyses.AcousticPreconditionerType",
        )
        self.wrapped.Preconditioner = value

    @property
    def show_advanced_solver_settings(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ShowAdvancedSolverSettings

        if temp is None:
            return False

        return temp

    @show_advanced_solver_settings.setter
    @enforce_parameter_types
    def show_advanced_solver_settings(self: "Self", value: "bool") -> None:
        self.wrapped.ShowAdvancedSolverSettings = (
            bool(value) if value is not None else False
        )

    @property
    def solver_maximum_iterations(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.SolverMaximumIterations

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @solver_maximum_iterations.setter
    @enforce_parameter_types
    def solver_maximum_iterations(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.SolverMaximumIterations = value

    @property
    def solver_relative_tolerance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SolverRelativeTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @solver_relative_tolerance.setter
    @enforce_parameter_types
    def solver_relative_tolerance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SolverRelativeTolerance = value

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
    def cast_to(self: "Self") -> "_Cast_AcousticAnalysisOptions":
        """Cast to another type.

        Returns:
            _Cast_AcousticAnalysisOptions
        """
        return _Cast_AcousticAnalysisOptions(self)
