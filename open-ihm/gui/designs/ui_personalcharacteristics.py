# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_personalcharacteristics.ui'
#
# Created: Thu Jun 03 22:22:51 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PersonalCharacteristics(object):
    def setupUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setObjectName("PersonalCharacteristics")
        PersonalCharacteristics.resize(341, 206)
        PersonalCharacteristics.setMinimumSize(QtCore.QSize(341, 206))
        self.btnPCharsClose = QtGui.QPushButton(PersonalCharacteristics)
        self.btnPCharsClose.setGeometry(QtCore.QRect(250, 170, 80, 28))
        self.btnPCharsClose.setObjectName("btnPCharsClose")
        self.btnCharacteristicDelete = QtGui.QPushButton(PersonalCharacteristics)
        self.btnCharacteristicDelete.setGeometry(QtCore.QRect(150, 170, 80, 28))
        self.btnCharacteristicDelete.setObjectName("btnCharacteristicDelete")
        self.btnCharacteristicSave = QtGui.QPushButton(PersonalCharacteristics)
        self.btnCharacteristicSave.setGeometry(QtCore.QRect(50, 170, 80, 28))
        self.btnCharacteristicSave.setObjectName("btnCharacteristicSave")
        self.cmbCharacteristic = QtGui.QComboBox(PersonalCharacteristics)
        self.cmbCharacteristic.setGeometry(QtCore.QRect(90, 20, 241, 27))
        self.cmbCharacteristic.setEditable(True)
        self.cmbCharacteristic.setObjectName("cmbCharacteristic")
        self.cmbDataType = QtGui.QComboBox(PersonalCharacteristics)
        self.cmbDataType.setGeometry(QtCore.QRect(90, 70, 241, 27))
        self.cmbDataType.setObjectName("cmbDataType")
        self.label = QtGui.QLabel(PersonalCharacteristics)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(PersonalCharacteristics)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 61, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(PersonalCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 71, 18))
        self.label_3.setObjectName("label_3")
        self.txtDescription = QtGui.QLineEdit(PersonalCharacteristics)
        self.txtDescription.setGeometry(QtCore.QRect(90, 120, 241, 28))
        self.txtDescription.setObjectName("txtDescription")

        self.retranslateUi(PersonalCharacteristics)
        QtCore.QMetaObject.connectSlotsByName(PersonalCharacteristics)

    def retranslateUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setWindowTitle(QtGui.QApplication.translate("PersonalCharacteristics", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPCharsClose.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicDelete.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicSave.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))

