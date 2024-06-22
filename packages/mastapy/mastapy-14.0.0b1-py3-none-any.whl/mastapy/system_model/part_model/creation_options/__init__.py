"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model.creation_options._2627 import (
        BeltCreationOptions,
    )
    from mastapy._private.system_model.part_model.creation_options._2628 import (
        CycloidalAssemblyCreationOptions,
    )
    from mastapy._private.system_model.part_model.creation_options._2629 import (
        CylindricalGearLinearTrainCreationOptions,
    )
    from mastapy._private.system_model.part_model.creation_options._2630 import (
        MicrophoneArrayCreationOptions,
    )
    from mastapy._private.system_model.part_model.creation_options._2631 import (
        PlanetCarrierCreationOptions,
    )
    from mastapy._private.system_model.part_model.creation_options._2632 import (
        ShaftCreationOptions,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.creation_options._2627": [
            "BeltCreationOptions"
        ],
        "_private.system_model.part_model.creation_options._2628": [
            "CycloidalAssemblyCreationOptions"
        ],
        "_private.system_model.part_model.creation_options._2629": [
            "CylindricalGearLinearTrainCreationOptions"
        ],
        "_private.system_model.part_model.creation_options._2630": [
            "MicrophoneArrayCreationOptions"
        ],
        "_private.system_model.part_model.creation_options._2631": [
            "PlanetCarrierCreationOptions"
        ],
        "_private.system_model.part_model.creation_options._2632": [
            "ShaftCreationOptions"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "MicrophoneArrayCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)
