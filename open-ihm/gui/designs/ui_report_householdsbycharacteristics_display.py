# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_report_householdsbycharacteristics_display.ui'
#
# Created: Fri Oct 01 16:40:55 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DisplayHouseholdsByChar(object):
    def setupUi(self, DisplayHouseholdsByChar):
        DisplayHouseholdsByChar.setObjectName(_fromUtf8("DisplayHouseholdsByChar"))
        DisplayHouseholdsByChar.resize(447, 629)
        DisplayHouseholdsByChar.setMinimumSize(QtCore.QSize(447, 629))
        self.tableView = QtGui.QTableView(DisplayHouseholdsByChar)
        self.tableView.setGeometry(QtCore.QRect(0, 30, 441, 551))
        self.tableView.setMinimumSize(QtCore.QSize(300, 551))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.cmdClose = QtGui.QPushButton(DisplayHouseholdsByChar)
        self.cmdClose.setGeometry(QtCore.QRect(160, 600, 91, 23))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.cmdSaveAsSpreadsheet = QtGui.QPushButton(DisplayHouseholdsByChar)
        self.cmdSaveAsSpreadsheet.setGeometry(QtCore.QRect(10, 600, 121, 23))
        self.cmdSaveAsSpreadsheet.setObjectName(_fromUtf8("cmdSaveAsSpreadsheet"))
        self.label = QtGui.QLabel(DisplayHouseholdsByChar)
        self.label.setGeometry(QtCore.QRect(0, 0, 281, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(DisplayHouseholdsByChar)
        QtCore.QMetaObject.connectSlotsByName(DisplayHouseholdsByChar)

    def retranslateUi(self, DisplayHouseholdsByChar):
        DisplayHouseholdsByChar.setWindowTitle(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Report: Households By Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSaveAsSpreadsheet.setText(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Save As Spreadsheet", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Households By Charateristics", None, QtGui.QApplication.UnicodeUTF8))

