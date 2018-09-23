"""
/***************************************************************************
SoilTexture
A QGIS plugin
Define soil texture from sand and clay raster maps
                             -------------------
begin                : 2010-11-14
copyright            : (C) 2010-2018 by Gianluca Massei
email                : g_massa@libero.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

def classFactory(iface):
  # load SoilTexture class from file SoilTexture
  from .SoilTexture import SoilTexture
  return SoilTexture(iface)
