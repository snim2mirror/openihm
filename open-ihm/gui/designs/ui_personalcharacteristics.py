# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_personalcharacteristics.ui'
#
# Created: Fri Apr 22 21:52:29 2011
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
        PersonalCharacteristics.resize(341, 184)
        PersonalCharacteristics.setMinimumSize(QtCore.QSize(341, 184))
        self.formLayout = QtGui.QFormLayout(PersonalCharacteristics)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(PersonalCharacteristics)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cmbCharacteristic = QtGui.QComboBox(PersonalCharacteristics)
        self.cmbCharacteristic.setEditable(True)
        self.cmbCharacteristic.setObjectName(_fromUtf8("cmbCharacteristic"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbCharacteristic)
        self.label_2 = QtGui.QLabel(PersonalCharacteristics)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbDataType = QtGui.QComboBox(PersonalCharacteristics)
        self.cmbDataType.setObjectName(_fromUtf8("cmbDataType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cmbDataType)
        self.label_3 = QtGui.QLabel(PersonalCharacteristics)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtDescription = QtGui.QLineEdit(PersonalCharacteristics)
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtDescription)
        self.groupBox = QtGui.QGroupBox(PersonalCharacteristics)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnCharacteristicSave = QtGui.QPushButton(self.groupBox)
        self.btnCharacteristicSave.setObjectName(_fromUtf8("btnCharacteristicSave"))
        self.horizontalLayout.addWidget(self.btnCharacteristicSave)
        self.btnCharacteristicDelete = QtGui.QPushButton(self.groupBox)
        self.btnCharacteristicDelete.setObjectName(_fromUtf8("btnCharacteristicDelete"))
        self.horizontalLayout.addWidget(self.btnCharacteristicDelete)
        self.btnPCharsClose = QtGui.QPushButton(self.groupBox)
        self.btnPCharsClose.setObjectName(_fromUtf8("btnPCharsClose"))
        self.horizontalLayout.addWidget(self.btnPCharsClose)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label.setBuddy(self.cmbCharacteristic)
        self.label_2.setBuddy(self.cmbDataType)
        self.label_3.setBuddy(self.txtDescription)

        self.retranslateUi(PersonalCharacteristics)
        QtCore.QObject.connect(self.cmbCharacteristic, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), PersonalCharacteristics.populateForm)
        QtCore.QObject.connect(self.btnCharacteristicSave, QtCore.SIGNAL(_fromUtf8("clicked()")), PersonalCharacteristics.savePersonalCharacteristic)
        QtCore.QObject.connect(self.btnCharacteristicDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), PersonalCharacteristics.deletePersonalCharacteristic)
        QtCore.QObject.connect(self.btnPCharsClose, QtCore.SIGNAL(_fromUtf8("clicked()")), PersonalCharacteristics.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(PersonalCharacteristics)
        PersonalCharacteristics.setTabOrder(self.cmbCharacteristic, self.cmbDataType)
        PersonalCharacteristics.setTabOrder(self.cmbDataType, self.txtDescription)

    def retranslateUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setWindowTitle(QtGui.QApplication.translate("PersonalCharacteristics", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicSave.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicDelete.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPCharsClose.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))

