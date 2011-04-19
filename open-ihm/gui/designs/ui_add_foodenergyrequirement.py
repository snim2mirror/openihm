# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_add_foodenergyrequirement.ui'
#
# Created: Tue Apr 19 08:09:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddFoodEnergyRequirement(object):
    def setupUi(self, AddFoodEnergyRequirement):
        AddFoodEnergyRequirement.setObjectName(_fromUtf8("AddFoodEnergyRequirement"))
        AddFoodEnergyRequirement.resize(380, 175)
        AddFoodEnergyRequirement.setMinimumSize(QtCore.QSize(380, 175))
        self.txtAge = QtGui.QLineEdit(AddFoodEnergyRequirement)
        self.txtAge.setGeometry(QtCore.QRect(170, 40, 201, 20))
        self.txtAge.setObjectName(_fromUtf8("txtAge"))
        self.label_2 = QtGui.QLabel(AddFoodEnergyRequirement)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(AddFoodEnergyRequirement)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cmdSave = QtGui.QPushButton(AddFoodEnergyRequirement)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmdCancel = QtGui.QPushButton(AddFoodEnergyRequirement)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label_6 = QtGui.QLabel(AddFoodEnergyRequirement)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtEnergyRequirementMales = QtGui.QLineEdit(AddFoodEnergyRequirement)
        self.txtEnergyRequirementMales.setGeometry(QtCore.QRect(170, 70, 201, 20))
        self.txtEnergyRequirementMales.setObjectName(_fromUtf8("txtEnergyRequirementMales"))
        self.txtEnergyRequirementFemales = QtGui.QLineEdit(AddFoodEnergyRequirement)
        self.txtEnergyRequirementFemales.setGeometry(QtCore.QRect(170, 100, 201, 20))
        self.txtEnergyRequirementFemales.setObjectName(_fromUtf8("txtEnergyRequirementFemales"))

        self.retranslateUi(AddFoodEnergyRequirement)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodEnergyRequirement.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodEnergyRequirement.saveFoodEnergyRequirementDetails)
        QtCore.QMetaObject.connectSlotsByName(AddFoodEnergyRequirement)
        AddFoodEnergyRequirement.setTabOrder(self.txtAge, self.txtEnergyRequirementMales)
        AddFoodEnergyRequirement.setTabOrder(self.txtEnergyRequirementMales, self.txtEnergyRequirementFemales)
        AddFoodEnergyRequirement.setTabOrder(self.txtEnergyRequirementFemales, self.cmdSave)
        AddFoodEnergyRequirement.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddFoodEnergyRequirement):
        AddFoodEnergyRequirement.setWindowTitle(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Add Food Energy Requirement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Energy Requirements - Males", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Energy Requirements - Females", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Age", None, QtGui.QApplication.UnicodeUTF8))

