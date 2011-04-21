# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editmembercharacteristic.ui'
#
# Created: Thu Apr 21 19:28:06 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditMemberCharacteristic(object):
    def setupUi(self, EditMemberCharacteristic):
        EditMemberCharacteristic.setObjectName(_fromUtf8("EditMemberCharacteristic"))
        EditMemberCharacteristic.resize(455, 174)
        self.formLayout = QtGui.QFormLayout(EditMemberCharacteristic)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(EditMemberCharacteristic)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblCharName = QtGui.QLabel(EditMemberCharacteristic)
        self.lblCharName.setObjectName(_fromUtf8("lblCharName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblCharName)
        self.label_2 = QtGui.QLabel(EditMemberCharacteristic)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cboYesNoVal = QtGui.QComboBox(EditMemberCharacteristic)
        self.cboYesNoVal.setObjectName(_fromUtf8("cboYesNoVal"))
        self.cboYesNoVal.addItem(_fromUtf8(""))
        self.cboYesNoVal.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboYesNoVal)
        self.txtValue = QtGui.QLineEdit(EditMemberCharacteristic)
        self.txtValue.setObjectName(_fromUtf8("txtValue"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtValue)
        self.groupBox = QtGui.QGroupBox(EditMemberCharacteristic)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOk = QtGui.QPushButton(self.groupBox)
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.horizontalLayout.addWidget(self.cmdOk)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(EditMemberCharacteristic)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditMemberCharacteristic.mdiClose)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), EditMemberCharacteristic.saveCharacteristic)
        QtCore.QMetaObject.connectSlotsByName(EditMemberCharacteristic)
        EditMemberCharacteristic.setTabOrder(self.txtValue, self.cboYesNoVal)
        EditMemberCharacteristic.setTabOrder(self.cboYesNoVal, self.cmdOk)
        EditMemberCharacteristic.setTabOrder(self.cmdOk, self.cmdCancel)

    def retranslateUi(self, EditMemberCharacteristic):
        EditMemberCharacteristic.setWindowTitle(QtGui.QApplication.translate("EditMemberCharacteristic", "Edit Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Characteristic:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCharName.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "{charname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(0, QtGui.QApplication.translate("EditMemberCharacteristic", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(1, QtGui.QApplication.translate("EditMemberCharacteristic", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

