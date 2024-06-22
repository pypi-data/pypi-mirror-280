"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.math_utility._1535 import Range
    from mastapy._private.math_utility._1536 import AcousticWeighting
    from mastapy._private.math_utility._1537 import AlignmentAxis
    from mastapy._private.math_utility._1538 import Axis
    from mastapy._private.math_utility._1539 import CirclesOnAxis
    from mastapy._private.math_utility._1540 import ComplexMatrix
    from mastapy._private.math_utility._1541 import ComplexPartDisplayOption
    from mastapy._private.math_utility._1542 import ComplexVector
    from mastapy._private.math_utility._1543 import ComplexVector3D
    from mastapy._private.math_utility._1544 import ComplexVector6D
    from mastapy._private.math_utility._1545 import CoordinateSystem3D
    from mastapy._private.math_utility._1546 import CoordinateSystemEditor
    from mastapy._private.math_utility._1547 import CoordinateSystemForRotation
    from mastapy._private.math_utility._1548 import CoordinateSystemForRotationOrigin
    from mastapy._private.math_utility._1549 import DataPrecision
    from mastapy._private.math_utility._1550 import DegreeOfFreedom
    from mastapy._private.math_utility._1551 import DynamicsResponseScalarResult
    from mastapy._private.math_utility._1552 import DynamicsResponseScaling
    from mastapy._private.math_utility._1553 import Eigenmode
    from mastapy._private.math_utility._1554 import Eigenmodes
    from mastapy._private.math_utility._1555 import EulerParameters
    from mastapy._private.math_utility._1556 import ExtrapolationOptions
    from mastapy._private.math_utility._1557 import FacetedBody
    from mastapy._private.math_utility._1558 import FacetedSurface
    from mastapy._private.math_utility._1559 import FourierSeries
    from mastapy._private.math_utility._1560 import GenericMatrix
    from mastapy._private.math_utility._1561 import GriddedSurface
    from mastapy._private.math_utility._1562 import HarmonicValue
    from mastapy._private.math_utility._1563 import InertiaTensor
    from mastapy._private.math_utility._1564 import MassProperties
    from mastapy._private.math_utility._1565 import MaxMinMean
    from mastapy._private.math_utility._1566 import ComplexMagnitudeMethod
    from mastapy._private.math_utility._1567 import MultipleFourierSeriesInterpolator
    from mastapy._private.math_utility._1568 import Named2DLocation
    from mastapy._private.math_utility._1569 import PIDControlUpdateMethod
    from mastapy._private.math_utility._1570 import Quaternion
    from mastapy._private.math_utility._1571 import RealMatrix
    from mastapy._private.math_utility._1572 import RealVector
    from mastapy._private.math_utility._1573 import ResultOptionsFor3DVector
    from mastapy._private.math_utility._1574 import RotationAxis
    from mastapy._private.math_utility._1575 import RoundedOrder
    from mastapy._private.math_utility._1576 import SinCurve
    from mastapy._private.math_utility._1577 import SquareMatrix
    from mastapy._private.math_utility._1578 import StressPoint
    from mastapy._private.math_utility._1579 import TransformMatrix3D
    from mastapy._private.math_utility._1580 import TranslationRotation
    from mastapy._private.math_utility._1581 import Vector2DListAccessor
    from mastapy._private.math_utility._1582 import Vector6D
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.math_utility._1535": ["Range"],
        "_private.math_utility._1536": ["AcousticWeighting"],
        "_private.math_utility._1537": ["AlignmentAxis"],
        "_private.math_utility._1538": ["Axis"],
        "_private.math_utility._1539": ["CirclesOnAxis"],
        "_private.math_utility._1540": ["ComplexMatrix"],
        "_private.math_utility._1541": ["ComplexPartDisplayOption"],
        "_private.math_utility._1542": ["ComplexVector"],
        "_private.math_utility._1543": ["ComplexVector3D"],
        "_private.math_utility._1544": ["ComplexVector6D"],
        "_private.math_utility._1545": ["CoordinateSystem3D"],
        "_private.math_utility._1546": ["CoordinateSystemEditor"],
        "_private.math_utility._1547": ["CoordinateSystemForRotation"],
        "_private.math_utility._1548": ["CoordinateSystemForRotationOrigin"],
        "_private.math_utility._1549": ["DataPrecision"],
        "_private.math_utility._1550": ["DegreeOfFreedom"],
        "_private.math_utility._1551": ["DynamicsResponseScalarResult"],
        "_private.math_utility._1552": ["DynamicsResponseScaling"],
        "_private.math_utility._1553": ["Eigenmode"],
        "_private.math_utility._1554": ["Eigenmodes"],
        "_private.math_utility._1555": ["EulerParameters"],
        "_private.math_utility._1556": ["ExtrapolationOptions"],
        "_private.math_utility._1557": ["FacetedBody"],
        "_private.math_utility._1558": ["FacetedSurface"],
        "_private.math_utility._1559": ["FourierSeries"],
        "_private.math_utility._1560": ["GenericMatrix"],
        "_private.math_utility._1561": ["GriddedSurface"],
        "_private.math_utility._1562": ["HarmonicValue"],
        "_private.math_utility._1563": ["InertiaTensor"],
        "_private.math_utility._1564": ["MassProperties"],
        "_private.math_utility._1565": ["MaxMinMean"],
        "_private.math_utility._1566": ["ComplexMagnitudeMethod"],
        "_private.math_utility._1567": ["MultipleFourierSeriesInterpolator"],
        "_private.math_utility._1568": ["Named2DLocation"],
        "_private.math_utility._1569": ["PIDControlUpdateMethod"],
        "_private.math_utility._1570": ["Quaternion"],
        "_private.math_utility._1571": ["RealMatrix"],
        "_private.math_utility._1572": ["RealVector"],
        "_private.math_utility._1573": ["ResultOptionsFor3DVector"],
        "_private.math_utility._1574": ["RotationAxis"],
        "_private.math_utility._1575": ["RoundedOrder"],
        "_private.math_utility._1576": ["SinCurve"],
        "_private.math_utility._1577": ["SquareMatrix"],
        "_private.math_utility._1578": ["StressPoint"],
        "_private.math_utility._1579": ["TransformMatrix3D"],
        "_private.math_utility._1580": ["TranslationRotation"],
        "_private.math_utility._1581": ["Vector2DListAccessor"],
        "_private.math_utility._1582": ["Vector6D"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
