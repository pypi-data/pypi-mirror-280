"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7691 import (
        AcousticPreconditionerType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7692 import (
        HarmonicAcousticAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7693 import (
        InitialGuessOption,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7694 import (
        M2LHfCacheType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7695 import (
        NearFieldIntegralsCacheType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7696 import (
        OctreeCreationMethod,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7697 import (
        SingleExcitationDetails,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7698 import (
        SingleHarmonicExcitationAnalysisDetail,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7699 import (
        UnitForceExcitationAnalysisDetail,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results.acoustic_analyses._7691": [
            "AcousticPreconditionerType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7692": [
            "HarmonicAcousticAnalysis"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7693": [
            "InitialGuessOption"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7694": [
            "M2LHfCacheType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7695": [
            "NearFieldIntegralsCacheType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7696": [
            "OctreeCreationMethod"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7697": [
            "SingleExcitationDetails"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7698": [
            "SingleHarmonicExcitationAnalysisDetail"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7699": [
            "UnitForceExcitationAnalysisDetail"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AcousticPreconditionerType",
    "HarmonicAcousticAnalysis",
    "InitialGuessOption",
    "M2LHfCacheType",
    "NearFieldIntegralsCacheType",
    "OctreeCreationMethod",
    "SingleExcitationDetails",
    "SingleHarmonicExcitationAnalysisDetail",
    "UnitForceExcitationAnalysisDetail",
)
