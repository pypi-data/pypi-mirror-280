"""AbstractGearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.analysis import _1254
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearMeshRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating import _371, _376
    from mastapy._private.gears.rating.zerol_bevel import _380
    from mastapy._private.gears.rating.worm import _384, _388
    from mastapy._private.gears.rating.straight_bevel import _406
    from mastapy._private.gears.rating.straight_bevel_diff import _409
    from mastapy._private.gears.rating.spiral_bevel import _413
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _416
    from mastapy._private.gears.rating.klingelnberg_hypoid import _419
    from mastapy._private.gears.rating.klingelnberg_conical import _422
    from mastapy._private.gears.rating.hypoid import _449
    from mastapy._private.gears.rating.face import _457, _458
    from mastapy._private.gears.rating.cylindrical import _469, _477
    from mastapy._private.gears.rating.conical import _550, _555
    from mastapy._private.gears.rating.concept import _560, _561
    from mastapy._private.gears.rating.bevel import _565
    from mastapy._private.gears.rating.agma_gleason_conical import _576

    Self = TypeVar("Self", bound="AbstractGearMeshRating")
    CastSelf = TypeVar(
        "CastSelf", bound="AbstractGearMeshRating._Cast_AbstractGearMeshRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractGearMeshRating:
    """Special nested class for casting AbstractGearMeshRating to subclasses."""

    __parent__: "AbstractGearMeshRating"

    @property
    def abstract_gear_mesh_analysis(
        self: "CastSelf",
    ) -> "_1254.AbstractGearMeshAnalysis":
        return self.__parent__._cast(_1254.AbstractGearMeshAnalysis)

    @property
    def gear_mesh_rating(self: "CastSelf") -> "_371.GearMeshRating":
        from mastapy._private.gears.rating import _371

        return self.__parent__._cast(_371.GearMeshRating)

    @property
    def mesh_duty_cycle_rating(self: "CastSelf") -> "_376.MeshDutyCycleRating":
        from mastapy._private.gears.rating import _376

        return self.__parent__._cast(_376.MeshDutyCycleRating)

    @property
    def zerol_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_380.ZerolBevelGearMeshRating":
        from mastapy._private.gears.rating.zerol_bevel import _380

        return self.__parent__._cast(_380.ZerolBevelGearMeshRating)

    @property
    def worm_gear_mesh_rating(self: "CastSelf") -> "_384.WormGearMeshRating":
        from mastapy._private.gears.rating.worm import _384

        return self.__parent__._cast(_384.WormGearMeshRating)

    @property
    def worm_mesh_duty_cycle_rating(self: "CastSelf") -> "_388.WormMeshDutyCycleRating":
        from mastapy._private.gears.rating.worm import _388

        return self.__parent__._cast(_388.WormMeshDutyCycleRating)

    @property
    def straight_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_406.StraightBevelGearMeshRating":
        from mastapy._private.gears.rating.straight_bevel import _406

        return self.__parent__._cast(_406.StraightBevelGearMeshRating)

    @property
    def straight_bevel_diff_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_409.StraightBevelDiffGearMeshRating":
        from mastapy._private.gears.rating.straight_bevel_diff import _409

        return self.__parent__._cast(_409.StraightBevelDiffGearMeshRating)

    @property
    def spiral_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_413.SpiralBevelGearMeshRating":
        from mastapy._private.gears.rating.spiral_bevel import _413

        return self.__parent__._cast(_413.SpiralBevelGearMeshRating)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_416.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _416

        return self.__parent__._cast(
            _416.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_419.KlingelnbergCycloPalloidHypoidGearMeshRating":
        from mastapy._private.gears.rating.klingelnberg_hypoid import _419

        return self.__parent__._cast(_419.KlingelnbergCycloPalloidHypoidGearMeshRating)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_422.KlingelnbergCycloPalloidConicalGearMeshRating":
        from mastapy._private.gears.rating.klingelnberg_conical import _422

        return self.__parent__._cast(_422.KlingelnbergCycloPalloidConicalGearMeshRating)

    @property
    def hypoid_gear_mesh_rating(self: "CastSelf") -> "_449.HypoidGearMeshRating":
        from mastapy._private.gears.rating.hypoid import _449

        return self.__parent__._cast(_449.HypoidGearMeshRating)

    @property
    def face_gear_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_457.FaceGearMeshDutyCycleRating":
        from mastapy._private.gears.rating.face import _457

        return self.__parent__._cast(_457.FaceGearMeshDutyCycleRating)

    @property
    def face_gear_mesh_rating(self: "CastSelf") -> "_458.FaceGearMeshRating":
        from mastapy._private.gears.rating.face import _458

        return self.__parent__._cast(_458.FaceGearMeshRating)

    @property
    def cylindrical_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_469.CylindricalGearMeshRating":
        from mastapy._private.gears.rating.cylindrical import _469

        return self.__parent__._cast(_469.CylindricalGearMeshRating)

    @property
    def cylindrical_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_477.CylindricalMeshDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _477

        return self.__parent__._cast(_477.CylindricalMeshDutyCycleRating)

    @property
    def conical_gear_mesh_rating(self: "CastSelf") -> "_550.ConicalGearMeshRating":
        from mastapy._private.gears.rating.conical import _550

        return self.__parent__._cast(_550.ConicalGearMeshRating)

    @property
    def conical_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_555.ConicalMeshDutyCycleRating":
        from mastapy._private.gears.rating.conical import _555

        return self.__parent__._cast(_555.ConicalMeshDutyCycleRating)

    @property
    def concept_gear_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_560.ConceptGearMeshDutyCycleRating":
        from mastapy._private.gears.rating.concept import _560

        return self.__parent__._cast(_560.ConceptGearMeshDutyCycleRating)

    @property
    def concept_gear_mesh_rating(self: "CastSelf") -> "_561.ConceptGearMeshRating":
        from mastapy._private.gears.rating.concept import _561

        return self.__parent__._cast(_561.ConceptGearMeshRating)

    @property
    def bevel_gear_mesh_rating(self: "CastSelf") -> "_565.BevelGearMeshRating":
        from mastapy._private.gears.rating.bevel import _565

        return self.__parent__._cast(_565.BevelGearMeshRating)

    @property
    def agma_gleason_conical_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_576.AGMAGleasonConicalGearMeshRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _576

        return self.__parent__._cast(_576.AGMAGleasonConicalGearMeshRating)

    @property
    def abstract_gear_mesh_rating(self: "CastSelf") -> "AbstractGearMeshRating":
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
class AbstractGearMeshRating(_1254.AbstractGearMeshAnalysis):
    """AbstractGearMeshRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_GEAR_MESH_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def calculated_mesh_efficiency(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedMeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_safety_factor_for_fatigue(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_safety_factor_for_static(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractGearMeshRating":
        """Cast to another type.

        Returns:
            _Cast_AbstractGearMeshRating
        """
        return _Cast_AbstractGearMeshRating(self)
