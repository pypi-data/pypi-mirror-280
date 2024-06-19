"""
Ce module donne divers outils pouvant s'avérer utiles en propagation extérieur. 
Il permet par exemple de manipuler les conversions de température, de résistance au 
passage de l'air, de vitesses de vent.
"""

import numpy as np
import numpy.typing as npt


# -------------------- GEOMETRY --------------------


def calculate_source_receptor_distance(
    source_height: npt.ArrayLike,
    receptor_height: npt.ArrayLike,
    horizontal_distance: npt.ArrayLike,
    source_altitude: npt.ArrayLike = 0,
    receptor_altitude: npt.ArrayLike = 0,
) -> npt.ArrayLike:
    return np.sqrt(
        (
            (np.asarray(source_height) + np.asarray(source_altitude))
            - (np.asarray(receptor_height) + np.asarray(receptor_altitude))
        )
        ** 2
        + np.asarray(horizontal_distance) ** 2
    )


# -------------------- CELSIUS <-> KELVIN CONVERSIONS --------------------


def convert_celsius_to_kelvin(temperature_celsius: npt.ArrayLike) -> npt.ArrayLike:
    return np.asarray(temperature_celsius) + 273.15


def convert_kelvin_to_celsius(temperature_kelvin: npt.ArrayLike) -> npt.ArrayLike:
    return np.asarray(temperature_kelvin) - 273.15


# -------------------- FLOW RESISTTIVITY <-> G CONVERSION --------------------


def convert_flow_resistivity_to_ground_factor(
    flow_resistivity: npt.ArrayLike,
) -> npt.ArrayLike:
    flow_resistivity = np.asarray(flow_resistivity)
    return np.select(
        [
            flow_resistivity <= 200,
            (flow_resistivity > 200) & (flow_resistivity <= 800),
            (flow_resistivity > 800) & (flow_resistivity <= 1700),
            (flow_resistivity > 1700) & (flow_resistivity <= 2300),
        ],
        [1.0, 0.7, 0.5, 0.3],
        0.0,
    )


def convert_ground_factor_to_flow_resistivity(
    ground_factor: npt.ArrayLike,
) -> npt.ArrayLike:
    ground_factor = np.asarray(ground_factor)
    return np.select(
        [
            ground_factor > 0.8,
            (ground_factor <= 0.8) & (ground_factor > 0.6),
            (ground_factor <= 0.6) & (ground_factor > 0.4),
            (ground_factor <= 0.4) & (ground_factor > 0.2),
        ],
        [12.5, 500, 1000, 2000],
        200000,
    )


# -------------------- WIND SPEED CONVERSIONS --------------------


def convert_to_10m_wind_speed(
    known_wind_speed: npt.ArrayLike, height: npt.ArrayLike
) -> npt.ArrayLike:
    return np.asarray(known_wind_speed) * (
        np.log(10 / 0.05) / np.log(np.asarray(height) / 0.05)
    )


# -------------------- DISTANCE ROUNDING --------------------


def adjust_distances(distance: npt.ArrayLike, precision: float = 5.0) -> npt.ArrayLike:
    distance = np.asarray(distance)
    distance[~np.isnan(distance)] = (
        np.round(
            distance[~np.isnan(distance)] / precision,
            decimals=0,
        )
        * precision
    )
    return distance
