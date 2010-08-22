# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_expendituretypes.ui'
#
# Created: Mon Jun 07 23:51:45 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ExpenditureTypes(object):
    def setupUi(self, ExpenditureTypes):
        ExpenditureTypes.setObjectName("ExpenditureTypes")
        ExpenditureTypes.resize(419, 297)
        ExpenditureTypes.setMinimumSize(QtCore.QSize(419, 297))
        ExpenditureTypes.setMaximumSize(QtCore.QSize(419, 16777215))
        self.btnExpenditureClose = QtGui.QPushButton(ExpenditureTypes)
        self.btnExpenditureClose.setGeometry(QtCore.QRect(330, 260, 80, 28))
        self.btnExpenditureClose.setObjectName("btnExpenditureClose")
        self.expenseCategoryListView = QtGui.QTabWidget(ExpenditureTypes)
        self.expenseCategoryListView.setGeometry(QtCore.QRect(0, 0, 411, 251))
        self.expenseCategoryListView.setObjectName("expenseCategoryListView")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 111, 18))
        self.label_2.setObjectName("label_2")
        self.btnExpenseDelete = QtGui.QPushButton(self.tab)
        self.btnExpenseDelete.setGeometry(QtCore.QRect(320, 90, 80, 28))
        self.btnExpenseDelete.setObjectName("btnExpenseDelete")
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 18))
        self.label.setObjectName("label")
        self.txtExpenseType = QtGui.QLineEdit(self.tab)
        self.txtExpenseType.setGeometry(QtCore.QRect(210, 30, 191, 28))
        self.txtExpenseType.setObjectName("txtExpenseType")
        self.btnExpenseSave = QtGui.QPushButton(self.tab)
        self.btnExpenseSave.setGeometry(QtCore.QRect(220, 90, 81, 28))
        self.btnExpenseSave.setObjectName("btnExpenseSave")
        self.expenseTypeListView = QtGui.QListView(self.tab)
        self.expenseTypeListView.setGeometry(QtCore.QRect(10, 30, 191, 191))
        self.expenseTypeListView.setObjectName("expenseTypeListView")
        self.expenseCategoryListView.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.expenditureCategorylistView = QtGui.QListView(self.tab_2)
        self.expenditureCategorylistView.setGeometry(QtCore.QRect(10, 30, 191, 191))
        self.expenditureCategorylistView.setObjectName("expenditureCategorylistView")
        self.btnCategorySave = QtGui.QPushButton(self.tab_2)
        self.btnCategorySave.setGeometry(QtCore.QRect(220, 90, 81, 28))
        self.btnCategorySave.setObjectName("btnCategorySave")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 111, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 191, 18))
        self.label_4.setObjectName("label_4")
        self.btnCategoryDelete = QtGui.QPushButton(self.tab_2)
        self.btnCategoryDelete.setGeometry(QtCore.QRect(320, 90, 80, 28))
        self.btnCategoryDelete.setObjectName("btnCategoryDelete")
        self.txtCategory = QtGui.QLineEdit(self.tab_2)
        self.txtCategory.setGeometry(QtCore.QRect(210, 30, 191, 28))
        self.txtCategory.setObjectName("txtCategory")
        self.expenseCategoryListView.addTab(self.tab_2, "")

        self.retranslateUi(ExpenditureTypes)
        self.expenseCategoryListView.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ExpenditureTypes)

    def retranslateUi(self, ExpenditureTypes):
        ExpenditureTypes.setWindowTitle(QtGui.QApplication.translate("ExpenditureTypes", "Manage Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenditureClose.setText(QtGui.QApplication.translate("ExpenditureTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExpenditureTypes", "Expenditure Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenseDelete.setText(QtGui.QApplication.translate("ExpenditureTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExpenditureTypes", "List of Existing Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenseSave.setText(QtGui.QApplication.translate("ExpenditureTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.expenseCategoryListView.setTabText(self.expenseCategoryListView.indexOf(self.tab), QtGui.QApplication.translate("ExpenditureTypes", "Individual Expense Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCategorySave.setText(QtGui.QApplication.translate("ExpenditureTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExpenditureTypes", "Expenditure Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ExpenditureTypes", "List of Existing Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCategoryDelete.setText(QtGui.QApplication.translate("ExpenditureTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.expenseCategoryListView.setTabText(self.expenseCategoryListView.indexOf(self.tab_2), QtGui.QApplication.translate("ExpenditureTypes", "Main Expense Categories", None, QtGui.QApplication.UnicodeUTF8))

