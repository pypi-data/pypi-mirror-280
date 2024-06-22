"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1125 import (
        CylindricalGearBiasModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1126 import (
        CylindricalGearCommonFlankMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1127 import (
        CylindricalGearFlankMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1128 import (
        CylindricalGearLeadModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1129 import (
        CylindricalGearLeadModificationAtProfilePosition,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1130 import (
        CylindricalGearMeshMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1131 import (
        CylindricalGearMeshMicroGeometryDutyCycle,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1132 import (
        CylindricalGearMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1133 import (
        CylindricalGearMicroGeometryBase,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1134 import (
        CylindricalGearMicroGeometryDutyCycle,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1135 import (
        CylindricalGearMicroGeometryMap,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1136 import (
        CylindricalGearMicroGeometryPerTooth,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1137 import (
        CylindricalGearProfileModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1138 import (
        CylindricalGearProfileModificationAtFaceWidthPosition,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1139 import (
        CylindricalGearSetMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1140 import (
        CylindricalGearSetMicroGeometryDutyCycle,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1141 import (
        CylindricalGearToothMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1142 import (
        CylindricalGearTriangularEndModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1143 import (
        CylindricalGearTriangularEndModificationAtOrientation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1144 import (
        DrawDefiningGearOrBoth,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1145 import (
        GearAlignment,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1146 import (
        LeadFormReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1147 import (
        LeadModificationForCustomer102CAD,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1148 import (
        LeadReliefSpecificationForCustomer102,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1149 import (
        LeadReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1150 import (
        LeadSlopeReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1151 import (
        LinearCylindricalGearTriangularEndModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1152 import (
        MeasuredMapDataTypes,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1153 import (
        MeshAlignment,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1154 import (
        MeshedCylindricalGearFlankMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1155 import (
        MeshedCylindricalGearMicroGeometry,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1156 import (
        MicroGeometryLeadToleranceChartView,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1157 import (
        MicroGeometryViewingOptions,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1158 import (
        ModificationForCustomer102CAD,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1159 import (
        ParabolicCylindricalGearTriangularEndModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1160 import (
        ProfileFormReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1161 import (
        ProfileModificationForCustomer102CAD,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1162 import (
        ProfileReliefSpecificationForCustomer102,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1163 import (
        ProfileReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1164 import (
        ProfileSlopeReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1165 import (
        ReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1166 import (
        SingleCylindricalGearTriangularEndModification,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1167 import (
        TotalLeadReliefWithDeviation,
    )
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry._1168 import (
        TotalProfileReliefWithDeviation,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_designs.cylindrical.micro_geometry._1125": [
            "CylindricalGearBiasModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1126": [
            "CylindricalGearCommonFlankMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1127": [
            "CylindricalGearFlankMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1128": [
            "CylindricalGearLeadModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1129": [
            "CylindricalGearLeadModificationAtProfilePosition"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1130": [
            "CylindricalGearMeshMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1131": [
            "CylindricalGearMeshMicroGeometryDutyCycle"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1132": [
            "CylindricalGearMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1133": [
            "CylindricalGearMicroGeometryBase"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1134": [
            "CylindricalGearMicroGeometryDutyCycle"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1135": [
            "CylindricalGearMicroGeometryMap"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1136": [
            "CylindricalGearMicroGeometryPerTooth"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1137": [
            "CylindricalGearProfileModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1138": [
            "CylindricalGearProfileModificationAtFaceWidthPosition"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1139": [
            "CylindricalGearSetMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1140": [
            "CylindricalGearSetMicroGeometryDutyCycle"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1141": [
            "CylindricalGearToothMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1142": [
            "CylindricalGearTriangularEndModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1143": [
            "CylindricalGearTriangularEndModificationAtOrientation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1144": [
            "DrawDefiningGearOrBoth"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1145": [
            "GearAlignment"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1146": [
            "LeadFormReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1147": [
            "LeadModificationForCustomer102CAD"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1148": [
            "LeadReliefSpecificationForCustomer102"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1149": [
            "LeadReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1150": [
            "LeadSlopeReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1151": [
            "LinearCylindricalGearTriangularEndModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1152": [
            "MeasuredMapDataTypes"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1153": [
            "MeshAlignment"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1154": [
            "MeshedCylindricalGearFlankMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1155": [
            "MeshedCylindricalGearMicroGeometry"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1156": [
            "MicroGeometryLeadToleranceChartView"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1157": [
            "MicroGeometryViewingOptions"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1158": [
            "ModificationForCustomer102CAD"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1159": [
            "ParabolicCylindricalGearTriangularEndModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1160": [
            "ProfileFormReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1161": [
            "ProfileModificationForCustomer102CAD"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1162": [
            "ProfileReliefSpecificationForCustomer102"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1163": [
            "ProfileReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1164": [
            "ProfileSlopeReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1165": [
            "ReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1166": [
            "SingleCylindricalGearTriangularEndModification"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1167": [
            "TotalLeadReliefWithDeviation"
        ],
        "_private.gears.gear_designs.cylindrical.micro_geometry._1168": [
            "TotalProfileReliefWithDeviation"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadModificationForCustomer102CAD",
    "LeadReliefSpecificationForCustomer102",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ModificationForCustomer102CAD",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileModificationForCustomer102CAD",
    "ProfileReliefSpecificationForCustomer102",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)
