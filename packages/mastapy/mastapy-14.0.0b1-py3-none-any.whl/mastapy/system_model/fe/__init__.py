"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.fe._2408 import AlignConnectedComponentOptions
    from mastapy._private.system_model.fe._2409 import AlignmentMethod
    from mastapy._private.system_model.fe._2410 import AlignmentMethodForRaceBearing
    from mastapy._private.system_model.fe._2411 import AlignmentUsingAxialNodePositions
    from mastapy._private.system_model.fe._2412 import AngleSource
    from mastapy._private.system_model.fe._2413 import BaseFEWithSelection
    from mastapy._private.system_model.fe._2414 import BatchOperations
    from mastapy._private.system_model.fe._2415 import BearingNodeAlignmentOption
    from mastapy._private.system_model.fe._2416 import BearingNodeOption
    from mastapy._private.system_model.fe._2417 import BearingRaceNodeLink
    from mastapy._private.system_model.fe._2418 import BearingRacePosition
    from mastapy._private.system_model.fe._2419 import ComponentOrientationOption
    from mastapy._private.system_model.fe._2420 import ContactPairWithSelection
    from mastapy._private.system_model.fe._2421 import CoordinateSystemWithSelection
    from mastapy._private.system_model.fe._2422 import CreateConnectedComponentOptions
    from mastapy._private.system_model.fe._2423 import (
        CreateMicrophoneNormalToSurfaceOptions,
    )
    from mastapy._private.system_model.fe._2424 import DegreeOfFreedomBoundaryCondition
    from mastapy._private.system_model.fe._2425 import (
        DegreeOfFreedomBoundaryConditionAngular,
    )
    from mastapy._private.system_model.fe._2426 import (
        DegreeOfFreedomBoundaryConditionLinear,
    )
    from mastapy._private.system_model.fe._2427 import ElectricMachineDataSet
    from mastapy._private.system_model.fe._2428 import ElectricMachineDynamicLoadData
    from mastapy._private.system_model.fe._2429 import ElementFaceGroupWithSelection
    from mastapy._private.system_model.fe._2430 import ElementPropertiesWithSelection
    from mastapy._private.system_model.fe._2431 import FEEntityGroupWithSelection
    from mastapy._private.system_model.fe._2432 import FEExportSettings
    from mastapy._private.system_model.fe._2433 import FEPartDRIVASurfaceSelection
    from mastapy._private.system_model.fe._2434 import FEPartWithBatchOptions
    from mastapy._private.system_model.fe._2435 import FEStiffnessGeometry
    from mastapy._private.system_model.fe._2436 import FEStiffnessTester
    from mastapy._private.system_model.fe._2437 import FESubstructure
    from mastapy._private.system_model.fe._2438 import FESubstructureExportOptions
    from mastapy._private.system_model.fe._2439 import FESubstructureNode
    from mastapy._private.system_model.fe._2440 import FESubstructureNodeModeShape
    from mastapy._private.system_model.fe._2441 import FESubstructureNodeModeShapes
    from mastapy._private.system_model.fe._2442 import FESubstructureType
    from mastapy._private.system_model.fe._2443 import FESubstructureWithBatchOptions
    from mastapy._private.system_model.fe._2444 import FESubstructureWithSelection
    from mastapy._private.system_model.fe._2445 import (
        FESubstructureWithSelectionComponents,
    )
    from mastapy._private.system_model.fe._2446 import (
        FESubstructureWithSelectionForHarmonicAnalysis,
    )
    from mastapy._private.system_model.fe._2447 import (
        FESubstructureWithSelectionForModalAnalysis,
    )
    from mastapy._private.system_model.fe._2448 import (
        FESubstructureWithSelectionForStaticAnalysis,
    )
    from mastapy._private.system_model.fe._2449 import GearMeshingOptions
    from mastapy._private.system_model.fe._2450 import (
        IndependentMASTACreatedCondensationNode,
    )
    from mastapy._private.system_model.fe._2451 import (
        LinkComponentAxialPositionErrorReporter,
    )
    from mastapy._private.system_model.fe._2452 import LinkNodeSource
    from mastapy._private.system_model.fe._2453 import MaterialPropertiesWithSelection
    from mastapy._private.system_model.fe._2454 import (
        NodeBoundaryConditionStaticAnalysis,
    )
    from mastapy._private.system_model.fe._2455 import NodeGroupWithSelection
    from mastapy._private.system_model.fe._2456 import NodeSelectionDepthOption
    from mastapy._private.system_model.fe._2457 import (
        OptionsWhenExternalFEFileAlreadyExists,
    )
    from mastapy._private.system_model.fe._2458 import PerLinkExportOptions
    from mastapy._private.system_model.fe._2459 import PerNodeExportOptions
    from mastapy._private.system_model.fe._2460 import RaceBearingFE
    from mastapy._private.system_model.fe._2461 import RaceBearingFESystemDeflection
    from mastapy._private.system_model.fe._2462 import RaceBearingFEWithSelection
    from mastapy._private.system_model.fe._2463 import ReplacedShaftSelectionHelper
    from mastapy._private.system_model.fe._2464 import SystemDeflectionFEExportOptions
    from mastapy._private.system_model.fe._2465 import ThermalExpansionOption
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.fe._2408": ["AlignConnectedComponentOptions"],
        "_private.system_model.fe._2409": ["AlignmentMethod"],
        "_private.system_model.fe._2410": ["AlignmentMethodForRaceBearing"],
        "_private.system_model.fe._2411": ["AlignmentUsingAxialNodePositions"],
        "_private.system_model.fe._2412": ["AngleSource"],
        "_private.system_model.fe._2413": ["BaseFEWithSelection"],
        "_private.system_model.fe._2414": ["BatchOperations"],
        "_private.system_model.fe._2415": ["BearingNodeAlignmentOption"],
        "_private.system_model.fe._2416": ["BearingNodeOption"],
        "_private.system_model.fe._2417": ["BearingRaceNodeLink"],
        "_private.system_model.fe._2418": ["BearingRacePosition"],
        "_private.system_model.fe._2419": ["ComponentOrientationOption"],
        "_private.system_model.fe._2420": ["ContactPairWithSelection"],
        "_private.system_model.fe._2421": ["CoordinateSystemWithSelection"],
        "_private.system_model.fe._2422": ["CreateConnectedComponentOptions"],
        "_private.system_model.fe._2423": ["CreateMicrophoneNormalToSurfaceOptions"],
        "_private.system_model.fe._2424": ["DegreeOfFreedomBoundaryCondition"],
        "_private.system_model.fe._2425": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_private.system_model.fe._2426": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_private.system_model.fe._2427": ["ElectricMachineDataSet"],
        "_private.system_model.fe._2428": ["ElectricMachineDynamicLoadData"],
        "_private.system_model.fe._2429": ["ElementFaceGroupWithSelection"],
        "_private.system_model.fe._2430": ["ElementPropertiesWithSelection"],
        "_private.system_model.fe._2431": ["FEEntityGroupWithSelection"],
        "_private.system_model.fe._2432": ["FEExportSettings"],
        "_private.system_model.fe._2433": ["FEPartDRIVASurfaceSelection"],
        "_private.system_model.fe._2434": ["FEPartWithBatchOptions"],
        "_private.system_model.fe._2435": ["FEStiffnessGeometry"],
        "_private.system_model.fe._2436": ["FEStiffnessTester"],
        "_private.system_model.fe._2437": ["FESubstructure"],
        "_private.system_model.fe._2438": ["FESubstructureExportOptions"],
        "_private.system_model.fe._2439": ["FESubstructureNode"],
        "_private.system_model.fe._2440": ["FESubstructureNodeModeShape"],
        "_private.system_model.fe._2441": ["FESubstructureNodeModeShapes"],
        "_private.system_model.fe._2442": ["FESubstructureType"],
        "_private.system_model.fe._2443": ["FESubstructureWithBatchOptions"],
        "_private.system_model.fe._2444": ["FESubstructureWithSelection"],
        "_private.system_model.fe._2445": ["FESubstructureWithSelectionComponents"],
        "_private.system_model.fe._2446": [
            "FESubstructureWithSelectionForHarmonicAnalysis"
        ],
        "_private.system_model.fe._2447": [
            "FESubstructureWithSelectionForModalAnalysis"
        ],
        "_private.system_model.fe._2448": [
            "FESubstructureWithSelectionForStaticAnalysis"
        ],
        "_private.system_model.fe._2449": ["GearMeshingOptions"],
        "_private.system_model.fe._2450": ["IndependentMASTACreatedCondensationNode"],
        "_private.system_model.fe._2451": ["LinkComponentAxialPositionErrorReporter"],
        "_private.system_model.fe._2452": ["LinkNodeSource"],
        "_private.system_model.fe._2453": ["MaterialPropertiesWithSelection"],
        "_private.system_model.fe._2454": ["NodeBoundaryConditionStaticAnalysis"],
        "_private.system_model.fe._2455": ["NodeGroupWithSelection"],
        "_private.system_model.fe._2456": ["NodeSelectionDepthOption"],
        "_private.system_model.fe._2457": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_private.system_model.fe._2458": ["PerLinkExportOptions"],
        "_private.system_model.fe._2459": ["PerNodeExportOptions"],
        "_private.system_model.fe._2460": ["RaceBearingFE"],
        "_private.system_model.fe._2461": ["RaceBearingFESystemDeflection"],
        "_private.system_model.fe._2462": ["RaceBearingFEWithSelection"],
        "_private.system_model.fe._2463": ["ReplacedShaftSelectionHelper"],
        "_private.system_model.fe._2464": ["SystemDeflectionFEExportOptions"],
        "_private.system_model.fe._2465": ["ThermalExpansionOption"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "CreateMicrophoneNormalToSurfaceOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
