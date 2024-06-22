"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.cycloidal._1497 import ContactSpecification
    from mastapy._private.cycloidal._1498 import CrowningSpecificationMethod
    from mastapy._private.cycloidal._1499 import CycloidalAssemblyDesign
    from mastapy._private.cycloidal._1500 import CycloidalDiscDesign
    from mastapy._private.cycloidal._1501 import CycloidalDiscDesignExporter
    from mastapy._private.cycloidal._1502 import CycloidalDiscMaterial
    from mastapy._private.cycloidal._1503 import CycloidalDiscMaterialDatabase
    from mastapy._private.cycloidal._1504 import CycloidalDiscModificationsSpecification
    from mastapy._private.cycloidal._1505 import DirectionOfMeasuredModifications
    from mastapy._private.cycloidal._1506 import GeometryToExport
    from mastapy._private.cycloidal._1507 import NamedDiscPhase
    from mastapy._private.cycloidal._1508 import RingPinsDesign
    from mastapy._private.cycloidal._1509 import RingPinsMaterial
    from mastapy._private.cycloidal._1510 import RingPinsMaterialDatabase
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.cycloidal._1497": ["ContactSpecification"],
        "_private.cycloidal._1498": ["CrowningSpecificationMethod"],
        "_private.cycloidal._1499": ["CycloidalAssemblyDesign"],
        "_private.cycloidal._1500": ["CycloidalDiscDesign"],
        "_private.cycloidal._1501": ["CycloidalDiscDesignExporter"],
        "_private.cycloidal._1502": ["CycloidalDiscMaterial"],
        "_private.cycloidal._1503": ["CycloidalDiscMaterialDatabase"],
        "_private.cycloidal._1504": ["CycloidalDiscModificationsSpecification"],
        "_private.cycloidal._1505": ["DirectionOfMeasuredModifications"],
        "_private.cycloidal._1506": ["GeometryToExport"],
        "_private.cycloidal._1507": ["NamedDiscPhase"],
        "_private.cycloidal._1508": ["RingPinsDesign"],
        "_private.cycloidal._1509": ["RingPinsMaterial"],
        "_private.cycloidal._1510": ["RingPinsMaterialDatabase"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
