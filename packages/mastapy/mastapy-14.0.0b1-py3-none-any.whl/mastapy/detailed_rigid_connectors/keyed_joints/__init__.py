"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.detailed_rigid_connectors.keyed_joints._1483 import (
        KeyedJointDesign,
    )
    from mastapy._private.detailed_rigid_connectors.keyed_joints._1484 import KeyTypes
    from mastapy._private.detailed_rigid_connectors.keyed_joints._1485 import (
        KeywayJointHalfDesign,
    )
    from mastapy._private.detailed_rigid_connectors.keyed_joints._1486 import (
        NumberOfKeys,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.detailed_rigid_connectors.keyed_joints._1483": ["KeyedJointDesign"],
        "_private.detailed_rigid_connectors.keyed_joints._1484": ["KeyTypes"],
        "_private.detailed_rigid_connectors.keyed_joints._1485": [
            "KeywayJointHalfDesign"
        ],
        "_private.detailed_rigid_connectors.keyed_joints._1486": ["NumberOfKeys"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)
