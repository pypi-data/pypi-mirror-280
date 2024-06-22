"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.manufacturing.bevel._795 import AbstractTCA
    from mastapy._private.gears.manufacturing.bevel._796 import (
        BevelMachineSettingOptimizationResult,
    )
    from mastapy._private.gears.manufacturing.bevel._797 import (
        ConicalFlankDeviationsData,
    )
    from mastapy._private.gears.manufacturing.bevel._798 import (
        ConicalGearManufacturingAnalysis,
    )
    from mastapy._private.gears.manufacturing.bevel._799 import (
        ConicalGearManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._800 import (
        ConicalGearMicroGeometryConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._801 import (
        ConicalGearMicroGeometryConfigBase,
    )
    from mastapy._private.gears.manufacturing.bevel._802 import (
        ConicalMeshedGearManufacturingAnalysis,
    )
    from mastapy._private.gears.manufacturing.bevel._803 import (
        ConicalMeshedWheelFlankManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._804 import (
        ConicalMeshFlankManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._805 import (
        ConicalMeshFlankMicroGeometryConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._806 import (
        ConicalMeshFlankNURBSMicroGeometryConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._807 import (
        ConicalMeshManufacturingAnalysis,
    )
    from mastapy._private.gears.manufacturing.bevel._808 import (
        ConicalMeshManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._809 import (
        ConicalMeshMicroGeometryConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._810 import (
        ConicalMeshMicroGeometryConfigBase,
    )
    from mastapy._private.gears.manufacturing.bevel._811 import (
        ConicalPinionManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._812 import (
        ConicalPinionMicroGeometryConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._813 import (
        ConicalSetManufacturingAnalysis,
    )
    from mastapy._private.gears.manufacturing.bevel._814 import (
        ConicalSetManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._815 import (
        ConicalSetMicroGeometryConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._816 import (
        ConicalSetMicroGeometryConfigBase,
    )
    from mastapy._private.gears.manufacturing.bevel._817 import (
        ConicalWheelManufacturingConfig,
    )
    from mastapy._private.gears.manufacturing.bevel._818 import EaseOffBasedTCA
    from mastapy._private.gears.manufacturing.bevel._819 import FlankMeasurementBorder
    from mastapy._private.gears.manufacturing.bevel._820 import HypoidAdvancedLibrary
    from mastapy._private.gears.manufacturing.bevel._821 import MachineTypes
    from mastapy._private.gears.manufacturing.bevel._822 import ManufacturingMachine
    from mastapy._private.gears.manufacturing.bevel._823 import (
        ManufacturingMachineDatabase,
    )
    from mastapy._private.gears.manufacturing.bevel._824 import (
        PinionBevelGeneratingModifiedRollMachineSettings,
    )
    from mastapy._private.gears.manufacturing.bevel._825 import (
        PinionBevelGeneratingTiltMachineSettings,
    )
    from mastapy._private.gears.manufacturing.bevel._826 import PinionConcave
    from mastapy._private.gears.manufacturing.bevel._827 import (
        PinionConicalMachineSettingsSpecified,
    )
    from mastapy._private.gears.manufacturing.bevel._828 import PinionConvex
    from mastapy._private.gears.manufacturing.bevel._829 import (
        PinionFinishMachineSettings,
    )
    from mastapy._private.gears.manufacturing.bevel._830 import (
        PinionHypoidFormateTiltMachineSettings,
    )
    from mastapy._private.gears.manufacturing.bevel._831 import (
        PinionHypoidGeneratingTiltMachineSettings,
    )
    from mastapy._private.gears.manufacturing.bevel._832 import PinionMachineSettingsSMT
    from mastapy._private.gears.manufacturing.bevel._833 import (
        PinionRoughMachineSetting,
    )
    from mastapy._private.gears.manufacturing.bevel._834 import Wheel
    from mastapy._private.gears.manufacturing.bevel._835 import WheelFormatMachineTypes
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.manufacturing.bevel._795": ["AbstractTCA"],
        "_private.gears.manufacturing.bevel._796": [
            "BevelMachineSettingOptimizationResult"
        ],
        "_private.gears.manufacturing.bevel._797": ["ConicalFlankDeviationsData"],
        "_private.gears.manufacturing.bevel._798": ["ConicalGearManufacturingAnalysis"],
        "_private.gears.manufacturing.bevel._799": ["ConicalGearManufacturingConfig"],
        "_private.gears.manufacturing.bevel._800": ["ConicalGearMicroGeometryConfig"],
        "_private.gears.manufacturing.bevel._801": [
            "ConicalGearMicroGeometryConfigBase"
        ],
        "_private.gears.manufacturing.bevel._802": [
            "ConicalMeshedGearManufacturingAnalysis"
        ],
        "_private.gears.manufacturing.bevel._803": [
            "ConicalMeshedWheelFlankManufacturingConfig"
        ],
        "_private.gears.manufacturing.bevel._804": [
            "ConicalMeshFlankManufacturingConfig"
        ],
        "_private.gears.manufacturing.bevel._805": [
            "ConicalMeshFlankMicroGeometryConfig"
        ],
        "_private.gears.manufacturing.bevel._806": [
            "ConicalMeshFlankNURBSMicroGeometryConfig"
        ],
        "_private.gears.manufacturing.bevel._807": ["ConicalMeshManufacturingAnalysis"],
        "_private.gears.manufacturing.bevel._808": ["ConicalMeshManufacturingConfig"],
        "_private.gears.manufacturing.bevel._809": ["ConicalMeshMicroGeometryConfig"],
        "_private.gears.manufacturing.bevel._810": [
            "ConicalMeshMicroGeometryConfigBase"
        ],
        "_private.gears.manufacturing.bevel._811": ["ConicalPinionManufacturingConfig"],
        "_private.gears.manufacturing.bevel._812": ["ConicalPinionMicroGeometryConfig"],
        "_private.gears.manufacturing.bevel._813": ["ConicalSetManufacturingAnalysis"],
        "_private.gears.manufacturing.bevel._814": ["ConicalSetManufacturingConfig"],
        "_private.gears.manufacturing.bevel._815": ["ConicalSetMicroGeometryConfig"],
        "_private.gears.manufacturing.bevel._816": [
            "ConicalSetMicroGeometryConfigBase"
        ],
        "_private.gears.manufacturing.bevel._817": ["ConicalWheelManufacturingConfig"],
        "_private.gears.manufacturing.bevel._818": ["EaseOffBasedTCA"],
        "_private.gears.manufacturing.bevel._819": ["FlankMeasurementBorder"],
        "_private.gears.manufacturing.bevel._820": ["HypoidAdvancedLibrary"],
        "_private.gears.manufacturing.bevel._821": ["MachineTypes"],
        "_private.gears.manufacturing.bevel._822": ["ManufacturingMachine"],
        "_private.gears.manufacturing.bevel._823": ["ManufacturingMachineDatabase"],
        "_private.gears.manufacturing.bevel._824": [
            "PinionBevelGeneratingModifiedRollMachineSettings"
        ],
        "_private.gears.manufacturing.bevel._825": [
            "PinionBevelGeneratingTiltMachineSettings"
        ],
        "_private.gears.manufacturing.bevel._826": ["PinionConcave"],
        "_private.gears.manufacturing.bevel._827": [
            "PinionConicalMachineSettingsSpecified"
        ],
        "_private.gears.manufacturing.bevel._828": ["PinionConvex"],
        "_private.gears.manufacturing.bevel._829": ["PinionFinishMachineSettings"],
        "_private.gears.manufacturing.bevel._830": [
            "PinionHypoidFormateTiltMachineSettings"
        ],
        "_private.gears.manufacturing.bevel._831": [
            "PinionHypoidGeneratingTiltMachineSettings"
        ],
        "_private.gears.manufacturing.bevel._832": ["PinionMachineSettingsSMT"],
        "_private.gears.manufacturing.bevel._833": ["PinionRoughMachineSetting"],
        "_private.gears.manufacturing.bevel._834": ["Wheel"],
        "_private.gears.manufacturing.bevel._835": ["WheelFormatMachineTypes"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractTCA",
    "BevelMachineSettingOptimizationResult",
    "ConicalFlankDeviationsData",
    "ConicalGearManufacturingAnalysis",
    "ConicalGearManufacturingConfig",
    "ConicalGearMicroGeometryConfig",
    "ConicalGearMicroGeometryConfigBase",
    "ConicalMeshedGearManufacturingAnalysis",
    "ConicalMeshedWheelFlankManufacturingConfig",
    "ConicalMeshFlankManufacturingConfig",
    "ConicalMeshFlankMicroGeometryConfig",
    "ConicalMeshFlankNURBSMicroGeometryConfig",
    "ConicalMeshManufacturingAnalysis",
    "ConicalMeshManufacturingConfig",
    "ConicalMeshMicroGeometryConfig",
    "ConicalMeshMicroGeometryConfigBase",
    "ConicalPinionManufacturingConfig",
    "ConicalPinionMicroGeometryConfig",
    "ConicalSetManufacturingAnalysis",
    "ConicalSetManufacturingConfig",
    "ConicalSetMicroGeometryConfig",
    "ConicalSetMicroGeometryConfigBase",
    "ConicalWheelManufacturingConfig",
    "EaseOffBasedTCA",
    "FlankMeasurementBorder",
    "HypoidAdvancedLibrary",
    "MachineTypes",
    "ManufacturingMachine",
    "ManufacturingMachineDatabase",
    "PinionBevelGeneratingModifiedRollMachineSettings",
    "PinionBevelGeneratingTiltMachineSettings",
    "PinionConcave",
    "PinionConicalMachineSettingsSpecified",
    "PinionConvex",
    "PinionFinishMachineSettings",
    "PinionHypoidFormateTiltMachineSettings",
    "PinionHypoidGeneratingTiltMachineSettings",
    "PinionMachineSettingsSMT",
    "PinionRoughMachineSetting",
    "Wheel",
    "WheelFormatMachineTypes",
)
