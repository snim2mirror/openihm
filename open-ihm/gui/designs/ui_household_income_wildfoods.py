# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_wildfoods.ui'
#
# Created: Mon Jun 21 23:14:28 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdIncomeWildfoods(object):
    def setupUi(self, AddHouseholdIncomeWildfoods):
        AddHouseholdIncomeWildfoods.setObjectName("AddHouseholdIncomeWildfoods")
        AddHouseholdIncomeWildfoods.resize(400, 300)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitPrice.setGeometry(QtCore.QRect(120, 200, 111, 20))
        self.txtUnitPrice.setObjectName("txtUnitPrice")
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeWildfoods)
        self.cboIncomeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName("cboIncomeType")
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 111, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 160, 111, 20))
        self.txtUnitsSold.setObjectName("txtUnitsSold")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeWildfoods)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 240, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_5.setObjectName("label_5")
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 120, 111, 20))
        self.txtUnitsConsumed.setObjectName("txtUnitsConsumed")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_3.setObjectName("label_3")
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeWildfoods)
        self.cmdSave.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName("cmdSave")

        self.retranslateUi(AddHouseholdIncomeWildfoods)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeWildfoods)
        AddHouseholdIncomeWildfoods.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsConsumed)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsConsumed, self.txtUnitsSold)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitPrice, self.cmdSave)
        AddHouseholdIncomeWildfoods.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeWildfoods):
        AddHouseholdIncomeWildfoods.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Add Wildfoods Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Save", None, QtGui.QApplication.UnicodeUTF8))

