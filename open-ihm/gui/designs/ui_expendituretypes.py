# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_expendituretypes.ui'
#
# Created: Fri Apr 22 16:06:03 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExpenditureTypes(object):
    def setupUi(self, ExpenditureTypes):
        ExpenditureTypes.setObjectName(_fromUtf8("ExpenditureTypes"))
        ExpenditureTypes.resize(485, 329)
        ExpenditureTypes.setMinimumSize(QtCore.QSize(419, 297))
        ExpenditureTypes.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.formLayout_2 = QtGui.QFormLayout(ExpenditureTypes)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(ExpenditureTypes)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(ExpenditureTypes)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_4)
        self.expenseTypeListView = QtGui.QListView(ExpenditureTypes)
        self.expenseTypeListView.setAlternatingRowColors(True)
        self.expenseTypeListView.setObjectName(_fromUtf8("expenseTypeListView"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.expenseTypeListView)
        self.txtExpenseType = QtGui.QLineEdit(ExpenditureTypes)
        self.txtExpenseType.setObjectName(_fromUtf8("txtExpenseType"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtExpenseType)
        self.btnExpenseSave = QtGui.QPushButton(ExpenditureTypes)
        self.btnExpenseSave.setObjectName(_fromUtf8("btnExpenseSave"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.btnExpenseSave)
        self.btnExpenseDelete = QtGui.QPushButton(ExpenditureTypes)
        self.btnExpenseDelete.setObjectName(_fromUtf8("btnExpenseDelete"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.btnExpenseDelete)
        self.btnExpenditureClose = QtGui.QPushButton(ExpenditureTypes)
        self.btnExpenditureClose.setObjectName(_fromUtf8("btnExpenditureClose"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.btnExpenditureClose)

        self.retranslateUi(ExpenditureTypes)
        QtCore.QObject.connect(self.btnExpenditureClose, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.mdiClose)
        QtCore.QObject.connect(self.btnExpenseDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.deleteExpenditureType)
        QtCore.QObject.connect(self.btnExpenseSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.saveExpenditureType)
        QtCore.QObject.connect(self.expenseTypeListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ExpenditureTypes.pickSelectedExpenditure)
        QtCore.QMetaObject.connectSlotsByName(ExpenditureTypes)

    def retranslateUi(self, ExpenditureTypes):
        ExpenditureTypes.setWindowTitle(QtGui.QApplication.translate("ExpenditureTypes", "Manage Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExpenditureTypes", "List of Existing Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ExpenditureTypes", "Expenditure Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenseSave.setText(QtGui.QApplication.translate("ExpenditureTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenseDelete.setText(QtGui.QApplication.translate("ExpenditureTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenditureClose.setText(QtGui.QApplication.translate("ExpenditureTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))

