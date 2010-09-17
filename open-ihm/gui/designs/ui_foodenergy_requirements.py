# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foodenergy_requirements.ui'
#
# Created: Fri Sep 17 15:01:08 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FrmFoodEnergyRequirements(object):
    def setupUi(self, FrmFoodEnergyRequirements):
        FrmFoodEnergyRequirements.setObjectName(_fromUtf8("FrmFoodEnergyRequirements"))
        FrmFoodEnergyRequirements.resize(486, 317)
        FrmFoodEnergyRequirements.setMinimumSize(QtCore.QSize(486, 317))
        self.tblFoodEnergyRequirements = QtGui.QTableWidget(FrmFoodEnergyRequirements)
        self.tblFoodEnergyRequirements.setGeometry(QtCore.QRect(0, 10, 481, 261))
        self.tblFoodEnergyRequirements.setObjectName(_fromUtf8("tblFoodEnergyRequirements"))
        self.tblFoodEnergyRequirements.setColumnCount(3)
        self.tblFoodEnergyRequirements.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblFoodEnergyRequirements.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblFoodEnergyRequirements.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblFoodEnergyRequirements.setHorizontalHeaderItem(2, item)
        self.cmdFERequirementsClose = QtGui.QPushButton(FrmFoodEnergyRequirements)
        self.cmdFERequirementsClose.setGeometry(QtCore.QRect(400, 290, 75, 23))
        self.cmdFERequirementsClose.setObjectName(_fromUtf8("cmdFERequirementsClose"))

        self.retranslateUi(FrmFoodEnergyRequirements)
        QtCore.QMetaObject.connectSlotsByName(FrmFoodEnergyRequirements)

    def retranslateUi(self, FrmFoodEnergyRequirements):
        FrmFoodEnergyRequirements.setWindowTitle(QtGui.QApplication.translate("FrmFoodEnergyRequirements", "View Food Energy Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.tblFoodEnergyRequirements.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("FrmFoodEnergyRequirements", "Age", None, QtGui.QApplication.UnicodeUTF8))
        self.tblFoodEnergyRequirements.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("FrmFoodEnergyRequirements", "FoodReqM", None, QtGui.QApplication.UnicodeUTF8))
        self.tblFoodEnergyRequirements.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("FrmFoodEnergyRequirements", "FoodReqF", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdFERequirementsClose.setText(QtGui.QApplication.translate("FrmFoodEnergyRequirements", "Close", None, QtGui.QApplication.UnicodeUTF8))

