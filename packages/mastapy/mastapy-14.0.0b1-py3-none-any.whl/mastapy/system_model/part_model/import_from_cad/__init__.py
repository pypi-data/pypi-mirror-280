"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model.import_from_cad._2549 import (
        AbstractShaftFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2550 import (
        ClutchFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2551 import (
        ComponentFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2552 import (
        ConceptBearingFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2553 import (
        ConnectorFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2554 import (
        CylindricalGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2555 import (
        CylindricalGearInPlanetarySetFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2556 import (
        CylindricalPlanetGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2557 import (
        CylindricalRingGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2558 import (
        CylindricalSunGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2559 import (
        HousedOrMounted,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2560 import (
        MountableComponentFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2561 import (
        PlanetShaftFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2562 import (
        PulleyFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2563 import (
        RigidConnectorFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2564 import (
        RollingBearingFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2565 import (
        ShaftFromCAD,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.import_from_cad._2549": [
            "AbstractShaftFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2550": ["ClutchFromCAD"],
        "_private.system_model.part_model.import_from_cad._2551": ["ComponentFromCAD"],
        "_private.system_model.part_model.import_from_cad._2552": [
            "ConceptBearingFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2553": ["ConnectorFromCAD"],
        "_private.system_model.part_model.import_from_cad._2554": [
            "CylindricalGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2555": [
            "CylindricalGearInPlanetarySetFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2556": [
            "CylindricalPlanetGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2557": [
            "CylindricalRingGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2558": [
            "CylindricalSunGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2559": ["HousedOrMounted"],
        "_private.system_model.part_model.import_from_cad._2560": [
            "MountableComponentFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2561": [
            "PlanetShaftFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2562": ["PulleyFromCAD"],
        "_private.system_model.part_model.import_from_cad._2563": [
            "RigidConnectorFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2564": [
            "RollingBearingFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2565": ["ShaftFromCAD"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)
