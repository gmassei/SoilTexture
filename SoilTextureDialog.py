"""
/***************************************************************************
SoilTextureDialog
A QGIS plugin
Define soil texture from sand and clay raster maps
                             -------------------
begin                : 2010-11-14 
copyright            : (C) 2010 by Gianluca Massei
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

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog
from .Ui_SoilTexture import Ui_SoilTexture

class SoilTextureDialog(QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_SoilTexture()
    self.ui.setupUi(self) 

