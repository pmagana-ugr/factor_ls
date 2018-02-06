# coding: utf-8
from __future__ import division

import numpy as np


def calculo_ls(m, n, a_e, sin_theta):
    """Calcula el factor LS dentro de USLE

    Args:
        m: constante que depende del tipo de erosion
        n: constante que depende del tipo de erosion
        a_e: area especifica de captacion
        sin_theta: seno de la pendiente en grados

    Returns:
        Factor LS
    """
    ls = (m + 1) * (a_e / 22.13)**m * (sin_theta / 0.0896)**n

    return ls


def calculo_a_e(resolucion, flowacc, aspect):
    """Calcula el area especifica de captacion

    Args:
        resolucion: tamaño de celda
        flowacc: nombre del fichero raster con flow accumulation
        aspect: nombre de fichero raster con aspect

    Returns:
        Area especifica de captacion
    """
    a = calculo_a(flowacc, resolucion)
    b = calculo_b(aspect, resolucion)

    a_e = a / b

    return a_e


def calculo_a(flowacc, resolucion):
    """Calcula el area de contribucion aguas arriba

    Args:
        flowacc: nombre del fichero raster con flow accumulation
        resolucion: tamaño de celda

    Returns:
        Area de contribucion aguas arriba
    """
    a = flowacc * resolucion**2

    return a


def calculo_b(aspect, resolucion):
    """Calcula la longitud efectiva de curva de nivel

    Args:
        aspect: nombre de fichero raster con aspect
        resolucion: tamaño de celda

    Returns:
        Longitud efectiva de curva de nivel
    """
    # Conversion a radianes
    aspect_rad = aspect * np.pi/180

    sin_rad = np.sin(aspect_rad)
    cos_rad = np.cos(aspect_rad)

    # Se eliminan los valores negativos
    sin_abs = np.abs(sin_rad)
    cos_abs = np.abs(cos_rad)

    b = resolucion * (sin_abs + cos_abs)

    return b


def calculo_sin_theta(slope):
    """Calcula el seno de la pendiente

    Args:
        slope: nombre de fichero raster con slope

    Returns:
        Seno de la pendiente en grados
    """
    slope_rad = slope * np.pi/180

    sin_theta = np.sin(slope_rad)

    return sin_theta
