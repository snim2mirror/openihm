# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addexpense.ui'
#
# Created: Thu Apr 21 19:28:06 2011
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
        self.formLayout = QtGui.QFormLayout(AddHouseholdExpense)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AddHouseholdExpense)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdExpense)
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblHouseholdName)
        self.label_2 = QtGui.QLabel(AddHouseholdExpense)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cboExpenditure = QtGui.QComboBox(AddHouseholdExpense)
        self.cboExpenditure.setEditable(True)
        self.cboExpenditure.setObjectName(_fromUtf8("cboExpenditure"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboExpenditure)
        self.label_4 = QtGui.QLabel(AddHouseholdExpense)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtUnitOfMeasure)
        self.label_3 = QtGui.QLabel(AddHouseholdExpense)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtKCalPerUnit = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtKCalPerUnit.setObjectName(_fromUtf8("txtKCalPerUnit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtKCalPerUnit)
        self.label_7 = QtGui.QLabel(AddHouseholdExpense)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_7)
        self.label_5 = QtGui.QLabel(AddHouseholdExpense)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtCostPerUnit = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtCostPerUnit.setObjectName(_fromUtf8("txtCostPerUnit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtCostPerUnit)
        self.label_6 = QtGui.QLabel(AddHouseholdExpense)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtNumberOfUnits = QtGui.QLineEdit(AddHouseholdExpense)
        self.txtNumberOfUnits.setObjectName(_fromUtf8("txtNumberOfUnits"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.txtNumberOfUnits)
        self.groupBox = QtGui.QGroupBox(AddHouseholdExpense)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.groupBox)

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
        self.label.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdExpense", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Expenditure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdExpense", "KCal per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdExpense", "(optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Cost per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Number of Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdExpense", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

