# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edithousehold_getid.ui'
#
# Created: Fri Mar 05 11:17:21 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditHouseholdGetID(object):
    def setupUi(self, EditHouseholdGetID):
        EditHouseholdGetID.setObjectName("EditHouseholdGetID")
        EditHouseholdGetID.resize(393, 114)
        self.cmdOk = QtGui.QPushButton(EditHouseholdGetID)
        self.cmdOk.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.cmdOk.setObjectName("cmdOk")
        self.cmdCancel = QtGui.QPushButton(EditHouseholdGetID)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 60, 81, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label = QtGui.QLabel(EditHouseholdGetID)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.cboHouseholdName = QtGui.QComboBox(EditHouseholdGetID)
        self.cboHouseholdName.setGeometry(QtCore.QRect(100, 20, 281, 22))
        self.cboHouseholdName.setObjectName("cboHouseholdName")

        self.retranslateUi(EditHouseholdGetID)
        QtCore.QMetaObject.connectSlotsByName(EditHouseholdGetID)

    def retranslateUi(self, EditHouseholdGetID):
        EditHouseholdGetID.setWindowTitle(QtGui.QApplication.translate("EditHouseholdGetID", "Edit Household - Select Household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))

