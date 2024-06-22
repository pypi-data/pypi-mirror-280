"""PerMachineSettings"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.utility import _1642
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PER_MACHINE_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "PerMachineSettings")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.nodal_analysis import _68
    from mastapy._private.nodal_analysis.geometry_modeller_link import _167
    from mastapy._private.gears.materials import _610
    from mastapy._private.gears.ltca.cylindrical import _878
    from mastapy._private.gears.gear_designs.cylindrical import _1041
    from mastapy._private.utility import _1643, _1644
    from mastapy._private.utility.units_and_measurements import _1653
    from mastapy._private.utility.scripting import _1787
    from mastapy._private.utility.databases import _1877
    from mastapy._private.utility.cad_export import _1882
    from mastapy._private.bearings import _1951
    from mastapy._private.system_model.part_model import _2526

    Self = TypeVar("Self", bound="PerMachineSettings")
    CastSelf = TypeVar("CastSelf", bound="PerMachineSettings._Cast_PerMachineSettings")


__docformat__ = "restructuredtext en"
__all__ = ("PerMachineSettings",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PerMachineSettings:
    """Special nested class for casting PerMachineSettings to subclasses."""

    __parent__: "PerMachineSettings"

    @property
    def persistent_singleton(self: "CastSelf") -> "_1642.PersistentSingleton":
        return self.__parent__._cast(_1642.PersistentSingleton)

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
    def per_machine_settings(self: "CastSelf") -> "PerMachineSettings":
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
class PerMachineSettings(_1642.PersistentSingleton):
    """PerMachineSettings

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PER_MACHINE_SETTINGS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    def reset_to_defaults(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ResetToDefaults()

    @property
    def cast_to(self: "Self") -> "_Cast_PerMachineSettings":
        """Cast to another type.

        Returns:
            _Cast_PerMachineSettings
        """
        return _Cast_PerMachineSettings(self)
