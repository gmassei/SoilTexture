"""
/***************************************************************************
SoilTexture
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from SoilTextureDialog import SoilTextureDialog
import doTexture

class SoilTexture:

	def __init__(self, iface):
		# Save reference to the QGIS interface
		self.iface = iface

	def initGui(self):
		# Create action that will start plugin configuration
		self.action = QAction(QIcon(":/plugins/soiltexture/icon.png"), \
			"Soil texture", self.iface.mainWindow())
		# connect the action to the run method
		QObject.connect(self.action, SIGNAL("triggered()"), self.run)

		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu("&Soil texture", self.action)

	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu("&Soil texture",self.action)
		self.iface.removeToolBarIcon(self.action)

	# run method that performs all the real work

	def run(self):
	# create and show a configuration dialog or something similar
		dlg = doTexture.SoilTextureDialog(self.iface)
		dlg.exec_()



