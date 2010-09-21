# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_foodenergyrequirement.ui'
#
# Created: Tue Sep 21 15:04:03 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditFoodEnergyRequirement(object):
    def setupUi(self, EditFoodEnergyRequirement):
        EditFoodEnergyRequirement.setObjectName(_fromUtf8("EditFoodEnergyRequirement"))
        EditFoodEnergyRequirement.resize(380, 175)
        EditFoodEnergyRequirement.setMinimumSize(QtCore.QSize(380, 175))
        self.txtAge = QtGui.QLineEdit(EditFoodEnergyRequirement)
        self.txtAge.setGeometry(QtCore.QRect(170, 40, 201, 20))
        self.txtAge.setObjectName(_fromUtf8("txtAge"))
        self.label_2 = QtGui.QLabel(EditFoodEnergyRequirement)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(EditFoodEnergyRequirement)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cmdSave = QtGui.QPushButton(EditFoodEnergyRequirement)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmdCancel = QtGui.QPushButton(EditFoodEnergyRequirement)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label_6 = QtGui.QLabel(EditFoodEnergyRequirement)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtEnergyRequirementMales = QtGui.QLineEdit(EditFoodEnergyRequirement)
        self.txtEnergyRequirementMales.setGeometry(QtCore.QRect(170, 70, 201, 20))
        self.txtEnergyRequirementMales.setObjectName(_fromUtf8("txtEnergyRequirementMales"))
        self.txtEnergyRequirementFemales = QtGui.QLineEdit(EditFoodEnergyRequirement)
        self.txtEnergyRequirementFemales.setGeometry(QtCore.QRect(170, 100, 201, 20))
        self.txtEnergyRequirementFemales.setObjectName(_fromUtf8("txtEnergyRequirementFemales"))

        self.retranslateUi(EditFoodEnergyRequirement)
        QtCore.QMetaObject.connectSlotsByName(EditFoodEnergyRequirement)

    def retranslateUi(self, EditFoodEnergyRequirement):
        EditFoodEnergyRequirement.setWindowTitle(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Edit Food Energy Requirement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Energy Requirements - Males", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Energy Requirements - Females", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Age", None, QtGui.QApplication.UnicodeUTF8))

