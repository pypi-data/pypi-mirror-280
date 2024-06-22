"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.analysis._1253 import AbstractGearAnalysis
    from mastapy._private.gears.analysis._1254 import AbstractGearMeshAnalysis
    from mastapy._private.gears.analysis._1255 import AbstractGearSetAnalysis
    from mastapy._private.gears.analysis._1256 import GearDesignAnalysis
    from mastapy._private.gears.analysis._1257 import GearImplementationAnalysis
    from mastapy._private.gears.analysis._1258 import (
        GearImplementationAnalysisDutyCycle,
    )
    from mastapy._private.gears.analysis._1259 import GearImplementationDetail
    from mastapy._private.gears.analysis._1260 import GearMeshDesignAnalysis
    from mastapy._private.gears.analysis._1261 import GearMeshImplementationAnalysis
    from mastapy._private.gears.analysis._1262 import (
        GearMeshImplementationAnalysisDutyCycle,
    )
    from mastapy._private.gears.analysis._1263 import GearMeshImplementationDetail
    from mastapy._private.gears.analysis._1264 import GearSetDesignAnalysis
    from mastapy._private.gears.analysis._1265 import GearSetGroupDutyCycle
    from mastapy._private.gears.analysis._1266 import GearSetImplementationAnalysis
    from mastapy._private.gears.analysis._1267 import (
        GearSetImplementationAnalysisAbstract,
    )
    from mastapy._private.gears.analysis._1268 import (
        GearSetImplementationAnalysisDutyCycle,
    )
    from mastapy._private.gears.analysis._1269 import GearSetImplementationDetail
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.analysis._1253": ["AbstractGearAnalysis"],
        "_private.gears.analysis._1254": ["AbstractGearMeshAnalysis"],
        "_private.gears.analysis._1255": ["AbstractGearSetAnalysis"],
        "_private.gears.analysis._1256": ["GearDesignAnalysis"],
        "_private.gears.analysis._1257": ["GearImplementationAnalysis"],
        "_private.gears.analysis._1258": ["GearImplementationAnalysisDutyCycle"],
        "_private.gears.analysis._1259": ["GearImplementationDetail"],
        "_private.gears.analysis._1260": ["GearMeshDesignAnalysis"],
        "_private.gears.analysis._1261": ["GearMeshImplementationAnalysis"],
        "_private.gears.analysis._1262": ["GearMeshImplementationAnalysisDutyCycle"],
        "_private.gears.analysis._1263": ["GearMeshImplementationDetail"],
        "_private.gears.analysis._1264": ["GearSetDesignAnalysis"],
        "_private.gears.analysis._1265": ["GearSetGroupDutyCycle"],
        "_private.gears.analysis._1266": ["GearSetImplementationAnalysis"],
        "_private.gears.analysis._1267": ["GearSetImplementationAnalysisAbstract"],
        "_private.gears.analysis._1268": ["GearSetImplementationAnalysisDutyCycle"],
        "_private.gears.analysis._1269": ["GearSetImplementationDetail"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)
