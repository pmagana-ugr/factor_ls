import matplotlib.pyplot as plt
from osgeo import gdal
import rasterio


def calcular_slope(mde, slope):
    """Calcula la pendiente a partir del modelo digital de elevaciones

    Args:
        mde: nombre del fichero con el modelo digital de elevaciones
        slope: nombre del fichero de salida con la pendiente
    """
    gdal.DEMProcessing(slope, mde, 'slope')


def calcular_aspect(mde, aspect):
    """Calcula la orientacion a partir del modelo digital de elevaciones

    Args:
        mde: nombre del fichero con el modelo digital de elevaciones
        aspect: nombre del fichero de salida con la orientacion
    """
    gdal.DEMProcessing(aspect, mde, 'aspect')


def cargar_capa(raster, id_capa=1):
    """Carga los datos contenido en un raster

    Args:
        raster: nombre del archivo con el raster de lectura
        id_capa: identificador de la capa

    Returns:
        Datos del raster y perfil del raster
    """
    contenido_raster = rasterio.open(raster)
    capa = contenido_raster.read(id_capa, masked=True)
    perfil = contenido_raster.profile
    contenido_raster.close()

    return capa, perfil


def guardar_capa(datos, raster, perfil):
    """Guarda los datos en un fichero raster

    Args:
        datos: datos del raster
        raster: nombre del fichero para el raster
        perfil: perfil del raster
    """
    capa = rasterio.open(raster, 'w', **perfil)
    capa.write(datos, 1)
    capa.close()


def pintar_capa(raster):
    """Pinta los datos del raster en una ventana

    Args:
        raster: datos del raster
    """
    plt.imshow(raster, cmap='gist_earth')
    plt.show()
