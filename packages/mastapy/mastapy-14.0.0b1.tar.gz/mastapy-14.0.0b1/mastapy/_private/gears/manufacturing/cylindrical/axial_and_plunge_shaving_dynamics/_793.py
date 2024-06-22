"""ShavingDynamicsViewModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.gears.gear_designs.cylindrical import _1111
from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _794,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsViewModel",
)

if TYPE_CHECKING:
    from typing import Any, Type, List

    from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _772,
        _789,
        _784,
        _788,
        _777,
        _783,
    )
    from mastapy._private.gears.gear_designs.cylindrical import _1056
    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.gears.manufacturing.cylindrical import _651

    Self = TypeVar("Self", bound="ShavingDynamicsViewModel")
    CastSelf = TypeVar(
        "CastSelf", bound="ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel"
    )

T = TypeVar("T", bound="_788.ShavingDynamics")

__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsViewModel",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShavingDynamicsViewModel:
    """Special nested class for casting ShavingDynamicsViewModel to subclasses."""

    __parent__: "ShavingDynamicsViewModel"

    @property
    def shaving_dynamics_view_model_base(
        self: "CastSelf",
    ) -> "_794.ShavingDynamicsViewModelBase":
        return self.__parent__._cast(_794.ShavingDynamicsViewModelBase)

    @property
    def gear_manufacturing_configuration_view_model(
        self: "CastSelf",
    ) -> "_651.GearManufacturingConfigurationViewModel":
        from mastapy._private.gears.manufacturing.cylindrical import _651

        return self.__parent__._cast(_651.GearManufacturingConfigurationViewModel)

    @property
    def conventional_shaving_dynamics_view_model(
        self: "CastSelf",
    ) -> "_777.ConventionalShavingDynamicsViewModel":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _777,
        )

        return self.__parent__._cast(_777.ConventionalShavingDynamicsViewModel)

    @property
    def plunge_shaving_dynamics_view_model(
        self: "CastSelf",
    ) -> "_783.PlungeShavingDynamicsViewModel":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _783,
        )

        return self.__parent__._cast(_783.PlungeShavingDynamicsViewModel)

    @property
    def shaving_dynamics_view_model(self: "CastSelf") -> "ShavingDynamicsViewModel":
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
class ShavingDynamicsViewModel(_794.ShavingDynamicsViewModelBase, Generic[T]):
    """ShavingDynamicsViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _SHAVING_DYNAMICS_VIEW_MODEL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def active_profile_range_calculation_source(
        self: "Self",
    ) -> "_772.ActiveProfileRangeCalculationSource":
        """mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ActiveProfileRangeCalculationSource"""
        temp = self.wrapped.ActiveProfileRangeCalculationSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.ActiveProfileRangeCalculationSource",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics._772",
            "ActiveProfileRangeCalculationSource",
        )(value)

    @active_profile_range_calculation_source.setter
    @enforce_parameter_types
    def active_profile_range_calculation_source(
        self: "Self", value: "_772.ActiveProfileRangeCalculationSource"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.ActiveProfileRangeCalculationSource",
        )
        self.wrapped.ActiveProfileRangeCalculationSource = value

    @property
    def chart_display_method(
        self: "Self",
    ) -> "_1056.CylindricalGearProfileMeasurementType":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurementType"""
        temp = self.wrapped.ChartDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1056",
            "CylindricalGearProfileMeasurementType",
        )(value)

    @chart_display_method.setter
    @enforce_parameter_types
    def chart_display_method(
        self: "Self", value: "_1056.CylindricalGearProfileMeasurementType"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )
        self.wrapped.ChartDisplayMethod = value

    @property
    def redressing_chart(self: "Self") -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_measurement_method(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ThicknessType":
        """EnumWithSelectedValue[mastapy._private.gears.gear_designs.cylindrical.ThicknessType]"""
        temp = self.wrapped.SelectedMeasurementMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ThicknessType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @selected_measurement_method.setter
    @enforce_parameter_types
    def selected_measurement_method(self: "Self", value: "_1111.ThicknessType") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SelectedMeasurementMethod = value

    @property
    def shaver_tip_diameter_adjustment(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShaverTipDiameterAdjustment

        if temp is None:
            return 0.0

        return temp

    @shaver_tip_diameter_adjustment.setter
    @enforce_parameter_types
    def shaver_tip_diameter_adjustment(self: "Self", value: "float") -> None:
        self.wrapped.ShaverTipDiameterAdjustment = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_shaver_from_database(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseShaverFromDatabase

        if temp is None:
            return False

        return temp

    @use_shaver_from_database.setter
    @enforce_parameter_types
    def use_shaver_from_database(self: "Self", value: "bool") -> None:
        self.wrapped.UseShaverFromDatabase = bool(value) if value is not None else False

    @property
    def calculation(self: "Self") -> "_789.ShavingDynamicsCalculation[T]":
        """mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShavingDynamicsCalculation[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Calculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

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

    def add_shaver_to_database(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.AddShaverToDatabase()

    def calculate(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Calculate()

    @property
    def cast_to(self: "Self") -> "_Cast_ShavingDynamicsViewModel":
        """Cast to another type.

        Returns:
            _Cast_ShavingDynamicsViewModel
        """
        return _Cast_ShavingDynamicsViewModel(self)
