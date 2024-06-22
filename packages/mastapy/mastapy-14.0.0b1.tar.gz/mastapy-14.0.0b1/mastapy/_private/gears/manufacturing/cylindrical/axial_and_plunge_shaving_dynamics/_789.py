"""ShavingDynamicsCalculation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable, list_with_selected_item
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAVING_DYNAMICS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsCalculation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, Union, Tuple

    from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _785,
        _784,
        _788,
        _775,
        _776,
        _781,
        _782,
        _790,
        _791,
    )
    from mastapy._private.gears.manufacturing.cylindrical.cutter_simulation import _755
    from mastapy._private.gears.gear_designs.cylindrical import _1055
    from mastapy._private.gears.manufacturing.cylindrical.cutters import _738

    Self = TypeVar("Self", bound="ShavingDynamicsCalculation")
    CastSelf = TypeVar(
        "CastSelf", bound="ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation"
    )

T = TypeVar("T", bound="_788.ShavingDynamics")

__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsCalculation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShavingDynamicsCalculation:
    """Special nested class for casting ShavingDynamicsCalculation to subclasses."""

    __parent__: "ShavingDynamicsCalculation"

    @property
    def conventional_shaving_dynamics_calculation_for_designed_gears(
        self: "CastSelf",
    ) -> "_775.ConventionalShavingDynamicsCalculationForDesignedGears":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _775,
        )

        return self.__parent__._cast(
            _775.ConventionalShavingDynamicsCalculationForDesignedGears
        )

    @property
    def conventional_shaving_dynamics_calculation_for_hobbed_gears(
        self: "CastSelf",
    ) -> "_776.ConventionalShavingDynamicsCalculationForHobbedGears":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _776,
        )

        return self.__parent__._cast(
            _776.ConventionalShavingDynamicsCalculationForHobbedGears
        )

    @property
    def plunge_shaving_dynamics_calculation_for_designed_gears(
        self: "CastSelf",
    ) -> "_781.PlungeShavingDynamicsCalculationForDesignedGears":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _781,
        )

        return self.__parent__._cast(
            _781.PlungeShavingDynamicsCalculationForDesignedGears
        )

    @property
    def plunge_shaving_dynamics_calculation_for_hobbed_gears(
        self: "CastSelf",
    ) -> "_782.PlungeShavingDynamicsCalculationForHobbedGears":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _782,
        )

        return self.__parent__._cast(
            _782.PlungeShavingDynamicsCalculationForHobbedGears
        )

    @property
    def shaving_dynamics_calculation_for_designed_gears(
        self: "CastSelf",
    ) -> "_790.ShavingDynamicsCalculationForDesignedGears":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _790,
        )

        return self.__parent__._cast(_790.ShavingDynamicsCalculationForDesignedGears)

    @property
    def shaving_dynamics_calculation_for_hobbed_gears(
        self: "CastSelf",
    ) -> "_791.ShavingDynamicsCalculationForHobbedGears":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _791,
        )

        return self.__parent__._cast(_791.ShavingDynamicsCalculationForHobbedGears)

    @property
    def shaving_dynamics_calculation(self: "CastSelf") -> "ShavingDynamicsCalculation":
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
class ShavingDynamicsCalculation(_0.APIBase, Generic[T]):
    """ShavingDynamicsCalculation

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _SHAVING_DYNAMICS_CALCULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def adjusted_tip_diameter(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedTipDiameter

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def life_cutter_normal_thickness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LifeCutterNormalThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @life_cutter_normal_thickness.setter
    @enforce_parameter_types
    def life_cutter_normal_thickness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LifeCutterNormalThickness = value

    @property
    def life_cutter_tip_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LifeCutterTipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @life_cutter_tip_diameter.setter
    @enforce_parameter_types
    def life_cutter_tip_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LifeCutterTipDiameter = value

    @property
    def new_cutter_tip_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NewCutterTipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def normal_tooth_thickness_reduction_between_redressings(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NormalToothThicknessReductionBetweenRedressings

        if temp is None:
            return 0.0

        return temp

    @normal_tooth_thickness_reduction_between_redressings.setter
    @enforce_parameter_types
    def normal_tooth_thickness_reduction_between_redressings(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.NormalToothThicknessReductionBetweenRedressings = (
            float(value) if value is not None else 0.0
        )

    @property
    def selected_redressing(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_T":
        """ListWithSelectedItem[T]"""
        temp = self.wrapped.SelectedRedressing

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_T",
        )(temp)

    @selected_redressing.setter
    @enforce_parameter_types
    def selected_redressing(self: "Self", value: "T") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_T.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_T.implicit_type()
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.SelectedRedressing = value

    @property
    def accuracy_level_iso6(self: "Self") -> "_785.RollAngleRangeRelativeToAccuracy":
        """mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.RollAngleRangeRelativeToAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyLevelISO6

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def accuracy_level_iso7(self: "Self") -> "_785.RollAngleRangeRelativeToAccuracy":
        """mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.RollAngleRangeRelativeToAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyLevelISO7

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def designed_gear(self: "Self") -> "_755.CylindricalCutterSimulatableGear":
        """mastapy._private.gears.manufacturing.cylindrical.cutter_simulation.CylindricalCutterSimulatableGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignedGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def life_cutter_start_of_shaving(
        self: "Self",
    ) -> "_1055.CylindricalGearProfileMeasurement":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeCutterStartOfShaving

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def life_shaver(self: "Self") -> "_738.CylindricalGearShaver":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.CylindricalGearShaver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeShaver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def new_cutter_start_of_shaving(
        self: "Self",
    ) -> "_1055.CylindricalGearProfileMeasurement":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NewCutterStartOfShaving

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaver(self: "Self") -> "_738.CylindricalGearShaver":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.CylindricalGearShaver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def redressing_settings(self: "Self") -> "List[_784.RedressingSettings[T]]":
        """List[mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.RedressingSettings[T]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingSettings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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

    def cutter_simulation_calculation_required(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CutterSimulationCalculationRequired()

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
    def cast_to(self: "Self") -> "_Cast_ShavingDynamicsCalculation":
        """Cast to another type.

        Returns:
            _Cast_ShavingDynamicsCalculation
        """
        return _Cast_ShavingDynamicsCalculation(self)
