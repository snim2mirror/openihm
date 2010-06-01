# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_households_add.ui'
#
# Created: Fri May 21 16:39:19 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Households_Add(object):
    def setupUi(self, Households_Add):
        Households_Add.setObjectName("Households_Add")
        Households_Add.resize(384, 175)
        self.lblProjectName = QtGui.QLabel(Households_Add)
        self.lblProjectName.setGeometry(QtCore.QRect(130, 10, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblProjectName.setFont(font)
        self.lblProjectName.setObjectName("lblProjectName")
        self.label_5 = QtGui.QLabel(Households_Add)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cmdCancel = QtGui.QPushButton(Households_Add)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.dtpDateVisted = QtGui.QDateEdit(Households_Add)
        self.dtpDateVisted.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.dtpDateVisted.setObjectName("dtpDateVisted")
        self.label_6 = QtGui.QLabel(Households_Add)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cmdSave = QtGui.QPushButton(Households_Add)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.txtShortHouseHoldName = QtGui.QLineEdit(Households_Add)
        self.txtShortHouseHoldName.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.txtShortHouseHoldName.setObjectName("txtShortHouseHoldName")
        self.label_2 = QtGui.QLabel(Households_Add)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtHouseholdName = QtGui.QLineEdit(Households_Add)
        self.txtHouseholdName.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.txtHouseholdName.setObjectName("txtHouseholdName")
        self.label_3 = QtGui.QLabel(Households_Add)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Households_Add)
        QtCore.QMetaObject.connectSlotsByName(Households_Add)

    def retranslateUi(self, Households_Add):
        Households_Add.setWindowTitle(QtGui.QApplication.translate("Households_Add", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("Households_Add", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Households_Add", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("Households_Add", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Households_Add", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("Households_Add", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Households_Add", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Households_Add", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))

