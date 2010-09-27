# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_currencymanager.ui'
#
# Created: Mon Sep 27 18:00:30 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CurrencyManager(object):
    def setupUi(self, CurrencyManager):
        CurrencyManager.setObjectName("CurrencyManager")
        CurrencyManager.resize(694, 334)
        CurrencyManager.setMinimumSize(QtCore.QSize(694, 334))
        self.tblCurrencies = QtGui.QTableView(CurrencyManager)
        self.tblCurrencies.setGeometry(QtCore.QRect(10, 30, 381, 291))
        self.tblCurrencies.setObjectName("tblCurrencies")
        self.cmdDelete = QtGui.QPushButton(CurrencyManager)
        self.cmdDelete.setGeometry(QtCore.QRect(400, 290, 81, 31))
        self.cmdDelete.setObjectName("cmdDelete")
        self.cmdClose = QtGui.QPushButton(CurrencyManager)
        self.cmdClose.setGeometry(QtCore.QRect(600, 290, 81, 31))
        self.cmdClose.setObjectName("cmdClose")
        self.groupBox = QtGui.QGroupBox(CurrencyManager)
        self.groupBox.setGeometry(QtCore.QRect(400, 30, 281, 181))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtCurrencyName = QtGui.QLineEdit(self.groupBox)
        self.txtCurrencyName.setGeometry(QtCore.QRect(100, 30, 171, 20))
        self.txtCurrencyName.setObjectName("txtCurrencyName")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 46, 21))
        self.label_3.setObjectName("label_3")
        self.txtSymbol = QtGui.QLineEdit(self.groupBox)
        self.txtSymbol.setGeometry(QtCore.QRect(100, 110, 171, 20))
        self.txtSymbol.setObjectName("txtSymbol")
        self.txtAbbreviation = QtGui.QLineEdit(self.groupBox)
        self.txtAbbreviation.setGeometry(QtCore.QRect(100, 70, 171, 20))
        self.txtAbbreviation.setObjectName("txtAbbreviation")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setObjectName("label")
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setGeometry(QtCore.QRect(190, 140, 81, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.label_4 = QtGui.QLabel(CurrencyManager)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(CurrencyManager)
        QtCore.QMetaObject.connectSlotsByName(CurrencyManager)

    def retranslateUi(self, CurrencyManager):
        CurrencyManager.setWindowTitle(QtGui.QApplication.translate("CurrencyManager", "Manage Currencies", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("CurrencyManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("CurrencyManager", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CurrencyManager", "Abbreviation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CurrencyManager", "Symbol:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CurrencyManager", "Currency Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("CurrencyManager", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CurrencyManager", "Available Currencies", None, QtGui.QApplication.UnicodeUTF8))

