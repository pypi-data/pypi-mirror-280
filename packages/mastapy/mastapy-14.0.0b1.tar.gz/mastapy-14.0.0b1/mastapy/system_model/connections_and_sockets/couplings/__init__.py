"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.connections_and_sockets.couplings._2395 import (
        ClutchConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2396 import (
        ClutchSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2397 import (
        ConceptCouplingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2398 import (
        ConceptCouplingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2399 import (
        CouplingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2400 import (
        CouplingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2401 import (
        PartToPartShearCouplingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2402 import (
        PartToPartShearCouplingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2403 import (
        SpringDamperConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2404 import (
        SpringDamperSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2405 import (
        TorqueConverterConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2406 import (
        TorqueConverterPumpSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings._2407 import (
        TorqueConverterTurbineSocket,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.connections_and_sockets.couplings._2395": [
            "ClutchConnection"
        ],
        "_private.system_model.connections_and_sockets.couplings._2396": [
            "ClutchSocket"
        ],
        "_private.system_model.connections_and_sockets.couplings._2397": [
            "ConceptCouplingConnection"
        ],
        "_private.system_model.connections_and_sockets.couplings._2398": [
            "ConceptCouplingSocket"
        ],
        "_private.system_model.connections_and_sockets.couplings._2399": [
            "CouplingConnection"
        ],
        "_private.system_model.connections_and_sockets.couplings._2400": [
            "CouplingSocket"
        ],
        "_private.system_model.connections_and_sockets.couplings._2401": [
            "PartToPartShearCouplingConnection"
        ],
        "_private.system_model.connections_and_sockets.couplings._2402": [
            "PartToPartShearCouplingSocket"
        ],
        "_private.system_model.connections_and_sockets.couplings._2403": [
            "SpringDamperConnection"
        ],
        "_private.system_model.connections_and_sockets.couplings._2404": [
            "SpringDamperSocket"
        ],
        "_private.system_model.connections_and_sockets.couplings._2405": [
            "TorqueConverterConnection"
        ],
        "_private.system_model.connections_and_sockets.couplings._2406": [
            "TorqueConverterPumpSocket"
        ],
        "_private.system_model.connections_and_sockets.couplings._2407": [
            "TorqueConverterTurbineSocket"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)
