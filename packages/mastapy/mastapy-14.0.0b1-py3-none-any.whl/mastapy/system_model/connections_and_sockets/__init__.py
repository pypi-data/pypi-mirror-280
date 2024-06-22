"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.connections_and_sockets._2318 import (
        AbstractShaftToMountableComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2319 import (
        BearingInnerSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2320 import (
        BearingOuterSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2321 import (
        BeltConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2322 import (
        CoaxialConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2323 import (
        ComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2324 import (
        ComponentMeasurer,
    )
    from mastapy._private.system_model.connections_and_sockets._2325 import Connection
    from mastapy._private.system_model.connections_and_sockets._2326 import (
        CVTBeltConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2327 import (
        CVTPulleySocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2328 import (
        CylindricalComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2329 import (
        CylindricalSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2330 import (
        DatumMeasurement,
    )
    from mastapy._private.system_model.connections_and_sockets._2331 import (
        ElectricMachineStatorSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2332 import (
        InnerShaftSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2333 import (
        InnerShaftSocketBase,
    )
    from mastapy._private.system_model.connections_and_sockets._2334 import (
        InterMountableComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2335 import (
        MountableComponentInnerSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2336 import (
        MountableComponentOuterSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2337 import (
        MountableComponentSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2338 import (
        OuterShaftSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2339 import (
        OuterShaftSocketBase,
    )
    from mastapy._private.system_model.connections_and_sockets._2340 import (
        PlanetaryConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2341 import (
        PlanetarySocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2342 import (
        PlanetarySocketBase,
    )
    from mastapy._private.system_model.connections_and_sockets._2343 import PulleySocket
    from mastapy._private.system_model.connections_and_sockets._2344 import (
        RealignmentResult,
    )
    from mastapy._private.system_model.connections_and_sockets._2345 import (
        RollingRingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2346 import (
        RollingRingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2347 import ShaftSocket
    from mastapy._private.system_model.connections_and_sockets._2348 import (
        ShaftToMountableComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2349 import Socket
    from mastapy._private.system_model.connections_and_sockets._2350 import (
        SocketConnectionOptions,
    )
    from mastapy._private.system_model.connections_and_sockets._2351 import (
        SocketConnectionSelection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.connections_and_sockets._2318": [
            "AbstractShaftToMountableComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2319": ["BearingInnerSocket"],
        "_private.system_model.connections_and_sockets._2320": ["BearingOuterSocket"],
        "_private.system_model.connections_and_sockets._2321": ["BeltConnection"],
        "_private.system_model.connections_and_sockets._2322": ["CoaxialConnection"],
        "_private.system_model.connections_and_sockets._2323": ["ComponentConnection"],
        "_private.system_model.connections_and_sockets._2324": ["ComponentMeasurer"],
        "_private.system_model.connections_and_sockets._2325": ["Connection"],
        "_private.system_model.connections_and_sockets._2326": ["CVTBeltConnection"],
        "_private.system_model.connections_and_sockets._2327": ["CVTPulleySocket"],
        "_private.system_model.connections_and_sockets._2328": [
            "CylindricalComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2329": ["CylindricalSocket"],
        "_private.system_model.connections_and_sockets._2330": ["DatumMeasurement"],
        "_private.system_model.connections_and_sockets._2331": [
            "ElectricMachineStatorSocket"
        ],
        "_private.system_model.connections_and_sockets._2332": ["InnerShaftSocket"],
        "_private.system_model.connections_and_sockets._2333": ["InnerShaftSocketBase"],
        "_private.system_model.connections_and_sockets._2334": [
            "InterMountableComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2335": [
            "MountableComponentInnerSocket"
        ],
        "_private.system_model.connections_and_sockets._2336": [
            "MountableComponentOuterSocket"
        ],
        "_private.system_model.connections_and_sockets._2337": [
            "MountableComponentSocket"
        ],
        "_private.system_model.connections_and_sockets._2338": ["OuterShaftSocket"],
        "_private.system_model.connections_and_sockets._2339": ["OuterShaftSocketBase"],
        "_private.system_model.connections_and_sockets._2340": ["PlanetaryConnection"],
        "_private.system_model.connections_and_sockets._2341": ["PlanetarySocket"],
        "_private.system_model.connections_and_sockets._2342": ["PlanetarySocketBase"],
        "_private.system_model.connections_and_sockets._2343": ["PulleySocket"],
        "_private.system_model.connections_and_sockets._2344": ["RealignmentResult"],
        "_private.system_model.connections_and_sockets._2345": [
            "RollingRingConnection"
        ],
        "_private.system_model.connections_and_sockets._2346": ["RollingRingSocket"],
        "_private.system_model.connections_and_sockets._2347": ["ShaftSocket"],
        "_private.system_model.connections_and_sockets._2348": [
            "ShaftToMountableComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2349": ["Socket"],
        "_private.system_model.connections_and_sockets._2350": [
            "SocketConnectionOptions"
        ],
        "_private.system_model.connections_and_sockets._2351": [
            "SocketConnectionSelection"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
