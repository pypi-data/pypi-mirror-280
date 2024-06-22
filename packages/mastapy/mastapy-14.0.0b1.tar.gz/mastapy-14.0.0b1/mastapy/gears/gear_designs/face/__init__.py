"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_designs.face._1013 import FaceGearDesign
    from mastapy._private.gears.gear_designs.face._1014 import (
        FaceGearDiameterFaceWidthSpecificationMethod,
    )
    from mastapy._private.gears.gear_designs.face._1015 import FaceGearMeshDesign
    from mastapy._private.gears.gear_designs.face._1016 import FaceGearMeshMicroGeometry
    from mastapy._private.gears.gear_designs.face._1017 import FaceGearMicroGeometry
    from mastapy._private.gears.gear_designs.face._1018 import FaceGearPinionDesign
    from mastapy._private.gears.gear_designs.face._1019 import FaceGearSetDesign
    from mastapy._private.gears.gear_designs.face._1020 import FaceGearSetMicroGeometry
    from mastapy._private.gears.gear_designs.face._1021 import FaceGearWheelDesign
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_designs.face._1013": ["FaceGearDesign"],
        "_private.gears.gear_designs.face._1014": [
            "FaceGearDiameterFaceWidthSpecificationMethod"
        ],
        "_private.gears.gear_designs.face._1015": ["FaceGearMeshDesign"],
        "_private.gears.gear_designs.face._1016": ["FaceGearMeshMicroGeometry"],
        "_private.gears.gear_designs.face._1017": ["FaceGearMicroGeometry"],
        "_private.gears.gear_designs.face._1018": ["FaceGearPinionDesign"],
        "_private.gears.gear_designs.face._1019": ["FaceGearSetDesign"],
        "_private.gears.gear_designs.face._1020": ["FaceGearSetMicroGeometry"],
        "_private.gears.gear_designs.face._1021": ["FaceGearWheelDesign"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "FaceGearDesign",
    "FaceGearDiameterFaceWidthSpecificationMethod",
    "FaceGearMeshDesign",
    "FaceGearMeshMicroGeometry",
    "FaceGearMicroGeometry",
    "FaceGearPinionDesign",
    "FaceGearSetDesign",
    "FaceGearSetMicroGeometry",
    "FaceGearWheelDesign",
)
