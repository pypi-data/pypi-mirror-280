"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.fe_tools.vis_tools_global._1271 import ElementEdge
    from mastapy._private.fe_tools.vis_tools_global._1272 import ElementFace
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.fe_tools.vis_tools_global._1271": ["ElementEdge"],
        "_private.fe_tools.vis_tools_global._1272": ["ElementFace"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ElementEdge",
    "ElementFace",
)
