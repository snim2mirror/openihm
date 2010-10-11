# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_add.ui'
#
# Created: Mon Oct 11 18:09:15 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddFoodTypes(object):
    def setupUi(self, AddFoodTypes):
        AddFoodTypes.setObjectName(_fromUtf8("AddFoodTypes"))
        AddFoodTypes.resize(350, 204)
        AddFoodTypes.setMinimumSize(QtCore.QSize(350, 204))
        self.cmdCancel = QtGui.QPushButton(AddFoodTypes)
        self.cmdCancel.setGeometry(QtCore.QRect(260, 170, 80, 28))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.cmdSave = QtGui.QPushButton(AddFoodTypes)
        self.cmdSave.setGeometry(QtCore.QRect(70, 170, 80, 28))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label = QtGui.QLabel(AddFoodTypes)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmbUnitOfMeasure = QtGui.QComboBox(AddFoodTypes)
        self.cmbUnitOfMeasure.setGeometry(QtCore.QRect(120, 110, 131, 27))
        self.cmbUnitOfMeasure.setEditable(True)
        self.cmbUnitOfMeasure.setObjectName(_fromUtf8("cmbUnitOfMeasure"))
        self.label_3 = QtGui.QLabel(AddFoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AddFoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtKCalories = QtGui.QLineEdit(AddFoodTypes)
        self.txtKCalories.setGeometry(QtCore.QRect(120, 60, 131, 31))
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.txtFoodType = QtGui.QLineEdit(AddFoodTypes)
        self.txtFoodType.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.txtFoodType.setObjectName(_fromUtf8("txtFoodType"))

        self.retranslateUi(AddFoodTypes)
        QtCore.QMetaObject.connectSlotsByName(AddFoodTypes)

    def retranslateUi(self, AddFoodTypes):
        AddFoodTypes.setWindowTitle(QtGui.QApplication.translate("AddFoodTypes", "Add Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddFoodTypes", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddFoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddFoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddFoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddFoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))

