# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_currencymanager.ui'
#
# Created: Fri Apr 22 21:52:26 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CurrencyManager(object):
    def setupUi(self, CurrencyManager):
        CurrencyManager.setObjectName(_fromUtf8("CurrencyManager"))
        CurrencyManager.resize(640, 250)
        CurrencyManager.setMinimumSize(QtCore.QSize(640, 250))
        self.groupBox = QtGui.QGroupBox(CurrencyManager)
        self.groupBox.setGeometry(QtCore.QRect(310, 20, 314, 132))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtCurrencyName = QtGui.QLineEdit(self.groupBox)
        self.txtCurrencyName.setObjectName(_fromUtf8("txtCurrencyName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtCurrencyName)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtAbbreviation = QtGui.QLineEdit(self.groupBox)
        self.txtAbbreviation.setObjectName(_fromUtf8("txtAbbreviation"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtAbbreviation)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtSymbol = QtGui.QLineEdit(self.groupBox)
        self.txtSymbol.setObjectName(_fromUtf8("txtSymbol"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtSymbol)
        self.label_4 = QtGui.QLabel(CurrencyManager)
        self.label_4.setGeometry(QtCore.QRect(9, 9, 170, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tblCurrencies = QtGui.QTableView(CurrencyManager)
        self.tblCurrencies.setGeometry(QtCore.QRect(9, 33, 256, 192))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblCurrencies.sizePolicy().hasHeightForWidth())
        self.tblCurrencies.setSizePolicy(sizePolicy)
        self.tblCurrencies.setAlternatingRowColors(True)
        self.tblCurrencies.setSortingEnabled(True)
        self.tblCurrencies.setObjectName(_fromUtf8("tblCurrencies"))
        self.groupBox_2 = QtGui.QGroupBox(CurrencyManager)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 160, 349, 71))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox_2)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdDelete = QtGui.QPushButton(self.groupBox_2)
        self.cmdDelete.setObjectName(_fromUtf8("cmdDelete"))
        self.horizontalLayout.addWidget(self.cmdDelete)
        self.cmdClose = QtGui.QPushButton(self.groupBox_2)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.label.setBuddy(self.txtCurrencyName)
        self.label_2.setBuddy(self.txtAbbreviation)
        self.label_3.setBuddy(self.txtSymbol)
        self.label_4.setBuddy(self.tblCurrencies)

        self.retranslateUi(CurrencyManager)
        QtCore.QObject.connect(self.tblCurrencies, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), CurrencyManager.showSelectedCurrency)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), CurrencyManager.mdiClose)
        QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), CurrencyManager.delCurrencies)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), CurrencyManager.saveCurrency)
        QtCore.QMetaObject.connectSlotsByName(CurrencyManager)
        CurrencyManager.setTabOrder(self.tblCurrencies, self.txtCurrencyName)
        CurrencyManager.setTabOrder(self.txtCurrencyName, self.txtAbbreviation)
        CurrencyManager.setTabOrder(self.txtAbbreviation, self.txtSymbol)
        CurrencyManager.setTabOrder(self.txtSymbol, self.cmdSave)
        CurrencyManager.setTabOrder(self.cmdSave, self.cmdDelete)
        CurrencyManager.setTabOrder(self.cmdDelete, self.cmdClose)

    def retranslateUi(self, CurrencyManager):
        CurrencyManager.setWindowTitle(QtGui.QApplication.translate("CurrencyManager", "Manage Currencies", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CurrencyManager", "Currency Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CurrencyManager", "Abbreviation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CurrencyManager", "Symbol:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CurrencyManager", "Available Currencies", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("CurrencyManager", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("CurrencyManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("CurrencyManager", "Close", None, QtGui.QApplication.UnicodeUTF8))

