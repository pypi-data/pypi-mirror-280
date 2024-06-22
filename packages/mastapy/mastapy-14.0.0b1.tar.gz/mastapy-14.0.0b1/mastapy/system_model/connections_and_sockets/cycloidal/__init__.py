"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2386 import (
        CycloidalDiscAxialLeftSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2387 import (
        CycloidalDiscAxialRightSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2388 import (
        CycloidalDiscCentralBearingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2389 import (
        CycloidalDiscInnerSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2390 import (
        CycloidalDiscOuterSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2391 import (
        CycloidalDiscPlanetaryBearingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2392 import (
        CycloidalDiscPlanetaryBearingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2393 import (
        RingPinsSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2394 import (
        RingPinsToDiscConnection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.connections_and_sockets.cycloidal._2386": [
            "CycloidalDiscAxialLeftSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2387": [
            "CycloidalDiscAxialRightSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2388": [
            "CycloidalDiscCentralBearingConnection"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2389": [
            "CycloidalDiscInnerSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2390": [
            "CycloidalDiscOuterSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2391": [
            "CycloidalDiscPlanetaryBearingConnection"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2392": [
            "CycloidalDiscPlanetaryBearingSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2393": [
            "RingPinsSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2394": [
            "RingPinsToDiscConnection"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
