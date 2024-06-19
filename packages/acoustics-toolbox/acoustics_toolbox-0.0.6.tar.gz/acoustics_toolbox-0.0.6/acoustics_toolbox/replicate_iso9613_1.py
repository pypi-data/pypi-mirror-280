"""
Not empty
"""

import dataclasses
import numpy as np
import numpy.typing as npt


# --------------- CONSTANTS SETUP ---------------


@dataclasses.dataclass
class ThermodynamicsConstants:
    """_summary_

    :param object: _description_
    :type object: _type_
    """

    atmospheric_pressure_ref: float
    atmospheric_pressure: float
    isothermal_temperature_triple_point: float
    temperature_ref: float


# Constantes thermodynamiques par défaut, à modifier ici si besoin
THERMODYNAMICS_CONSTANTS = ThermodynamicsConstants(
    atmospheric_pressure_ref=101.325,
    atmospheric_pressure=101.325,
    isothermal_temperature_triple_point=273.16,
    temperature_ref=293.15,
)


# --------------- HUMIDITY CONVERSION ---------------


def calculate_saturated_vapor_pressure(
    temperature: npt.ArrayLike,
    thermodynamics_constants: object = THERMODYNAMICS_CONSTANTS,
) -> npt.ArrayLike:
    """_summary_

    :param temperature: _description_
    :type temperature: npt.ArrayLike
    :param isothermal_temperature_triple_point: _description_,
    defaults to ISOTHERMAL_TEMPERATURE_TRIPLE_POINT
    :type isothermal_temperature_triple_point: float, optional
    :param atmospheric_pressure_ref: _description_, defaults to ATMOSPHERIC_PRESSURE_REF
    :type atmospheric_pressure_ref: float, optional
    :return: _description_
    :rtype: npt.ArrayLike
    """
    return thermodynamics_constants.atmospheric_pressure_ref * 10 ** (
        -6.8346
        * (
            thermodynamics_constants.isothermal_temperature_triple_point
            / np.asarray(temperature)
        )
        ** 1.261
        + 4.6151
    )


def calculate_molar_fraction_of_water_vapor(
    humidity: npt.ArrayLike,
    saturated_vapor_pressure: npt.ArrayLike,
    thermodynamics_constants: object = THERMODYNAMICS_CONSTANTS,
) -> npt.ArrayLike:
    """_summary_

    :param humidity: _description_
    :type humidity: npt.ArrayLike
    :param saturated_vapor_pressure: _description_
    :type saturated_vapor_pressure: npt.ArrayLike
    :param atmospheric_pressure: _description_, defaults to atmospheric_pressure
    :type atmospheric_pressure: float, optional
    :param atmospheric_pressure_ref: _description_, defaults to atmospheric_pressure_ref
    :type atmospheric_pressure_ref: float, optional
    :return: _description_
    :rtype: npt.ArrayLike
    """
    return (
        np.asarray(humidity)
        * (
            np.asarray(saturated_vapor_pressure)
            / thermodynamics_constants.atmospheric_pressure_ref
        )
        * (
            thermodynamics_constants.atmospheric_pressure
            / thermodynamics_constants.atmospheric_pressure_ref
        )
    )


# --------------- RELAXATION FREQUENCIES ---------------


def calculate_oxygen_relaxation_frequency(
    molar_fraction_of_water_vapor: npt.ArrayLike,
    thermodynamics_constants: object = THERMODYNAMICS_CONSTANTS,
) -> npt.ArrayLike:
    """_summary_

    :param molar_fraction_of_water_vapor: _description_
    :type molar_fraction_of_water_vapor: npt.ArrayLike
    :param atmospheric_pressure: _description_, defaults to atmospheric_pressure
    :type atmospheric_pressure: float, optional
    :param atmospheric_pressure_ref: _description_, defaults to atmospheric_pressure_ref
    :type atmospheric_pressure_ref: float, optional
    :return: _description_
    :rtype: npt.ArrayLike
    """
    return (
        thermodynamics_constants.atmospheric_pressure
        / thermodynamics_constants.atmospheric_pressure_ref
    ) * (
        24
        + 4.04
        * 10**4
        * np.asarray(molar_fraction_of_water_vapor)
        * (
            (0.02 + np.asarray(molar_fraction_of_water_vapor))
            / (0.391 + np.asarray(molar_fraction_of_water_vapor))
        )
    )


def calculate_nitrogen_relaxation_frequency(
    temperature: npt.ArrayLike,
    molar_fraction_of_water_vapor: npt.ArrayLike,
    thermodynamics_constants: object = THERMODYNAMICS_CONSTANTS,
) -> npt.ArrayLike:
    """_summary_

    :param temperature: _description_
    :type temperature: npt.ArrayLike
    :param molar_fraction_of_water_vapor: _description_
    :type molar_fraction_of_water_vapor: npt.ArrayLike
    :param atmospheric_pressure: _description_, defaults to atmospheric_pressure
    :type atmospheric_pressure: float, optional
    :param temperature_ref: _description_, defaults to temperature_ref
    :type temperature_ref: float, optional
    :param atmospheric_pressure_ref: _description_, defaults to atmospheric_pressure_ref
    :type atmospheric_pressure_ref: float, optional
    :return: _description_
    :rtype: npt.ArrayLike
    """
    return (
        (
            thermodynamics_constants.atmospheric_pressure
            / thermodynamics_constants.atmospheric_pressure_ref
        )
        * (np.asarray(temperature) / thermodynamics_constants.temperature_ref)
        ** (-1 / 2)
        * (
            9
            + 280
            * np.asarray(molar_fraction_of_water_vapor)
            * np.exp(
                -4.170
                * (
                    (np.asarray(temperature) / thermodynamics_constants.temperature_ref)
                    ** (-1 / 3)
                    - 1
                )
            )
        )
    )


