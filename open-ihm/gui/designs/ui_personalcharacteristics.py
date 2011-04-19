# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_personalcharacteristics.ui'
#
# Created: Tue Apr 19 08:09:04 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PersonalCharacteristics(object):
    def setupUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setObjectName(_fromUtf8("PersonalCharacteristics"))
        PersonalCharacteristics.resize(341, 206)
        PersonalCharacteristics.setMinimumSize(QtCore.QSize(341, 206))
        self.btnPCharsClose = QtGui.QPushButton(PersonalCharacteristics)
        self.btnPCharsClose.setGeometry(QtCore.QRect(250, 170, 80, 28))
        self.btnPCharsClose.setObjectName(_fromUtf8("btnPCharsClose"))
        self.btnCharacteristicDelete = QtGui.QPushButton(PersonalCharacteristics)
        self.btnCharacteristicDelete.setGeometry(QtCore.QRect(150, 170, 80, 28))
        self.btnCharacteristicDelete.setObjectName(_fromUtf8("btnCharacteristicDelete"))
        self.btnCharacteristicSave = QtGui.QPushButton(PersonalCharacteristics)
        self.btnCharacteristicSave.setGeometry(QtCore.QRect(50, 170, 80, 28))
        self.btnCharacteristicSave.setObjectName(_fromUtf8("btnCharacteristicSave"))
        self.cmbCharacteristic = QtGui.QComboBox(PersonalCharacteristics)
        self.cmbCharacteristic.setGeometry(QtCore.QRect(90, 20, 241, 27))
        self.cmbCharacteristic.setEditable(True)
        self.cmbCharacteristic.setObjectName(_fromUtf8("cmbCharacteristic"))
        self.cmbDataType = QtGui.QComboBox(PersonalCharacteristics)
        self.cmbDataType.setGeometry(QtCore.QRect(90, 70, 241, 27))
        self.cmbDataType.setObjectName(_fromUtf8("cmbDataType"))
        self.label = QtGui.QLabel(PersonalCharacteristics)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(PersonalCharacteristics)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 61, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(PersonalCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 71, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtDescription = QtGui.QLineEdit(PersonalCharacteristics)
        self.txtDescription.setGeometry(QtCore.QRect(90, 120, 241, 28))
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))

        self.retranslateUi(PersonalCharacteristics)
        QtCore.QObject.connect(self.cmbCharacteristic, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), PersonalCharacteristics.populateForm)
        QtCore.QObject.connect(self.btnCharacteristicSave, QtCore.SIGNAL(_fromUtf8("clicked()")), PersonalCharacteristics.savePersonalCharacteristic)
        QtCore.QObject.connect(self.btnCharacteristicDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), PersonalCharacteristics.deletePersonalCharacteristic)
        QtCore.QObject.connect(self.btnPCharsClose, QtCore.SIGNAL(_fromUtf8("clicked()")), PersonalCharacteristics.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(PersonalCharacteristics)
        PersonalCharacteristics.setTabOrder(self.cmbCharacteristic, self.cmbDataType)
        PersonalCharacteristics.setTabOrder(self.cmbDataType, self.txtDescription)
        PersonalCharacteristics.setTabOrder(self.txtDescription, self.btnCharacteristicSave)
        PersonalCharacteristics.setTabOrder(self.btnCharacteristicSave, self.btnCharacteristicDelete)
        PersonalCharacteristics.setTabOrder(self.btnCharacteristicDelete, self.btnPCharsClose)

    def retranslateUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setWindowTitle(QtGui.QApplication.translate("PersonalCharacteristics", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPCharsClose.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicDelete.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicSave.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))

