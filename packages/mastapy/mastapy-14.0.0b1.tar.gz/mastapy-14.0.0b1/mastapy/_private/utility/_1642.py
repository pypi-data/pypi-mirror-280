"""PersistentSingleton"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PERSISTENT_SINGLETON = python_net_import("SMT.MastaAPI.Utility", "PersistentSingleton")

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.nodal_analysis import _68
    from mastapy._private.nodal_analysis.geometry_modeller_link import _167
    from mastapy._private.gears.materials import _610
    from mastapy._private.gears.ltca.cylindrical import _878
    from mastapy._private.gears.gear_designs.cylindrical import _1041
    from mastapy._private.utility import _1641, _1643, _1644
    from mastapy._private.utility.units_and_measurements import _1653
    from mastapy._private.utility.scripting import _1787
    from mastapy._private.utility.databases import _1877
    from mastapy._private.utility.cad_export import _1882
    from mastapy._private.bearings import _1951
    from mastapy._private.system_model.part_model import _2526

    Self = TypeVar("Self", bound="PersistentSingleton")
    CastSelf = TypeVar(
        "CastSelf", bound="PersistentSingleton._Cast_PersistentSingleton"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PersistentSingleton",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PersistentSingleton:
    """Special nested class for casting PersistentSingleton to subclasses."""

    __parent__: "PersistentSingleton"

    @property
    def fe_user_settings(self: "CastSelf") -> "_68.FEUserSettings":
        from mastapy._private.nodal_analysis import _68

        return self.__parent__._cast(_68.FEUserSettings)

    @property
    def geometry_modeller_settings(self: "CastSelf") -> "_167.GeometryModellerSettings":
        from mastapy._private.nodal_analysis.geometry_modeller_link import _167

        return self.__parent__._cast(_167.GeometryModellerSettings)

    @property
    def gear_material_expert_system_factor_settings(
        self: "CastSelf",
    ) -> "_610.GearMaterialExpertSystemFactorSettings":
        from mastapy._private.gears.materials import _610

        return self.__parent__._cast(_610.GearMaterialExpertSystemFactorSettings)

    @property
    def cylindrical_gear_fe_settings(
        self: "CastSelf",
    ) -> "_878.CylindricalGearFESettings":
        from mastapy._private.gears.ltca.cylindrical import _878

        return self.__parent__._cast(_878.CylindricalGearFESettings)

    @property
    def cylindrical_gear_defaults(self: "CastSelf") -> "_1041.CylindricalGearDefaults":
        from mastapy._private.gears.gear_designs.cylindrical import _1041

        return self.__parent__._cast(_1041.CylindricalGearDefaults)

    @property
    def per_machine_settings(self: "CastSelf") -> "_1641.PerMachineSettings":
        from mastapy._private.utility import _1641

        return self.__parent__._cast(_1641.PerMachineSettings)

    @property
    def program_settings(self: "CastSelf") -> "_1643.ProgramSettings":
        from mastapy._private.utility import _1643

        return self.__parent__._cast(_1643.ProgramSettings)

    @property
    def pushbullet_settings(self: "CastSelf") -> "_1644.PushbulletSettings":
        from mastapy._private.utility import _1644

        return self.__parent__._cast(_1644.PushbulletSettings)

    @property
    def measurement_settings(self: "CastSelf") -> "_1653.MeasurementSettings":
        from mastapy._private.utility.units_and_measurements import _1653

        return self.__parent__._cast(_1653.MeasurementSettings)

    @property
    def scripting_setup(self: "CastSelf") -> "_1787.ScriptingSetup":
        from mastapy._private.utility.scripting import _1787

        return self.__parent__._cast(_1787.ScriptingSetup)

    @property
    def database_settings(self: "CastSelf") -> "_1877.DatabaseSettings":
        from mastapy._private.utility.databases import _1877

        return self.__parent__._cast(_1877.DatabaseSettings)

    @property
    def cad_export_settings(self: "CastSelf") -> "_1882.CADExportSettings":
        from mastapy._private.utility.cad_export import _1882

        return self.__parent__._cast(_1882.CADExportSettings)

    @property
    def skf_settings(self: "CastSelf") -> "_1951.SKFSettings":
        from mastapy._private.bearings import _1951

        return self.__parent__._cast(_1951.SKFSettings)

    @property
    def planet_carrier_settings(self: "CastSelf") -> "_2526.PlanetCarrierSettings":
        from mastapy._private.system_model.part_model import _2526

        return self.__parent__._cast(_2526.PlanetCarrierSettings)

    @property
    def persistent_singleton(self: "CastSelf") -> "PersistentSingleton":
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
class PersistentSingleton(_0.APIBase):
    """PersistentSingleton

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PERSISTENT_SINGLETON

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

    def save(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Save()

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
    def cast_to(self: "Self") -> "_Cast_PersistentSingleton":
        """Cast to another type.

        Returns:
            _Cast_PersistentSingleton
        """
        return _Cast_PersistentSingleton(self)