# --------------- ABSORPTION CALCULATION ---------------


def calculate_absorption_coeff(
    frequency: npt.ArrayLike,
    temperature: npt.ArrayLike,
    oxygen_relaxation_frequency: npt.ArrayLike,
    nitrogen_relaxation_frequency: npt.ArrayLike,
    thermodynamics_constants: object = THERMODYNAMICS_CONSTANTS,
) -> npt.ArrayLike:
    """_summary_

    :param frequency: _description_
    :type frequency: npt.ArrayLike
    :param temperature: _description_
    :type temperature: npt.ArrayLike
    :param oxygen_relaxation_frequency: _description_
    :type oxygen_relaxation_frequency: npt.ArrayLike
    :param nitrogen_relaxation_frequency: _description_
    :type nitrogen_relaxation_frequency: npt.ArrayLike
    :param atmospheric_pressure: _description_, defaults to atmospheric_pressure
    :type atmospheric_pressure: float, optional
    :param temperature_ref: _description_, defaults to temperature_ref
    :type temperature_ref: float, optional
    :param atmospheric_pressure_ref: _description_, defaults to atmospheric_pressure_ref
    :type atmospheric_pressure_ref: float, optional
    :return: _description_
    :rtype: npt.ArrayLike
    """
    return (
        8.686
        * np.asarray(frequency) ** 2
        * (
            (
                1.84
                * 10 ** (-11)
                * (
                    thermodynamics_constants.atmospheric_pressure
                    / thermodynamics_constants.atmospheric_pressure_ref
                )
                ** (-1)
                * (np.asarray(temperature) / thermodynamics_constants.temperature_ref)
                ** (1 / 2)
            )
            + (np.asarray(temperature) / thermodynamics_constants.temperature_ref)
            ** (-5 / 2)
            * (
                0.01275
                * (np.exp(-2239.1 / np.asarray(temperature)))
                * (
                    oxygen_relaxation_frequency
                    + (np.asarray(frequency) ** 2 / oxygen_relaxation_frequency)
                )
                ** (-1)
                + 0.1068
                * (np.exp(-3352 / np.asarray(temperature)))
                * (
                    nitrogen_relaxation_frequency
                    + (np.asarray(frequency) ** 2 / nitrogen_relaxation_frequency)
                )
                ** (-1)
            )
        )
    )


def calculate_atmospheric_attenuation(
    source_receptor_distance: npt.ArrayLike, absorption_coeff: npt.ArrayLike
) -> npt.ArrayLike:
    """_summary_

    :param distance: _description_
    :type distance: npt.ArrayLike
    :param absorption_coeff: _description_
    :type absorption_coeff: npt.ArrayLike
    :return: _description_
    :rtype: npt.ArrayLike
    """
    return absorption_coeff * np.asarray(source_receptor_distance)


# --------------- ALL-IN-ONE FUNCTION ---------------


def compute_atmospheric_attenuation(
    frequency: npt.ArrayLike,
    source_receptor_distance: npt.ArrayLike,
    temperature: npt.ArrayLike,
    humdity: npt.ArrayLike,
    thermodynamics_constants: object = THERMODYNAMICS_CONSTANTS,
) -> npt.ArrayLike:
    """_summary_

    :param frequency: _description_
    :type frequency: npt.ArrayLike
    :param distance: _description_
    :type distance: npt.ArrayLike
    :param temperature: _description_
    :type temperature: npt.ArrayLike
    :param humdity: _description_
    :type humdity: npt.ArrayLike
    :return: _description_
    :rtype: npt.ArrayLike
    """
    temperature = temperature + 273.15 # Conversion en Kelvin
    saturated_vapor_pressure = calculate_saturated_vapor_pressure(
        temperature, thermodynamics_constants=thermodynamics_constants
    )
    molar_fraction_of_water_vapor = calculate_molar_fraction_of_water_vapor(
        humdity,
        saturated_vapor_pressure,
        thermodynamics_constants=thermodynamics_constants,
    )
    oxygen_relaxation_frequency = calculate_oxygen_relaxation_frequency(
        molar_fraction_of_water_vapor, thermodynamics_constants=thermodynamics_constants
    )
    nitrogen_relaxation_frequency = calculate_nitrogen_relaxation_frequency(
        temperature,
        molar_fraction_of_water_vapor,
        thermodynamics_constants=thermodynamics_constants,
    )
    absorption_coeff = calculate_absorption_coeff(
        frequency,
        temperature,
        oxygen_relaxation_frequency,
        nitrogen_relaxation_frequency,
    )
    return calculate_atmospheric_attenuation(source_receptor_distance, absorption_coeff)
