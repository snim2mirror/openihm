# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_expendituretypes.ui'
#
# Created: Tue Apr 19 08:09:02 2011
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
        ExpenditureTypes.resize(419, 297)
        ExpenditureTypes.setMinimumSize(QtCore.QSize(419, 297))
        ExpenditureTypes.setMaximumSize(QtCore.QSize(419, 16777215))
        self.btnExpenditureClose = QtGui.QPushButton(ExpenditureTypes)
        self.btnExpenditureClose.setGeometry(QtCore.QRect(330, 260, 80, 28))
        self.btnExpenditureClose.setObjectName(_fromUtf8("btnExpenditureClose"))
        self.expenseCategoryListView = QtGui.QTabWidget(ExpenditureTypes)
        self.expenseCategoryListView.setGeometry(QtCore.QRect(0, 0, 411, 251))
        self.expenseCategoryListView.setObjectName(_fromUtf8("expenseCategoryListView"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 111, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnExpenseDelete = QtGui.QPushButton(self.tab)
        self.btnExpenseDelete.setGeometry(QtCore.QRect(320, 90, 80, 28))
        self.btnExpenseDelete.setObjectName(_fromUtf8("btnExpenseDelete"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtExpenseType = QtGui.QLineEdit(self.tab)
        self.txtExpenseType.setGeometry(QtCore.QRect(210, 30, 191, 28))
        self.txtExpenseType.setObjectName(_fromUtf8("txtExpenseType"))
        self.btnExpenseSave = QtGui.QPushButton(self.tab)
        self.btnExpenseSave.setGeometry(QtCore.QRect(220, 90, 81, 28))
        self.btnExpenseSave.setObjectName(_fromUtf8("btnExpenseSave"))
        self.expenseTypeListView = QtGui.QListView(self.tab)
        self.expenseTypeListView.setGeometry(QtCore.QRect(10, 30, 191, 191))
        self.expenseTypeListView.setObjectName(_fromUtf8("expenseTypeListView"))
        self.expenseCategoryListView.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.expenditureCategorylistView = QtGui.QListView(self.tab_2)
        self.expenditureCategorylistView.setGeometry(QtCore.QRect(10, 30, 191, 191))
        self.expenditureCategorylistView.setObjectName(_fromUtf8("expenditureCategorylistView"))
        self.btnCategorySave = QtGui.QPushButton(self.tab_2)
        self.btnCategorySave.setGeometry(QtCore.QRect(220, 90, 81, 28))
        self.btnCategorySave.setObjectName(_fromUtf8("btnCategorySave"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 111, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 191, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnCategoryDelete = QtGui.QPushButton(self.tab_2)
        self.btnCategoryDelete.setGeometry(QtCore.QRect(320, 90, 80, 28))
        self.btnCategoryDelete.setObjectName(_fromUtf8("btnCategoryDelete"))
        self.txtCategory = QtGui.QLineEdit(self.tab_2)
        self.txtCategory.setGeometry(QtCore.QRect(210, 30, 191, 28))
        self.txtCategory.setObjectName(_fromUtf8("txtCategory"))
        self.expenseCategoryListView.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(ExpenditureTypes)
        self.expenseCategoryListView.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnExpenditureClose, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.mdiClose)
        QtCore.QObject.connect(self.btnExpenseSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.saveExpenditureType)
        QtCore.QObject.connect(self.btnExpenseDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.deleteExpenditureType)
        QtCore.QObject.connect(self.expenseTypeListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ExpenditureTypes.pickSelectedExpenditure)
        QtCore.QObject.connect(self.btnCategorySave, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.saveCategoryType)
        QtCore.QObject.connect(self.btnCategoryDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ExpenditureTypes.deleteCategoryType)
        QtCore.QObject.connect(self.expenditureCategorylistView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ExpenditureTypes.pickSelectedCategory)
        QtCore.QMetaObject.connectSlotsByName(ExpenditureTypes)
        ExpenditureTypes.setTabOrder(self.expenseCategoryListView, self.expenseTypeListView)
        ExpenditureTypes.setTabOrder(self.expenseTypeListView, self.txtExpenseType)
        ExpenditureTypes.setTabOrder(self.txtExpenseType, self.btnExpenseSave)
        ExpenditureTypes.setTabOrder(self.btnExpenseSave, self.expenditureCategorylistView)
        ExpenditureTypes.setTabOrder(self.expenditureCategorylistView, self.txtCategory)
        ExpenditureTypes.setTabOrder(self.txtCategory, self.btnExpenseDelete)
        ExpenditureTypes.setTabOrder(self.btnExpenseDelete, self.btnCategorySave)
        ExpenditureTypes.setTabOrder(self.btnCategorySave, self.btnCategoryDelete)
        ExpenditureTypes.setTabOrder(self.btnCategoryDelete, self.btnExpenditureClose)

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

