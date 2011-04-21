# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_add_foodenergyrequirement.ui'
#
# Created: Thu Apr 21 20:21:02 2011
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
        AddFoodEnergyRequirement.resize(380, 185)
        AddFoodEnergyRequirement.setMinimumSize(QtCore.QSize(380, 175))
        self.formLayout = QtGui.QFormLayout(AddFoodEnergyRequirement)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(AddFoodEnergyRequirement)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtAge = QtGui.QLineEdit(AddFoodEnergyRequirement)
        self.txtAge.setObjectName(_fromUtf8("txtAge"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtAge)
        self.label_2 = QtGui.QLabel(AddFoodEnergyRequirement)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtEnergyRequirementMales = QtGui.QLineEdit(AddFoodEnergyRequirement)
        self.txtEnergyRequirementMales.setObjectName(_fromUtf8("txtEnergyRequirementMales"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtEnergyRequirementMales)
        self.label_5 = QtGui.QLabel(AddFoodEnergyRequirement)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtEnergyRequirementFemales = QtGui.QLineEdit(AddFoodEnergyRequirement)
        self.txtEnergyRequirementFemales.setObjectName(_fromUtf8("txtEnergyRequirementFemales"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtEnergyRequirementFemales)
        self.groupBox = QtGui.QGroupBox(AddFoodEnergyRequirement)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(AddFoodEnergyRequirement)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodEnergyRequirement.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodEnergyRequirement.saveFoodEnergyRequirementDetails)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodEnergyRequirement.close)
        QtCore.QMetaObject.connectSlotsByName(AddFoodEnergyRequirement)
        AddFoodEnergyRequirement.setTabOrder(self.txtAge, self.txtEnergyRequirementMales)
        AddFoodEnergyRequirement.setTabOrder(self.txtEnergyRequirementMales, self.txtEnergyRequirementFemales)
        AddFoodEnergyRequirement.setTabOrder(self.txtEnergyRequirementFemales, self.cmdSave)
        AddFoodEnergyRequirement.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddFoodEnergyRequirement):
        AddFoodEnergyRequirement.setWindowTitle(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Add Food Energy Requirement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Age", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Energy Requirements - Males", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Energy Requirements - Females", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddFoodEnergyRequirement", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

