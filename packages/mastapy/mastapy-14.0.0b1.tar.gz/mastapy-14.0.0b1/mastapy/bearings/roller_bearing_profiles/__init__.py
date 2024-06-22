"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.bearings.roller_bearing_profiles._1979 import ProfileDataToUse
    from mastapy._private.bearings.roller_bearing_profiles._1980 import ProfileSet
    from mastapy._private.bearings.roller_bearing_profiles._1981 import ProfileToFit
    from mastapy._private.bearings.roller_bearing_profiles._1982 import (
        RollerBearingConicalProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1983 import (
        RollerBearingCrownedProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1984 import (
        RollerBearingDinLundbergProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1985 import (
        RollerBearingFlatProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1986 import (
        RollerBearingJohnsGoharProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1987 import (
        RollerBearingLundbergProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1988 import (
        RollerBearingProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1989 import (
        RollerBearingTangentialCrownedProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1990 import (
        RollerBearingUserSpecifiedProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1991 import (
        RollerRaceProfilePoint,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1992 import (
        UserSpecifiedProfilePoint,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1993 import (
        UserSpecifiedRollerRaceProfilePoint,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bearings.roller_bearing_profiles._1979": ["ProfileDataToUse"],
        "_private.bearings.roller_bearing_profiles._1980": ["ProfileSet"],
        "_private.bearings.roller_bearing_profiles._1981": ["ProfileToFit"],
        "_private.bearings.roller_bearing_profiles._1982": [
            "RollerBearingConicalProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1983": [
            "RollerBearingCrownedProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1984": [
            "RollerBearingDinLundbergProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1985": ["RollerBearingFlatProfile"],
        "_private.bearings.roller_bearing_profiles._1986": [
            "RollerBearingJohnsGoharProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1987": [
            "RollerBearingLundbergProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1988": ["RollerBearingProfile"],
        "_private.bearings.roller_bearing_profiles._1989": [
            "RollerBearingTangentialCrownedProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1990": [
            "RollerBearingUserSpecifiedProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1991": ["RollerRaceProfilePoint"],
        "_private.bearings.roller_bearing_profiles._1992": [
            "UserSpecifiedProfilePoint"
        ],
        "_private.bearings.roller_bearing_profiles._1993": [
            "UserSpecifiedRollerRaceProfilePoint"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingTangentialCrownedProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
