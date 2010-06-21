# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_wildfoods.ui'
#
# Created: Mon Jun 21 12:39:24 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HouseholdIncomeWildfoods(object):
    def setupUi(self, HouseholdIncomeWildfoods):
        HouseholdIncomeWildfoods.setObjectName("HouseholdIncomeWildfoods")
        HouseholdIncomeWildfoods.resize(400, 300)
        self.label_2 = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtUnitPrice = QtGui.QLineEdit(HouseholdIncomeWildfoods)
        self.txtUnitPrice.setGeometry(QtCore.QRect(120, 200, 111, 20))
        self.txtUnitPrice.setObjectName("txtUnitPrice")
        self.cboIncomeType = QtGui.QComboBox(HouseholdIncomeWildfoods)
        self.cboIncomeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName("cboIncomeType")
        self.txtUnitOfMeasure = QtGui.QLineEdit(HouseholdIncomeWildfoods)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 111, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.txtUnitsSold = QtGui.QLineEdit(HouseholdIncomeWildfoods)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 160, 111, 20))
        self.txtUnitsSold.setObjectName("txtUnitsSold")
        self.cmdCancel = QtGui.QPushButton(HouseholdIncomeWildfoods)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 240, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label_6 = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_5.setObjectName("label_5")
        self.txtUnitsConsumed = QtGui.QLineEdit(HouseholdIncomeWildfoods)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 120, 111, 20))
        self.txtUnitsConsumed.setObjectName("txtUnitsConsumed")
        self.lblHouseholdName = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label_3 = QtGui.QLabel(HouseholdIncomeWildfoods)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_3.setObjectName("label_3")
        self.cmdSave = QtGui.QPushButton(HouseholdIncomeWildfoods)
        self.cmdSave.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName("cmdSave")

        self.retranslateUi(HouseholdIncomeWildfoods)
        QtCore.QMetaObject.connectSlotsByName(HouseholdIncomeWildfoods)
        HouseholdIncomeWildfoods.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        HouseholdIncomeWildfoods.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsConsumed)
        HouseholdIncomeWildfoods.setTabOrder(self.txtUnitsConsumed, self.txtUnitsSold)
        HouseholdIncomeWildfoods.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        HouseholdIncomeWildfoods.setTabOrder(self.txtUnitPrice, self.cmdSave)
        HouseholdIncomeWildfoods.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, HouseholdIncomeWildfoods):
        HouseholdIncomeWildfoods.setWindowTitle(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("HouseholdIncomeWildfoods", "Save", None, QtGui.QApplication.UnicodeUTF8))

