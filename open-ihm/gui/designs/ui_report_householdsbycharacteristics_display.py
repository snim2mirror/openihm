# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_report_householdsbycharacteristics_display.ui'
#
# Created: Thu Apr 21 19:28:08 2011
#      by: PyQt4 UI code generator 4.8.3
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
        DisplayHouseholdsByChar.resize(447, 580)
        DisplayHouseholdsByChar.setMinimumSize(QtCore.QSize(447, 580))
        self.verticalLayout = QtGui.QVBoxLayout(DisplayHouseholdsByChar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DisplayHouseholdsByChar)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtGui.QTableView(DisplayHouseholdsByChar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(300, 400))
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.groupBox = QtGui.QGroupBox(DisplayHouseholdsByChar)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSaveAsSpreadsheet = QtGui.QPushButton(self.groupBox)
        self.cmdSaveAsSpreadsheet.setObjectName(_fromUtf8("cmdSaveAsSpreadsheet"))
        self.horizontalLayout.addWidget(self.cmdSaveAsSpreadsheet)
        self.cmdClose = QtGui.QPushButton(self.groupBox)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(DisplayHouseholdsByChar)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), DisplayHouseholdsByChar.mdiClose)
        QtCore.QObject.connect(self.cmdSaveAsSpreadsheet, QtCore.SIGNAL(_fromUtf8("clicked()")), DisplayHouseholdsByChar.saveReportAsSpreadtsheet)
        QtCore.QMetaObject.connectSlotsByName(DisplayHouseholdsByChar)
        DisplayHouseholdsByChar.setTabOrder(self.tableView, self.cmdClose)

    def retranslateUi(self, DisplayHouseholdsByChar):
        DisplayHouseholdsByChar.setWindowTitle(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Report: Households By Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Households By Charateristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSaveAsSpreadsheet.setText(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Save As Spreadsheet", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("DisplayHouseholdsByChar", "Close", None, QtGui.QApplication.UnicodeUTF8))

