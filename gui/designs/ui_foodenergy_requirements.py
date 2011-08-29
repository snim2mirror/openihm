# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foodenergy_requirements.ui'
#
# Created: Thu Apr 21 20:23:44 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FoodEnergyRequirements(object):
    def setupUi(self, FoodEnergyRequirements):
        FoodEnergyRequirements.setObjectName(_fromUtf8("FoodEnergyRequirements"))
        FoodEnergyRequirements.resize(491, 550)
        FoodEnergyRequirements.setMinimumSize(QtCore.QSize(481, 550))
        self.verticalLayout = QtGui.QVBoxLayout(FoodEnergyRequirements)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(FoodEnergyRequirements)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.groupBox = QtGui.QGroupBox(FoodEnergyRequirements)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdAddRow = QtGui.QPushButton(self.groupBox)
        self.cmdAddRow.setObjectName(_fromUtf8("cmdAddRow"))
        self.horizontalLayout.addWidget(self.cmdAddRow)
        self.cmdEditRow = QtGui.QPushButton(self.groupBox)
        self.cmdEditRow.setObjectName(_fromUtf8("cmdEditRow"))
        self.horizontalLayout.addWidget(self.cmdEditRow)
        self.DeleteRow = QtGui.QPushButton(self.groupBox)
        self.DeleteRow.setObjectName(_fromUtf8("DeleteRow"))
        self.horizontalLayout.addWidget(self.DeleteRow)
        self.cmdFERequirementsClose = QtGui.QPushButton(self.groupBox)
        self.cmdFERequirementsClose.setObjectName(_fromUtf8("cmdFERequirementsClose"))
        self.horizontalLayout.addWidget(self.cmdFERequirementsClose)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FoodEnergyRequirements)
        QtCore.QObject.connect(self.cmdFERequirementsClose, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodEnergyRequirements.mdiClose)
        QtCore.QObject.connect(self.cmdAddRow, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodEnergyRequirements.addFoodEnergyRequirement)
        QtCore.QObject.connect(self.cmdEditRow, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodEnergyRequirements.editFoodEnergyRequirement)
        QtCore.QObject.connect(self.DeleteRow, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodEnergyRequirements.deleteSelectedEnergyRequirements)
        QtCore.QMetaObject.connectSlotsByName(FoodEnergyRequirements)
        FoodEnergyRequirements.setTabOrder(self.tableView, self.cmdAddRow)
        FoodEnergyRequirements.setTabOrder(self.cmdAddRow, self.cmdEditRow)
        FoodEnergyRequirements.setTabOrder(self.cmdEditRow, self.DeleteRow)
        FoodEnergyRequirements.setTabOrder(self.DeleteRow, self.cmdFERequirementsClose)

    def retranslateUi(self, FoodEnergyRequirements):
        FoodEnergyRequirements.setWindowTitle(QtGui.QApplication.translate("FoodEnergyRequirements", "Food Energy Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdFERequirementsClose.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Close", None, QtGui.QApplication.UnicodeUTF8))

