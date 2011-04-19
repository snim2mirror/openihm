# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foodenergy_requirements.ui'
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

class Ui_FoodEnergyRequirements(object):
    def setupUi(self, FoodEnergyRequirements):
        FoodEnergyRequirements.setObjectName(_fromUtf8("FoodEnergyRequirements"))
        FoodEnergyRequirements.resize(491, 582)
        FoodEnergyRequirements.setMinimumSize(QtCore.QSize(481, 582))
        self.cmdFERequirementsClose = QtGui.QPushButton(FoodEnergyRequirements)
        self.cmdFERequirementsClose.setGeometry(QtCore.QRect(390, 550, 75, 23))
        self.cmdFERequirementsClose.setObjectName(_fromUtf8("cmdFERequirementsClose"))
        self.cmdAddRow = QtGui.QPushButton(FoodEnergyRequirements)
        self.cmdAddRow.setGeometry(QtCore.QRect(90, 550, 75, 23))
        self.cmdAddRow.setObjectName(_fromUtf8("cmdAddRow"))
        self.cmdEditRow = QtGui.QPushButton(FoodEnergyRequirements)
        self.cmdEditRow.setGeometry(QtCore.QRect(190, 550, 75, 23))
        self.cmdEditRow.setObjectName(_fromUtf8("cmdEditRow"))
        self.DeleteRow = QtGui.QPushButton(FoodEnergyRequirements)
        self.DeleteRow.setGeometry(QtCore.QRect(290, 550, 75, 23))
        self.DeleteRow.setObjectName(_fromUtf8("DeleteRow"))
        self.tableView = QtGui.QTableView(FoodEnergyRequirements)
        self.tableView.setGeometry(QtCore.QRect(0, 10, 471, 531))
        self.tableView.setObjectName(_fromUtf8("tableView"))

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
        self.cmdFERequirementsClose.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Delete", None, QtGui.QApplication.UnicodeUTF8))

