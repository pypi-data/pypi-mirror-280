"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.electric_machines.load_cases_and_analyses._1392 import (
        BasicDynamicForceLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1393 import (
        DynamicForceAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1394 import (
        DynamicForceLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1395 import (
        DynamicForcesOperatingPoint,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1396 import (
        EfficiencyMapAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1397 import (
        EfficiencyMapLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1398 import (
        ElectricMachineAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1399 import (
        ElectricMachineBasicMechanicalLossSettings,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1400 import (
        ElectricMachineControlStrategy,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1401 import (
        ElectricMachineEfficiencyMapSettings,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1402 import (
        ElectricMachineFEAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1403 import (
        ElectricMachineFEMechanicalAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1404 import (
        ElectricMachineLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1405 import (
        ElectricMachineLoadCaseBase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1406 import (
        ElectricMachineLoadCaseGroup,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1407 import (
        ElectricMachineMechanicalLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1408 import (
        EndWindingInductanceMethod,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1409 import (
        LeadingOrLagging,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1410 import (
        LoadCaseType,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1411 import (
        LoadCaseTypeSelector,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1412 import (
        MotoringOrGenerating,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1413 import (
        NonLinearDQModelMultipleOperatingPointsLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1414 import (
        NumberOfStepsPerOperatingPointSpecificationMethod,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1415 import (
        OperatingPointsSpecificationMethod,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1416 import (
        SingleOperatingPointAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1417 import (
        SlotDetailForAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1418 import (
        SpecifyTorqueOrCurrent,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1419 import (
        SpeedPointsDistribution,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1420 import (
        SpeedTorqueCurveAnalysis,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1421 import (
        SpeedTorqueCurveLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1422 import (
        SpeedTorqueLoadCase,
    )
    from mastapy._private.electric_machines.load_cases_and_analyses._1423 import (
        Temperatures,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.electric_machines.load_cases_and_analyses._1392": [
            "BasicDynamicForceLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1393": [
            "DynamicForceAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1394": [
            "DynamicForceLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1395": [
            "DynamicForcesOperatingPoint"
        ],
        "_private.electric_machines.load_cases_and_analyses._1396": [
            "EfficiencyMapAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1397": [
            "EfficiencyMapLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1398": [
            "ElectricMachineAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1399": [
            "ElectricMachineBasicMechanicalLossSettings"
        ],
        "_private.electric_machines.load_cases_and_analyses._1400": [
            "ElectricMachineControlStrategy"
        ],
        "_private.electric_machines.load_cases_and_analyses._1401": [
            "ElectricMachineEfficiencyMapSettings"
        ],
        "_private.electric_machines.load_cases_and_analyses._1402": [
            "ElectricMachineFEAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1403": [
            "ElectricMachineFEMechanicalAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1404": [
            "ElectricMachineLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1405": [
            "ElectricMachineLoadCaseBase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1406": [
            "ElectricMachineLoadCaseGroup"
        ],
        "_private.electric_machines.load_cases_and_analyses._1407": [
            "ElectricMachineMechanicalLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1408": [
            "EndWindingInductanceMethod"
        ],
        "_private.electric_machines.load_cases_and_analyses._1409": [
            "LeadingOrLagging"
        ],
        "_private.electric_machines.load_cases_and_analyses._1410": ["LoadCaseType"],
        "_private.electric_machines.load_cases_and_analyses._1411": [
            "LoadCaseTypeSelector"
        ],
        "_private.electric_machines.load_cases_and_analyses._1412": [
            "MotoringOrGenerating"
        ],
        "_private.electric_machines.load_cases_and_analyses._1413": [
            "NonLinearDQModelMultipleOperatingPointsLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1414": [
            "NumberOfStepsPerOperatingPointSpecificationMethod"
        ],
        "_private.electric_machines.load_cases_and_analyses._1415": [
            "OperatingPointsSpecificationMethod"
        ],
        "_private.electric_machines.load_cases_and_analyses._1416": [
            "SingleOperatingPointAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1417": [
            "SlotDetailForAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1418": [
            "SpecifyTorqueOrCurrent"
        ],
        "_private.electric_machines.load_cases_and_analyses._1419": [
            "SpeedPointsDistribution"
        ],
        "_private.electric_machines.load_cases_and_analyses._1420": [
            "SpeedTorqueCurveAnalysis"
        ],
        "_private.electric_machines.load_cases_and_analyses._1421": [
            "SpeedTorqueCurveLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1422": [
            "SpeedTorqueLoadCase"
        ],
        "_private.electric_machines.load_cases_and_analyses._1423": ["Temperatures"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
