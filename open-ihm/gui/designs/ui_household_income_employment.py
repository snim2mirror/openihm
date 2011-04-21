# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_employment.ui'
#
# Created: Thu Apr 21 19:28:07 2011
#      by: PyQt4 UI code generator 4.8.3
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
        AddHouseholdIncomeEmployment.resize(452, 370)
        self.formLayout_2 = QtGui.QFormLayout(AddHouseholdIncomeEmployment)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblHouseholdName)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cboEmploymentType = QtGui.QComboBox(AddHouseholdIncomeEmployment)
        self.cboEmploymentType.setEditable(True)
        self.cboEmploymentType.setObjectName(_fromUtf8("cboEmploymentType"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboEmploymentType)
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeEmployment)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtCashPaid = QtGui.QLineEdit(AddHouseholdIncomeEmployment)
        self.txtCashPaid.setObjectName(_fromUtf8("txtCashPaid"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtCashPaid)
        self.groupBox = QtGui.QGroupBox(AddHouseholdIncomeEmployment)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cboFoodType = QtGui.QComboBox(self.groupBox)
        self.cboFoodType.setEditable(True)
        self.cboFoodType.setObjectName(_fromUtf8("cboFoodType"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboFoodType)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtUnitOfMeasure = QtGui.QLineEdit(self.groupBox)
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtUnitOfMeasure)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtUnitsPaid = QtGui.QLineEdit(self.groupBox)
        self.txtUnitsPaid.setObjectName(_fromUtf8("txtUnitsPaid"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtUnitsPaid)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.label_6)
        self.txtTotalEnergyValue = QtGui.QLineEdit(self.groupBox)
        self.txtTotalEnergyValue.setObjectName(_fromUtf8("txtTotalEnergyValue"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtTotalEnergyValue)
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(AddHouseholdIncomeEmployment)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox_2)
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox_2)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox_2)

        self.retranslateUi(AddHouseholdIncomeEmployment)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeEmployment.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeEmployment.saveIncome)
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
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Employment Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Cash Paid:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Food Payment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Food Type Paid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Units Paid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Total Energy Value (KCals):", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeEmployment", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

