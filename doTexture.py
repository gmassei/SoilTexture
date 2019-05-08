
##***************************************************************************
## SoilTexture
## A QGIS plugin
## Define soil texture from sand and clay raster maps
##							 -------------------
## begin				: 2010-11-14
## copyright			: (C) 2010-2017 by Gianluca Massei
## email				: g_massa@libero.it
## **************************************************************************
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, print to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------


from __future__ import absolute_import

from builtins import zip
from builtins import str
from builtins import range


from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox # QMenu

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.PyQt import QtGui
from qgis.core import *
from qgis.gui import *

from .Ui_SoilTexture import Ui_SoilTexture

import os, sys, time
from osgeo import gdal
from osgeo import ogr
from osgeo import osr
from osgeo.gdalconst import *

import numpy as np
from matplotlib.path import Path
import fnmatch
import webbrowser

class SoilTextureDialog(QDialog, Ui_SoilTexture):

	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.btnOutput.clicked.connect(self.outFile)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
		self.btnHelp.clicked.connect(self.open_help)

		mapCanvas = self.iface.mapCanvas()
		# init dictionaries of items:
		self.rastItems = {}
		for i in range(mapCanvas.layerCount()):
			layer = mapCanvas.layer(i)
			if ( layer.type() == layer.RasterLayer ):
		# read  layers
				provider = layer.dataProvider()
				self.cmbClay.addItem(layer.source())
				self.cmbSand.addItem(layer.source())

		currentDIR = unicode(os.path.abspath( os.path.dirname(__file__)))
		listDat=[s for s in os.listdir(currentDIR) if fnmatch.fnmatch(s,'*.dat')]
		self.cmbSchema.addItems(listDat)
		#self.textEdit.append(str(currentDIR))
		print(currentDIR,listDat)
		self.textEdit.clear()

	def outFile(self):
		"Display file dialog for output texture file"
		self.lineOutput.clear()
		outName = QFileDialog.getSaveFileName(self, "Texture output file",".", "GeoTiff (*.tif)")
		print(outName[0])
		#if not outName.isEmpty():
		self.lineOutput.clear()
		self.lineOutput.insert(outName[0])
		return outName

	def readSchema(self,schema):
		"Read the rule file for texture define"
		#---------------------------------------------------------
		#   x=sand, y=clay bi-axial texture triangle
		#---------------------------------------------------------
		try:
			f1=open(schema,"r")
			numpoly=f1.readline()
			numpoly=int(numpoly)
			RuleList=[numpoly]
			for i in range(numpoly):
				texture=f1.readline().split()
				num_vert=f1.readline().split()
				sand_vert=f1.readline().split()
				clay_vert=f1.readline().split()
				TextureRule={'Texture':texture, 'Num_vert':num_vert, 'Sand_vert':sand_vert, 'Clay_vert':clay_vert,}
				RuleList.insert(i,TextureRule) #'list of roule dictionary
			legend=[line for line in f1.read().split('\n')]
			f1.close()

			for i in range(numpoly):
				RuleList[i]['Texture'][0]=int(RuleList[i]['Texture'][0])
				RuleList[i]['Num_vert'][0]=int(RuleList[i]['Num_vert'][0])
				for j in range(RuleList[i]['Num_vert'][0]):
					RuleList[i]['Clay_vert'][j]=float(RuleList[i]['Clay_vert'][j])
					RuleList[i]['Sand_vert'][j]=float(RuleList[i]['Sand_vert'][j])
			self.textEdit.clear()
			for l in legend:
				self.textEdit.append(l)
				print(l)
			return RuleList, numpoly,legend

		except:
			QMessageBox.information(None,"Exiting","File %s does not exist or is not readeable." % schema)
			return


	def ProcessRaster(self,sand,clay):
		"Register all of the GDAL drivers"
		gdal.AllRegister()
		# open the image
		clay=str(clay)
		sand=str(sand)

		imgClay = gdal.Open(clay,GA_ReadOnly)
		if imgClay is None:
			QMessageBox.information(None,"Exiting","Could not open raster %s!" % clay)

		imgSand = gdal.Open(sand,GA_ReadOnly)
		if imgSand is None:
			QMessageBox.information(None,"Exiting","Could not open raster %s!" % sand)

		# get image size
		rows = imgClay.RasterYSize
		cols = imgClay.RasterXSize
		bands = imgClay.RasterCount
		if bands >1:
			QMessageBox.information(None,"Exiting","Raster %s has %d bands!" % (clay,bands))

		# get georeference info
		transform = imgClay.GetGeoTransform()
		xOrigin = transform[0]
		yOrigin = transform[3]
		pixelWidth = transform[1]
		pixelHeight = transform[5]
		dataClay = imgClay.ReadAsArray()
		dataSand = imgSand.ReadAsArray()
		return dataClay,dataSand,rows,cols,transform


	def InsidePolygon(self,RuleList,numpoly, xS, yC):
		"Determining if a point lies in or out a polygon (texture triangle)"
		NODATA=-9999
		for p in range(numpoly):
			polygon=[]
			isInside=False
			num_vert= int(RuleList[p]['Num_vert'][0])
			texture=RuleList[p]['Texture'][0] #numeric code define texture
			sand=RuleList[p]['Sand_vert']# coord. list of texturale polugons
			clay=RuleList[p]['Clay_vert']#
			if (xS <0 or yC <0 ):
				return NODATA
			else:
				polygon=np.asarray([[sand[i],clay[i]] for i in range(len(clay))])
				path = Path(polygon)
				isInside = path.contains_point([xS, yC])
				if isInside==True:
					return texture

	def writeTextureGeoTiff(self,arrayData, transform, rows, cols, outFile):
		"Write the given array data to the file 'outfile' with the given extent."
		try:
			format = "GTiff"
			driver = gdal.GetDriverByName( format )
			NOVALUE=-9999
			metadata = driver.GetMetadata()
			#if metadata.has_key(gdal.DCAP_CREATE) \
				#and metadata[gdal.DCAP_CREATE] == 'YES':
				#pass
			#else:
				#QMessageBox.information(None,"info","Driver %s does not support Create() method." % format)
				#return False
			outDataset = driver.Create(str(outFile), cols, rows, 1, gdal.GDT_Byte)
			outTexture=outDataset.GetRasterBand(1)
			outTexture.WriteArray(arrayData)
			outTexture.SetNoDataValue(NOVALUE)
			outDataset.SetGeoTransform(transform)
			print(transform)
			return True
		except:
			QMessageBox.information(None,"Exiting","I can't write %s texture file." % outFile)
			return 1

	def loadTextureRaster(self,outFile):
		"Load texture map in TOC"
		fileInfo = QFileInfo(outFile)
		baseName = fileInfo.baseName()
		rlayer = QgsRasterLayer(outFile, baseName)
		if not rlayer.isValid():
			self.textEdit.append("Layer failed to load!")
		#rlayer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
		#rlayer.setColorShadingAlgorithm(QgsRasterLayer.FreakOutShader)
		QgsProject.instance().addMapLayer(rlayer)
		return rlayer

	def rast2vect(self,rasterTexture,legend):
		"convert raster to vector"
		gdal.AllRegister()
		options=[]
		# open the image
		rasterTexture=str(rasterTexture)
		srcRaster = gdal.Open(rasterTexture,GA_ReadOnly)
		srcband = srcRaster.GetRasterBand(1)
		spatialReference = osr.SpatialReference()
		spatialReference.ImportFromWkt( srcRaster.GetProjectionRef() )
		# 	Create output file.
		pathSource=os.path.dirname(rasterTexture)
		fileName=os.path.splitext(os.path.basename(rasterTexture))[0]
		driver = ogr.GetDriverByName('ESRI Shapefile')
		dstPath=os.path.join(pathSource,fileName+".shp")
		dstFile = driver.CreateDataSource(dstPath)
		if os.path.exists(dstPath)==False:
			#Find or create destination layer.
			dstLayer = dstFile.CreateLayer("layer", spatialReference )
			#Create texture int code field from raster value
			fieldDef = ogr.FieldDefn( "code", ogr.OFTInteger )
			dstLayer.CreateField( fieldDef )
			dst_field = 0
			#Polygonize
			prog_func = gdal.TermProgress
			gdal.Polygonize(srcband, None, dstLayer, dst_field, options, callback =None)
			#Create texture label field
			fieldLabel = ogr.FieldDefn('label_txt', ogr.OFTString )
			fieldLabel.SetWidth(50)
			dstLayer.CreateField( fieldLabel )
			#fieldLabel = 1
			codeList=[line.split("=") for line in legend[1:-1]]
			codeDict={int(v[0]):v[1] for (v) in codeList}
			for i in range(dstLayer.GetFeatureCount()):
				feature=dstLayer.GetFeature(i)
				code=feature.GetField("code")
				iIndex=feature.GetFieldIndex("label_txt")
				feature.SetField(iIndex,str(codeDict[code]))
				dstLayer.SetFeature(feature)
				feature.Destroy()
			dstFile.Destroy()
			return dstPath
		else:
			self.textEdit.append("""<b>There is a file with the same output name.
			Vector texture file will not be created. Only the raster texture
			file will be processed file.<\b>""")
			return 'None'

	def loadTextureVector(self,vectorTexture):
		""" Load thematic layers in canvas """
		if os.path.exists(vectorTexture):
			layer = QgsVectorLayer(vectorTexture, "texture", "ogr")
			QgsProject.instance().addMapLayer(layer)
		else:
			return 0


	def open_help(self):
		webbrowser.open('http://maplab.alwaysdata.net/')

	def plotFile(self,dataClay,dataSand,outFile):
		outDIR = unicode(os.path.abspath( os.path.dirname(outFile)))
		ternaryPlot=os.path.join(outDIR,'ternaryPlot.csv')
		pf=open(ternaryPlot,'w')
		pf.write('CLAY,SAND,SILT\n')
		for crow,srow in zip(dataClay,dataSand):
			for c,s in zip(crow,srow):
				if c>=0 and s>=0:
					values='%s,%s,%s\n' % (c,s,(100-c-s))
					pf.write(values)
		pf.close()

	def accept(self):
		# Called when "OK" button pressed

		clay=self.cmbClay.currentText()
		sand=self.cmbSand.currentText()
		currentDIR = unicode(os.path.abspath( os.path.dirname(__file__)))
		schema=self.cmbSchema.currentText()
		schema=os.path.join(currentDIR,str(schema))
		outFile=self.lineOutput.text()
		self.textEdit.append("Starting...")

		RuleList,numpoly,legend=self.readSchema(schema)
		dataClay,dataSand,rows,cols,transform=self.ProcessRaster(sand,clay)
		self.progressBar.setRange(0,rows)

		TextureList=[]
		row=[]
		self.textEdit.append("rows:%d, columns:%d" % (rows,cols))

		for i in range(rows):
			self.progressBar.setValue(i)
			row=[self.InsidePolygon(RuleList,numpoly, dS, dC) for (dS,dC) in zip(dataSand[i],dataClay[i])]
			TextureList.append(row)

		TextureList=np.asarray(TextureList)
		self.writeTextureGeoTiff(TextureList,transform, rows, cols, outFile)
		self.loadTextureRaster(outFile)
		vectorTexture=self.rast2vect(outFile,legend)
		print(vectorTexture)
		self.loadTextureVector(vectorTexture)
		self.plotFile(dataClay,dataSand,outFile)
		self.textEdit.append("end")
