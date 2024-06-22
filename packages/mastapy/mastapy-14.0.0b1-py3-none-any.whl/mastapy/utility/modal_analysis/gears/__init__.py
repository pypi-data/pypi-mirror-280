"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.utility.modal_analysis.gears._1847 import GearMeshForTE
    from mastapy._private.utility.modal_analysis.gears._1848 import GearOrderForTE
    from mastapy._private.utility.modal_analysis.gears._1849 import GearPositions
    from mastapy._private.utility.modal_analysis.gears._1850 import HarmonicOrderForTE
    from mastapy._private.utility.modal_analysis.gears._1851 import LabelOnlyOrder
    from mastapy._private.utility.modal_analysis.gears._1852 import OrderForTE
    from mastapy._private.utility.modal_analysis.gears._1853 import OrderSelector
    from mastapy._private.utility.modal_analysis.gears._1854 import OrderWithRadius
    from mastapy._private.utility.modal_analysis.gears._1855 import RollingBearingOrder
    from mastapy._private.utility.modal_analysis.gears._1856 import ShaftOrderForTE
    from mastapy._private.utility.modal_analysis.gears._1857 import (
        UserDefinedOrderForTE,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.modal_analysis.gears._1847": ["GearMeshForTE"],
        "_private.utility.modal_analysis.gears._1848": ["GearOrderForTE"],
        "_private.utility.modal_analysis.gears._1849": ["GearPositions"],
        "_private.utility.modal_analysis.gears._1850": ["HarmonicOrderForTE"],
        "_private.utility.modal_analysis.gears._1851": ["LabelOnlyOrder"],
        "_private.utility.modal_analysis.gears._1852": ["OrderForTE"],
        "_private.utility.modal_analysis.gears._1853": ["OrderSelector"],
        "_private.utility.modal_analysis.gears._1854": ["OrderWithRadius"],
        "_private.utility.modal_analysis.gears._1855": ["RollingBearingOrder"],
        "_private.utility.modal_analysis.gears._1856": ["ShaftOrderForTE"],
        "_private.utility.modal_analysis.gears._1857": ["UserDefinedOrderForTE"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)
