# coding: utf-8
from __future__ import division

import factor_ls
import raster


# Resolucion de celda
resolucion = 5

# Erosion laminar
m = 0.4
n = 1

# Calculo de capas necesarias
raster.calcular_aspect('fill_mde.tif', 'aspect.tif')
raster.calcular_slope('fill_mde.tif', 'slope.tif')

# Lectura de las capas de entrada
aspect, perfil_aspect = raster.cargar_capa('aspect.tif')
slope, perfil_slope = raster.cargar_capa('slope.tif')
flowacc, perfil_flowacc = raster.cargar_capa('flowacc.tif')

# Calculo de LS
a_e = factor_ls.calculo_a_e(resolucion, flowacc, aspect)
sin_theta = factor_ls.calculo_sin_theta(slope)

ls = factor_ls.calculo_ls(m, n, a_e, sin_theta)

# Guardar resultado a disco
raster.guardar_capa(ls, 'capa_ls.tif', perfil_aspect)

# Pintar resultado por pantalla
capa_ls, perfil_ls = raster.cargar_capa('capa_ls.tif')
raster.pintar_capa(aspect)
