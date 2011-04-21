# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes.ui'
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

class Ui_FoodTypes(object):
    def setupUi(self, FoodTypes):
        FoodTypes.setObjectName(_fromUtf8("FoodTypes"))
        FoodTypes.resize(384, 184)
        FoodTypes.setMinimumSize(QtCore.QSize(384, 180))
        self.formLayout = QtGui.QFormLayout(FoodTypes)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(FoodTypes)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cmbFoodType = QtGui.QComboBox(FoodTypes)
        self.cmbFoodType.setEditable(True)
        self.cmbFoodType.setObjectName(_fromUtf8("cmbFoodType"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbFoodType)
        self.label_4 = QtGui.QLabel(FoodTypes)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtKCalories = QtGui.QLineEdit(FoodTypes)
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtKCalories)
        self.label_3 = QtGui.QLabel(FoodTypes)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cmbUnitOfMeasure = QtGui.QComboBox(FoodTypes)
        self.cmbUnitOfMeasure.setEditable(True)
        self.cmbUnitOfMeasure.setObjectName(_fromUtf8("cmbUnitOfMeasure"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cmbUnitOfMeasure)
        self.groupBox = QtGui.QGroupBox(FoodTypes)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdDelete = QtGui.QPushButton(self.groupBox)
        self.cmdDelete.setObjectName(_fromUtf8("cmdDelete"))
        self.horizontalLayout.addWidget(self.cmdDelete)
        self.cmdManageFoodClose = QtGui.QPushButton(self.groupBox)
        self.cmdManageFoodClose.setObjectName(_fromUtf8("cmdManageFoodClose"))
        self.horizontalLayout.addWidget(self.cmdManageFoodClose)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(FoodTypes)
        QtCore.QObject.connect(self.cmdManageFoodClose, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodTypes.close)
        QtCore.QMetaObject.connectSlotsByName(FoodTypes)
        FoodTypes.setTabOrder(self.cmbFoodType, self.txtKCalories)
        FoodTypes.setTabOrder(self.txtKCalories, self.cmbUnitOfMeasure)
        FoodTypes.setTabOrder(self.cmbUnitOfMeasure, self.cmdSave)
        FoodTypes.setTabOrder(self.cmdSave, self.cmdDelete)
        FoodTypes.setTabOrder(self.cmdDelete, self.cmdManageFoodClose)

    def retranslateUi(self, FoodTypes):
        FoodTypes.setWindowTitle(QtGui.QApplication.translate("FoodTypes", "Manage Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("FoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("FoodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdManageFoodClose.setText(QtGui.QApplication.translate("FoodTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))

