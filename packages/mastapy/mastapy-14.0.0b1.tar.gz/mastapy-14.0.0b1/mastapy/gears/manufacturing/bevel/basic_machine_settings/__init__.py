"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.manufacturing.bevel.basic_machine_settings._844 import (
        BasicConicalGearMachineSettings,
    )
    from mastapy._private.gears.manufacturing.bevel.basic_machine_settings._845 import (
        BasicConicalGearMachineSettingsFormate,
    )
    from mastapy._private.gears.manufacturing.bevel.basic_machine_settings._846 import (
        BasicConicalGearMachineSettingsGenerated,
    )
    from mastapy._private.gears.manufacturing.bevel.basic_machine_settings._847 import (
        CradleStyleConicalMachineSettingsGenerated,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.manufacturing.bevel.basic_machine_settings._844": [
            "BasicConicalGearMachineSettings"
        ],
        "_private.gears.manufacturing.bevel.basic_machine_settings._845": [
            "BasicConicalGearMachineSettingsFormate"
        ],
        "_private.gears.manufacturing.bevel.basic_machine_settings._846": [
            "BasicConicalGearMachineSettingsGenerated"
        ],
        "_private.gears.manufacturing.bevel.basic_machine_settings._847": [
            "CradleStyleConicalMachineSettingsGenerated"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BasicConicalGearMachineSettings",
    "BasicConicalGearMachineSettingsFormate",
    "BasicConicalGearMachineSettingsGenerated",
    "CradleStyleConicalMachineSettingsGenerated",
)
