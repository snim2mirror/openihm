# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_wildfoods.ui'
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

class Ui_AddHouseholdIncomeWildfoods(object):
    def setupUi(self, AddHouseholdIncomeWildfoods):
        AddHouseholdIncomeWildfoods.setObjectName(_fromUtf8("AddHouseholdIncomeWildfoods"))
        AddHouseholdIncomeWildfoods.resize(400, 324)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeWildfoods)
        self.cboIncomeType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName(_fromUtf8("cboIncomeType"))
        self.label = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 160, 71, 20))
        self.txtUnitsSold.setObjectName(_fromUtf8("txtUnitsSold"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeWildfoods)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 280, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 151, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeWildfoods)
        self.cmdSave.setGeometry(QtCore.QRect(20, 280, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 240, 71, 20))
        self.txtUnitsConsumed.setObjectName(_fromUtf8("txtUnitsConsumed"))
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitPrice.setGeometry(QtCore.QRect(270, 160, 111, 20))
        self.txtUnitPrice.setObjectName(_fromUtf8("txtUnitPrice"))
        self.label_8 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txtUnitsProduced = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsProduced.setGeometry(QtCore.QRect(120, 120, 71, 20))
        self.txtUnitsProduced.setObjectName(_fromUtf8("txtUnitsProduced"))
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtUnitsOtherUses = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsOtherUses.setGeometry(QtCore.QRect(120, 200, 71, 20))
        self.txtUnitsOtherUses.setObjectName(_fromUtf8("txtUnitsOtherUses"))
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(AddHouseholdIncomeWildfoods)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeWildfoods.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeWildfoods.saveIncome)
        QtCore.QObject.connect(self.cboIncomeType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdIncomeWildfoods.displayUnitOfMeasure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeWildfoods)
        AddHouseholdIncomeWildfoods.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsProduced)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsProduced, self.txtUnitsSold)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitPrice, self.txtUnitsOtherUses)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsOtherUses, self.txtUnitsConsumed)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsConsumed, self.cmdSave)
        AddHouseholdIncomeWildfoods.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeWildfoods):
        AddHouseholdIncomeWildfoods.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Add Wildfoods Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Produced:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Other Uses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Unit:", None, QtGui.QApplication.UnicodeUTF8))

