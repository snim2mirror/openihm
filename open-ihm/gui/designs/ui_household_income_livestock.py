# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_livestock.ui'
#
# Created: Tue Apr 19 08:13:16 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdIncomeLivestock(object):
    def setupUi(self, AddHouseholdIncomeLivestock):
        AddHouseholdIncomeLivestock.setObjectName(_fromUtf8("AddHouseholdIncomeLivestock"))
        AddHouseholdIncomeLivestock.resize(400, 322)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeLivestock)
        self.cboIncomeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName(_fromUtf8("cboIncomeType"))
        self.label = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 160, 71, 20))
        self.txtUnitsSold.setObjectName(_fromUtf8("txtUnitsSold"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeLivestock)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 280, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 151, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeLivestock)
        self.cmdSave.setGeometry(QtCore.QRect(20, 280, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 240, 71, 20))
        self.txtUnitsConsumed.setObjectName(_fromUtf8("txtUnitsConsumed"))
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitPrice.setGeometry(QtCore.QRect(270, 160, 111, 20))
        self.txtUnitPrice.setObjectName(_fromUtf8("txtUnitPrice"))
        self.label_8 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txtUnitsProduced = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsProduced.setGeometry(QtCore.QRect(120, 120, 71, 20))
        self.txtUnitsProduced.setObjectName(_fromUtf8("txtUnitsProduced"))
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtUnitsOtherUses = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsOtherUses.setGeometry(QtCore.QRect(120, 200, 71, 20))
        self.txtUnitsOtherUses.setObjectName(_fromUtf8("txtUnitsOtherUses"))
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(AddHouseholdIncomeLivestock)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeLivestock.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeLivestock.saveIncome)
        QtCore.QObject.connect(self.cboIncomeType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdIncomeLivestock.displayUnitOfMeasure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeLivestock)
        AddHouseholdIncomeLivestock.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsProduced)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsProduced, self.txtUnitsSold)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitPrice, self.txtUnitsOtherUses)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsOtherUses, self.txtUnitsConsumed)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsConsumed, self.cmdSave)
        AddHouseholdIncomeLivestock.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeLivestock):
        AddHouseholdIncomeLivestock.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Add Livestock Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Units Produced:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Other Uses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Unit:", None, QtGui.QApplication.UnicodeUTF8))

