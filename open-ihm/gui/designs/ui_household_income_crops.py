# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_crops.ui'
#
# Created: Tue Apr 19 08:09:03 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdIncomeCrops(object):
    def setupUi(self, AddHouseholdIncomeCrops):
        AddHouseholdIncomeCrops.setObjectName(_fromUtf8("AddHouseholdIncomeCrops"))
        AddHouseholdIncomeCrops.resize(400, 322)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitPrice.setGeometry(QtCore.QRect(270, 160, 111, 20))
        self.txtUnitPrice.setObjectName(_fromUtf8("txtUnitPrice"))
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeCrops)
        self.cboIncomeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName(_fromUtf8("cboIncomeType"))
        self.txtUnitsProduced = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitsProduced.setGeometry(QtCore.QRect(120, 120, 71, 20))
        self.txtUnitsProduced.setObjectName(_fromUtf8("txtUnitsProduced"))
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 240, 71, 20))
        self.txtUnitsConsumed.setObjectName(_fromUtf8("txtUnitsConsumed"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeCrops)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 280, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 160, 71, 20))
        self.txtUnitsSold.setObjectName(_fromUtf8("txtUnitsSold"))
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeCrops)
        self.cmdSave.setGeometry(QtCore.QRect(20, 280, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 151, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.txtUnitsOtherUses = QtGui.QLineEdit(AddHouseholdIncomeCrops)
        self.txtUnitsOtherUses.setGeometry(QtCore.QRect(120, 200, 71, 20))
        self.txtUnitsOtherUses.setObjectName(_fromUtf8("txtUnitsOtherUses"))
        self.label_8 = QtGui.QLabel(AddHouseholdIncomeCrops)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(AddHouseholdIncomeCrops)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeCrops.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeCrops.saveIncome)
        QtCore.QObject.connect(self.cboIncomeType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdIncomeCrops.displayUnitOfMeasure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeCrops)
        AddHouseholdIncomeCrops.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsProduced)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitsProduced, self.txtUnitsSold)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitPrice, self.txtUnitsOtherUses)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitsOtherUses, self.txtUnitsConsumed)
        AddHouseholdIncomeCrops.setTabOrder(self.txtUnitsConsumed, self.cmdSave)
        AddHouseholdIncomeCrops.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeCrops):
        AddHouseholdIncomeCrops.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Add Crop Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Units Produced:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddHouseholdIncomeCrops", "Other Uses:", None, QtGui.QApplication.UnicodeUTF8))

