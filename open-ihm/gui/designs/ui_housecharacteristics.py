# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_housecharacteristics.ui'
#
# Created: Mon Jun 07 00:21:45 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HouseCharacteristics(object):
    def setupUi(self, HouseCharacteristics):
        HouseCharacteristics.setObjectName("HouseCharacteristics")
        HouseCharacteristics.resize(341, 200)
        HouseCharacteristics.setMinimumSize(QtCore.QSize(341, 200))
        self.btnHouseClose = QtGui.QPushButton(HouseCharacteristics)
        self.btnHouseClose.setGeometry(QtCore.QRect(250, 160, 80, 28))
        self.btnHouseClose.setObjectName("btnHouseClose")
        self.btnCharacteristicDelete = QtGui.QPushButton(HouseCharacteristics)
        self.btnCharacteristicDelete.setGeometry(QtCore.QRect(150, 160, 80, 28))
        self.btnCharacteristicDelete.setObjectName("btnCharacteristicDelete")
        self.btnCharacteristicSave = QtGui.QPushButton(HouseCharacteristics)
        self.btnCharacteristicSave.setGeometry(QtCore.QRect(50, 160, 80, 28))
        self.btnCharacteristicSave.setObjectName("btnCharacteristicSave")
        self.cmbCharacteristic = QtGui.QComboBox(HouseCharacteristics)
        self.cmbCharacteristic.setGeometry(QtCore.QRect(80, 10, 251, 27))
        self.cmbCharacteristic.setEditable(True)
        self.cmbCharacteristic.setObjectName("cmbCharacteristic")
        self.cmbDataType = QtGui.QComboBox(HouseCharacteristics)
        self.cmbDataType.setGeometry(QtCore.QRect(80, 60, 251, 27))
        self.cmbDataType.setObjectName("cmbDataType")
        self.label = QtGui.QLabel(HouseCharacteristics)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(HouseCharacteristics)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 18))
        self.label_2.setObjectName("label_2")
        self.txtDescription = QtGui.QLineEdit(HouseCharacteristics)
        self.txtDescription.setGeometry(QtCore.QRect(80, 110, 251, 28))
        self.txtDescription.setObjectName("txtDescription")
        self.label_3 = QtGui.QLabel(HouseCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 61, 18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(HouseCharacteristics)
        QtCore.QMetaObject.connectSlotsByName(HouseCharacteristics)

    def retranslateUi(self, HouseCharacteristics):
        HouseCharacteristics.setWindowTitle(QtGui.QApplication.translate("HouseCharacteristics", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHouseClose.setText(QtGui.QApplication.translate("HouseCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicDelete.setText(QtGui.QApplication.translate("HouseCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicSave.setText(QtGui.QApplication.translate("HouseCharacteristics", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HouseCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))

