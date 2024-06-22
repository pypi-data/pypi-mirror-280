"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model.acoustics._2681 import (
        AcousticAnalysisOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2682 import (
        AcousticAnalysisSetup,
    )
    from mastapy._private.system_model.part_model.acoustics._2683 import (
        AcousticAnalysisSetupCacheReporting,
    )
    from mastapy._private.system_model.part_model.acoustics._2684 import (
        AcousticAnalysisSetupCollection,
    )
    from mastapy._private.system_model.part_model.acoustics._2685 import (
        AcousticEnvelopeType,
    )
    from mastapy._private.system_model.part_model.acoustics._2686 import (
        AcousticInputSurfaceOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2687 import (
        FEPartInputSurfaceOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2688 import (
        FESurfaceSelectionForAcousticEnvelope,
    )
    from mastapy._private.system_model.part_model.acoustics._2689 import HoleInFaceGroup
    from mastapy._private.system_model.part_model.acoustics._2690 import (
        MeshedResultPlane,
    )
    from mastapy._private.system_model.part_model.acoustics._2691 import (
        MeshedResultSphere,
    )
    from mastapy._private.system_model.part_model.acoustics._2692 import (
        MeshedResultSurface,
    )
    from mastapy._private.system_model.part_model.acoustics._2693 import (
        MeshedResultSurfaceBase,
    )
    from mastapy._private.system_model.part_model.acoustics._2694 import (
        MicrophoneArrayDesign,
    )
    from mastapy._private.system_model.part_model.acoustics._2695 import (
        PartSelectionForAcousticEnvelope,
    )
    from mastapy._private.system_model.part_model.acoustics._2696 import (
        ResultPlaneOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2697 import (
        ResultSphereOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2698 import (
        ResultSurfaceCollection,
    )
    from mastapy._private.system_model.part_model.acoustics._2699 import (
        ResultSurfaceOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2700 import (
        SphericalEnvelopeCentreDefinition,
    )
    from mastapy._private.system_model.part_model.acoustics._2701 import (
        SphericalEnvelopeType,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.acoustics._2681": ["AcousticAnalysisOptions"],
        "_private.system_model.part_model.acoustics._2682": ["AcousticAnalysisSetup"],
        "_private.system_model.part_model.acoustics._2683": [
            "AcousticAnalysisSetupCacheReporting"
        ],
        "_private.system_model.part_model.acoustics._2684": [
            "AcousticAnalysisSetupCollection"
        ],
        "_private.system_model.part_model.acoustics._2685": ["AcousticEnvelopeType"],
        "_private.system_model.part_model.acoustics._2686": [
            "AcousticInputSurfaceOptions"
        ],
        "_private.system_model.part_model.acoustics._2687": [
            "FEPartInputSurfaceOptions"
        ],
        "_private.system_model.part_model.acoustics._2688": [
            "FESurfaceSelectionForAcousticEnvelope"
        ],
        "_private.system_model.part_model.acoustics._2689": ["HoleInFaceGroup"],
        "_private.system_model.part_model.acoustics._2690": ["MeshedResultPlane"],
        "_private.system_model.part_model.acoustics._2691": ["MeshedResultSphere"],
        "_private.system_model.part_model.acoustics._2692": ["MeshedResultSurface"],
        "_private.system_model.part_model.acoustics._2693": ["MeshedResultSurfaceBase"],
        "_private.system_model.part_model.acoustics._2694": ["MicrophoneArrayDesign"],
        "_private.system_model.part_model.acoustics._2695": [
            "PartSelectionForAcousticEnvelope"
        ],
        "_private.system_model.part_model.acoustics._2696": ["ResultPlaneOptions"],
        "_private.system_model.part_model.acoustics._2697": ["ResultSphereOptions"],
        "_private.system_model.part_model.acoustics._2698": ["ResultSurfaceCollection"],
        "_private.system_model.part_model.acoustics._2699": ["ResultSurfaceOptions"],
        "_private.system_model.part_model.acoustics._2700": [
            "SphericalEnvelopeCentreDefinition"
        ],
        "_private.system_model.part_model.acoustics._2701": ["SphericalEnvelopeType"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AcousticAnalysisOptions",
    "AcousticAnalysisSetup",
    "AcousticAnalysisSetupCacheReporting",
    "AcousticAnalysisSetupCollection",
    "AcousticEnvelopeType",
    "AcousticInputSurfaceOptions",
    "FEPartInputSurfaceOptions",
    "FESurfaceSelectionForAcousticEnvelope",
    "HoleInFaceGroup",
    "MeshedResultPlane",
    "MeshedResultSphere",
    "MeshedResultSurface",
    "MeshedResultSurfaceBase",
    "MicrophoneArrayDesign",
    "PartSelectionForAcousticEnvelope",
    "ResultPlaneOptions",
    "ResultSphereOptions",
    "ResultSurfaceCollection",
    "ResultSurfaceOptions",
    "SphericalEnvelopeCentreDefinition",
    "SphericalEnvelopeType",
)
