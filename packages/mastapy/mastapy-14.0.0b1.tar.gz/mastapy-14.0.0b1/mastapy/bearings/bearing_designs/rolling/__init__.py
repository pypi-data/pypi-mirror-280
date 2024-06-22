"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.bearings.bearing_designs.rolling._2188 import (
        AngularContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2189 import (
        AngularContactThrustBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2190 import (
        AsymmetricSphericalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2191 import (
        AxialThrustCylindricalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2192 import (
        AxialThrustNeedleRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2193 import BallBearing
    from mastapy._private.bearings.bearing_designs.rolling._2194 import (
        BallBearingShoulderDefinition,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2195 import (
        BarrelRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2196 import (
        BearingProtection,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2197 import (
        BearingProtectionDetailsModifier,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2198 import (
        BearingProtectionLevel,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2199 import (
        BearingTypeExtraInformation,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2200 import CageBridgeShape
    from mastapy._private.bearings.bearing_designs.rolling._2201 import (
        CrossedRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2202 import (
        CylindricalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2203 import (
        DeepGrooveBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2204 import DiameterSeries
    from mastapy._private.bearings.bearing_designs.rolling._2205 import (
        FatigueLoadLimitCalculationMethodEnum,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2206 import (
        FourPointContactAngleDefinition,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2207 import (
        FourPointContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2208 import (
        GeometricConstants,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2209 import (
        GeometricConstantsForRollingFrictionalMoments,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2210 import (
        GeometricConstantsForSlidingFrictionalMoments,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2211 import HeightSeries
    from mastapy._private.bearings.bearing_designs.rolling._2212 import (
        MultiPointContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2213 import (
        NeedleRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2214 import (
        NonBarrelRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2215 import RollerBearing
    from mastapy._private.bearings.bearing_designs.rolling._2216 import RollerEndShape
    from mastapy._private.bearings.bearing_designs.rolling._2217 import RollerRibDetail
    from mastapy._private.bearings.bearing_designs.rolling._2218 import RollingBearing
    from mastapy._private.bearings.bearing_designs.rolling._2219 import (
        SelfAligningBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2220 import (
        SKFSealFrictionalMomentConstants,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2221 import SleeveType
    from mastapy._private.bearings.bearing_designs.rolling._2222 import (
        SphericalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2223 import (
        SphericalRollerThrustBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2224 import (
        TaperRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2225 import (
        ThreePointContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2226 import (
        ThrustBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2227 import (
        ToroidalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2228 import WidthSeries
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bearings.bearing_designs.rolling._2188": [
            "AngularContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2189": [
            "AngularContactThrustBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2190": [
            "AsymmetricSphericalRollerBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2191": [
            "AxialThrustCylindricalRollerBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2192": [
            "AxialThrustNeedleRollerBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2193": ["BallBearing"],
        "_private.bearings.bearing_designs.rolling._2194": [
            "BallBearingShoulderDefinition"
        ],
        "_private.bearings.bearing_designs.rolling._2195": ["BarrelRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2196": ["BearingProtection"],
        "_private.bearings.bearing_designs.rolling._2197": [
            "BearingProtectionDetailsModifier"
        ],
        "_private.bearings.bearing_designs.rolling._2198": ["BearingProtectionLevel"],
        "_private.bearings.bearing_designs.rolling._2199": [
            "BearingTypeExtraInformation"
        ],
        "_private.bearings.bearing_designs.rolling._2200": ["CageBridgeShape"],
        "_private.bearings.bearing_designs.rolling._2201": ["CrossedRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2202": ["CylindricalRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2203": ["DeepGrooveBallBearing"],
        "_private.bearings.bearing_designs.rolling._2204": ["DiameterSeries"],
        "_private.bearings.bearing_designs.rolling._2205": [
            "FatigueLoadLimitCalculationMethodEnum"
        ],
        "_private.bearings.bearing_designs.rolling._2206": [
            "FourPointContactAngleDefinition"
        ],
        "_private.bearings.bearing_designs.rolling._2207": [
            "FourPointContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2208": ["GeometricConstants"],
        "_private.bearings.bearing_designs.rolling._2209": [
            "GeometricConstantsForRollingFrictionalMoments"
        ],
        "_private.bearings.bearing_designs.rolling._2210": [
            "GeometricConstantsForSlidingFrictionalMoments"
        ],
        "_private.bearings.bearing_designs.rolling._2211": ["HeightSeries"],
        "_private.bearings.bearing_designs.rolling._2212": [
            "MultiPointContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2213": ["NeedleRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2214": ["NonBarrelRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2215": ["RollerBearing"],
        "_private.bearings.bearing_designs.rolling._2216": ["RollerEndShape"],
        "_private.bearings.bearing_designs.rolling._2217": ["RollerRibDetail"],
        "_private.bearings.bearing_designs.rolling._2218": ["RollingBearing"],
        "_private.bearings.bearing_designs.rolling._2219": ["SelfAligningBallBearing"],
        "_private.bearings.bearing_designs.rolling._2220": [
            "SKFSealFrictionalMomentConstants"
        ],
        "_private.bearings.bearing_designs.rolling._2221": ["SleeveType"],
        "_private.bearings.bearing_designs.rolling._2222": ["SphericalRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2223": [
            "SphericalRollerThrustBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2224": ["TaperRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2225": [
            "ThreePointContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2226": ["ThrustBallBearing"],
        "_private.bearings.bearing_designs.rolling._2227": ["ToroidalRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2228": ["WidthSeries"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
