# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_1.ui'
#
# Created: Fri Apr 15 16:13:44 2011
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FoodTypes(object):
    def setupUi(self, FoodTypes):
        FoodTypes.setObjectName(_fromUtf8("FoodTypes"))
        FoodTypes.resize(456, 580)
        FoodTypes.setMinimumSize(QtCore.QSize(456, 580))
        self.cmdClose = QtGui.QPushButton(FoodTypes)
        self.cmdClose.setGeometry(QtCore.QRect(370, 540, 75, 31))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.cmdAddRow = QtGui.QPushButton(FoodTypes)
        self.cmdAddRow.setGeometry(QtCore.QRect(70, 540, 75, 31))
        self.cmdAddRow.setObjectName(_fromUtf8("cmdAddRow"))
        self.cmdEditRow = QtGui.QPushButton(FoodTypes)
        self.cmdEditRow.setGeometry(QtCore.QRect(170, 540, 75, 31))
        self.cmdEditRow.setObjectName(_fromUtf8("cmdEditRow"))
        self.cmdDeleteRows = QtGui.QPushButton(FoodTypes)
        self.cmdDeleteRows.setGeometry(QtCore.QRect(270, 540, 75, 31))
        self.cmdDeleteRows.setObjectName(_fromUtf8("cmdDeleteRows"))
        self.tableView = QtGui.QTableView(FoodTypes)
        self.tableView.setGeometry(QtCore.QRect(0, 80, 451, 451))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.line = QtGui.QFrame(FoodTypes)
        self.line.setGeometry(QtCore.QRect(0, 0, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(FoodTypes)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 451, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(FoodTypes)
        self.label.setGeometry(QtCore.QRect(0, 30, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtSearchCrop = QtGui.QLineEdit(FoodTypes)
        self.txtSearchCrop.setGeometry(QtCore.QRect(110, 20, 241, 31))
        self.txtSearchCrop.setObjectName(_fromUtf8("txtSearchCrop"))
        self.cmdSearch = QtGui.QPushButton(FoodTypes)
        self.cmdSearch.setGeometry(QtCore.QRect(370, 22, 75, 31))
        self.cmdSearch.setObjectName(_fromUtf8("cmdSearch"))

        self.retranslateUi(FoodTypes)
        QtCore.QMetaObject.connectSlotsByName(FoodTypes)

    def retranslateUi(self, FoodTypes):
        FoodTypes.setWindowTitle(QtGui.QApplication.translate("FoodTypes", "Food Energy Values", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("FoodTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddRow.setText(QtGui.QApplication.translate("FoodTypes", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditRow.setText(QtGui.QApplication.translate("FoodTypes", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDeleteRows.setText(QtGui.QApplication.translate("FoodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FoodTypes", "Search for Food Type", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSearch.setText(QtGui.QApplication.translate("FoodTypes", "Search", None, QtGui.QApplication.UnicodeUTF8))

