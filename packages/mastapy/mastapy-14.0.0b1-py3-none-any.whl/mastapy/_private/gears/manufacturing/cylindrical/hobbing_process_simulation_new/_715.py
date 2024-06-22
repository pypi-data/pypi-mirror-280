"""WormGrindingCutterCalculation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _717,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_WORM_GRINDING_CUTTER_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingCutterCalculation",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.gears.manufacturing.cylindrical.plunge_shaving import _676
    from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _703,
    )

    Self = TypeVar("Self", bound="WormGrindingCutterCalculation")
    CastSelf = TypeVar(
        "CastSelf",
        bound="WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingCutterCalculation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGrindingCutterCalculation:
    """Special nested class for casting WormGrindingCutterCalculation to subclasses."""

    __parent__: "WormGrindingCutterCalculation"

    @property
    def worm_grinding_process_calculation(
        self: "CastSelf",
    ) -> "_717.WormGrindingProcessCalculation":
        return self.__parent__._cast(_717.WormGrindingProcessCalculation)

    @property
    def process_calculation(self: "CastSelf") -> "_703.ProcessCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _703,
        )

        return self.__parent__._cast(_703.ProcessCalculation)

    @property
    def worm_grinding_cutter_calculation(
        self: "CastSelf",
    ) -> "WormGrindingCutterCalculation":
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
class WormGrindingCutterCalculation(_717.WormGrindingProcessCalculation):
    """WormGrindingCutterCalculation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GRINDING_CUTTER_CALCULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def grinder_tooth_shape_chart(self: "Self") -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GrinderToothShapeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_profile_bands(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    @enforce_parameter_types
    def number_of_profile_bands(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def use_design_mode_micro_geometry(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignModeMicroGeometry

        if temp is None:
            return False

        return temp

    @use_design_mode_micro_geometry.setter
    @enforce_parameter_types
    def use_design_mode_micro_geometry(self: "Self", value: "bool") -> None:
        self.wrapped.UseDesignModeMicroGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def worm_axial_z(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormAxialZ

        if temp is None:
            return 0.0

        return temp

    @property
    def worm_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def input_gear_point_of_interest(self: "Self") -> "_676.PointOfInterest":
        """mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.PointOfInterest

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputGearPointOfInterest

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def calculate_grinder_axial_section_tooth_shape(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CalculateGrinderAxialSectionToothShape()

    def calculate_point_of_interest(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CalculatePointOfInterest()

    @property
    def cast_to(self: "Self") -> "_Cast_WormGrindingCutterCalculation":
        """Cast to another type.

        Returns:
            _Cast_WormGrindingCutterCalculation
        """
        return _Cast_WormGrindingCutterCalculation(self)
