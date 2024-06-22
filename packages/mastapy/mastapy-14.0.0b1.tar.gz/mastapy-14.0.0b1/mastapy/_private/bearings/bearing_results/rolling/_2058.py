"""LoadedCrossedRollerBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.bearings.bearing_results.rolling import _2082
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_LOADED_CROSSED_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedCrossedRollerBearingResults"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import _2086
    from mastapy._private.bearings.bearing_results import _2007, _2010, _2002
    from mastapy._private.bearings import _1927

    Self = TypeVar("Self", bound="LoadedCrossedRollerBearingResults")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCrossedRollerBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedCrossedRollerBearingResults:
    """Special nested class for casting LoadedCrossedRollerBearingResults to subclasses."""

    __parent__: "LoadedCrossedRollerBearingResults"

    @property
    def loaded_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2082.LoadedRollerBearingResults":
        return self.__parent__._cast(_2082.LoadedRollerBearingResults)

    @property
    def loaded_rolling_bearing_results(
        self: "CastSelf",
    ) -> "_2086.LoadedRollingBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2086

        return self.__parent__._cast(_2086.LoadedRollingBearingResults)

    @property
    def loaded_detailed_bearing_results(
        self: "CastSelf",
    ) -> "_2007.LoadedDetailedBearingResults":
        from mastapy._private.bearings.bearing_results import _2007

        return self.__parent__._cast(_2007.LoadedDetailedBearingResults)

    @property
    def loaded_non_linear_bearing_results(
        self: "CastSelf",
    ) -> "_2010.LoadedNonLinearBearingResults":
        from mastapy._private.bearings.bearing_results import _2010

        return self.__parent__._cast(_2010.LoadedNonLinearBearingResults)

    @property
    def loaded_bearing_results(self: "CastSelf") -> "_2002.LoadedBearingResults":
        from mastapy._private.bearings.bearing_results import _2002

        return self.__parent__._cast(_2002.LoadedBearingResults)

    @property
    def bearing_load_case_results_lightweight(
        self: "CastSelf",
    ) -> "_1927.BearingLoadCaseResultsLightweight":
        from mastapy._private.bearings import _1927

        return self.__parent__._cast(_1927.BearingLoadCaseResultsLightweight)

    @property
    def loaded_crossed_roller_bearing_results(
        self: "CastSelf",
    ) -> "LoadedCrossedRollerBearingResults":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class LoadedCrossedRollerBearingResults(_2082.LoadedRollerBearingResults):
    """LoadedCrossedRollerBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_CROSSED_ROLLER_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedCrossedRollerBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedCrossedRollerBearingResults
        """
        return _Cast_LoadedCrossedRollerBearingResults(self)
