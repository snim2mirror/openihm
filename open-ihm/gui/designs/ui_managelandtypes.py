# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managelandtypes.ui'
#
# Created: Sun Feb 28 13:43:28 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LandTypes(object):
    def setupUi(self, LandTypes):
        LandTypes.setObjectName("LandTypes")
        LandTypes.resize(QtCore.QSize(QtCore.QRect(0,0,371,204).size()).expandedTo(LandTypes.minimumSizeHint()))
        LandTypes.setMinimumSize(QtCore.QSize(369,204))

        self.btnLandTypesClose = QtGui.QPushButton(LandTypes)
        self.btnLandTypesClose.setGeometry(QtCore.QRect(280,160,80,28))
        self.btnLandTypesClose.setObjectName("btnLandTypesClose")

        self.pushButton_3 = QtGui.QPushButton(LandTypes)
        self.pushButton_3.setGeometry(QtCore.QRect(50,160,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(LandTypes)
        self.comboBox.setGeometry(QtCore.QRect(120,10,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(LandTypes)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(LandTypes)
        self.comboBox_3.setGeometry(QtCore.QRect(120,60,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(LandTypes)
        self.label_3.setGeometry(QtCore.QRect(10,70,91,18))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtGui.QLineEdit(LandTypes)
        self.lineEdit.setGeometry(QtCore.QRect(120,110,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(LandTypes)
        self.label_5.setGeometry(QtCore.QRect(10,110,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(LandTypes)
        self.pushButton.setGeometry(QtCore.QRect(170,160,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LandTypes)
        QtCore.QMetaObject.connectSlotsByName(LandTypes)

    def retranslateUi(self, LandTypes):
        LandTypes.setWindowTitle(QtGui.QApplication.translate("LandTypes", "Manage Land Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLandTypesClose.setText(QtGui.QApplication.translate("LandTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("LandTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LandTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LandTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("LandTypes", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LandTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))

