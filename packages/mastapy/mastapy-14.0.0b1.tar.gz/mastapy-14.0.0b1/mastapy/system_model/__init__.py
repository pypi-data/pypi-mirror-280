"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model._2253 import Design
    from mastapy._private.system_model._2254 import ComponentDampingOption
    from mastapy._private.system_model._2255 import (
        ConceptCouplingSpeedRatioSpecificationMethod,
    )
    from mastapy._private.system_model._2256 import DesignEntity
    from mastapy._private.system_model._2257 import DesignEntityId
    from mastapy._private.system_model._2258 import DesignSettings
    from mastapy._private.system_model._2259 import DutyCycleImporter
    from mastapy._private.system_model._2260 import DutyCycleImporterDesignEntityMatch
    from mastapy._private.system_model._2261 import ExternalFullFELoader
    from mastapy._private.system_model._2262 import HypoidWindUpRemovalMethod
    from mastapy._private.system_model._2263 import IncludeDutyCycleOption
    from mastapy._private.system_model._2264 import MAAElectricMachineGroup
    from mastapy._private.system_model._2265 import MASTASettings
    from mastapy._private.system_model._2266 import MemorySummary
    from mastapy._private.system_model._2267 import MeshStiffnessModel
    from mastapy._private.system_model._2268 import (
        PlanetPinManufacturingErrorsCoordinateSystem,
    )
    from mastapy._private.system_model._2269 import (
        PowerLoadDragTorqueSpecificationMethod,
    )
    from mastapy._private.system_model._2270 import (
        PowerLoadInputTorqueSpecificationMethod,
    )
    from mastapy._private.system_model._2271 import PowerLoadPIDControlSpeedInputType
    from mastapy._private.system_model._2272 import PowerLoadType
    from mastapy._private.system_model._2273 import RelativeComponentAlignment
    from mastapy._private.system_model._2274 import RelativeOffsetOption
    from mastapy._private.system_model._2275 import SystemReporting
    from mastapy._private.system_model._2276 import (
        ThermalExpansionOptionForGroundedNodes,
    )
    from mastapy._private.system_model._2277 import TransmissionTemperatureSet
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model._2253": ["Design"],
        "_private.system_model._2254": ["ComponentDampingOption"],
        "_private.system_model._2255": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_private.system_model._2256": ["DesignEntity"],
        "_private.system_model._2257": ["DesignEntityId"],
        "_private.system_model._2258": ["DesignSettings"],
        "_private.system_model._2259": ["DutyCycleImporter"],
        "_private.system_model._2260": ["DutyCycleImporterDesignEntityMatch"],
        "_private.system_model._2261": ["ExternalFullFELoader"],
        "_private.system_model._2262": ["HypoidWindUpRemovalMethod"],
        "_private.system_model._2263": ["IncludeDutyCycleOption"],
        "_private.system_model._2264": ["MAAElectricMachineGroup"],
        "_private.system_model._2265": ["MASTASettings"],
        "_private.system_model._2266": ["MemorySummary"],
        "_private.system_model._2267": ["MeshStiffnessModel"],
        "_private.system_model._2268": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_private.system_model._2269": ["PowerLoadDragTorqueSpecificationMethod"],
        "_private.system_model._2270": ["PowerLoadInputTorqueSpecificationMethod"],
        "_private.system_model._2271": ["PowerLoadPIDControlSpeedInputType"],
        "_private.system_model._2272": ["PowerLoadType"],
        "_private.system_model._2273": ["RelativeComponentAlignment"],
        "_private.system_model._2274": ["RelativeOffsetOption"],
        "_private.system_model._2275": ["SystemReporting"],
        "_private.system_model._2276": ["ThermalExpansionOptionForGroundedNodes"],
        "_private.system_model._2277": ["TransmissionTemperatureSet"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MAAElectricMachineGroup",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
