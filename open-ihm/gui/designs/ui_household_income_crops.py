# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_crops.ui'
#
# Created: Mon Jun 21 17:51:51 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdIncomeCrops(object):
    def setupUi(self, AddHouseholdIncomeCrops):
        AddHouseholdIncomeCrops.setObjectName("AddHouseholdIncomeCrops")
        AddHouseholdIncomeCrops.resize(400, 300)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitPrice.setGeometry(QtCore.QRect(120, 200, 111, 20))
        self.txtUnitPrice.setObjectName("txtUnitPrice")
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeCrops)
        self.cboIncomeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName("cboIncomeType")
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 111, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 160, 111, 20))
        self.txtUnitsSold.setObjectName("txtUnitsSold")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeCrops)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 240, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_5.setObjectName("label_5")
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 120, 111, 20))
        self.txtUnitsConsumed.setObjectName("txtUnitsConsumed")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_3.setObjectName("label_3")
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeCrops)
        self.cmdSave.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName("cmdSave")

        self.retranslateUi(AddHouseholdIncomeCrops)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeCrops)
        AddHouseholdIncomeCrops.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsConsumed)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitsConsumed, self.txtUnitsSold)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitPrice, self.cmdSave)
        AddHouseholdIncomeCrops.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeCrops):
        AddHouseholdIncomeCrops.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Add Crop Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Save", None, QtGui.QApplication.UnicodeUTF8))

