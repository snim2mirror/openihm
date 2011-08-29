# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_housecharacteristics.ui'
#
# Created: Fri Apr 22 21:52:27 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HouseCharacteristics(object):
    def setupUi(self, HouseCharacteristics):
        HouseCharacteristics.setObjectName(_fromUtf8("HouseCharacteristics"))
        HouseCharacteristics.resize(361, 184)
        HouseCharacteristics.setMinimumSize(QtCore.QSize(341, 180))
        self.formLayout = QtGui.QFormLayout(HouseCharacteristics)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(HouseCharacteristics)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cmbCharacteristic = QtGui.QComboBox(HouseCharacteristics)
        self.cmbCharacteristic.setEditable(True)
        self.cmbCharacteristic.setObjectName(_fromUtf8("cmbCharacteristic"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbCharacteristic)
        self.label_2 = QtGui.QLabel(HouseCharacteristics)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbDataType = QtGui.QComboBox(HouseCharacteristics)
        self.cmbDataType.setEditable(False)
        self.cmbDataType.setObjectName(_fromUtf8("cmbDataType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cmbDataType)
        self.label_3 = QtGui.QLabel(HouseCharacteristics)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtDescription = QtGui.QLineEdit(HouseCharacteristics)
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtDescription)
        self.groupBox = QtGui.QGroupBox(HouseCharacteristics)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
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
        self.btnHouseClose = QtGui.QPushButton(self.groupBox)
        self.btnHouseClose.setObjectName(_fromUtf8("btnHouseClose"))
        self.horizontalLayout.addWidget(self.btnHouseClose)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label.setBuddy(self.cmbCharacteristic)
        self.label_2.setBuddy(self.cmbDataType)
        self.label_3.setBuddy(self.txtDescription)

        self.retranslateUi(HouseCharacteristics)
        QtCore.QObject.connect(self.cmbCharacteristic, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), HouseCharacteristics.populateForm)
        QtCore.QObject.connect(self.btnCharacteristicSave, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseCharacteristics.saveHouseholdCharacteristic)
        QtCore.QObject.connect(self.btnCharacteristicDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseCharacteristics.deleteHouseholdCharacteristic)
        QtCore.QObject.connect(self.btnHouseClose, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseCharacteristics.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(HouseCharacteristics)
        HouseCharacteristics.setTabOrder(self.cmbCharacteristic, self.cmbDataType)
        HouseCharacteristics.setTabOrder(self.cmbDataType, self.txtDescription)

    def retranslateUi(self, HouseCharacteristics):
        HouseCharacteristics.setWindowTitle(QtGui.QApplication.translate("HouseCharacteristics", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HouseCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicSave.setText(QtGui.QApplication.translate("HouseCharacteristics", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCharacteristicDelete.setText(QtGui.QApplication.translate("HouseCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHouseClose.setText(QtGui.QApplication.translate("HouseCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))

