# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SoilTexture.ui'
#
# Created: Sun Apr 19 21:51:01 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SoilTexture(object):
    def setupUi(self, SoilTexture):
        SoilTexture.setObjectName(_fromUtf8("SoilTexture"))
        SoilTexture.resize(478, 459)
        self.toolBox = QtGui.QToolBox(SoilTexture)
        self.toolBox.setGeometry(QtCore.QRect(8, 12, 451, 421))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.TexturePage = QtGui.QWidget()
        self.TexturePage.setGeometry(QtCore.QRect(0, 0, 451, 367))
        self.TexturePage.setObjectName(_fromUtf8("TexturePage"))
        self.groupBox_5 = QtGui.QGroupBox(self.TexturePage)
        self.groupBox_5.setGeometry(QtCore.QRect(230, 230, 201, 61))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.cmbSchema = QtGui.QComboBox(self.groupBox_5)
        self.cmbSchema.setGeometry(QtCore.QRect(20, 20, 151, 25))
        self.cmbSchema.setMinimumSize(QtCore.QSize(0, 25))
        self.cmbSchema.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cmbSchema.setObjectName(_fromUtf8("cmbSchema"))
        self.groupBox = QtGui.QGroupBox(self.TexturePage)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 421, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 401, 91))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblClay = QtGui.QLabel(self.gridLayoutWidget_4)
        self.lblClay.setMaximumSize(QtCore.QSize(50, 20))
        self.lblClay.setObjectName(_fromUtf8("lblClay"))
        self.gridLayout_3.addWidget(self.lblClay, 1, 0, 1, 1)
        self.lblSand = QtGui.QLabel(self.gridLayoutWidget_4)
        self.lblSand.setMaximumSize(QtCore.QSize(50, 20))
        self.lblSand.setAutoFillBackground(False)
        self.lblSand.setMargin(1)
        self.lblSand.setObjectName(_fromUtf8("lblSand"))
        self.gridLayout_3.addWidget(self.lblSand, 0, 0, 1, 1)
        self.cmbClay = QtGui.QComboBox(self.gridLayoutWidget_4)
        self.cmbClay.setMinimumSize(QtCore.QSize(280, 25))
        self.cmbClay.setMaximumSize(QtCore.QSize(300, 25))
        self.cmbClay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cmbClay.setObjectName(_fromUtf8("cmbClay"))
        self.gridLayout_3.addWidget(self.cmbClay, 1, 1, 1, 1)
        self.cmbSand = QtGui.QComboBox(self.gridLayoutWidget_4)
        self.cmbSand.setMinimumSize(QtCore.QSize(280, 25))
        self.cmbSand.setMaximumSize(QtCore.QSize(300, 25))
        self.cmbSand.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cmbSand.setObjectName(_fromUtf8("cmbSand"))
        self.gridLayout_3.addWidget(self.cmbSand, 0, 1, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.TexturePage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 300, 401, 52))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.buttonBox = QtGui.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setAutoFillBackground(True)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_5.addWidget(self.buttonBox, 0, 1, 1, 1)
        self.btnHelp = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.gridLayout_5.addWidget(self.btnHelp, 0, 2, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.TexturePage)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 230, 201, 61))
        self.groupBox_4.setStyleSheet(_fromUtf8("border-color: rgb(4, 4, 4);"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(20, 20, 159, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.groupBox_2 = QtGui.QGroupBox(self.TexturePage)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 421, 91))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 401, 51))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineOutput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineOutput.setMinimumSize(QtCore.QSize(280, 25))
        self.lineOutput.setMaximumSize(QtCore.QSize(280, 25))
        self.lineOutput.setObjectName(_fromUtf8("lineOutput"))
        self.gridLayout.addWidget(self.lineOutput, 2, 1, 1, 1)
        self.btnOutput = QtGui.QToolButton(self.gridLayoutWidget_2)
        self.btnOutput.setMinimumSize(QtCore.QSize(0, 25))
        self.btnOutput.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btnOutput.setObjectName(_fromUtf8("btnOutput"))
        self.gridLayout.addWidget(self.btnOutput, 2, 0, 1, 1)
        self.toolBox.addItem(self.TexturePage, _fromUtf8(""))
        self.MessagesPage = QtGui.QWidget()
        self.MessagesPage.setGeometry(QtCore.QRect(0, 0, 451, 367))
        self.MessagesPage.setObjectName(_fromUtf8("MessagesPage"))
        self.groupBox_3 = QtGui.QGroupBox(self.MessagesPage)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 12, 441, 341))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 411, 311))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.toolBox.addItem(self.MessagesPage, _fromUtf8(""))

        self.retranslateUi(SoilTexture)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SoilTexture)

    def retranslateUi(self, SoilTexture):
        SoilTexture.setWindowTitle(_translate("SoilTexture", "SoilTexture", None))
        self.groupBox_5.setTitle(_translate("SoilTexture", "Texture scheme", None))
        self.groupBox.setTitle(_translate("SoilTexture", "Input ", None))
        self.lblClay.setText(_translate("SoilTexture", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Clay</span></p></body></html>", None))
        self.lblSand.setText(_translate("SoilTexture", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Sand</span></p></body></html>", None))
        self.btnHelp.setText(_translate("SoilTexture", "Help", None))
        self.groupBox_4.setTitle(_translate("SoilTexture", "Progress...", None))
        self.groupBox_2.setTitle(_translate("SoilTexture", "Output ", None))
        self.btnOutput.setText(_translate("SoilTexture", "...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.TexturePage), _translate("SoilTexture", "Texture", None))
        self.groupBox_3.setTitle(_translate("SoilTexture", "Messages", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.MessagesPage), _translate("SoilTexture", "Messages", None))

