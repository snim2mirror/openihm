# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editcharacteristic.ui'
#
# Created: Thu Jun 10 18:57:22 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditHouseholdCharacteristic(object):
    def setupUi(self, EditHouseholdCharacteristic):
        EditHouseholdCharacteristic.setObjectName("EditHouseholdCharacteristic")
        EditHouseholdCharacteristic.resize(400, 131)
        self.label = QtGui.QLabel(EditHouseholdCharacteristic)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(EditHouseholdCharacteristic)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.txtValue = QtGui.QLineEdit(EditHouseholdCharacteristic)
        self.txtValue.setGeometry(QtCore.QRect(90, 50, 301, 20))
        self.txtValue.setObjectName("txtValue")
        self.cboYesNoVal = QtGui.QComboBox(EditHouseholdCharacteristic)
        self.cboYesNoVal.setGeometry(QtCore.QRect(90, 50, 131, 22))
        self.cboYesNoVal.setObjectName("cboYesNoVal")
        self.cboYesNoVal.addItem("")
        self.cboYesNoVal.addItem("")
        self.lblCharName = QtGui.QLabel(EditHouseholdCharacteristic)
        self.lblCharName.setGeometry(QtCore.QRect(90, 10, 301, 21))
        self.lblCharName.setObjectName("lblCharName")
        self.cmdOk = QtGui.QPushButton(EditHouseholdCharacteristic)
        self.cmdOk.setGeometry(QtCore.QRect(10, 90, 75, 31))
        self.cmdOk.setObjectName("cmdOk")
        self.cmdCancel = QtGui.QPushButton(EditHouseholdCharacteristic)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 90, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")

        self.retranslateUi(EditHouseholdCharacteristic)
        QtCore.QMetaObject.connectSlotsByName(EditHouseholdCharacteristic)

    def retranslateUi(self, EditHouseholdCharacteristic):
        EditHouseholdCharacteristic.setWindowTitle(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Edit Characteristic", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Characteristic:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(0, QtGui.QApplication.translate("EditHouseholdCharacteristic", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(1, QtGui.QApplication.translate("EditHouseholdCharacteristic", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCharName.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "{charname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHouseholdCharacteristic", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

