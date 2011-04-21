# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_foodenergyrequirement.ui'
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

class Ui_EditFoodEnergyRequirement(object):
    def setupUi(self, EditFoodEnergyRequirement):
        EditFoodEnergyRequirement.setObjectName(_fromUtf8("EditFoodEnergyRequirement"))
        EditFoodEnergyRequirement.resize(380, 187)
        EditFoodEnergyRequirement.setMinimumSize(QtCore.QSize(380, 175))
        self.formLayout = QtGui.QFormLayout(EditFoodEnergyRequirement)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(EditFoodEnergyRequirement)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtAge = QtGui.QLineEdit(EditFoodEnergyRequirement)
        self.txtAge.setObjectName(_fromUtf8("txtAge"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtAge)
        self.label_2 = QtGui.QLabel(EditFoodEnergyRequirement)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtEnergyRequirementMales = QtGui.QLineEdit(EditFoodEnergyRequirement)
        self.txtEnergyRequirementMales.setObjectName(_fromUtf8("txtEnergyRequirementMales"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtEnergyRequirementMales)
        self.label_5 = QtGui.QLabel(EditFoodEnergyRequirement)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtEnergyRequirementFemales = QtGui.QLineEdit(EditFoodEnergyRequirement)
        self.txtEnergyRequirementFemales.setObjectName(_fromUtf8("txtEnergyRequirementFemales"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtEnergyRequirementFemales)
        self.groupBox = QtGui.QGroupBox(EditFoodEnergyRequirement)
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

        self.retranslateUi(EditFoodEnergyRequirement)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodEnergyRequirement.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodEnergyRequirement.saveFoodEnergyRequirementDetails)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodEnergyRequirement.close)
        QtCore.QMetaObject.connectSlotsByName(EditFoodEnergyRequirement)
        EditFoodEnergyRequirement.setTabOrder(self.txtAge, self.txtEnergyRequirementMales)
        EditFoodEnergyRequirement.setTabOrder(self.txtEnergyRequirementMales, self.txtEnergyRequirementFemales)
        EditFoodEnergyRequirement.setTabOrder(self.txtEnergyRequirementFemales, self.cmdSave)
        EditFoodEnergyRequirement.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, EditFoodEnergyRequirement):
        EditFoodEnergyRequirement.setWindowTitle(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Edit Food Energy Requirement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Age", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Energy Requirements - Males", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Energy Requirements - Females", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditFoodEnergyRequirement", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

