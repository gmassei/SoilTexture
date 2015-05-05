PLUGINNAME = SoilTexture

PY_FILES = doTexture.py SoilTexture.py __init__.py

EXTRAS = icon.png metadata.txt FAO.dat INTERNATIONAL.dat ISSS.dat USDA.dat

UI_FILES = Ui_SoilTexture.py SoilTextureDialog.py

RESOURCE_FILES = resources.py

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@ $<

%.py : %.ui
	pyuic4 -o $@ $<

deploy: compile
	mkdir -p $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)

