"""AdvancedSystemDeflectionOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private.system_model.part_model.gears import _2588
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AdvancedSystemDeflectionOptions",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.ltca import _873
    from mastapy._private.system_model.analyses_and_results import _2767

    Self = TypeVar("Self", bound="AdvancedSystemDeflectionOptions")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AdvancedSystemDeflectionOptions._Cast_AdvancedSystemDeflectionOptions",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedSystemDeflectionOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AdvancedSystemDeflectionOptions:
    """Special nested class for casting AdvancedSystemDeflectionOptions to subclasses."""

    __parent__: "AdvancedSystemDeflectionOptions"

    @property
    def advanced_system_deflection_options(
        self: "CastSelf",
    ) -> "AdvancedSystemDeflectionOptions":
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
class AdvancedSystemDeflectionOptions(_0.APIBase):
    """AdvancedSystemDeflectionOptions

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ADVANCED_SYSTEM_DEFLECTION_OPTIONS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def include_pitch_error(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludePitchError

        if temp is None:
            return False

        return temp

    @include_pitch_error.setter
    @enforce_parameter_types
    def include_pitch_error(self: "Self", value: "bool") -> None:
        self.wrapped.IncludePitchError = bool(value) if value is not None else False

    @property
    def run_for_single_gear_set(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.RunForSingleGearSet

        if temp is None:
            return False

        return temp

    @run_for_single_gear_set.setter
    @enforce_parameter_types
    def run_for_single_gear_set(self: "Self", value: "bool") -> None:
        self.wrapped.RunForSingleGearSet = bool(value) if value is not None else False

    @property
    def seed_analysis(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.SeedAnalysis

        if temp is None:
            return False

        return temp

    @seed_analysis.setter
    @enforce_parameter_types
    def seed_analysis(self: "Self", value: "bool") -> None:
        self.wrapped.SeedAnalysis = bool(value) if value is not None else False

    @property
    def specified_gear_set(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_GearSet":
        """ListWithSelectedItem[mastapy._private.system_model.part_model.gears.GearSet]"""
        temp = self.wrapped.SpecifiedGearSet

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GearSet",
        )(temp)

    @specified_gear_set.setter
    @enforce_parameter_types
    def specified_gear_set(self: "Self", value: "_2588.GearSet") -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GearSet.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GearSet.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SpecifiedGearSet = value

    @property
    def total_number_of_time_steps(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.TotalNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @total_number_of_time_steps.setter
    @enforce_parameter_types
    def total_number_of_time_steps(self: "Self", value: "int") -> None:
        self.wrapped.TotalNumberOfTimeSteps = int(value) if value is not None else 0

    @property
    def use_advanced_ltca(self: "Self") -> "_873.UseAdvancedLTCAOptions":
        """mastapy._private.gears.ltca.UseAdvancedLTCAOptions"""
        temp = self.wrapped.UseAdvancedLTCA

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.LTCA.UseAdvancedLTCAOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.ltca._873", "UseAdvancedLTCAOptions"
        )(value)

    @use_advanced_ltca.setter
    @enforce_parameter_types
    def use_advanced_ltca(self: "Self", value: "_873.UseAdvancedLTCAOptions") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.LTCA.UseAdvancedLTCAOptions"
        )
        self.wrapped.UseAdvancedLTCA = value

    @property
    def use_data_logger(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseDataLogger

        if temp is None:
            return False

        return temp

    @use_data_logger.setter
    @enforce_parameter_types
    def use_data_logger(self: "Self", value: "bool") -> None:
        self.wrapped.UseDataLogger = bool(value) if value is not None else False

    @property
    def time_options(self: "Self") -> "_2767.TimeOptions":
        """mastapy._private.system_model.analyses_and_results.TimeOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AdvancedSystemDeflectionOptions":
        """Cast to another type.

        Returns:
            _Cast_AdvancedSystemDeflectionOptions
        """
        return _Cast_AdvancedSystemDeflectionOptions(self)
