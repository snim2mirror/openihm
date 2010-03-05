# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edithousehold_details.ui'
#
# Created: Fri Mar 05 11:16:41 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditHousehold(object):
    def setupUi(self, EditHousehold):
        EditHousehold.setObjectName("EditHousehold")
        EditHousehold.resize(380, 175)
        EditHousehold.setMinimumSize(QtCore.QSize(380, 175))
        self.txtShortHouseHoldName = QtGui.QLineEdit(EditHousehold)
        self.txtShortHouseHoldName.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.txtShortHouseHoldName.setObjectName("txtShortHouseHoldName")
        self.label_2 = QtGui.QLabel(EditHousehold)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(EditHousehold)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lblProjectName = QtGui.QLabel(EditHousehold)
        self.lblProjectName.setGeometry(QtCore.QRect(130, 10, 101, 16))
        self.lblProjectName.setObjectName("lblProjectName")
        self.label_5 = QtGui.QLabel(EditHousehold)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_5.setObjectName("label_5")
        self.dtpDateVisted = QtGui.QDateEdit(EditHousehold)
        self.dtpDateVisted.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.dtpDateVisted.setObjectName("dtpDateVisted")
        self.cmdSave = QtGui.QPushButton(EditHousehold)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.cmdCancel = QtGui.QPushButton(EditHousehold)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label_6 = QtGui.QLabel(EditHousehold)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_6.setObjectName("label_6")
        self.txtHouseholdName = QtGui.QLineEdit(EditHousehold)
        self.txtHouseholdName.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.txtHouseholdName.setObjectName("txtHouseholdName")

        self.retranslateUi(EditHousehold)
        QtCore.QMetaObject.connectSlotsByName(EditHousehold)

    def retranslateUi(self, EditHousehold):
        EditHousehold.setWindowTitle(QtGui.QApplication.translate("EditHousehold", "Edit Household Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditHousehold", "Household Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditHousehold", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("EditHousehold", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditHousehold", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditHousehold", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditHousehold", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))

