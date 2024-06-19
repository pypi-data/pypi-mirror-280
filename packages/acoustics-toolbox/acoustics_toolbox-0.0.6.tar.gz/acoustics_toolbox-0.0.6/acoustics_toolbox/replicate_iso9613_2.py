"""
Not empty
"""

import numpy as np
import numpy.typing as npt

from .replicate_iso9613_1 import compute_atmospheric_attenuation


# --------------- CONSTANTS SETUP ---------------


STANDARD_FREQUENCIES = 1000 * (10 ** (3 / 10 / 3)) ** np.arange(
    -5 * 3 + 2, 4 * 3 - 1, 1, dtype=float
)


# --------------- GEOMETRIC ATTENUATION ---------------


def compute_geometric_attenuation(
    source_receptor_distance: npt.ArrayLike, distance_ref: float = 1.0
) -> npt.ArrayLike:
    """Calculates the attenuation due to geometric divergence
    ISO 9613-2, equation (7)

    Args:
        distance (float): [m]
        distance_ref (float, optional): [m]. Defaults to 1.0.

    Returns:
        float: [dB] geometric attenuation
    """
    return 20 * np.log10(np.asarray(source_receptor_distance) / distance_ref) + 11


# -------------------- GROUND ATTENUATION --------------------


def calculate_ground_functions(
    frequency: npt.ArrayLike, horizontal_distance: npt.ArrayLike, height: npt.ArrayLike
) -> npt.ArrayLike:
    frequency = np.asarray(frequency)
    horizontal_distance = np.asarray(horizontal_distance)
    height = np.asarray(height)
    return np.select(
        [
            (frequency >= STANDARD_FREQUENCIES[3])
            & (frequency <= STANDARD_FREQUENCIES[5]),
            (frequency >= STANDARD_FREQUENCIES[6])
            & (frequency <= STANDARD_FREQUENCIES[8]),
            (frequency >= STANDARD_FREQUENCIES[9])
            & (frequency <= STANDARD_FREQUENCIES[11]),
            (frequency >= STANDARD_FREQUENCIES[12])
            & (frequency <= STANDARD_FREQUENCIES[14]),
        ],
        [
            1.5
            + 3
            * np.exp(-0.12 * (height - 5) ** 2)
            * (1 - np.exp(-horizontal_distance / 50))
            + 5.7
            * np.exp(-0.09 * height**2)
            * (1 - np.exp(-2.8 * 1e-6 * horizontal_distance**2)),
            1.5
            + 8.6
            * np.exp(-0.09 * height**2)
            * (1 - np.exp(-horizontal_distance / 50)),
            1.5
            + 14.0
            * np.exp(-0.46 * height**2)
            * (1 - np.exp(-horizontal_distance / 50)),
            1.5
            + 5.0
            * np.exp(-0.9 * height**2)
            * (1 - np.exp(-horizontal_distance / 50)),
        ],
        0,
    )


def calculate_ground__attenuation_source_or_receptor(
    frequency: npt.ArrayLike,
    ground_functions: npt.ArrayLike,
    ground_factor: npt.ArrayLike,
) -> npt.ArrayLike:
    frequency = np.asarray(frequency)
    ground_functions = np.asarray(ground_functions)
    ground_factor = np.asarray(ground_factor)
    return np.select(
        [frequency <= STANDARD_FREQUENCIES[2], frequency >= STANDARD_FREQUENCIES[15]],
        [-1.5, -1.5 * (1 - ground_factor)],
        -1.5 + ground_factor * ground_functions,
    )


def calculate_ground_attenuation_middle(
    frequency: npt.ArrayLike,
    horizontal_distance: npt.ArrayLike,
    source_height: npt.ArrayLike,
    receptor_height: npt.ArrayLike,
    ground_factor: npt.ArrayLike,
) -> npt.ArrayLike:
    frequency = np.asarray(frequency)
    horizontal_distance = np.asarray(horizontal_distance)
    source_height = np.asarray(source_height)
    receptor_height = np.asarray(receptor_height)
    ground_factor = np.asarray(ground_factor)
    q_coeff = np.where(
        horizontal_distance > 30 * (source_height + receptor_height),
        1 - (30 * (source_height + receptor_height)) / horizontal_distance,
        0,
    )
    return np.where(
        frequency >= STANDARD_FREQUENCIES[3],
        -3 * q_coeff * (1 - ground_factor),
        -3 * q_coeff,
    )


def compute_ground_attenuation(
    frequency: npt.ArrayLike,
    horizontal_distance: npt.ArrayLike,
    source_height: npt.ArrayLike,
    receptor_height: npt.ArrayLike,
    ground_factor: npt.ArrayLike,
) -> npt.ArrayLike:
    source_ground_functions = calculate_ground_functions(
        frequency,
        horizontal_distance,
        source_height,
    )
    receptor_ground_functions = calculate_ground_functions(
        frequency,
        horizontal_distance,
        receptor_height,
    )
    source_ground_attenuation = calculate_ground__attenuation_source_or_receptor(
        frequency,
        source_ground_functions,
        ground_factor,
    )
    receptor_ground_attenuation = calculate_ground__attenuation_source_or_receptor(
        frequency,
        receptor_ground_functions,
        ground_factor,
    )
    middle_ground_attenuation = calculate_ground_attenuation_middle(
        frequency,
        horizontal_distance,
        source_height,
        receptor_height,
        ground_factor,
    )
    return (
        source_ground_attenuation
        + receptor_ground_attenuation
        + middle_ground_attenuation,
    )


def compute_ground_attenuation_alternative(
    mean_height: npt.ArrayLike, distance: npt.ArrayLike
) -> npt.ArrayLike:
    ground_attenuation = 4.8 - (2 * np.asarray(mean_height) / np.asarray(distance)) * (
        17 + (300 / np.asarray(distance))
    )
    if ground_attenuation > 0:
        return ground_attenuation
    return 0


# -------------------- TOTAL ATTENUATION --------------------


def compute_total_attenuation(
    frequency: npt.ArrayLike,
    horizontal_distance: npt.ArrayLike,
    source_receptor_distance: npt.ArrayLike,
    source_height: npt.ArrayLike,
    receptor_height: npt.ArrayLike,
    ground_factor: npt.ArrayLike,
    temperature: npt.ArrayLike,
    humidity: npt.ArrayLike,
) -> npt.ArrayLike:
    # pylint: disable=too-many-arguments
    return (
        compute_geometric_attenuation(source_receptor_distance)
        + compute_ground_attenuation(
            frequency,
            horizontal_distance,
            source_height,
            receptor_height,
            ground_factor,
        )
        + compute_atmospheric_attenuation(
            frequency, source_receptor_distance, temperature, humidity
        )
    )
