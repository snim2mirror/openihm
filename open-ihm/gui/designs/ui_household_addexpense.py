# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addexpense.ui'
#
# Created: Fri Jun 18 11:41:38 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdExpense(object):
    def setupUi(self, AddHouseholdExpense):
        AddHouseholdExpense.setObjectName("AddHouseholdExpense")
        AddHouseholdExpense.resize(400, 300)
        self.txtNumberOfUnits = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtNumberOfUnits.setGeometry(QtCore.QRect(120, 200, 111, 20))
        self.txtNumberOfUnits.setObjectName("txtNumberOfUnits")
        self.label_5 = QtGui.QLabel(AddHouseholdExpense)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label = QtGui.QLabel(AddHouseholdExpense)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(AddHouseholdExpense)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtGui.QLabel(AddHouseholdExpense)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.cboExpenditure = QtGui.QComboBox(AddHouseholdExpense)
        self.cboExpenditure.setGeometry(QtCore.QRect(120, 40, 231, 22))
        self.cboExpenditure.setEditable(True)
        self.cboExpenditure.setObjectName("cboExpenditure")
        self.txtCostPerUnit = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtCostPerUnit.setGeometry(QtCore.QRect(120, 160, 261, 20))
        self.txtCostPerUnit.setObjectName("txtCostPerUnit")
        self.label_6 = QtGui.QLabel(AddHouseholdExpense)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label_6.setObjectName("label_6")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdExpense)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 240, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdExpense)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.cmdSave = QtGui.QPushButton(AddHouseholdExpense)
        self.cmdSave.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.label_3 = QtGui.QLabel(AddHouseholdExpense)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_3.setObjectName("label_3")
        self.txtKCalPerUnit = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtKCalPerUnit.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.txtKCalPerUnit.setObjectName("txtKCalPerUnit")
        self.label_7 = QtGui.QLabel(AddHouseholdExpense)
        self.label_7.setGeometry(QtCore.QRect(240, 120, 61, 21))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(AddHouseholdExpense)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdExpense)

    def retranslateUi(self, AddHouseholdExpense):
        AddHouseholdExpense.setWindowTitle(QtGui.QApplication.translate("AddHouseholdExpense", "Add Household Expenditure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Cost per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Expenditure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Number of Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdExpense", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdExpense", "KCal per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdExpense", "(optional)", None, QtGui.QApplication.UnicodeUTF8))

