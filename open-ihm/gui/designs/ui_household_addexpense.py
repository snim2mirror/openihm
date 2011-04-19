# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addexpense.ui'
#
# Created: Tue Apr 19 14:35:32 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdExpense(object):
    def setupUi(self, AddHouseholdExpense):
        AddHouseholdExpense.setObjectName(_fromUtf8("AddHouseholdExpense"))
        AddHouseholdExpense.resize(400, 300)
        self.txtNumberOfUnits = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtNumberOfUnits.setGeometry(QtCore.QRect(120, 200, 111, 20))
        self.txtNumberOfUnits.setObjectName(_fromUtf8("txtNumberOfUnits"))
        self.label_5 = QtGui.QLabel(AddHouseholdExpense)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(AddHouseholdExpense)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AddHouseholdExpense)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(AddHouseholdExpense)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.cboExpenditure = QtGui.QComboBox(AddHouseholdExpense)
        self.cboExpenditure.setGeometry(QtCore.QRect(120, 40, 231, 22))
        self.cboExpenditure.setEditable(True)
        self.cboExpenditure.setObjectName(_fromUtf8("cboExpenditure"))
        self.txtCostPerUnit = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtCostPerUnit.setGeometry(QtCore.QRect(120, 160, 261, 20))
        self.txtCostPerUnit.setObjectName(_fromUtf8("txtCostPerUnit"))
        self.label_6 = QtGui.QLabel(AddHouseholdExpense)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdExpense)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 240, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdExpense)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdExpense)
        self.cmdSave.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label_3 = QtGui.QLabel(AddHouseholdExpense)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtKCalPerUnit = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtKCalPerUnit.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.txtKCalPerUnit.setObjectName(_fromUtf8("txtKCalPerUnit"))
        self.label_7 = QtGui.QLabel(AddHouseholdExpense)
        self.label_7.setGeometry(QtCore.QRect(240, 120, 61, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(AddHouseholdExpense)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdExpense.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdExpense.saveExpenditure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdExpense)
        AddHouseholdExpense.setTabOrder(self.cboExpenditure, self.txtUnitOfMeasure)
        AddHouseholdExpense.setTabOrder(self.txtUnitOfMeasure, self.txtKCalPerUnit)
        AddHouseholdExpense.setTabOrder(self.txtKCalPerUnit, self.txtCostPerUnit)
        AddHouseholdExpense.setTabOrder(self.txtCostPerUnit, self.txtNumberOfUnits)
        AddHouseholdExpense.setTabOrder(self.txtNumberOfUnits, self.cmdSave)
        AddHouseholdExpense.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdExpense):
        AddHouseholdExpense.setWindowTitle(QtGui.QApplication.translate("AddHouseholdExpense", "Add Household Expenditure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Cost per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Expenditure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Number of Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdExpense", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdExpense", "KCal per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdExpense", "(optional)", None, QtGui.QApplication.UnicodeUTF8))

