"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.electric_machines.harmonic_load_data._1424 import (
        ElectricMachineHarmonicLoadDataBase,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1425 import (
        ForceDisplayOption,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1426 import (
        HarmonicLoadDataBase,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1427 import (
        HarmonicLoadDataControlExcitationOptionBase,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1428 import (
        HarmonicLoadDataType,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1429 import (
        SpeedDependentHarmonicLoadData,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1430 import (
        StatorToothInterpolator,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1431 import (
        StatorToothLoadInterpolator,
    )
    from mastapy._private.electric_machines.harmonic_load_data._1432 import (
        StatorToothMomentInterpolator,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.electric_machines.harmonic_load_data._1424": [
            "ElectricMachineHarmonicLoadDataBase"
        ],
        "_private.electric_machines.harmonic_load_data._1425": ["ForceDisplayOption"],
        "_private.electric_machines.harmonic_load_data._1426": ["HarmonicLoadDataBase"],
        "_private.electric_machines.harmonic_load_data._1427": [
            "HarmonicLoadDataControlExcitationOptionBase"
        ],
        "_private.electric_machines.harmonic_load_data._1428": ["HarmonicLoadDataType"],
        "_private.electric_machines.harmonic_load_data._1429": [
            "SpeedDependentHarmonicLoadData"
        ],
        "_private.electric_machines.harmonic_load_data._1430": [
            "StatorToothInterpolator"
        ],
        "_private.electric_machines.harmonic_load_data._1431": [
            "StatorToothLoadInterpolator"
        ],
        "_private.electric_machines.harmonic_load_data._1432": [
            "StatorToothMomentInterpolator"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
