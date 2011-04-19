# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editmembercharacteristic.ui'
#
# Created: Tue Apr 19 03:45:25 2011
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
        EditMemberCharacteristic.resize(455, 163)
        self.lblCharName = QtGui.QLabel(EditMemberCharacteristic)
        self.lblCharName.setGeometry(QtCore.QRect(90, 10, 301, 21))
        self.lblCharName.setObjectName(_fromUtf8("lblCharName"))
        self.label_2 = QtGui.QLabel(EditMemberCharacteristic)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cmdCancel = QtGui.QPushButton(EditMemberCharacteristic)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 90, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label = QtGui.QLabel(EditMemberCharacteristic)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.cmdOk = QtGui.QPushButton(EditMemberCharacteristic)
        self.cmdOk.setGeometry(QtCore.QRect(10, 90, 75, 31))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.txtValue = QtGui.QLineEdit(EditMemberCharacteristic)
        self.txtValue.setGeometry(QtCore.QRect(90, 50, 301, 20))
        self.txtValue.setObjectName(_fromUtf8("txtValue"))
        self.cboYesNoVal = QtGui.QComboBox(EditMemberCharacteristic)
        self.cboYesNoVal.setGeometry(QtCore.QRect(90, 50, 131, 22))
        self.cboYesNoVal.setObjectName(_fromUtf8("cboYesNoVal"))
        self.cboYesNoVal.addItem(_fromUtf8(""))
        self.cboYesNoVal.addItem(_fromUtf8(""))

        self.retranslateUi(EditMemberCharacteristic)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditMemberCharacteristic.mdiClose)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), EditMemberCharacteristic.saveCharacteristic)
        QtCore.QMetaObject.connectSlotsByName(EditMemberCharacteristic)
        EditMemberCharacteristic.setTabOrder(self.txtValue, self.cboYesNoVal)
        EditMemberCharacteristic.setTabOrder(self.cboYesNoVal, self.cmdOk)
        EditMemberCharacteristic.setTabOrder(self.cmdOk, self.cmdCancel)

    def retranslateUi(self, EditMemberCharacteristic):
        EditMemberCharacteristic.setWindowTitle(QtGui.QApplication.translate("EditMemberCharacteristic", "Edit Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCharName.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "{charname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "Characteristic:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditMemberCharacteristic", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(0, QtGui.QApplication.translate("EditMemberCharacteristic", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.cboYesNoVal.setItemText(1, QtGui.QApplication.translate("EditMemberCharacteristic", "No", None, QtGui.QApplication.UnicodeUTF8))

