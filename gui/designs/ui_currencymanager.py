# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_currencymanager.ui'
#
# Created: Fri Apr 22 23:46:28 2011
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
        self.gridLayout = QtGui.QGridLayout(CurrencyManager)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(CurrencyManager)
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
        self.gridLayout.addWidget(self.groupBox, 0, 1, 3, 1)
        self.groupBox_2 = QtGui.QGroupBox(CurrencyManager)
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
        self.gridLayout.addWidget(self.groupBox_2, 3, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(CurrencyManager)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tblCurrencies = QtGui.QTableView(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblCurrencies.sizePolicy().hasHeightForWidth())
        self.tblCurrencies.setSizePolicy(sizePolicy)
        self.tblCurrencies.setAlternatingRowColors(True)
        self.tblCurrencies.setSortingEnabled(True)
        self.tblCurrencies.setObjectName(_fromUtf8("tblCurrencies"))
        self.verticalLayout.addWidget(self.tblCurrencies)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 4, 1)
        self.label.setBuddy(self.txtCurrencyName)
        self.label_2.setBuddy(self.txtAbbreviation)
        self.label_3.setBuddy(self.txtSymbol)

        self.retranslateUi(CurrencyManager)
        QtCore.QObject.connect(self.tblCurrencies, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), CurrencyManager.showSelectedCurrency)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), CurrencyManager.mdiClose)
        QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), CurrencyManager.delCurrencies)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), CurrencyManager.saveCurrency)
        QtCore.QMetaObject.connectSlotsByName(CurrencyManager)
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
        self.cmdSave.setText(QtGui.QApplication.translate("CurrencyManager", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("CurrencyManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("CurrencyManager", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("CurrencyManager", "Available Currencies", None, QtGui.QApplication.UnicodeUTF8))

