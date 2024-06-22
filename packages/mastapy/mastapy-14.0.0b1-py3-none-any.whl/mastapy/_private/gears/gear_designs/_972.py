"""GearDesignComponent"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_DESIGN_COMPONENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "GearDesignComponent"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility.scripting import _1789
    from mastapy._private.gears.gear_designs import _971, _973, _974
    from mastapy._private.gears.gear_designs.zerol_bevel import _976, _977, _978, _979
    from mastapy._private.gears.gear_designs.worm import _980, _981, _982, _983, _984
    from mastapy._private.gears.gear_designs.straight_bevel import (
        _985,
        _986,
        _987,
        _988,
    )
    from mastapy._private.gears.gear_designs.straight_bevel_diff import (
        _989,
        _990,
        _991,
        _992,
    )
    from mastapy._private.gears.gear_designs.spiral_bevel import _993, _994, _995, _996
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import (
        _997,
        _998,
        _999,
        _1000,
    )
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import (
        _1001,
        _1002,
        _1003,
        _1004,
    )
    from mastapy._private.gears.gear_designs.klingelnberg_conical import (
        _1005,
        _1006,
        _1007,
        _1008,
    )
    from mastapy._private.gears.gear_designs.hypoid import _1009, _1010, _1011, _1012
    from mastapy._private.gears.gear_designs.face import (
        _1013,
        _1015,
        _1018,
        _1019,
        _1021,
    )
    from mastapy._private.gears.gear_designs.cylindrical import (
        _1042,
        _1048,
        _1058,
        _1071,
        _1072,
    )
    from mastapy._private.gears.gear_designs.conical import _1192, _1193, _1194, _1197
    from mastapy._private.gears.gear_designs.concept import _1214, _1215, _1216
    from mastapy._private.gears.gear_designs.bevel import _1218, _1219, _1220, _1221
    from mastapy._private.gears.gear_designs.agma_gleason_conical import (
        _1231,
        _1232,
        _1233,
        _1234,
    )

    Self = TypeVar("Self", bound="GearDesignComponent")
    CastSelf = TypeVar(
        "CastSelf", bound="GearDesignComponent._Cast_GearDesignComponent"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignComponent",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearDesignComponent:
    """Special nested class for casting GearDesignComponent to subclasses."""

    __parent__: "GearDesignComponent"

    @property
    def gear_design(self: "CastSelf") -> "_971.GearDesign":
        from mastapy._private.gears.gear_designs import _971

        return self.__parent__._cast(_971.GearDesign)

    @property
    def gear_mesh_design(self: "CastSelf") -> "_973.GearMeshDesign":
        from mastapy._private.gears.gear_designs import _973

        return self.__parent__._cast(_973.GearMeshDesign)

    @property
    def gear_set_design(self: "CastSelf") -> "_974.GearSetDesign":
        from mastapy._private.gears.gear_designs import _974

        return self.__parent__._cast(_974.GearSetDesign)

    @property
    def zerol_bevel_gear_design(self: "CastSelf") -> "_976.ZerolBevelGearDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _976

        return self.__parent__._cast(_976.ZerolBevelGearDesign)

    @property
    def zerol_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_977.ZerolBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _977

        return self.__parent__._cast(_977.ZerolBevelGearMeshDesign)

    @property
    def zerol_bevel_gear_set_design(self: "CastSelf") -> "_978.ZerolBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _978

        return self.__parent__._cast(_978.ZerolBevelGearSetDesign)

    @property
    def zerol_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_979.ZerolBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.zerol_bevel import _979

        return self.__parent__._cast(_979.ZerolBevelMeshedGearDesign)

    @property
    def worm_design(self: "CastSelf") -> "_980.WormDesign":
        from mastapy._private.gears.gear_designs.worm import _980

        return self.__parent__._cast(_980.WormDesign)

    @property
    def worm_gear_design(self: "CastSelf") -> "_981.WormGearDesign":
        from mastapy._private.gears.gear_designs.worm import _981

        return self.__parent__._cast(_981.WormGearDesign)

    @property
    def worm_gear_mesh_design(self: "CastSelf") -> "_982.WormGearMeshDesign":
        from mastapy._private.gears.gear_designs.worm import _982

        return self.__parent__._cast(_982.WormGearMeshDesign)

    @property
    def worm_gear_set_design(self: "CastSelf") -> "_983.WormGearSetDesign":
        from mastapy._private.gears.gear_designs.worm import _983

        return self.__parent__._cast(_983.WormGearSetDesign)

    @property
    def worm_wheel_design(self: "CastSelf") -> "_984.WormWheelDesign":
        from mastapy._private.gears.gear_designs.worm import _984

        return self.__parent__._cast(_984.WormWheelDesign)

    @property
    def straight_bevel_gear_design(self: "CastSelf") -> "_985.StraightBevelGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _985

        return self.__parent__._cast(_985.StraightBevelGearDesign)

    @property
    def straight_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_986.StraightBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _986

        return self.__parent__._cast(_986.StraightBevelGearMeshDesign)

    @property
    def straight_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_987.StraightBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _987

        return self.__parent__._cast(_987.StraightBevelGearSetDesign)

    @property
    def straight_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_988.StraightBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel import _988

        return self.__parent__._cast(_988.StraightBevelMeshedGearDesign)

    @property
    def straight_bevel_diff_gear_design(
        self: "CastSelf",
    ) -> "_989.StraightBevelDiffGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _989

        return self.__parent__._cast(_989.StraightBevelDiffGearDesign)

    @property
    def straight_bevel_diff_gear_mesh_design(
        self: "CastSelf",
    ) -> "_990.StraightBevelDiffGearMeshDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _990

        return self.__parent__._cast(_990.StraightBevelDiffGearMeshDesign)

    @property
    def straight_bevel_diff_gear_set_design(
        self: "CastSelf",
    ) -> "_991.StraightBevelDiffGearSetDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _991

        return self.__parent__._cast(_991.StraightBevelDiffGearSetDesign)

    @property
    def straight_bevel_diff_meshed_gear_design(
        self: "CastSelf",
    ) -> "_992.StraightBevelDiffMeshedGearDesign":
        from mastapy._private.gears.gear_designs.straight_bevel_diff import _992

        return self.__parent__._cast(_992.StraightBevelDiffMeshedGearDesign)

    @property
    def spiral_bevel_gear_design(self: "CastSelf") -> "_993.SpiralBevelGearDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _993

        return self.__parent__._cast(_993.SpiralBevelGearDesign)

    @property
    def spiral_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_994.SpiralBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _994

        return self.__parent__._cast(_994.SpiralBevelGearMeshDesign)

    @property
    def spiral_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_995.SpiralBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _995

        return self.__parent__._cast(_995.SpiralBevelGearSetDesign)

    @property
    def spiral_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_996.SpiralBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.spiral_bevel import _996

        return self.__parent__._cast(_996.SpiralBevelMeshedGearDesign)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
        self: "CastSelf",
    ) -> "_997.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _997

        return self.__parent__._cast(_997.KlingelnbergCycloPalloidSpiralBevelGearDesign)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
        self: "CastSelf",
    ) -> "_998.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _998

        return self.__parent__._cast(
            _998.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _999

        return self.__parent__._cast(
            _999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1000.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _1000

        return self.__parent__._cast(
            _1000.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_design(
        self: "CastSelf",
    ) -> "_1001.KlingelnbergCycloPalloidHypoidGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1001

        return self.__parent__._cast(_1001.KlingelnbergCycloPalloidHypoidGearDesign)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1002.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1002

        return self.__parent__._cast(_1002.KlingelnbergCycloPalloidHypoidGearMeshDesign)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
        self: "CastSelf",
    ) -> "_1003.KlingelnbergCycloPalloidHypoidGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1003

        return self.__parent__._cast(_1003.KlingelnbergCycloPalloidHypoidGearSetDesign)

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1004.KlingelnbergCycloPalloidHypoidMeshedGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1004

        return self.__parent__._cast(
            _1004.KlingelnbergCycloPalloidHypoidMeshedGearDesign
        )

    @property
    def klingelnberg_conical_gear_design(
        self: "CastSelf",
    ) -> "_1005.KlingelnbergConicalGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1005

        return self.__parent__._cast(_1005.KlingelnbergConicalGearDesign)

    @property
    def klingelnberg_conical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1006.KlingelnbergConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1006

        return self.__parent__._cast(_1006.KlingelnbergConicalGearMeshDesign)

    @property
    def klingelnberg_conical_gear_set_design(
        self: "CastSelf",
    ) -> "_1007.KlingelnbergConicalGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1007

        return self.__parent__._cast(_1007.KlingelnbergConicalGearSetDesign)

    @property
    def klingelnberg_conical_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1008.KlingelnbergConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_conical import _1008

        return self.__parent__._cast(_1008.KlingelnbergConicalMeshedGearDesign)

    @property
    def hypoid_gear_design(self: "CastSelf") -> "_1009.HypoidGearDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1009

        return self.__parent__._cast(_1009.HypoidGearDesign)

    @property
    def hypoid_gear_mesh_design(self: "CastSelf") -> "_1010.HypoidGearMeshDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1010

        return self.__parent__._cast(_1010.HypoidGearMeshDesign)

    @property
    def hypoid_gear_set_design(self: "CastSelf") -> "_1011.HypoidGearSetDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1011

        return self.__parent__._cast(_1011.HypoidGearSetDesign)

    @property
    def hypoid_meshed_gear_design(self: "CastSelf") -> "_1012.HypoidMeshedGearDesign":
        from mastapy._private.gears.gear_designs.hypoid import _1012

        return self.__parent__._cast(_1012.HypoidMeshedGearDesign)

    @property
    def face_gear_design(self: "CastSelf") -> "_1013.FaceGearDesign":
        from mastapy._private.gears.gear_designs.face import _1013

        return self.__parent__._cast(_1013.FaceGearDesign)

    @property
    def face_gear_mesh_design(self: "CastSelf") -> "_1015.FaceGearMeshDesign":
        from mastapy._private.gears.gear_designs.face import _1015

        return self.__parent__._cast(_1015.FaceGearMeshDesign)

    @property
    def face_gear_pinion_design(self: "CastSelf") -> "_1018.FaceGearPinionDesign":
        from mastapy._private.gears.gear_designs.face import _1018

        return self.__parent__._cast(_1018.FaceGearPinionDesign)

    @property
    def face_gear_set_design(self: "CastSelf") -> "_1019.FaceGearSetDesign":
        from mastapy._private.gears.gear_designs.face import _1019

        return self.__parent__._cast(_1019.FaceGearSetDesign)

    @property
    def face_gear_wheel_design(self: "CastSelf") -> "_1021.FaceGearWheelDesign":
        from mastapy._private.gears.gear_designs.face import _1021

        return self.__parent__._cast(_1021.FaceGearWheelDesign)

    @property
    def cylindrical_gear_design(self: "CastSelf") -> "_1042.CylindricalGearDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1042

        return self.__parent__._cast(_1042.CylindricalGearDesign)

    @property
    def cylindrical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1048.CylindricalGearMeshDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1048

        return self.__parent__._cast(_1048.CylindricalGearMeshDesign)

    @property
    def cylindrical_gear_set_design(
        self: "CastSelf",
    ) -> "_1058.CylindricalGearSetDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1058

        return self.__parent__._cast(_1058.CylindricalGearSetDesign)

    @property
    def cylindrical_planetary_gear_set_design(
        self: "CastSelf",
    ) -> "_1071.CylindricalPlanetaryGearSetDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1071

        return self.__parent__._cast(_1071.CylindricalPlanetaryGearSetDesign)

    @property
    def cylindrical_planet_gear_design(
        self: "CastSelf",
    ) -> "_1072.CylindricalPlanetGearDesign":
        from mastapy._private.gears.gear_designs.cylindrical import _1072

        return self.__parent__._cast(_1072.CylindricalPlanetGearDesign)

    @property
    def conical_gear_design(self: "CastSelf") -> "_1192.ConicalGearDesign":
        from mastapy._private.gears.gear_designs.conical import _1192

        return self.__parent__._cast(_1192.ConicalGearDesign)

    @property
    def conical_gear_mesh_design(self: "CastSelf") -> "_1193.ConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.conical import _1193

        return self.__parent__._cast(_1193.ConicalGearMeshDesign)

    @property
    def conical_gear_set_design(self: "CastSelf") -> "_1194.ConicalGearSetDesign":
        from mastapy._private.gears.gear_designs.conical import _1194

        return self.__parent__._cast(_1194.ConicalGearSetDesign)

    @property
    def conical_meshed_gear_design(self: "CastSelf") -> "_1197.ConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.conical import _1197

        return self.__parent__._cast(_1197.ConicalMeshedGearDesign)

    @property
    def concept_gear_design(self: "CastSelf") -> "_1214.ConceptGearDesign":
        from mastapy._private.gears.gear_designs.concept import _1214

        return self.__parent__._cast(_1214.ConceptGearDesign)

    @property
    def concept_gear_mesh_design(self: "CastSelf") -> "_1215.ConceptGearMeshDesign":
        from mastapy._private.gears.gear_designs.concept import _1215

        return self.__parent__._cast(_1215.ConceptGearMeshDesign)

    @property
    def concept_gear_set_design(self: "CastSelf") -> "_1216.ConceptGearSetDesign":
        from mastapy._private.gears.gear_designs.concept import _1216

        return self.__parent__._cast(_1216.ConceptGearSetDesign)

    @property
    def bevel_gear_design(self: "CastSelf") -> "_1218.BevelGearDesign":
        from mastapy._private.gears.gear_designs.bevel import _1218

        return self.__parent__._cast(_1218.BevelGearDesign)

    @property
    def bevel_gear_mesh_design(self: "CastSelf") -> "_1219.BevelGearMeshDesign":
        from mastapy._private.gears.gear_designs.bevel import _1219

        return self.__parent__._cast(_1219.BevelGearMeshDesign)

    @property
    def bevel_gear_set_design(self: "CastSelf") -> "_1220.BevelGearSetDesign":
        from mastapy._private.gears.gear_designs.bevel import _1220

        return self.__parent__._cast(_1220.BevelGearSetDesign)

    @property
    def bevel_meshed_gear_design(self: "CastSelf") -> "_1221.BevelMeshedGearDesign":
        from mastapy._private.gears.gear_designs.bevel import _1221

        return self.__parent__._cast(_1221.BevelMeshedGearDesign)

    @property
    def agma_gleason_conical_gear_design(
        self: "CastSelf",
    ) -> "_1231.AGMAGleasonConicalGearDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1231

        return self.__parent__._cast(_1231.AGMAGleasonConicalGearDesign)

    @property
    def agma_gleason_conical_gear_mesh_design(
        self: "CastSelf",
    ) -> "_1232.AGMAGleasonConicalGearMeshDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1232

        return self.__parent__._cast(_1232.AGMAGleasonConicalGearMeshDesign)

    @property
    def agma_gleason_conical_gear_set_design(
        self: "CastSelf",
    ) -> "_1233.AGMAGleasonConicalGearSetDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1233

        return self.__parent__._cast(_1233.AGMAGleasonConicalGearSetDesign)

    @property
    def agma_gleason_conical_meshed_gear_design(
        self: "CastSelf",
    ) -> "_1234.AGMAGleasonConicalMeshedGearDesign":
        from mastapy._private.gears.gear_designs.agma_gleason_conical import _1234

        return self.__parent__._cast(_1234.AGMAGleasonConicalMeshedGearDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "GearDesignComponent":
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
class GearDesignComponent(_0.APIBase):
    """GearDesignComponent

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_DESIGN_COMPONENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def user_specified_data(self: "Self") -> "_1789.UserSpecifiedData":
        """mastapy._private.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def dispose(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Dispose()

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    def __enter__(self: "Self") -> None:
        return self

    def __exit__(
        self: "Self", exception_type: "Any", exception_value: "Any", traceback: "Any"
    ) -> None:
        self.dispose()

    @property
    def cast_to(self: "Self") -> "_Cast_GearDesignComponent":
        """Cast to another type.

        Returns:
            _Cast_GearDesignComponent
        """
        return _Cast_GearDesignComponent(self)
