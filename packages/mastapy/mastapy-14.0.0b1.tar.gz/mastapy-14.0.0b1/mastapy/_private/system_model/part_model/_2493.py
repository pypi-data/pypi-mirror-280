"""Bearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar


from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    enum_with_selected_value_runtime,
    overridable_enum_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import overridable, enum_with_selected_value
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.bearings.tolerances import _1955
from mastapy._private.materials.efficiency import _303
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.bearings import _1929
from mastapy._private.bearings.bearing_results import _1995, _2014
from mastapy._private.system_model.part_model import _2501
from mastapy._private._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ARRAY = python_net_import("System", "Array")
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.bearings.tolerances import (
        _1956,
        _1965,
        _1959,
        _1972,
        _1958,
        _1969,
        _1964,
        _1974,
        _1976,
    )
    from mastapy._private.bearings import _1925, _1938, _1921
    from mastapy._private.system_model.part_model import (
        _2494,
        _2492,
        _2529,
        _2495,
        _2499,
        _2520,
        _2498,
        _2524,
    )
    from mastapy._private.utility.report import _1834
    from mastapy._private.bearings.bearing_results import _2013
    from mastapy._private.bearings.bearing_designs import _2183
    from mastapy._private.math_utility.measured_vectors import _1610
    from mastapy._private.bearings.bearing_results.rolling import _2123
    from mastapy._private.materials import _278
    from mastapy._private.system_model.part_model.shaft_model import _2538
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="Bearing")
    CastSelf = TypeVar("CastSelf", bound="Bearing._Cast_Bearing")


__docformat__ = "restructuredtext en"
__all__ = ("Bearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Bearing:
    """Special nested class for casting Bearing to subclasses."""

    __parent__: "Bearing"

    @property
    def connector(self: "CastSelf") -> "_2501.Connector":
        return self.__parent__._cast(_2501.Connector)

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        from mastapy._private.system_model.part_model import _2498

        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def bearing(self: "CastSelf") -> "Bearing":
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
class Bearing(_2501.Connector):
    """Bearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def axial_displacement_preload(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    @enforce_parameter_types
    def axial_displacement_preload(self: "Self", value: "float") -> None:
        self.wrapped.AxialDisplacementPreload = (
            float(value) if value is not None else 0.0
        )

    @property
    def axial_force_preload(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AxialForcePreload

        if temp is None:
            return 0.0

        return temp

    @axial_force_preload.setter
    @enforce_parameter_types
    def axial_force_preload(self: "Self", value: "float") -> None:
        self.wrapped.AxialForcePreload = float(value) if value is not None else 0.0

    @property
    def axial_internal_clearance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_internal_clearance.setter
    @enforce_parameter_types
    def axial_internal_clearance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialInternalClearance = value

    @property
    def axial_stiffness_at_mounting_points(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AxialStiffnessAtMountingPoints

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness_at_mounting_points.setter
    @enforce_parameter_types
    def axial_stiffness_at_mounting_points(self: "Self", value: "float") -> None:
        self.wrapped.AxialStiffnessAtMountingPoints = (
            float(value) if value is not None else 0.0
        )

    @property
    def bearing_life_adjustment_factor_for_operating_conditions(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_life_adjustment_factor_for_operating_conditions.setter
    @enforce_parameter_types
    def bearing_life_adjustment_factor_for_operating_conditions(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions = value

    @property
    def bearing_life_adjustment_factor_for_special_bearing_properties(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_life_adjustment_factor_for_special_bearing_properties.setter
    @enforce_parameter_types
    def bearing_life_adjustment_factor_for_special_bearing_properties(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties = value

    @property
    def bearing_life_modification_factor(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingLifeModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_life_modification_factor.setter
    @enforce_parameter_types
    def bearing_life_modification_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingLifeModificationFactor = value

    @property
    def bearing_tolerance_class(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass":
        """EnumWithSelectedValue[mastapy._private.bearings.tolerances.BearingToleranceClass]"""
        temp = self.wrapped.BearingToleranceClass

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @bearing_tolerance_class.setter
    @enforce_parameter_types
    def bearing_tolerance_class(
        self: "Self", value: "_1955.BearingToleranceClass"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingToleranceClass = value

    @property
    def bearing_tolerance_definition(
        self: "Self",
    ) -> "_1956.BearingToleranceDefinitionOptions":
        """mastapy._private.bearings.tolerances.BearingToleranceDefinitionOptions"""
        temp = self.wrapped.BearingToleranceDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.BearingToleranceDefinitionOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.tolerances._1956",
            "BearingToleranceDefinitionOptions",
        )(value)

    @bearing_tolerance_definition.setter
    @enforce_parameter_types
    def bearing_tolerance_definition(
        self: "Self", value: "_1956.BearingToleranceDefinitionOptions"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.BearingToleranceDefinitionOptions"
        )
        self.wrapped.BearingToleranceDefinition = value

    @property
    def coefficient_of_friction(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @coefficient_of_friction.setter
    @enforce_parameter_types
    def coefficient_of_friction(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CoefficientOfFriction = value

    @property
    def damping_options(self: "Self") -> "_1925.BearingDampingMatrixOption":
        """mastapy._private.bearings.BearingDampingMatrixOption"""
        temp = self.wrapped.DampingOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDampingMatrixOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings._1925", "BearingDampingMatrixOption"
        )(value)

    @damping_options.setter
    @enforce_parameter_types
    def damping_options(
        self: "Self", value: "_1925.BearingDampingMatrixOption"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingDampingMatrixOption"
        )
        self.wrapped.DampingOptions = value

    @property
    def diameter_of_contact_on_inner_race_at_nominal_contact_angle(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterOfContactOnInnerRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_of_contact_on_left_race(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterOfContactOnLeftRace

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_of_contact_on_outer_race_at_nominal_contact_angle(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterOfContactOnOuterRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_of_contact_on_right_race(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterOfContactOnRightRace

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency_rating_method(
        self: "Self",
    ) -> "overridable.Overridable_BearingEfficiencyRatingMethod":
        """Overridable[mastapy._private.materials.efficiency.BearingEfficiencyRatingMethod]"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = overridable.Overridable_BearingEfficiencyRatingMethod.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(
        self: "Self",
        value: "Union[_303.BearingEfficiencyRatingMethod, Tuple[_303.BearingEfficiencyRatingMethod, bool]]",
    ) -> None:
        wrapper_type = (
            overridable.Overridable_BearingEfficiencyRatingMethod.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_BearingEfficiencyRatingMethod.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def feed_flow_rate(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FeedFlowRate

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @feed_flow_rate.setter
    @enforce_parameter_types
    def feed_flow_rate(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FeedFlowRate = value

    @property
    def feed_pressure(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FeedPressure

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @feed_pressure.setter
    @enforce_parameter_types
    def feed_pressure(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FeedPressure = value

    @property
    def first_element_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FirstElementAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @first_element_angle.setter
    @enforce_parameter_types
    def first_element_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FirstElementAngle = value

    @property
    def force_at_zero_displacement_input_method(
        self: "Self",
    ) -> "_2494.BearingF0InputMethod":
        """mastapy._private.system_model.part_model.BearingF0InputMethod"""
        temp = self.wrapped.ForceAtZeroDisplacementInputMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.BearingF0InputMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.part_model._2494", "BearingF0InputMethod"
        )(value)

    @force_at_zero_displacement_input_method.setter
    @enforce_parameter_types
    def force_at_zero_displacement_input_method(
        self: "Self", value: "_2494.BearingF0InputMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.BearingF0InputMethod"
        )
        self.wrapped.ForceAtZeroDisplacementInputMethod = value

    @property
    def has_radial_mounting_clearance(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.HasRadialMountingClearance

        if temp is None:
            return False

        return temp

    @has_radial_mounting_clearance.setter
    @enforce_parameter_types
    def has_radial_mounting_clearance(self: "Self", value: "bool") -> None:
        self.wrapped.HasRadialMountingClearance = (
            bool(value) if value is not None else False
        )

    @property
    def inner_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_diameter.setter
    @enforce_parameter_types
    def inner_diameter(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerDiameter = value

    @property
    def inner_fitting_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFittingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_node_position_from_centre(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def is_internal_clearance_adjusted_after_fitting(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IsInternalClearanceAdjustedAfterFitting

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @is_internal_clearance_adjusted_after_fitting.setter
    @enforce_parameter_types
    def is_internal_clearance_adjusted_after_fitting(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IsInternalClearanceAdjustedAfterFitting = value

    @property
    def journal_bearing_type(self: "Self") -> "_1938.JournalBearingType":
        """mastapy._private.bearings.JournalBearingType"""
        temp = self.wrapped.JournalBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.JournalBearingType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings._1938", "JournalBearingType"
        )(value)

    @journal_bearing_type.setter
    @enforce_parameter_types
    def journal_bearing_type(self: "Self", value: "_1938.JournalBearingType") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.JournalBearingType"
        )
        self.wrapped.JournalBearingType = value

    @property
    def left_node_position_from_centre(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: "Self", value: "float") -> None:
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def lubrication_detail(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.LubricationDetail.SelectedItemName

        if temp is None:
            return ""

        return temp

    @lubrication_detail.setter
    @enforce_parameter_types
    def lubrication_detail(self: "Self", value: "str") -> None:
        self.wrapped.LubricationDetail.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def maximum_bearing_life_modification_factor(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumBearingLifeModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_bearing_life_modification_factor.setter
    @enforce_parameter_types
    def maximum_bearing_life_modification_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumBearingLifeModificationFactor = value

    @property
    def model(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BearingModel":
        """EnumWithSelectedValue[mastapy._private.bearings.BearingModel]"""
        temp = self.wrapped.Model

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BearingModel.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @model.setter
    @enforce_parameter_types
    def model(self: "Self", value: "_1929.BearingModel") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Model = value

    @property
    def offset_of_contact_on_inner_race_at_nominal_contact_angle(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetOfContactOnInnerRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_of_contact_on_left_race(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetOfContactOnLeftRace

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_of_contact_on_outer_race_at_nominal_contact_angle(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetOfContactOnOuterRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_of_contact_on_right_race(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetOfContactOnRightRace

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self: "Self") -> "_2013.Orientations":
        """mastapy._private.bearings.bearing_results.Orientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.bearing_results._2013", "Orientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: "Self", value: "_2013.Orientations") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )
        self.wrapped.Orientation = value

    @property
    def outer_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterDiameter = value

    @property
    def outer_fitting_chart(self: "Self") -> "_1834.SimpleChartDefinition":
        """mastapy._private.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterFittingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_node_position_from_centre(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def override_design_lubrication_detail(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignLubricationDetail

        if temp is None:
            return False

        return temp

    @override_design_lubrication_detail.setter
    @enforce_parameter_types
    def override_design_lubrication_detail(self: "Self", value: "bool") -> None:
        self.wrapped.OverrideDesignLubricationDetail = (
            bool(value) if value is not None else False
        )

    @property
    def percentage_difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_load_calculation_method(
        self: "Self",
    ) -> "overridable.Overridable_CylindricalRollerMaxAxialLoadMethod":
        """Overridable[mastapy._private.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod]"""
        temp = self.wrapped.PermissibleAxialLoadCalculationMethod

        if temp is None:
            return None

        value = (
            overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapped_type()
        )
        return overridable_enum_runtime.create(temp, value)

    @permissible_axial_load_calculation_method.setter
    @enforce_parameter_types
    def permissible_axial_load_calculation_method(
        self: "Self",
        value: "Union[_1995.CylindricalRollerMaxAxialLoadMethod, Tuple[_1995.CylindricalRollerMaxAxialLoadMethod, bool]]",
    ) -> None:
        wrapper_type = (
            overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.PermissibleAxialLoadCalculationMethod = value

    @property
    def permissible_track_truncation(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PermissibleTrackTruncation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @permissible_track_truncation.setter
    @enforce_parameter_types
    def permissible_track_truncation(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PermissibleTrackTruncation = value

    @property
    def preload(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PreloadType":
        """EnumWithSelectedValue[mastapy._private.bearings.bearing_results.PreloadType]"""
        temp = self.wrapped.Preload

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PreloadType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @preload.setter
    @enforce_parameter_types
    def preload(self: "Self", value: "_2014.PreloadType") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Preload = value

    @property
    def preload_spring_initial_compression(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PreloadSpringInitialCompression

        if temp is None:
            return 0.0

        return temp

    @preload_spring_initial_compression.setter
    @enforce_parameter_types
    def preload_spring_initial_compression(self: "Self", value: "float") -> None:
        self.wrapped.PreloadSpringInitialCompression = (
            float(value) if value is not None else 0.0
        )

    @property
    def preload_spring_max_travel(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PreloadSpringMaxTravel

        if temp is None:
            return 0.0

        return temp

    @preload_spring_max_travel.setter
    @enforce_parameter_types
    def preload_spring_max_travel(self: "Self", value: "float") -> None:
        self.wrapped.PreloadSpringMaxTravel = float(value) if value is not None else 0.0

    @property
    def preload_spring_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PreloadSpringStiffness

        if temp is None:
            return 0.0

        return temp

    @preload_spring_stiffness.setter
    @enforce_parameter_types
    def preload_spring_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.PreloadSpringStiffness = float(value) if value is not None else 0.0

    @property
    def preload_spring_on_outer(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.PreloadSpringOnOuter

        if temp is None:
            return False

        return temp

    @preload_spring_on_outer.setter
    @enforce_parameter_types
    def preload_spring_on_outer(self: "Self", value: "bool") -> None:
        self.wrapped.PreloadSpringOnOuter = bool(value) if value is not None else False

    @property
    def preload_is_from_left(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.PreloadIsFromLeft

        if temp is None:
            return False

        return temp

    @preload_is_from_left.setter
    @enforce_parameter_types
    def preload_is_from_left(self: "Self", value: "bool") -> None:
        self.wrapped.PreloadIsFromLeft = bool(value) if value is not None else False

    @property
    def radial_internal_clearance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_internal_clearance.setter
    @enforce_parameter_types
    def radial_internal_clearance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialInternalClearance = value

    @property
    def right_node_position_from_centre(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def system_includes_oil_pump(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemIncludesOilPump

        if temp is None:
            return False

        return temp

    @property
    def use_design_iso14179_settings(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignISO14179Settings

        if temp is None:
            return False

        return temp

    @use_design_iso14179_settings.setter
    @enforce_parameter_types
    def use_design_iso14179_settings(self: "Self", value: "bool") -> None:
        self.wrapped.UseDesignISO14179Settings = (
            bool(value) if value is not None else False
        )

    @property
    def axial_internal_clearance_tolerance(
        self: "Self",
    ) -> "_2492.AxialInternalClearanceTolerance":
        """mastapy._private.system_model.part_model.AxialInternalClearanceTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialInternalClearanceTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def detail(self: "Self") -> "_2183.BearingDesign":
        """mastapy._private.bearings.bearing_designs.BearingDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Detail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def displacement_for_stiffness_operating_point(
        self: "Self",
    ) -> "_1610.VectorWithLinearAndAngularComponents":
        """mastapy._private.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementForStiffnessOperatingPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_at_zero_displacement(
        self: "Self",
    ) -> "_1610.VectorWithLinearAndAngularComponents":
        """mastapy._private.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAtZeroDisplacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_for_stiffness_operating_point(
        self: "Self",
    ) -> "_1610.VectorWithLinearAndAngularComponents":
        """mastapy._private.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceForStiffnessOperatingPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def friction_coefficients(
        self: "Self",
    ) -> "_2123.RollingBearingFrictionCoefficients":
        """mastapy._private.bearings.bearing_results.rolling.RollingBearingFrictionCoefficients

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionCoefficients

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_mounting_sleeve_bore_tolerance(
        self: "Self",
    ) -> "_1965.OuterSupportTolerance":
        """mastapy._private.bearings.tolerances.OuterSupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerMountingSleeveBoreTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_mounting_sleeve_outer_diameter_tolerance(
        self: "Self",
    ) -> "_1959.InnerSupportTolerance":
        """mastapy._private.bearings.tolerances.InnerSupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerMountingSleeveOuterDiameterTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_support_detail(self: "Self") -> "_1972.SupportDetail":
        """mastapy._private.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_support_detail(self: "Self") -> "_1972.SupportDetail":
        """mastapy._private.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_mounting_sleeve_bore_tolerance(
        self: "Self",
    ) -> "_1965.OuterSupportTolerance":
        """mastapy._private.bearings.tolerances.OuterSupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterMountingSleeveBoreTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_mounting_sleeve_outer_diameter_tolerance(
        self: "Self",
    ) -> "_1959.InnerSupportTolerance":
        """mastapy._private.bearings.tolerances.InnerSupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterMountingSleeveOuterDiameterTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_support_detail(self: "Self") -> "_1972.SupportDetail":
        """mastapy._private.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overridden_lubrication_detail(self: "Self") -> "_278.LubricationDetail":
        """mastapy._private.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverriddenLubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def radial_internal_clearance_tolerance(
        self: "Self",
    ) -> "_2529.RadialInternalClearanceTolerance":
        """mastapy._private.system_model.part_model.RadialInternalClearanceTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialInternalClearanceTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_support_detail(self: "Self") -> "_1972.SupportDetail":
        """mastapy._private.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_tolerance_inner(self: "Self") -> "_1958.InnerRingTolerance":
        """mastapy._private.bearings.tolerances.InnerRingTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingToleranceInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_tolerance_left(self: "Self") -> "_1969.RingTolerance":
        """mastapy._private.bearings.tolerances.RingTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingToleranceLeft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_tolerance_outer(self: "Self") -> "_1964.OuterRingTolerance":
        """mastapy._private.bearings.tolerances.OuterRingTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingToleranceOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_tolerance_right(self: "Self") -> "_1969.RingTolerance":
        """mastapy._private.bearings.tolerances.RingTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingToleranceRight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def simple_bearing_detail_property(self: "Self") -> "_2183.BearingDesign":
        """mastapy._private.bearings.bearing_designs.BearingDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def support_tolerance_inner(self: "Self") -> "_1959.InnerSupportTolerance":
        """mastapy._private.bearings.tolerances.InnerSupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SupportToleranceInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def support_tolerance_left(self: "Self") -> "_1974.SupportTolerance":
        """mastapy._private.bearings.tolerances.SupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SupportToleranceLeft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def support_tolerance_outer(self: "Self") -> "_1965.OuterSupportTolerance":
        """mastapy._private.bearings.tolerances.OuterSupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SupportToleranceOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def support_tolerance_right(self: "Self") -> "_1974.SupportTolerance":
        """mastapy._private.bearings.tolerances.SupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SupportToleranceRight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mounting(self: "Self") -> "List[_2495.BearingRaceMountingOptions]":
        """List[mastapy._private.system_model.part_model.BearingRaceMountingOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tolerance_combinations(self: "Self") -> "List[_1976.ToleranceCombination]":
        """List[mastapy._private.bearings.tolerances.ToleranceCombination]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToleranceCombinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def is_radial_bearing(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsRadialBearing

        if temp is None:
            return False

        return temp

    @property
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(
        self: "Self",
    ) -> "List[List[float]]":
        """List[List[float]]"""
        temp = self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)

        if value is None:
            return None

        return value

    @specified_stiffness_for_linear_bearing_in_local_coordinate_system.setter
    @enforce_parameter_types
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(
        self: "Self", value: "List[List[float]]"
    ) -> None:
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem = value

    @enforce_parameter_types
    def set_detail_from_catalogue(
        self: "Self", catalogue: "_1921.BearingCatalog", designation: "str"
    ) -> None:
        """Method does not return.

        Args:
            catalogue (mastapy._private.bearings.BearingCatalog)
            designation (str)
        """
        catalogue = conversion.mp_to_pn_enum(
            catalogue, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        designation = str(designation)
        self.wrapped.SetDetailFromCatalogue(
            catalogue, designation if designation else ""
        )

    @enforce_parameter_types
    def try_attach_left_side_to(
        self: "Self", shaft: "_2538.Shaft", offset: "float" = float("nan")
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy._private.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryAttachLeftSideTo(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_attach_right_side_to(
        self: "Self", shaft: "_2538.Shaft", offset: "float" = float("nan")
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy._private.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryAttachRightSideTo(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_Bearing":
        """Cast to another type.

        Returns:
            _Cast_Bearing
        """
        return _Cast_Bearing(self)
