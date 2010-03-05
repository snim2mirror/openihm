# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addhousehold.ui'
#
# Created: Fri Mar 05 11:11:25 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHousehold(object):
    def setupUi(self, AddHousehold):
        AddHousehold.setObjectName("AddHousehold")
        AddHousehold.resize(380, 175)
        AddHousehold.setMinimumSize(QtCore.QSize(380, 175))
        self.txtShortHouseHoldName = QtGui.QLineEdit(AddHousehold)
        self.txtShortHouseHoldName.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.txtShortHouseHoldName.setObjectName("txtShortHouseHoldName")
        self.label_2 = QtGui.QLabel(AddHousehold)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(AddHousehold)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lblProjectName = QtGui.QLabel(AddHousehold)
        self.lblProjectName.setGeometry(QtCore.QRect(130, 10, 101, 16))
        self.lblProjectName.setObjectName("lblProjectName")
        self.label_5 = QtGui.QLabel(AddHousehold)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_5.setObjectName("label_5")
        self.dtpDateVisted = QtGui.QDateEdit(AddHousehold)
        self.dtpDateVisted.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.dtpDateVisted.setObjectName("dtpDateVisted")
        self.btnSave = QtGui.QPushButton(AddHousehold)
        self.btnSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtGui.QPushButton(AddHousehold)
        self.btnCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.label_6 = QtGui.QLabel(AddHousehold)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_6.setObjectName("label_6")
        self.txtHouseholdName = QtGui.QLineEdit(AddHousehold)
        self.txtHouseholdName.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.txtHouseholdName.setObjectName("txtHouseholdName")

        self.retranslateUi(AddHousehold)
        QtCore.QMetaObject.connectSlotsByName(AddHousehold)

    def retranslateUi(self, AddHousehold):
        AddHousehold.setWindowTitle(QtGui.QApplication.translate("AddHousehold", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHousehold", "Household Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHousehold", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("AddHousehold", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHousehold", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("AddHousehold", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("AddHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHousehold", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))

