# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editcharacteristic.ui'
#
# Created: Tue Apr 19 08:13:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditHouseholdCharacteristic(object):
    def setupUi(self, EditHouseholdCharacteristic):
        EditHouseholdCharacteristic.setObjectName(_fromUtf8("EditHouseholdCharacteristic"))
        EditHouseholdCharacteristic.resize(400, 131)
        self.label = QtGui.QLabel(EditHouseholdCharacteristic)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(EditHouseholdCharacteristic)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtValue = QtGui.QLineEdit(EditHouseholdCharacteristic)
        self.txtValue.setGeometry(QtCore.QRect(90, 50, 301, 20))
        self.txtValue.setObjectName(_fromUtf8("txtValue"))
        self.cboYesNoVal = QtGui.QComboBox(EditHouseholdCharacteristic)
        self.cboYesNoVal.setGeometry(QtCore.QRect(90, 50, 131, 22))
        self.cboYesNoVal.setObjectName(_fromUtf8("cboYesNoVal"))
        self.cboYesNoVal.addItem(_fromUtf8(""))
        self.cboYesNoVal.addItem(_fromUtf8(""))
        self.lblCharName = QtGui.QLabel(EditHouseholdCharacteristic)
        self.lblCharName.setGeometry(QtCore.QRect(90, 10, 301, 21))
        self.lblCharName.setObjectName(_fromUtf8("lblCharName"))
        self.cmdOk = QtGui.QPushButton(EditHouseholdCharacteristic)
        self.cmdOk.setGeometry(QtCore.QRect(10, 90, 75, 31))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.cmdCancel = QtGui.QPushButton(EditHouseholdCharacteristic)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 90, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))

        self.retranslateUi(EditHouseholdCharacteristic)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHouseholdCharacteristic.open)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHouseholdCharacteristic.saveCharacteristic)
        QtCore.QMetaObject.connectSlotsByName(EditHouseholdCharacteristic)
        EditHouseholdCharacteristic.setTabOrder(self.cboYesNoVal, self.txtValue)
        EditHouseholdCharacteristic.setTabOrder(self.txtValue, self.cmdOk)
        EditHouseholdCharacteristic.setTabOrder(self.cmdOk, self.cmdCancel)

    def retranslateUi(self, EditHouseholdCharacteristic):
        EditHouseholdCharacteristic.setWindowTitle(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Edit Characteristic", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Characteristic:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(0, QtGui.QApplication.translate("EditHouseholdCharacteristic", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(1, QtGui.QApplication.translate("EditHouseholdCharacteristic", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCharName.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "{charname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

