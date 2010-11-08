# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_employment.ui'
#
# Created: Mon Nov 08 18:57:53 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdIncomeEmployment(object):
    def setupUi(self, AddHouseholdIncomeEmployment):
        AddHouseholdIncomeEmployment.setObjectName(_fromUtf8("AddHouseholdIncomeEmployment"))
        AddHouseholdIncomeEmployment.resize(450, 342)
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.lblHouseholdName.setGeometry(QtCore.QRect(130, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.txtCashPaid = QtGui.QLineEdit(AddHouseholdIncomeEmployment)
        self.txtCashPaid.setGeometry(QtCore.QRect(130, 80, 111, 20))
        self.txtCashPaid.setObjectName(_fromUtf8("txtCashPaid"))
        self.cboEmploymentType = QtGui.QComboBox(AddHouseholdIncomeEmployment)
        self.cboEmploymentType.setGeometry(QtCore.QRect(130, 40, 301, 22))
        self.cboEmploymentType.setEditable(True)
        self.cboEmploymentType.setObjectName(_fromUtf8("cboEmploymentType"))
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 101, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeEmployment)
        self.cmdSave.setGeometry(QtCore.QRect(20, 300, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeEmployment)
        self.cmdCancel.setGeometry(QtCore.QRect(350, 300, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.groupBox = QtGui.QGroupBox(AddHouseholdIncomeEmployment)
        self.groupBox.setGeometry(QtCore.QRect(20, 110, 411, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 131, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtUnitsPaid = QtGui.QLineEdit(self.groupBox)
        self.txtUnitsPaid.setGeometry(QtCore.QRect(110, 100, 111, 20))
        self.txtUnitsPaid.setObjectName(_fromUtf8("txtUnitsPaid"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(self.groupBox)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(110, 60, 111, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtTotalEnergyValue = QtGui.QLineEdit(self.groupBox)
        self.txtTotalEnergyValue.setGeometry(QtCore.QRect(160, 140, 111, 20))
        self.txtTotalEnergyValue.setObjectName(_fromUtf8("txtTotalEnergyValue"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 131, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cboFoodType = QtGui.QComboBox(self.groupBox)
        self.cboFoodType.setGeometry(QtCore.QRect(110, 20, 291, 22))
        self.cboFoodType.setEditable(True)
        self.cboFoodType.setObjectName(_fromUtf8("cboFoodType"))

        self.retranslateUi(AddHouseholdIncomeEmployment)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeEmployment)
        AddHouseholdIncomeEmployment.setTabOrder(self.cboEmploymentType, self.txtCashPaid)
        AddHouseholdIncomeEmployment.setTabOrder(self.txtCashPaid, self.cboFoodType)
        AddHouseholdIncomeEmployment.setTabOrder(self.cboFoodType, self.txtUnitOfMeasure)
        AddHouseholdIncomeEmployment.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsPaid)
        AddHouseholdIncomeEmployment.setTabOrder(self.txtUnitsPaid, self.txtTotalEnergyValue)
        AddHouseholdIncomeEmployment.setTabOrder(self.txtTotalEnergyValue, self.cmdSave)
        AddHouseholdIncomeEmployment.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeEmployment):
        AddHouseholdIncomeEmployment.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Add Employment Income", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Cash Paid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Employment Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Food Payment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Total Energy Value (KCals):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Units Paid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Food Type Paid:", None, QtGui.QApplication.UnicodeUTF8))

