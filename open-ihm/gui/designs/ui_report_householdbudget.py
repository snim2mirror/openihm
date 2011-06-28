# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_report_householdbudget.ui'
#
# Created: Tue Jun 28 23:34:58 2011
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HouseholdBudget(object):
    def setupUi(self, HouseholdBudget):
        HouseholdBudget.setObjectName("HouseholdBudget")
        HouseholdBudget.resize(760, 452)
        HouseholdBudget.setMinimumSize(QtCore.QSize(596, 399))
        self.gridLayout = QtGui.QGridLayout(HouseholdBudget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(HouseholdBudget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cmbProjectNames = QtGui.QComboBox(HouseholdBudget)
        self.cmbProjectNames.setObjectName("cmbProjectNames")
        self.gridLayout.addWidget(self.cmbProjectNames, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(HouseholdBudget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cmbHouseholds = QtGui.QComboBox(HouseholdBudget)
        self.cmbHouseholds.setObjectName("cmbHouseholds")
        self.cmbHouseholds.addItem("")
        self.cmbHouseholds.addItem("")
        self.gridLayout.addWidget(self.cmbHouseholds, 1, 1, 1, 2)
        self.groupBox = QtGui.QGroupBox(HouseholdBudget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listViewHNumbers = QtGui.QListView(self.groupBox)
        self.listViewHNumbers.setAlternatingRowColors(True)
        self.listViewHNumbers.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listViewHNumbers.setObjectName("listViewHNumbers")
        self.verticalLayout_6.addWidget(self.listViewHNumbers)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 2, 2)
        self.groupBox_2 = QtGui.QGroupBox(HouseholdBudget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.listViewHNames = QtGui.QListView(self.groupBox_2)
        self.listViewHNames.setAlternatingRowColors(True)
        self.listViewHNames.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listViewHNames.setObjectName("listViewHNames")
        self.verticalLayout_5.addWidget(self.listViewHNames)
        self.gridLayout.addWidget(self.groupBox_2, 2, 2, 2, 2)
        self.cmdGenerateReport = QtGui.QPushButton(HouseholdBudget)
        self.cmdGenerateReport.setObjectName("cmdGenerateReport")
        self.gridLayout.addWidget(self.cmdGenerateReport, 4, 2, 1, 1)
        self.cmdClose = QtGui.QPushButton(HouseholdBudget)
        self.cmdClose.setObjectName("cmdClose")
        self.gridLayout.addWidget(self.cmdClose, 4, 3, 1, 1)
        self.label.setBuddy(self.cmbProjectNames)
        self.label_2.setBuddy(self.cmbHouseholds)

        self.retranslateUi(HouseholdBudget)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL("clicked()"), HouseholdBudget.mdiClose)
        QtCore.QObject.connect(self.cmdGenerateReport, QtCore.SIGNAL("clicked()"), HouseholdBudget.writeSpreadsheet)
        QtCore.QObject.connect(self.cmbProjectNames, QtCore.SIGNAL("currentIndexChanged(int)"), HouseholdBudget.getHouseholds)
        QtCore.QMetaObject.connectSlotsByName(HouseholdBudget)
        HouseholdBudget.setTabOrder(self.cmbProjectNames, self.cmbHouseholds)
        HouseholdBudget.setTabOrder(self.cmbHouseholds, self.listViewHNumbers)
        HouseholdBudget.setTabOrder(self.listViewHNumbers, self.listViewHNames)

    def retranslateUi(self, HouseholdBudget):
        HouseholdBudget.setWindowTitle(QtGui.QApplication.translate("HouseholdBudget", "Report Households by Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseholdBudget", "Select Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseholdBudget", "Select Household(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHouseholds.setItemText(0, QtGui.QApplication.translate("HouseholdBudget", "All Households", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHouseholds.setItemText(1, QtGui.QApplication.translate("HouseholdBudget", "Select Particular Households", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("HouseholdBudget", "Household Number", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("HouseholdBudget", "Household Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdGenerateReport.setText(QtGui.QApplication.translate("HouseholdBudget", "Generate Report", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("HouseholdBudget", "Close", None, QtGui.QApplication.UnicodeUTF8))

