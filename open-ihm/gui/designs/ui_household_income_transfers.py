# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_transfers.ui'
#
# Created: Mon Jun 21 12:40:24 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HouseholdIncomeTransfers(object):
    def setupUi(self, HouseholdIncomeTransfers):
        HouseholdIncomeTransfers.setObjectName("HouseholdIncomeTransfers")
        HouseholdIncomeTransfers.resize(440, 322)
        self.cmdSave = QtGui.QPushButton(HouseholdIncomeTransfers)
        self.cmdSave.setGeometry(QtCore.QRect(20, 280, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName("cmdSave")
        self.txtCashPerDist = QtGui.QLineEdit(HouseholdIncomeTransfers)
        self.txtCashPerDist.setGeometry(QtCore.QRect(160, 200, 111, 20))
        self.txtCashPerDist.setObjectName("txtCashPerDist")
        self.lblHouseholdName = QtGui.QLabel(HouseholdIncomeTransfers)
        self.lblHouseholdName.setGeometry(QtCore.QRect(160, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.cmdCancel = QtGui.QPushButton(HouseholdIncomeTransfers)
        self.cmdCancel.setGeometry(QtCore.QRect(350, 280, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label_3 = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 111, 21))
        self.label_6.setObjectName("label_6")
        self.txtUnitofMeasure = QtGui.QLineEdit(HouseholdIncomeTransfers)
        self.txtUnitofMeasure.setGeometry(QtCore.QRect(160, 80, 111, 20))
        self.txtUnitofMeasure.setObjectName("txtUnitofMeasure")
        self.label = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.txtFoodPerDist = QtGui.QLineEdit(HouseholdIncomeTransfers)
        self.txtFoodPerDist.setGeometry(QtCore.QRect(160, 120, 111, 20))
        self.txtFoodPerDist.setObjectName("txtFoodPerDist")
        self.label_2 = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.cboAssistanceType = QtGui.QComboBox(HouseholdIncomeTransfers)
        self.cboAssistanceType.setGeometry(QtCore.QRect(160, 40, 271, 22))
        self.cboAssistanceType.setEditable(True)
        self.cboAssistanceType.setObjectName("cboAssistanceType")
        self.label_5 = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 111, 21))
        self.label_5.setObjectName("label_5")
        self.txtNumReceived = QtGui.QLineEdit(HouseholdIncomeTransfers)
        self.txtNumReceived.setGeometry(QtCore.QRect(160, 160, 111, 20))
        self.txtNumReceived.setObjectName("txtNumReceived")
        self.label_4 = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 131, 21))
        self.label_4.setObjectName("label_4")
        self.txtCashPerYear = QtGui.QLineEdit(HouseholdIncomeTransfers)
        self.txtCashPerYear.setGeometry(QtCore.QRect(160, 240, 111, 20))
        self.txtCashPerYear.setObjectName("txtCashPerYear")
        self.label_7 = QtGui.QLabel(HouseholdIncomeTransfers)
        self.label_7.setGeometry(QtCore.QRect(20, 240, 101, 21))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(HouseholdIncomeTransfers)
        QtCore.QMetaObject.connectSlotsByName(HouseholdIncomeTransfers)
        HouseholdIncomeTransfers.setTabOrder(self.cboAssistanceType, self.txtUnitofMeasure)
        HouseholdIncomeTransfers.setTabOrder(self.txtUnitofMeasure, self.txtFoodPerDist)
        HouseholdIncomeTransfers.setTabOrder(self.txtFoodPerDist, self.txtNumReceived)
        HouseholdIncomeTransfers.setTabOrder(self.txtNumReceived, self.txtCashPerDist)
        HouseholdIncomeTransfers.setTabOrder(self.txtCashPerDist, self.txtCashPerYear)
        HouseholdIncomeTransfers.setTabOrder(self.txtCashPerYear, self.cmdSave)
        HouseholdIncomeTransfers.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, HouseholdIncomeTransfers):
        HouseholdIncomeTransfers.setWindowTitle(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Cash per Distribution:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Assistance Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Food per Distribution:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Number of Times Received:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("HouseholdIncomeTransfers", "Cash per Year:", None, QtGui.QApplication.UnicodeUTF8))

