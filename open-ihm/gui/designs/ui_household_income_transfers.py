# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_transfers.ui'
#
# Created: Tue Jun 22 23:36:51 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdIncomeTransfers(object):
    def setupUi(self, AddHouseholdIncomeTransfers):
        AddHouseholdIncomeTransfers.setObjectName("AddHouseholdIncomeTransfers")
        AddHouseholdIncomeTransfers.resize(440, 322)
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeTransfers)
        self.cmdSave.setGeometry(QtCore.QRect(20, 280, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName("cmdSave")
        self.txtCashPerDist = QtGui.QLineEdit(AddHouseholdIncomeTransfers)
        self.txtCashPerDist.setGeometry(QtCore.QRect(160, 200, 111, 20))
        self.txtCashPerDist.setObjectName("txtCashPerDist")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.lblHouseholdName.setGeometry(QtCore.QRect(160, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeTransfers)
        self.cmdCancel.setGeometry(QtCore.QRect(350, 280, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 111, 21))
        self.label_6.setObjectName("label_6")
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeTransfers)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(160, 80, 111, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.label = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.txtFoodPerDist = QtGui.QLineEdit(AddHouseholdIncomeTransfers)
        self.txtFoodPerDist.setGeometry(QtCore.QRect(160, 120, 111, 20))
        self.txtFoodPerDist.setObjectName("txtFoodPerDist")
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.cboAssistanceType = QtGui.QComboBox(AddHouseholdIncomeTransfers)
        self.cboAssistanceType.setGeometry(QtCore.QRect(160, 40, 271, 22))
        self.cboAssistanceType.setEditable(True)
        self.cboAssistanceType.setObjectName("cboAssistanceType")
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 111, 21))
        self.label_5.setObjectName("label_5")
        self.txtNumReceived = QtGui.QLineEdit(AddHouseholdIncomeTransfers)
        self.txtNumReceived.setGeometry(QtCore.QRect(160, 160, 111, 20))
        self.txtNumReceived.setObjectName("txtNumReceived")
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 131, 21))
        self.label_4.setObjectName("label_4")
        self.txtCashPerYear = QtGui.QLineEdit(AddHouseholdIncomeTransfers)
        self.txtCashPerYear.setGeometry(QtCore.QRect(160, 240, 111, 20))
        self.txtCashPerYear.setObjectName("txtCashPerYear")
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_7.setGeometry(QtCore.QRect(20, 240, 101, 21))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(AddHouseholdIncomeTransfers)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeTransfers)
        AddHouseholdIncomeTransfers.setTabOrder(self.cboAssistanceType, self.txtUnitOfMeasure)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtUnitOfMeasure, self.txtFoodPerDist)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtFoodPerDist, self.txtNumReceived)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtNumReceived, self.txtCashPerDist)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtCashPerDist, self.txtCashPerYear)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtCashPerYear, self.cmdSave)
        AddHouseholdIncomeTransfers.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeTransfers):
        AddHouseholdIncomeTransfers.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Add Transfer Income", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Cash per Distribution:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Assistance Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Food per Distribution:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Number of Times Received:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Cash per Year:", None, QtGui.QApplication.UnicodeUTF8))

