"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7137 import (
        AdditionalForcesObtainedFrom,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7138 import (
        BoostPressureLoadCaseInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7139 import (
        DesignStateOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7140 import (
        DestinationDesignState,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7141 import (
        ForceInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7142 import (
        GearRatioInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7143 import (
        LoadCaseNameOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7144 import (
        MomentInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7145 import (
        MultiTimeSeriesDataInputFileOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7146 import (
        PointLoadInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7147 import (
        PowerLoadInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7148 import (
        RampOrSteadyStateInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7149 import (
        SpeedInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7150 import (
        TimeSeriesImporter,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7151 import (
        TimeStepInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7152 import (
        TorqueInputOptions,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7153 import (
        TorqueValuesObtainedFrom,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7137": [
            "AdditionalForcesObtainedFrom"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7138": [
            "BoostPressureLoadCaseInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7139": [
            "DesignStateOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7140": [
            "DestinationDesignState"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7141": [
            "ForceInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7142": [
            "GearRatioInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7143": [
            "LoadCaseNameOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7144": [
            "MomentInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7145": [
            "MultiTimeSeriesDataInputFileOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7146": [
            "PointLoadInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7147": [
            "PowerLoadInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7148": [
            "RampOrSteadyStateInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7149": [
            "SpeedInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7150": [
            "TimeSeriesImporter"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7151": [
            "TimeStepInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7152": [
            "TorqueInputOptions"
        ],
        "_private.system_model.analyses_and_results.static_loads.duty_cycle_definition._7153": [
            "TorqueValuesObtainedFrom"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)
