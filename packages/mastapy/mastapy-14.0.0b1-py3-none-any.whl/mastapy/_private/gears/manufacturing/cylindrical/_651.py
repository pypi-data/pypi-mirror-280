"""GearManufacturingConfigurationViewModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "GearManufacturingConfigurationViewModel",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical import _652
    from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _697,
        _710,
        _724,
    )
    from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _777,
        _783,
        _793,
        _794,
    )

    Self = TypeVar("Self", bound="GearManufacturingConfigurationViewModel")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearManufacturingConfigurationViewModel",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearManufacturingConfigurationViewModel:
    """Special nested class for casting GearManufacturingConfigurationViewModel to subclasses."""

    __parent__: "GearManufacturingConfigurationViewModel"

    @property
    def gear_manufacturing_configuration_view_model_placeholder(
        self: "CastSelf",
    ) -> "_652.GearManufacturingConfigurationViewModelPlaceholder":
        from mastapy._private.gears.manufacturing.cylindrical import _652

        return self.__parent__._cast(
            _652.GearManufacturingConfigurationViewModelPlaceholder
        )

    @property
    def hobbing_process_simulation_view_model(
        self: "CastSelf",
    ) -> "_697.HobbingProcessSimulationViewModel":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _697,
        )

        return self.__parent__._cast(_697.HobbingProcessSimulationViewModel)

    @property
    def process_simulation_view_model(
        self: "CastSelf",
    ) -> "_710.ProcessSimulationViewModel":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _710,
        )

        return self.__parent__._cast(_710.ProcessSimulationViewModel)

    @property
    def worm_grinding_process_simulation_view_model(
        self: "CastSelf",
    ) -> "_724.WormGrindingProcessSimulationViewModel":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _724,
        )

        return self.__parent__._cast(_724.WormGrindingProcessSimulationViewModel)

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
    def shaving_dynamics_view_model(
        self: "CastSelf",
    ) -> "_793.ShavingDynamicsViewModel":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _793,
        )

        return self.__parent__._cast(_793.ShavingDynamicsViewModel)

    @property
    def shaving_dynamics_view_model_base(
        self: "CastSelf",
    ) -> "_794.ShavingDynamicsViewModelBase":
        from mastapy._private.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
            _794,
        )

        return self.__parent__._cast(_794.ShavingDynamicsViewModelBase)

    @property
    def gear_manufacturing_configuration_view_model(
        self: "CastSelf",
    ) -> "GearManufacturingConfigurationViewModel":
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
class GearManufacturingConfigurationViewModel(_0.APIBase):
    """GearManufacturingConfigurationViewModel

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

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
    def cast_to(self: "Self") -> "_Cast_GearManufacturingConfigurationViewModel":
        """Cast to another type.

        Returns:
            _Cast_GearManufacturingConfigurationViewModel
        """
        return _Cast_GearManufacturingConfigurationViewModel(self)
