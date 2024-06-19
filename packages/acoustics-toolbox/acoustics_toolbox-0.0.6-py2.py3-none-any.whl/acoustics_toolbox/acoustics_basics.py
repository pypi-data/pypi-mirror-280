"""
Ce module permet de manipuler les grandeurs acoustiques : calcul de 
dB, pondérations, bandes de fréquences, ... Il s'agit de fonctions simples, 
utilisables dans n'importe quel contexte.
"""

import numpy as np
import numpy.typing as npt


# -------------------- LINEAR <-> dB CONVERSIONS --------------------


def convert_linear_to_db(
    linear_amplitude: npt.ArrayLike,
) -> npt.ArrayLike:
    """Permet de convertir une amplitude linéaire en niveau dB.
    Attention, l'amplitude donnée en entrée doit être non nulle.

    :param linear_amplitude: amplitude linéaire
    :type linear_amplitude: npt.ArrayLike
    :return: amplitude en dB
    :rtype: npt.ArrayLike
    """
    return 10 * np.log10(np.asarray(linear_amplitude) ** 2)


def convert_db_to_linear(log_amplitude: npt.ArrayLike) -> npt.ArrayLike:
    """Permet de convertir un niveau dB en amplitude linéaire.

    :param log_amplitude: amplitude en dB
    :type log_amplitude: npt.ArrayLike
    :return: amplitude linéaire
    :rtype: npt.ArrayLike
    """
    return np.sqrt(10 ** (np.asarray(log_amplitude) / 10))


# -------------------- A-WEIGHTING FUNCTION --------------------


def calculate_a_weighting_linear(frequency: npt.ArrayLike) -> npt.ArrayLike:
    """Calcule la pondération A en échelle linéaire, d'après Wikipedia :
    <https://en.wikipedia.org/wiki/A-weighting>

    :param frequency: fréquence pour laquelle on souhaite calculer la pondération
    associée
    :type frequency: npt.ArrayLike
    :return: pondération A en échelle linéaire associée à la fréquence donnée en
    entrée
    :rtype: npt.ArrayLike
    """
    frequency = np.asfarray(frequency)  # Indispensable d'avoir un array de float
    # Le calcul suivant donne des nombres dépassant la mémoire disponible en int
    return (
        (12194**2 * frequency**4)
        / (frequency**2 + 20.6**2)
        / np.sqrt((frequency**2 + 107.7**2) * (frequency**2 + 737.9**2))
        / (frequency**2 + 12194**2)
    )


def calculate_a_weighting_db(frequency: npt.ArrayLike) -> npt.ArrayLike:
    """Calcule la pondération A en dB, d'après Wikipedia :
    <https://en.wikipedia.org/wiki/A-weighting>. Cette fonction utilise la fonction
    `calculate_a_weighting_linear` du module.

    :param frequency: fréquence pour laquelle on souhaite calculer la pondération
    associée
    :type frequency: npt.ArrayLike
    :return: pondération A en dB associée à la fréquence donnée en
    entrée
    :rtype: npt.ArrayLike
    """
    return convert_linear_to_db(
        calculate_a_weighting_linear(frequency)
    ) - convert_linear_to_db(calculate_a_weighting_linear(1000))


# -------------------- dB <-> dB(A) CONVERSIONS --------------------


def convert_db_to_dba(
    frequency: npt.ArrayLike, db_sound_level: npt.ArrayLike
) -> npt.ArrayLike:
    """Permet de convertir un niveau sonore en dB en un niveau sonore en
    dB(A). Il est donc nécessaire d'avoir en entrée la fréquence associée
    au niveau sonore afin d'appliquer la bonne pondération. Cette pondération
    est calculée par le biais de la fonction `calculate_a_weighting_db` du
    module.

    :param frequency: fréquence associée au niveau sonore
    :type frequency: npt.ArrayLike
    :param db_sound_level: niveau sonore en dB, sans pondération
    :type db_sound_level: npt.ArrayLike
    :return: niveau sonore pondéré en dB(A)
    :rtype: npt.ArrayLike
    """
    return db_sound_level + calculate_a_weighting_db(frequency)


def convert_dba_to_db(
    frequency: npt.ArrayLike, dba_sound_level: npt.ArrayLike
) -> npt.ArrayLike:
    """Permet de convertir un niveau sonore en dB(A) en un niveau sonore en
    dB. Il est donc nécessaire d'avoir en entrée la fréquence associée
    au niveau sonore afin d'appliquer la bonne pondération inverse.
    Cette pondération est calculée par le biais de la fonction
    `calculate_a_weighting_db` du module.

    :param frequency: fréquence associée au niveau sonore
    :type frequency: npt.ArrayLike
    :param dba_sound_level: niveau sonore pondéré en dB(A)
    :type dba_sound_level: npt.ArrayLike
    :return: niveau sonore en dB, sans pondération
    :rtype: npt.ArrayLike
    """
    return dba_sound_level - calculate_a_weighting_db(frequency)


# -------------------- dB SUM --------------------


def sum_db(
    sound_levels: npt.ArrayLike,
) -> float:
    """Permet de sommer plusieurs niveaux en dB.

    :param sound_levels: niveaux sonores en dB. Ils peuvent être pondérés.
    :type sound_levels: npt.ArrayLike
    :return: niveau total résultant de la somme des niveaux sonores donnés en entrée.
    :rtype: float
    """
    return 10 * np.log10(np.sum(10 ** (np.asarray(sound_levels) / 10)))


# -------------------- FREQUENCY BANDS --------------------


def get_frequency_bands(octave_ratio: int, length_factor: int = 20) -> np.ndarray:
    """Permet de générer les fréquences centrales normalisées associées au ratio d'octave
    donné. Par exemple, un ratio de 1 renvoit les fréquences centrales en bandes d'octave,
    un ratio de 3 en bandes de tiers d'octave.

    :param octave_ratio: le choix du découpage des bandes de fréquence, en
    1/octave_ratio d'octave.
    :type octave_ratio: int
    :param length_factor: le facteur permettant de controler le nombre de fréquences
    retournées, defaults to 20
    :type length_factor: int, optional
    :return: un array des fréquences centrales associées au ratio d'octave choisi,
    de longeur 2 * octave_ratio * length_factor
    :rtype: np.ndarray
    """
    return 1000 * (10 ** (3 / 10 / octave_ratio)) ** np.arange(
        -length_factor * octave_ratio, length_factor * octave_ratio, dtype=float
    )


def map_to_nearest_frequency_band(
    frequency: npt.ArrayLike, octave_ratio: int = 3
) -> npt.ArrayLike:
    """Permet d'associer une fréquence donnée à la fréquence centrale la 
    plus proche.Utilise la fonction get_frequency_bands du module.

    :param frequency: la fréquence que l'on souhaite "normaliser"
    :type frequency: npt.ArrayLike
    :param octave_ratio: le découpage qu'on utilise, en bande de 1/octave_ratio 
    d'octave, defaults to 3
    :type octave_ratio: int, optional
    :return: la fréquence strandardisée associée
    :rtype: npt.ArrayLike
    """
    if np.isscalar(frequency): # Obligatoire pour fonctionnement avec scalaire
        frequency = np.array([frequency])
    frequency_bands = get_frequency_bands(octave_ratio)
    corresponding_index = np.argmin(
        np.abs(np.asarray(frequency)[:, np.newaxis] - frequency_bands), axis=1
    )
    return frequency_bands[corresponding_index]
