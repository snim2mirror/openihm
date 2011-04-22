# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_wildfoods.ui'
#
# Created: Fri Apr 22 16:31:22 2011
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
        AddHouseholdIncomeWildfoods.resize(405, 350)
        self.formLayout = QtGui.QFormLayout(AddHouseholdIncomeWildfoods)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblHouseholdName)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeWildfoods)
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName(_fromUtf8("cboIncomeType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboIncomeType)
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtUnitOfMeasure)
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtUnitsProduced = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsProduced.setObjectName(_fromUtf8("txtUnitsProduced"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtUnitsProduced)
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsSold.setObjectName(_fromUtf8("txtUnitsSold"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtUnitsSold)
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitPrice.setObjectName(_fromUtf8("txtUnitPrice"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.txtUnitPrice)
        self.label_8 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.txtUnitsOtherUses = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsOtherUses.setObjectName(_fromUtf8("txtUnitsOtherUses"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtUnitsOtherUses)
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeWildfoods)
        self.txtUnitsConsumed.setObjectName(_fromUtf8("txtUnitsConsumed"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.txtUnitsConsumed)
        self.groupBox = QtGui.QGroupBox(AddHouseholdIncomeWildfoods)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeWildfoods)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)

        self.retranslateUi(AddHouseholdIncomeWildfoods)
        QtCore.QObject.connect(self.cboIncomeType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdIncomeWildfoods.displayUnitOfMeasure)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeWildfoods.saveIncome)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeWildfoods.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeWildfoods)
        AddHouseholdIncomeWildfoods.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsProduced)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsProduced, self.txtUnitsSold)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitPrice, self.txtUnitsOtherUses)
        AddHouseholdIncomeWildfoods.setTabOrder(self.txtUnitsOtherUses, self.txtUnitsConsumed)

    def retranslateUi(self, AddHouseholdIncomeWildfoods):
        AddHouseholdIncomeWildfoods.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Add Wildfoods Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Produced:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Other Uses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeWildfoods", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))

