"""MeasurementBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.implicit import overridable, list_with_selected_item
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.units_and_measurements import _1657
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MEASUREMENT_BASE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "MeasurementBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.utility import _1645
    from mastapy._private.utility.units_and_measurements.measurements import (
        _1659,
        _1660,
        _1661,
        _1662,
        _1663,
        _1664,
        _1665,
        _1666,
        _1667,
        _1668,
        _1669,
        _1670,
        _1671,
        _1672,
        _1673,
        _1674,
        _1675,
        _1676,
        _1677,
        _1678,
        _1679,
        _1680,
        _1681,
        _1682,
        _1683,
        _1684,
        _1685,
        _1686,
        _1687,
        _1688,
        _1689,
        _1690,
        _1691,
        _1692,
        _1693,
        _1694,
        _1695,
        _1696,
        _1697,
        _1698,
        _1699,
        _1700,
        _1701,
        _1702,
        _1703,
        _1704,
        _1705,
        _1706,
        _1707,
        _1708,
        _1709,
        _1710,
        _1711,
        _1712,
        _1713,
        _1714,
        _1715,
        _1716,
        _1717,
        _1718,
        _1719,
        _1720,
        _1721,
        _1722,
        _1723,
        _1724,
        _1725,
        _1726,
        _1727,
        _1728,
        _1729,
        _1730,
        _1731,
        _1732,
        _1733,
        _1734,
        _1735,
        _1736,
        _1737,
        _1738,
        _1739,
        _1740,
        _1741,
        _1742,
        _1743,
        _1744,
        _1745,
        _1746,
        _1747,
        _1748,
        _1749,
        _1750,
        _1751,
        _1752,
        _1753,
        _1754,
        _1755,
        _1756,
        _1757,
        _1758,
        _1759,
        _1760,
        _1761,
        _1762,
        _1763,
        _1764,
        _1765,
        _1766,
        _1767,
        _1768,
        _1769,
        _1770,
        _1771,
        _1772,
        _1773,
        _1774,
        _1775,
        _1776,
        _1777,
        _1778,
        _1779,
        _1780,
        _1781,
        _1782,
        _1783,
        _1784,
        _1785,
        _1786,
    )

    Self = TypeVar("Self", bound="MeasurementBase")
    CastSelf = TypeVar("CastSelf", bound="MeasurementBase._Cast_MeasurementBase")


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MeasurementBase:
    """Special nested class for casting MeasurementBase to subclasses."""

    __parent__: "MeasurementBase"

    @property
    def acceleration(self: "CastSelf") -> "_1659.Acceleration":
        from mastapy._private.utility.units_and_measurements.measurements import _1659

        return self.__parent__._cast(_1659.Acceleration)

    @property
    def angle(self: "CastSelf") -> "_1660.Angle":
        from mastapy._private.utility.units_and_measurements.measurements import _1660

        return self.__parent__._cast(_1660.Angle)

    @property
    def angle_per_unit_temperature(self: "CastSelf") -> "_1661.AnglePerUnitTemperature":
        from mastapy._private.utility.units_and_measurements.measurements import _1661

        return self.__parent__._cast(_1661.AnglePerUnitTemperature)

    @property
    def angle_small(self: "CastSelf") -> "_1662.AngleSmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1662

        return self.__parent__._cast(_1662.AngleSmall)

    @property
    def angle_very_small(self: "CastSelf") -> "_1663.AngleVerySmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1663

        return self.__parent__._cast(_1663.AngleVerySmall)

    @property
    def angular_acceleration(self: "CastSelf") -> "_1664.AngularAcceleration":
        from mastapy._private.utility.units_and_measurements.measurements import _1664

        return self.__parent__._cast(_1664.AngularAcceleration)

    @property
    def angular_compliance(self: "CastSelf") -> "_1665.AngularCompliance":
        from mastapy._private.utility.units_and_measurements.measurements import _1665

        return self.__parent__._cast(_1665.AngularCompliance)

    @property
    def angular_jerk(self: "CastSelf") -> "_1666.AngularJerk":
        from mastapy._private.utility.units_and_measurements.measurements import _1666

        return self.__parent__._cast(_1666.AngularJerk)

    @property
    def angular_stiffness(self: "CastSelf") -> "_1667.AngularStiffness":
        from mastapy._private.utility.units_and_measurements.measurements import _1667

        return self.__parent__._cast(_1667.AngularStiffness)

    @property
    def angular_velocity(self: "CastSelf") -> "_1668.AngularVelocity":
        from mastapy._private.utility.units_and_measurements.measurements import _1668

        return self.__parent__._cast(_1668.AngularVelocity)

    @property
    def area(self: "CastSelf") -> "_1669.Area":
        from mastapy._private.utility.units_and_measurements.measurements import _1669

        return self.__parent__._cast(_1669.Area)

    @property
    def area_small(self: "CastSelf") -> "_1670.AreaSmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1670

        return self.__parent__._cast(_1670.AreaSmall)

    @property
    def carbon_emission_factor(self: "CastSelf") -> "_1671.CarbonEmissionFactor":
        from mastapy._private.utility.units_and_measurements.measurements import _1671

        return self.__parent__._cast(_1671.CarbonEmissionFactor)

    @property
    def current_density(self: "CastSelf") -> "_1672.CurrentDensity":
        from mastapy._private.utility.units_and_measurements.measurements import _1672

        return self.__parent__._cast(_1672.CurrentDensity)

    @property
    def current_per_length(self: "CastSelf") -> "_1673.CurrentPerLength":
        from mastapy._private.utility.units_and_measurements.measurements import _1673

        return self.__parent__._cast(_1673.CurrentPerLength)

    @property
    def cycles(self: "CastSelf") -> "_1674.Cycles":
        from mastapy._private.utility.units_and_measurements.measurements import _1674

        return self.__parent__._cast(_1674.Cycles)

    @property
    def damage(self: "CastSelf") -> "_1675.Damage":
        from mastapy._private.utility.units_and_measurements.measurements import _1675

        return self.__parent__._cast(_1675.Damage)

    @property
    def damage_rate(self: "CastSelf") -> "_1676.DamageRate":
        from mastapy._private.utility.units_and_measurements.measurements import _1676

        return self.__parent__._cast(_1676.DamageRate)

    @property
    def data_size(self: "CastSelf") -> "_1677.DataSize":
        from mastapy._private.utility.units_and_measurements.measurements import _1677

        return self.__parent__._cast(_1677.DataSize)

    @property
    def decibel(self: "CastSelf") -> "_1678.Decibel":
        from mastapy._private.utility.units_and_measurements.measurements import _1678

        return self.__parent__._cast(_1678.Decibel)

    @property
    def density(self: "CastSelf") -> "_1679.Density":
        from mastapy._private.utility.units_and_measurements.measurements import _1679

        return self.__parent__._cast(_1679.Density)

    @property
    def electrical_resistance(self: "CastSelf") -> "_1680.ElectricalResistance":
        from mastapy._private.utility.units_and_measurements.measurements import _1680

        return self.__parent__._cast(_1680.ElectricalResistance)

    @property
    def electrical_resistivity(self: "CastSelf") -> "_1681.ElectricalResistivity":
        from mastapy._private.utility.units_and_measurements.measurements import _1681

        return self.__parent__._cast(_1681.ElectricalResistivity)

    @property
    def electric_current(self: "CastSelf") -> "_1682.ElectricCurrent":
        from mastapy._private.utility.units_and_measurements.measurements import _1682

        return self.__parent__._cast(_1682.ElectricCurrent)

    @property
    def energy(self: "CastSelf") -> "_1683.Energy":
        from mastapy._private.utility.units_and_measurements.measurements import _1683

        return self.__parent__._cast(_1683.Energy)

    @property
    def energy_per_unit_area(self: "CastSelf") -> "_1684.EnergyPerUnitArea":
        from mastapy._private.utility.units_and_measurements.measurements import _1684

        return self.__parent__._cast(_1684.EnergyPerUnitArea)

    @property
    def energy_per_unit_area_small(self: "CastSelf") -> "_1685.EnergyPerUnitAreaSmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1685

        return self.__parent__._cast(_1685.EnergyPerUnitAreaSmall)

    @property
    def energy_small(self: "CastSelf") -> "_1686.EnergySmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1686

        return self.__parent__._cast(_1686.EnergySmall)

    @property
    def enum(self: "CastSelf") -> "_1687.Enum":
        from mastapy._private.utility.units_and_measurements.measurements import _1687

        return self.__parent__._cast(_1687.Enum)

    @property
    def flow_rate(self: "CastSelf") -> "_1688.FlowRate":
        from mastapy._private.utility.units_and_measurements.measurements import _1688

        return self.__parent__._cast(_1688.FlowRate)

    @property
    def force(self: "CastSelf") -> "_1689.Force":
        from mastapy._private.utility.units_and_measurements.measurements import _1689

        return self.__parent__._cast(_1689.Force)

    @property
    def force_per_unit_length(self: "CastSelf") -> "_1690.ForcePerUnitLength":
        from mastapy._private.utility.units_and_measurements.measurements import _1690

        return self.__parent__._cast(_1690.ForcePerUnitLength)

    @property
    def force_per_unit_pressure(self: "CastSelf") -> "_1691.ForcePerUnitPressure":
        from mastapy._private.utility.units_and_measurements.measurements import _1691

        return self.__parent__._cast(_1691.ForcePerUnitPressure)

    @property
    def force_per_unit_temperature(self: "CastSelf") -> "_1692.ForcePerUnitTemperature":
        from mastapy._private.utility.units_and_measurements.measurements import _1692

        return self.__parent__._cast(_1692.ForcePerUnitTemperature)

    @property
    def fraction_measurement_base(self: "CastSelf") -> "_1693.FractionMeasurementBase":
        from mastapy._private.utility.units_and_measurements.measurements import _1693

        return self.__parent__._cast(_1693.FractionMeasurementBase)

    @property
    def fraction_per_temperature(self: "CastSelf") -> "_1694.FractionPerTemperature":
        from mastapy._private.utility.units_and_measurements.measurements import _1694

        return self.__parent__._cast(_1694.FractionPerTemperature)

    @property
    def frequency(self: "CastSelf") -> "_1695.Frequency":
        from mastapy._private.utility.units_and_measurements.measurements import _1695

        return self.__parent__._cast(_1695.Frequency)

    @property
    def fuel_consumption_engine(self: "CastSelf") -> "_1696.FuelConsumptionEngine":
        from mastapy._private.utility.units_and_measurements.measurements import _1696

        return self.__parent__._cast(_1696.FuelConsumptionEngine)

    @property
    def fuel_efficiency_vehicle(self: "CastSelf") -> "_1697.FuelEfficiencyVehicle":
        from mastapy._private.utility.units_and_measurements.measurements import _1697

        return self.__parent__._cast(_1697.FuelEfficiencyVehicle)

    @property
    def gradient(self: "CastSelf") -> "_1698.Gradient":
        from mastapy._private.utility.units_and_measurements.measurements import _1698

        return self.__parent__._cast(_1698.Gradient)

    @property
    def heat_conductivity(self: "CastSelf") -> "_1699.HeatConductivity":
        from mastapy._private.utility.units_and_measurements.measurements import _1699

        return self.__parent__._cast(_1699.HeatConductivity)

    @property
    def heat_transfer(self: "CastSelf") -> "_1700.HeatTransfer":
        from mastapy._private.utility.units_and_measurements.measurements import _1700

        return self.__parent__._cast(_1700.HeatTransfer)

    @property
    def heat_transfer_coefficient_for_plastic_gear_tooth(
        self: "CastSelf",
    ) -> "_1701.HeatTransferCoefficientForPlasticGearTooth":
        from mastapy._private.utility.units_and_measurements.measurements import _1701

        return self.__parent__._cast(_1701.HeatTransferCoefficientForPlasticGearTooth)

    @property
    def heat_transfer_resistance(self: "CastSelf") -> "_1702.HeatTransferResistance":
        from mastapy._private.utility.units_and_measurements.measurements import _1702

        return self.__parent__._cast(_1702.HeatTransferResistance)

    @property
    def impulse(self: "CastSelf") -> "_1703.Impulse":
        from mastapy._private.utility.units_and_measurements.measurements import _1703

        return self.__parent__._cast(_1703.Impulse)

    @property
    def index(self: "CastSelf") -> "_1704.Index":
        from mastapy._private.utility.units_and_measurements.measurements import _1704

        return self.__parent__._cast(_1704.Index)

    @property
    def inductance(self: "CastSelf") -> "_1705.Inductance":
        from mastapy._private.utility.units_and_measurements.measurements import _1705

        return self.__parent__._cast(_1705.Inductance)

    @property
    def integer(self: "CastSelf") -> "_1706.Integer":
        from mastapy._private.utility.units_and_measurements.measurements import _1706

        return self.__parent__._cast(_1706.Integer)

    @property
    def inverse_short_length(self: "CastSelf") -> "_1707.InverseShortLength":
        from mastapy._private.utility.units_and_measurements.measurements import _1707

        return self.__parent__._cast(_1707.InverseShortLength)

    @property
    def inverse_short_time(self: "CastSelf") -> "_1708.InverseShortTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1708

        return self.__parent__._cast(_1708.InverseShortTime)

    @property
    def jerk(self: "CastSelf") -> "_1709.Jerk":
        from mastapy._private.utility.units_and_measurements.measurements import _1709

        return self.__parent__._cast(_1709.Jerk)

    @property
    def kinematic_viscosity(self: "CastSelf") -> "_1710.KinematicViscosity":
        from mastapy._private.utility.units_and_measurements.measurements import _1710

        return self.__parent__._cast(_1710.KinematicViscosity)

    @property
    def length_long(self: "CastSelf") -> "_1711.LengthLong":
        from mastapy._private.utility.units_and_measurements.measurements import _1711

        return self.__parent__._cast(_1711.LengthLong)

    @property
    def length_medium(self: "CastSelf") -> "_1712.LengthMedium":
        from mastapy._private.utility.units_and_measurements.measurements import _1712

        return self.__parent__._cast(_1712.LengthMedium)

    @property
    def length_per_unit_temperature(
        self: "CastSelf",
    ) -> "_1713.LengthPerUnitTemperature":
        from mastapy._private.utility.units_and_measurements.measurements import _1713

        return self.__parent__._cast(_1713.LengthPerUnitTemperature)

    @property
    def length_short(self: "CastSelf") -> "_1714.LengthShort":
        from mastapy._private.utility.units_and_measurements.measurements import _1714

        return self.__parent__._cast(_1714.LengthShort)

    @property
    def length_to_the_fourth(self: "CastSelf") -> "_1715.LengthToTheFourth":
        from mastapy._private.utility.units_and_measurements.measurements import _1715

        return self.__parent__._cast(_1715.LengthToTheFourth)

    @property
    def length_very_long(self: "CastSelf") -> "_1716.LengthVeryLong":
        from mastapy._private.utility.units_and_measurements.measurements import _1716

        return self.__parent__._cast(_1716.LengthVeryLong)

    @property
    def length_very_short(self: "CastSelf") -> "_1717.LengthVeryShort":
        from mastapy._private.utility.units_and_measurements.measurements import _1717

        return self.__parent__._cast(_1717.LengthVeryShort)

    @property
    def length_very_short_per_length_short(
        self: "CastSelf",
    ) -> "_1718.LengthVeryShortPerLengthShort":
        from mastapy._private.utility.units_and_measurements.measurements import _1718

        return self.__parent__._cast(_1718.LengthVeryShortPerLengthShort)

    @property
    def linear_angular_damping(self: "CastSelf") -> "_1719.LinearAngularDamping":
        from mastapy._private.utility.units_and_measurements.measurements import _1719

        return self.__parent__._cast(_1719.LinearAngularDamping)

    @property
    def linear_angular_stiffness_cross_term(
        self: "CastSelf",
    ) -> "_1720.LinearAngularStiffnessCrossTerm":
        from mastapy._private.utility.units_and_measurements.measurements import _1720

        return self.__parent__._cast(_1720.LinearAngularStiffnessCrossTerm)

    @property
    def linear_damping(self: "CastSelf") -> "_1721.LinearDamping":
        from mastapy._private.utility.units_and_measurements.measurements import _1721

        return self.__parent__._cast(_1721.LinearDamping)

    @property
    def linear_flexibility(self: "CastSelf") -> "_1722.LinearFlexibility":
        from mastapy._private.utility.units_and_measurements.measurements import _1722

        return self.__parent__._cast(_1722.LinearFlexibility)

    @property
    def linear_stiffness(self: "CastSelf") -> "_1723.LinearStiffness":
        from mastapy._private.utility.units_and_measurements.measurements import _1723

        return self.__parent__._cast(_1723.LinearStiffness)

    @property
    def magnetic_field_strength(self: "CastSelf") -> "_1724.MagneticFieldStrength":
        from mastapy._private.utility.units_and_measurements.measurements import _1724

        return self.__parent__._cast(_1724.MagneticFieldStrength)

    @property
    def magnetic_flux(self: "CastSelf") -> "_1725.MagneticFlux":
        from mastapy._private.utility.units_and_measurements.measurements import _1725

        return self.__parent__._cast(_1725.MagneticFlux)

    @property
    def magnetic_flux_density(self: "CastSelf") -> "_1726.MagneticFluxDensity":
        from mastapy._private.utility.units_and_measurements.measurements import _1726

        return self.__parent__._cast(_1726.MagneticFluxDensity)

    @property
    def magnetic_vector_potential(self: "CastSelf") -> "_1727.MagneticVectorPotential":
        from mastapy._private.utility.units_and_measurements.measurements import _1727

        return self.__parent__._cast(_1727.MagneticVectorPotential)

    @property
    def magnetomotive_force(self: "CastSelf") -> "_1728.MagnetomotiveForce":
        from mastapy._private.utility.units_and_measurements.measurements import _1728

        return self.__parent__._cast(_1728.MagnetomotiveForce)

    @property
    def mass(self: "CastSelf") -> "_1729.Mass":
        from mastapy._private.utility.units_and_measurements.measurements import _1729

        return self.__parent__._cast(_1729.Mass)

    @property
    def mass_per_unit_length(self: "CastSelf") -> "_1730.MassPerUnitLength":
        from mastapy._private.utility.units_and_measurements.measurements import _1730

        return self.__parent__._cast(_1730.MassPerUnitLength)

    @property
    def mass_per_unit_time(self: "CastSelf") -> "_1731.MassPerUnitTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1731

        return self.__parent__._cast(_1731.MassPerUnitTime)

    @property
    def moment_of_inertia(self: "CastSelf") -> "_1732.MomentOfInertia":
        from mastapy._private.utility.units_and_measurements.measurements import _1732

        return self.__parent__._cast(_1732.MomentOfInertia)

    @property
    def moment_of_inertia_per_unit_length(
        self: "CastSelf",
    ) -> "_1733.MomentOfInertiaPerUnitLength":
        from mastapy._private.utility.units_and_measurements.measurements import _1733

        return self.__parent__._cast(_1733.MomentOfInertiaPerUnitLength)

    @property
    def moment_per_unit_pressure(self: "CastSelf") -> "_1734.MomentPerUnitPressure":
        from mastapy._private.utility.units_and_measurements.measurements import _1734

        return self.__parent__._cast(_1734.MomentPerUnitPressure)

    @property
    def number(self: "CastSelf") -> "_1735.Number":
        from mastapy._private.utility.units_and_measurements.measurements import _1735

        return self.__parent__._cast(_1735.Number)

    @property
    def percentage(self: "CastSelf") -> "_1736.Percentage":
        from mastapy._private.utility.units_and_measurements.measurements import _1736

        return self.__parent__._cast(_1736.Percentage)

    @property
    def power(self: "CastSelf") -> "_1737.Power":
        from mastapy._private.utility.units_and_measurements.measurements import _1737

        return self.__parent__._cast(_1737.Power)

    @property
    def power_per_small_area(self: "CastSelf") -> "_1738.PowerPerSmallArea":
        from mastapy._private.utility.units_and_measurements.measurements import _1738

        return self.__parent__._cast(_1738.PowerPerSmallArea)

    @property
    def power_per_unit_time(self: "CastSelf") -> "_1739.PowerPerUnitTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1739

        return self.__parent__._cast(_1739.PowerPerUnitTime)

    @property
    def power_small(self: "CastSelf") -> "_1740.PowerSmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1740

        return self.__parent__._cast(_1740.PowerSmall)

    @property
    def power_small_per_area(self: "CastSelf") -> "_1741.PowerSmallPerArea":
        from mastapy._private.utility.units_and_measurements.measurements import _1741

        return self.__parent__._cast(_1741.PowerSmallPerArea)

    @property
    def power_small_per_mass(self: "CastSelf") -> "_1742.PowerSmallPerMass":
        from mastapy._private.utility.units_and_measurements.measurements import _1742

        return self.__parent__._cast(_1742.PowerSmallPerMass)

    @property
    def power_small_per_unit_area_per_unit_time(
        self: "CastSelf",
    ) -> "_1743.PowerSmallPerUnitAreaPerUnitTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1743

        return self.__parent__._cast(_1743.PowerSmallPerUnitAreaPerUnitTime)

    @property
    def power_small_per_unit_time(self: "CastSelf") -> "_1744.PowerSmallPerUnitTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1744

        return self.__parent__._cast(_1744.PowerSmallPerUnitTime)

    @property
    def power_small_per_volume(self: "CastSelf") -> "_1745.PowerSmallPerVolume":
        from mastapy._private.utility.units_and_measurements.measurements import _1745

        return self.__parent__._cast(_1745.PowerSmallPerVolume)

    @property
    def pressure(self: "CastSelf") -> "_1746.Pressure":
        from mastapy._private.utility.units_and_measurements.measurements import _1746

        return self.__parent__._cast(_1746.Pressure)

    @property
    def pressure_per_unit_time(self: "CastSelf") -> "_1747.PressurePerUnitTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1747

        return self.__parent__._cast(_1747.PressurePerUnitTime)

    @property
    def pressure_small(self: "CastSelf") -> "_1748.PressureSmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1748

        return self.__parent__._cast(_1748.PressureSmall)

    @property
    def pressure_velocity_product(self: "CastSelf") -> "_1749.PressureVelocityProduct":
        from mastapy._private.utility.units_and_measurements.measurements import _1749

        return self.__parent__._cast(_1749.PressureVelocityProduct)

    @property
    def pressure_viscosity_coefficient(
        self: "CastSelf",
    ) -> "_1750.PressureViscosityCoefficient":
        from mastapy._private.utility.units_and_measurements.measurements import _1750

        return self.__parent__._cast(_1750.PressureViscosityCoefficient)

    @property
    def price(self: "CastSelf") -> "_1751.Price":
        from mastapy._private.utility.units_and_measurements.measurements import _1751

        return self.__parent__._cast(_1751.Price)

    @property
    def price_per_unit_mass(self: "CastSelf") -> "_1752.PricePerUnitMass":
        from mastapy._private.utility.units_and_measurements.measurements import _1752

        return self.__parent__._cast(_1752.PricePerUnitMass)

    @property
    def quadratic_angular_damping(self: "CastSelf") -> "_1753.QuadraticAngularDamping":
        from mastapy._private.utility.units_and_measurements.measurements import _1753

        return self.__parent__._cast(_1753.QuadraticAngularDamping)

    @property
    def quadratic_drag(self: "CastSelf") -> "_1754.QuadraticDrag":
        from mastapy._private.utility.units_and_measurements.measurements import _1754

        return self.__parent__._cast(_1754.QuadraticDrag)

    @property
    def rescaled_measurement(self: "CastSelf") -> "_1755.RescaledMeasurement":
        from mastapy._private.utility.units_and_measurements.measurements import _1755

        return self.__parent__._cast(_1755.RescaledMeasurement)

    @property
    def rotatum(self: "CastSelf") -> "_1756.Rotatum":
        from mastapy._private.utility.units_and_measurements.measurements import _1756

        return self.__parent__._cast(_1756.Rotatum)

    @property
    def safety_factor(self: "CastSelf") -> "_1757.SafetyFactor":
        from mastapy._private.utility.units_and_measurements.measurements import _1757

        return self.__parent__._cast(_1757.SafetyFactor)

    @property
    def specific_acoustic_impedance(
        self: "CastSelf",
    ) -> "_1758.SpecificAcousticImpedance":
        from mastapy._private.utility.units_and_measurements.measurements import _1758

        return self.__parent__._cast(_1758.SpecificAcousticImpedance)

    @property
    def specific_heat(self: "CastSelf") -> "_1759.SpecificHeat":
        from mastapy._private.utility.units_and_measurements.measurements import _1759

        return self.__parent__._cast(_1759.SpecificHeat)

    @property
    def square_root_of_unit_force_per_unit_area(
        self: "CastSelf",
    ) -> "_1760.SquareRootOfUnitForcePerUnitArea":
        from mastapy._private.utility.units_and_measurements.measurements import _1760

        return self.__parent__._cast(_1760.SquareRootOfUnitForcePerUnitArea)

    @property
    def stiffness_per_unit_face_width(
        self: "CastSelf",
    ) -> "_1761.StiffnessPerUnitFaceWidth":
        from mastapy._private.utility.units_and_measurements.measurements import _1761

        return self.__parent__._cast(_1761.StiffnessPerUnitFaceWidth)

    @property
    def stress(self: "CastSelf") -> "_1762.Stress":
        from mastapy._private.utility.units_and_measurements.measurements import _1762

        return self.__parent__._cast(_1762.Stress)

    @property
    def temperature(self: "CastSelf") -> "_1763.Temperature":
        from mastapy._private.utility.units_and_measurements.measurements import _1763

        return self.__parent__._cast(_1763.Temperature)

    @property
    def temperature_difference(self: "CastSelf") -> "_1764.TemperatureDifference":
        from mastapy._private.utility.units_and_measurements.measurements import _1764

        return self.__parent__._cast(_1764.TemperatureDifference)

    @property
    def temperature_per_unit_time(self: "CastSelf") -> "_1765.TemperaturePerUnitTime":
        from mastapy._private.utility.units_and_measurements.measurements import _1765

        return self.__parent__._cast(_1765.TemperaturePerUnitTime)

    @property
    def text(self: "CastSelf") -> "_1766.Text":
        from mastapy._private.utility.units_and_measurements.measurements import _1766

        return self.__parent__._cast(_1766.Text)

    @property
    def thermal_contact_coefficient(
        self: "CastSelf",
    ) -> "_1767.ThermalContactCoefficient":
        from mastapy._private.utility.units_and_measurements.measurements import _1767

        return self.__parent__._cast(_1767.ThermalContactCoefficient)

    @property
    def thermal_expansion_coefficient(
        self: "CastSelf",
    ) -> "_1768.ThermalExpansionCoefficient":
        from mastapy._private.utility.units_and_measurements.measurements import _1768

        return self.__parent__._cast(_1768.ThermalExpansionCoefficient)

    @property
    def thermo_elastic_factor(self: "CastSelf") -> "_1769.ThermoElasticFactor":
        from mastapy._private.utility.units_and_measurements.measurements import _1769

        return self.__parent__._cast(_1769.ThermoElasticFactor)

    @property
    def time(self: "CastSelf") -> "_1770.Time":
        from mastapy._private.utility.units_and_measurements.measurements import _1770

        return self.__parent__._cast(_1770.Time)

    @property
    def time_short(self: "CastSelf") -> "_1771.TimeShort":
        from mastapy._private.utility.units_and_measurements.measurements import _1771

        return self.__parent__._cast(_1771.TimeShort)

    @property
    def time_very_short(self: "CastSelf") -> "_1772.TimeVeryShort":
        from mastapy._private.utility.units_and_measurements.measurements import _1772

        return self.__parent__._cast(_1772.TimeVeryShort)

    @property
    def torque(self: "CastSelf") -> "_1773.Torque":
        from mastapy._private.utility.units_and_measurements.measurements import _1773

        return self.__parent__._cast(_1773.Torque)

    @property
    def torque_converter_inverse_k(self: "CastSelf") -> "_1774.TorqueConverterInverseK":
        from mastapy._private.utility.units_and_measurements.measurements import _1774

        return self.__parent__._cast(_1774.TorqueConverterInverseK)

    @property
    def torque_converter_k(self: "CastSelf") -> "_1775.TorqueConverterK":
        from mastapy._private.utility.units_and_measurements.measurements import _1775

        return self.__parent__._cast(_1775.TorqueConverterK)

    @property
    def torque_per_current(self: "CastSelf") -> "_1776.TorquePerCurrent":
        from mastapy._private.utility.units_and_measurements.measurements import _1776

        return self.__parent__._cast(_1776.TorquePerCurrent)

    @property
    def torque_per_square_root_of_power(
        self: "CastSelf",
    ) -> "_1777.TorquePerSquareRootOfPower":
        from mastapy._private.utility.units_and_measurements.measurements import _1777

        return self.__parent__._cast(_1777.TorquePerSquareRootOfPower)

    @property
    def torque_per_unit_temperature(
        self: "CastSelf",
    ) -> "_1778.TorquePerUnitTemperature":
        from mastapy._private.utility.units_and_measurements.measurements import _1778

        return self.__parent__._cast(_1778.TorquePerUnitTemperature)

    @property
    def velocity(self: "CastSelf") -> "_1779.Velocity":
        from mastapy._private.utility.units_and_measurements.measurements import _1779

        return self.__parent__._cast(_1779.Velocity)

    @property
    def velocity_small(self: "CastSelf") -> "_1780.VelocitySmall":
        from mastapy._private.utility.units_and_measurements.measurements import _1780

        return self.__parent__._cast(_1780.VelocitySmall)

    @property
    def viscosity(self: "CastSelf") -> "_1781.Viscosity":
        from mastapy._private.utility.units_and_measurements.measurements import _1781

        return self.__parent__._cast(_1781.Viscosity)

    @property
    def voltage(self: "CastSelf") -> "_1782.Voltage":
        from mastapy._private.utility.units_and_measurements.measurements import _1782

        return self.__parent__._cast(_1782.Voltage)

    @property
    def voltage_per_angular_velocity(
        self: "CastSelf",
    ) -> "_1783.VoltagePerAngularVelocity":
        from mastapy._private.utility.units_and_measurements.measurements import _1783

        return self.__parent__._cast(_1783.VoltagePerAngularVelocity)

    @property
    def volume(self: "CastSelf") -> "_1784.Volume":
        from mastapy._private.utility.units_and_measurements.measurements import _1784

        return self.__parent__._cast(_1784.Volume)

    @property
    def wear_coefficient(self: "CastSelf") -> "_1785.WearCoefficient":
        from mastapy._private.utility.units_and_measurements.measurements import _1785

        return self.__parent__._cast(_1785.WearCoefficient)

    @property
    def yank(self: "CastSelf") -> "_1786.Yank":
        from mastapy._private.utility.units_and_measurements.measurements import _1786

        return self.__parent__._cast(_1786.Yank)

    @property
    def measurement_base(self: "CastSelf") -> "MeasurementBase":
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
class MeasurementBase(_0.APIBase):
    """MeasurementBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MEASUREMENT_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def absolute_tolerance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AbsoluteTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @absolute_tolerance.setter
    @enforce_parameter_types
    def absolute_tolerance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AbsoluteTolerance = value

    @property
    def default_unit(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy._private.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.DefaultUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @default_unit.setter
    @enforce_parameter_types
    def default_unit(self: "Self", value: "_1657.Unit") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DefaultUnit = value

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def percentage_tolerance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PercentageTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @percentage_tolerance.setter
    @enforce_parameter_types
    def percentage_tolerance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PercentageTolerance = value

    @property
    def rounding_digits(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.RoundingDigits

        if temp is None:
            return 0

        return temp

    @rounding_digits.setter
    @enforce_parameter_types
    def rounding_digits(self: "Self", value: "int") -> None:
        self.wrapped.RoundingDigits = int(value) if value is not None else 0

    @property
    def rounding_method(self: "Self") -> "_1645.RoundingMethods":
        """mastapy._private.utility.RoundingMethods"""
        temp = self.wrapped.RoundingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Utility.RoundingMethods")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.utility._1645", "RoundingMethods"
        )(value)

    @rounding_method.setter
    @enforce_parameter_types
    def rounding_method(self: "Self", value: "_1645.RoundingMethods") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Utility.RoundingMethods")
        self.wrapped.RoundingMethod = value

    @property
    def current_unit(self: "Self") -> "_1657.Unit":
        """mastapy._private.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentUnit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_units(self: "Self") -> "List[_1657.Unit]":
        """List[mastapy._private.utility.units_and_measurements.Unit]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableUnits

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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

    @property
    def cast_to(self: "Self") -> "_Cast_MeasurementBase":
        """Cast to another type.

        Returns:
            _Cast_MeasurementBase
        """
        return _Cast_MeasurementBase(self)
