"""CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6354,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6180,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6298,
        _6303,
        _6317,
        _6359,
        _6365,
        _6369,
        _6381,
        _6391,
        _6392,
        _6393,
        _6396,
        _6397,
        _6300,
        _6356,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"

    @property
    def mountable_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6354.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6354.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6300.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6300,
        )

        return self.__parent__._cast(
            _6300.ComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6356.PartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6356,
        )

        return self.__parent__._cast(
            _6356.PartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7708.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def clutch_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6298.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6298,
        )

        return self.__parent__._cast(
            _6298.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6303.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6303,
        )

        return self.__parent__._cast(
            _6303.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6317.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6317,
        )

        return self.__parent__._cast(
            _6317.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6359.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6359,
        )

        return self.__parent__._cast(
            _6359.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def pulley_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6365.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6365,
        )

        return self.__parent__._cast(
            _6365.PulleyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def rolling_ring_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6369.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6369,
        )

        return self.__parent__._cast(
            _6369.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6381.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6381,
        )

        return self.__parent__._cast(
            _6381.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6391.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6391,
        )

        return self.__parent__._cast(
            _6391.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6392.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6392,
        )

        return self.__parent__._cast(
            _6392.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6393.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6393,
        )

        return self.__parent__._cast(
            _6393.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6396.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6396,
        )

        return self.__parent__._cast(
            _6396.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6397.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6397,
        )

        return self.__parent__._cast(
            _6397.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
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
class CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(
    _6354.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6180.CouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHalfHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6180.CouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHalfHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(self)
