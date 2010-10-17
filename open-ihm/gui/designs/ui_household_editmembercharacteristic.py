# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editmembercharacteristic.ui'
#
# Created: Sun Oct 17 10:42:34 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditMemberCharacteristic(object):
    def setupUi(self, EditMemberCharacteristic):
        EditMemberCharacteristic.setObjectName("EditMemberCharacteristic")
        EditMemberCharacteristic.resize(402, 137)
        self.lblCharName = QtGui.QLabel(EditMemberCharacteristic)
        self.lblCharName.setGeometry(QtCore.QRect(90, 10, 301, 21))
        self.lblCharName.setObjectName("lblCharName")
        self.label_2 = QtGui.QLabel(EditMemberCharacteristic)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.cmdCancel = QtGui.QPushButton(EditMemberCharacteristic)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 90, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label = QtGui.QLabel(EditMemberCharacteristic)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.cmdOk = QtGui.QPushButton(EditMemberCharacteristic)
        self.cmdOk.setGeometry(QtCore.QRect(10, 90, 75, 31))
        self.cmdOk.setObjectName("cmdOk")
        self.txtValue = QtGui.QLineEdit(EditMemberCharacteristic)
        self.txtValue.setGeometry(QtCore.QRect(90, 50, 301, 20))
        self.txtValue.setObjectName("txtValue")
        self.cboYesNoVal = QtGui.QComboBox(EditMemberCharacteristic)
        self.cboYesNoVal.setGeometry(QtCore.QRect(90, 50, 131, 22))
        self.cboYesNoVal.setObjectName("cboYesNoVal")
        self.cboYesNoVal.addItem("")
        self.cboYesNoVal.addItem("")

        self.retranslateUi(EditMemberCharacteristic)
        QtCore.QMetaObject.connectSlotsByName(EditMemberCharacteristic)

    def retranslateUi(self, EditMemberCharacteristic):
        EditMemberCharacteristic.setWindowTitle(QtGui.QApplication.translate("EditMemberCharacteristic", "Edit Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCharName.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "{charname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Characteristic:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(0, QtGui.QApplication.translate("EditMemberCharacteristic", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(1, QtGui.QApplication.translate("EditMemberCharacteristic", "No", None, QtGui.QApplication.UnicodeUTF8))

