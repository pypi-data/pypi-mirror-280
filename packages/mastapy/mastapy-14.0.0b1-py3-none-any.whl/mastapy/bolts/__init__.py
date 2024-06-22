"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.bolts._1511 import AxialLoadType
    from mastapy._private.bolts._1512 import BoltedJointMaterial
    from mastapy._private.bolts._1513 import BoltedJointMaterialDatabase
    from mastapy._private.bolts._1514 import BoltGeometry
    from mastapy._private.bolts._1515 import BoltGeometryDatabase
    from mastapy._private.bolts._1516 import BoltMaterial
    from mastapy._private.bolts._1517 import BoltMaterialDatabase
    from mastapy._private.bolts._1518 import BoltSection
    from mastapy._private.bolts._1519 import BoltShankType
    from mastapy._private.bolts._1520 import BoltTypes
    from mastapy._private.bolts._1521 import ClampedSection
    from mastapy._private.bolts._1522 import ClampedSectionMaterialDatabase
    from mastapy._private.bolts._1523 import DetailedBoltDesign
    from mastapy._private.bolts._1524 import DetailedBoltedJointDesign
    from mastapy._private.bolts._1525 import HeadCapTypes
    from mastapy._private.bolts._1526 import JointGeometries
    from mastapy._private.bolts._1527 import JointTypes
    from mastapy._private.bolts._1528 import LoadedBolt
    from mastapy._private.bolts._1529 import RolledBeforeOrAfterHeatTreatment
    from mastapy._private.bolts._1530 import StandardSizes
    from mastapy._private.bolts._1531 import StrengthGrades
    from mastapy._private.bolts._1532 import ThreadTypes
    from mastapy._private.bolts._1533 import TighteningTechniques
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bolts._1511": ["AxialLoadType"],
        "_private.bolts._1512": ["BoltedJointMaterial"],
        "_private.bolts._1513": ["BoltedJointMaterialDatabase"],
        "_private.bolts._1514": ["BoltGeometry"],
        "_private.bolts._1515": ["BoltGeometryDatabase"],
        "_private.bolts._1516": ["BoltMaterial"],
        "_private.bolts._1517": ["BoltMaterialDatabase"],
        "_private.bolts._1518": ["BoltSection"],
        "_private.bolts._1519": ["BoltShankType"],
        "_private.bolts._1520": ["BoltTypes"],
        "_private.bolts._1521": ["ClampedSection"],
        "_private.bolts._1522": ["ClampedSectionMaterialDatabase"],
        "_private.bolts._1523": ["DetailedBoltDesign"],
        "_private.bolts._1524": ["DetailedBoltedJointDesign"],
        "_private.bolts._1525": ["HeadCapTypes"],
        "_private.bolts._1526": ["JointGeometries"],
        "_private.bolts._1527": ["JointTypes"],
        "_private.bolts._1528": ["LoadedBolt"],
        "_private.bolts._1529": ["RolledBeforeOrAfterHeatTreatment"],
        "_private.bolts._1530": ["StandardSizes"],
        "_private.bolts._1531": ["StrengthGrades"],
        "_private.bolts._1532": ["ThreadTypes"],
        "_private.bolts._1533": ["TighteningTechniques"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
