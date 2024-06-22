"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.electric_machines._1282 import AbstractStator
    from mastapy._private.electric_machines._1283 import AbstractToothAndSlot
    from mastapy._private.electric_machines._1284 import CADConductor
    from mastapy._private.electric_machines._1285 import CADElectricMachineDetail
    from mastapy._private.electric_machines._1286 import CADFieldWindingSpecification
    from mastapy._private.electric_machines._1287 import CADMagnetDetails
    from mastapy._private.electric_machines._1288 import CADMagnetsForLayer
    from mastapy._private.electric_machines._1289 import CADRotor
    from mastapy._private.electric_machines._1290 import CADStator
    from mastapy._private.electric_machines._1291 import CADToothAndSlot
    from mastapy._private.electric_machines._1292 import CADWoundFieldSynchronousRotor
    from mastapy._private.electric_machines._1293 import Coil
    from mastapy._private.electric_machines._1294 import CoilPositionInSlot
    from mastapy._private.electric_machines._1295 import CoolingDuctLayerSpecification
    from mastapy._private.electric_machines._1296 import CoolingDuctShape
    from mastapy._private.electric_machines._1297 import (
        CoreLossBuildFactorSpecificationMethod,
    )
    from mastapy._private.electric_machines._1298 import CoreLossCoefficients
    from mastapy._private.electric_machines._1299 import DoubleLayerWindingSlotPositions
    from mastapy._private.electric_machines._1300 import DQAxisConvention
    from mastapy._private.electric_machines._1301 import Eccentricity
    from mastapy._private.electric_machines._1302 import ElectricMachineDetail
    from mastapy._private.electric_machines._1303 import (
        ElectricMachineDetailInitialInformation,
    )
    from mastapy._private.electric_machines._1304 import ElectricMachineGroup
    from mastapy._private.electric_machines._1305 import (
        ElectricMachineMechanicalAnalysisMeshingOptions,
    )
    from mastapy._private.electric_machines._1306 import ElectricMachineMeshingOptions
    from mastapy._private.electric_machines._1307 import (
        ElectricMachineMeshingOptionsBase,
    )
    from mastapy._private.electric_machines._1308 import ElectricMachineSetup
    from mastapy._private.electric_machines._1309 import ElectricMachineType
    from mastapy._private.electric_machines._1310 import FieldWindingSpecification
    from mastapy._private.electric_machines._1311 import FieldWindingSpecificationBase
    from mastapy._private.electric_machines._1312 import FillFactorSpecificationMethod
    from mastapy._private.electric_machines._1313 import FluxBarriers
    from mastapy._private.electric_machines._1314 import FluxBarrierOrWeb
    from mastapy._private.electric_machines._1315 import FluxBarrierStyle
    from mastapy._private.electric_machines._1316 import HairpinConductor
    from mastapy._private.electric_machines._1317 import (
        HarmonicLoadDataControlExcitationOptionForElectricMachineMode,
    )
    from mastapy._private.electric_machines._1318 import (
        IndividualConductorSpecificationSource,
    )
    from mastapy._private.electric_machines._1319 import (
        InteriorPermanentMagnetAndSynchronousReluctanceRotor,
    )
    from mastapy._private.electric_machines._1320 import InteriorPermanentMagnetMachine
    from mastapy._private.electric_machines._1321 import (
        IronLossCoefficientSpecificationMethod,
    )
    from mastapy._private.electric_machines._1322 import MagnetClearance
    from mastapy._private.electric_machines._1323 import MagnetConfiguration
    from mastapy._private.electric_machines._1324 import MagnetData
    from mastapy._private.electric_machines._1325 import MagnetDesign
    from mastapy._private.electric_machines._1326 import MagnetForLayer
    from mastapy._private.electric_machines._1327 import MagnetisationDirection
    from mastapy._private.electric_machines._1328 import MagnetMaterial
    from mastapy._private.electric_machines._1329 import MagnetMaterialDatabase
    from mastapy._private.electric_machines._1330 import MotorRotorSideFaceDetail
    from mastapy._private.electric_machines._1331 import NonCADElectricMachineDetail
    from mastapy._private.electric_machines._1332 import NotchShape
    from mastapy._private.electric_machines._1333 import NotchSpecification
    from mastapy._private.electric_machines._1334 import (
        PermanentMagnetAssistedSynchronousReluctanceMachine,
    )
    from mastapy._private.electric_machines._1335 import PermanentMagnetRotor
    from mastapy._private.electric_machines._1336 import Phase
    from mastapy._private.electric_machines._1337 import RegionID
    from mastapy._private.electric_machines._1338 import Rotor
    from mastapy._private.electric_machines._1339 import RotorInternalLayerSpecification
    from mastapy._private.electric_machines._1340 import RotorSkewSlice
    from mastapy._private.electric_machines._1341 import RotorType
    from mastapy._private.electric_machines._1342 import SingleOrDoubleLayerWindings
    from mastapy._private.electric_machines._1343 import SlotSectionDetail
    from mastapy._private.electric_machines._1344 import Stator
    from mastapy._private.electric_machines._1345 import StatorCutoutSpecification
    from mastapy._private.electric_machines._1346 import StatorRotorMaterial
    from mastapy._private.electric_machines._1347 import StatorRotorMaterialDatabase
    from mastapy._private.electric_machines._1348 import SurfacePermanentMagnetMachine
    from mastapy._private.electric_machines._1349 import SurfacePermanentMagnetRotor
    from mastapy._private.electric_machines._1350 import SynchronousReluctanceMachine
    from mastapy._private.electric_machines._1351 import ToothAndSlot
    from mastapy._private.electric_machines._1352 import ToothSlotStyle
    from mastapy._private.electric_machines._1353 import ToothTaperSpecification
    from mastapy._private.electric_machines._1354 import (
        TwoDimensionalFEModelForAnalysis,
    )
    from mastapy._private.electric_machines._1355 import UShapedLayerSpecification
    from mastapy._private.electric_machines._1356 import VShapedMagnetLayerSpecification
    from mastapy._private.electric_machines._1357 import WindingConductor
    from mastapy._private.electric_machines._1358 import WindingConnection
    from mastapy._private.electric_machines._1359 import WindingMaterial
    from mastapy._private.electric_machines._1360 import WindingMaterialDatabase
    from mastapy._private.electric_machines._1361 import Windings
    from mastapy._private.electric_machines._1362 import WindingsViewer
    from mastapy._private.electric_machines._1363 import WindingType
    from mastapy._private.electric_machines._1364 import WireSizeSpecificationMethod
    from mastapy._private.electric_machines._1365 import WoundFieldSynchronousMachine
    from mastapy._private.electric_machines._1366 import WoundFieldSynchronousRotor
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.electric_machines._1282": ["AbstractStator"],
        "_private.electric_machines._1283": ["AbstractToothAndSlot"],
        "_private.electric_machines._1284": ["CADConductor"],
        "_private.electric_machines._1285": ["CADElectricMachineDetail"],
        "_private.electric_machines._1286": ["CADFieldWindingSpecification"],
        "_private.electric_machines._1287": ["CADMagnetDetails"],
        "_private.electric_machines._1288": ["CADMagnetsForLayer"],
        "_private.electric_machines._1289": ["CADRotor"],
        "_private.electric_machines._1290": ["CADStator"],
        "_private.electric_machines._1291": ["CADToothAndSlot"],
        "_private.electric_machines._1292": ["CADWoundFieldSynchronousRotor"],
        "_private.electric_machines._1293": ["Coil"],
        "_private.electric_machines._1294": ["CoilPositionInSlot"],
        "_private.electric_machines._1295": ["CoolingDuctLayerSpecification"],
        "_private.electric_machines._1296": ["CoolingDuctShape"],
        "_private.electric_machines._1297": ["CoreLossBuildFactorSpecificationMethod"],
        "_private.electric_machines._1298": ["CoreLossCoefficients"],
        "_private.electric_machines._1299": ["DoubleLayerWindingSlotPositions"],
        "_private.electric_machines._1300": ["DQAxisConvention"],
        "_private.electric_machines._1301": ["Eccentricity"],
        "_private.electric_machines._1302": ["ElectricMachineDetail"],
        "_private.electric_machines._1303": ["ElectricMachineDetailInitialInformation"],
        "_private.electric_machines._1304": ["ElectricMachineGroup"],
        "_private.electric_machines._1305": [
            "ElectricMachineMechanicalAnalysisMeshingOptions"
        ],
        "_private.electric_machines._1306": ["ElectricMachineMeshingOptions"],
        "_private.electric_machines._1307": ["ElectricMachineMeshingOptionsBase"],
        "_private.electric_machines._1308": ["ElectricMachineSetup"],
        "_private.electric_machines._1309": ["ElectricMachineType"],
        "_private.electric_machines._1310": ["FieldWindingSpecification"],
        "_private.electric_machines._1311": ["FieldWindingSpecificationBase"],
        "_private.electric_machines._1312": ["FillFactorSpecificationMethod"],
        "_private.electric_machines._1313": ["FluxBarriers"],
        "_private.electric_machines._1314": ["FluxBarrierOrWeb"],
        "_private.electric_machines._1315": ["FluxBarrierStyle"],
        "_private.electric_machines._1316": ["HairpinConductor"],
        "_private.electric_machines._1317": [
            "HarmonicLoadDataControlExcitationOptionForElectricMachineMode"
        ],
        "_private.electric_machines._1318": ["IndividualConductorSpecificationSource"],
        "_private.electric_machines._1319": [
            "InteriorPermanentMagnetAndSynchronousReluctanceRotor"
        ],
        "_private.electric_machines._1320": ["InteriorPermanentMagnetMachine"],
        "_private.electric_machines._1321": ["IronLossCoefficientSpecificationMethod"],
        "_private.electric_machines._1322": ["MagnetClearance"],
        "_private.electric_machines._1323": ["MagnetConfiguration"],
        "_private.electric_machines._1324": ["MagnetData"],
        "_private.electric_machines._1325": ["MagnetDesign"],
        "_private.electric_machines._1326": ["MagnetForLayer"],
        "_private.electric_machines._1327": ["MagnetisationDirection"],
        "_private.electric_machines._1328": ["MagnetMaterial"],
        "_private.electric_machines._1329": ["MagnetMaterialDatabase"],
        "_private.electric_machines._1330": ["MotorRotorSideFaceDetail"],
        "_private.electric_machines._1331": ["NonCADElectricMachineDetail"],
        "_private.electric_machines._1332": ["NotchShape"],
        "_private.electric_machines._1333": ["NotchSpecification"],
        "_private.electric_machines._1334": [
            "PermanentMagnetAssistedSynchronousReluctanceMachine"
        ],
        "_private.electric_machines._1335": ["PermanentMagnetRotor"],
        "_private.electric_machines._1336": ["Phase"],
        "_private.electric_machines._1337": ["RegionID"],
        "_private.electric_machines._1338": ["Rotor"],
        "_private.electric_machines._1339": ["RotorInternalLayerSpecification"],
        "_private.electric_machines._1340": ["RotorSkewSlice"],
        "_private.electric_machines._1341": ["RotorType"],
        "_private.electric_machines._1342": ["SingleOrDoubleLayerWindings"],
        "_private.electric_machines._1343": ["SlotSectionDetail"],
        "_private.electric_machines._1344": ["Stator"],
        "_private.electric_machines._1345": ["StatorCutoutSpecification"],
        "_private.electric_machines._1346": ["StatorRotorMaterial"],
        "_private.electric_machines._1347": ["StatorRotorMaterialDatabase"],
        "_private.electric_machines._1348": ["SurfacePermanentMagnetMachine"],
        "_private.electric_machines._1349": ["SurfacePermanentMagnetRotor"],
        "_private.electric_machines._1350": ["SynchronousReluctanceMachine"],
        "_private.electric_machines._1351": ["ToothAndSlot"],
        "_private.electric_machines._1352": ["ToothSlotStyle"],
        "_private.electric_machines._1353": ["ToothTaperSpecification"],
        "_private.electric_machines._1354": ["TwoDimensionalFEModelForAnalysis"],
        "_private.electric_machines._1355": ["UShapedLayerSpecification"],
        "_private.electric_machines._1356": ["VShapedMagnetLayerSpecification"],
        "_private.electric_machines._1357": ["WindingConductor"],
        "_private.electric_machines._1358": ["WindingConnection"],
        "_private.electric_machines._1359": ["WindingMaterial"],
        "_private.electric_machines._1360": ["WindingMaterialDatabase"],
        "_private.electric_machines._1361": ["Windings"],
        "_private.electric_machines._1362": ["WindingsViewer"],
        "_private.electric_machines._1363": ["WindingType"],
        "_private.electric_machines._1364": ["WireSizeSpecificationMethod"],
        "_private.electric_machines._1365": ["WoundFieldSynchronousMachine"],
        "_private.electric_machines._1366": ["WoundFieldSynchronousRotor"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADFieldWindingSpecification",
    "CADMagnetDetails",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "CADWoundFieldSynchronousRotor",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineGroup",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FieldWindingSpecification",
    "FieldWindingSpecificationBase",
    "FillFactorSpecificationMethod",
    "FluxBarriers",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetData",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetisationDirection",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutoutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
    "WoundFieldSynchronousRotor",
)
