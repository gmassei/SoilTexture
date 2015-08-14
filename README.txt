Soil texture for QGIS. The plugin require two raster: spatial distribution for sand and clay for the same area. The user must supply even the texture schema and the output file.

We obtain two output files:

1. raster map, with the representation of single pixels coded with a unique texture value based on schema selected by the user;

2. vector map with the representation of homogeneous areas with the same texture type. The attribute table contain the texture code and the label based on schema selected from the user. 

The plugin supply a text file too, named "ternaryPlot.csv", in the same output directory. You can use this file in R with packages "soiltexture". Follow a sample code for plot in a ternary chart. More info are available on site: http://soiltexture.r-forge.r-project.org/

#install soiltexture pakages,only firsth one time!
install.packages( pkgs = "soiltexture" )

#load soiltexture library
library( soiltexture )

#load file ternaryPlot.csv in dataframe
ternaryPlot <- read.csv("/your path/ternaryPlot.csv")

#plot data in ternary chart
TT.plot(class.sys= "USDA.TT", tri.data= ternaryPlot, main= "Soil texture data")

Overplotting two soil texture classification systems with the same geometry
geo<-TT.plot(class.sys= "none", tri.data= ternaryPlot, main= "Soil texture data")
TT.plot(geo=geo,class.sys="USDA.TT", add=TRUE)



##########################
# for rebuild gui:

rm *.pyc
pyuic4 -o Ui_SoilTexture.py Ui_SoilTexture.ui
pyrcc4 -o resources.py resources.qrc 
