# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_delete.ui'
#
# Created: Tue May 18 07:24:12 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeleteHousehold(object):
    def setupUi(self, DeleteHousehold):
        DeleteHousehold.setObjectName("DeleteHousehold")
        DeleteHousehold.resize(400, 108)
        self.cmdDel = QtGui.QPushButton(DeleteHousehold)
        self.cmdDel.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.cmdDel.setObjectName("cmdDel")
        self.label = QtGui.QLabel(DeleteHousehold)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cboHouseholdName = QtGui.QComboBox(DeleteHousehold)
        self.cboHouseholdName.setGeometry(QtCore.QRect(120, 20, 261, 22))
        self.cboHouseholdName.setObjectName("cboHouseholdName")
        self.cmdCancel = QtGui.QPushButton(DeleteHousehold)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 60, 81, 31))
        self.cmdCancel.setObjectName("cmdCancel")

        self.retranslateUi(DeleteHousehold)
        QtCore.QMetaObject.connectSlotsByName(DeleteHousehold)

    def retranslateUi(self, DeleteHousehold):
        DeleteHousehold.setWindowTitle(QtGui.QApplication.translate("DeleteHousehold", "Delete Household ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDel.setText(QtGui.QApplication.translate("DeleteHousehold", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DeleteHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("DeleteHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

