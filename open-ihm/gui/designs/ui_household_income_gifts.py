# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_gifts.ui'
#
# Created: Mon Jun 21 23:14:31 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdIncomeGifts(object):
    def setupUi(self, AddHouseholdIncomeGifts):
        AddHouseholdIncomeGifts.setObjectName("AddHouseholdIncomeGifts")
        AddHouseholdIncomeGifts.resize(400, 208)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeGifts)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.cboAssistanceTypeType = QtGui.QComboBox(AddHouseholdIncomeGifts)
        self.cboAssistanceTypeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboAssistanceTypeType.setEditable(True)
        self.cboAssistanceTypeType.setObjectName("cboAssistanceTypeType")
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeGifts)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 111, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeGifts)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 160, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label = QtGui.QLabel(AddHouseholdIncomeGifts)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeGifts)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeGifts)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 120, 111, 20))
        self.txtUnitsConsumed.setObjectName("txtUnitsConsumed")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeGifts)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeGifts)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_3.setObjectName("label_3")
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeGifts)
        self.cmdSave.setGeometry(QtCore.QRect(20, 160, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName("cmdSave")

        self.retranslateUi(AddHouseholdIncomeGifts)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeGifts)
        AddHouseholdIncomeGifts.setTabOrder(self.cboAssistanceTypeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeGifts.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsConsumed)
        AddHouseholdIncomeGifts.setTabOrder(self.txtUnitsConsumed, self.cmdSave)
        AddHouseholdIncomeGifts.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeGifts):
        AddHouseholdIncomeGifts.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Add Gifts", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Assistance Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeGifts", "Save", None, QtGui.QApplication.UnicodeUTF8))

