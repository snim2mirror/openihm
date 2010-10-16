# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_edit.ui'
#
# Created: Mon Oct 11 23:22:20 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditFoodTypes(object):
    def setupUi(self, EditFoodTypes):
        EditFoodTypes.setObjectName(_fromUtf8("EditFoodTypes"))
        EditFoodTypes.resize(350, 204)
        EditFoodTypes.setMinimumSize(QtCore.QSize(350, 204))
        self.cmdCancel = QtGui.QPushButton(EditFoodTypes)
        self.cmdCancel.setGeometry(QtCore.QRect(260, 170, 80, 28))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.cmdSave = QtGui.QPushButton(EditFoodTypes)
        self.cmdSave.setGeometry(QtCore.QRect(70, 170, 80, 28))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label = QtGui.QLabel(EditFoodTypes)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(EditFoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(EditFoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtKCalories = QtGui.QLineEdit(EditFoodTypes)
        self.txtKCalories.setGeometry(QtCore.QRect(120, 60, 131, 31))
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.txtFoodType = QtGui.QLineEdit(EditFoodTypes)
        self.txtFoodType.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.txtFoodType.setObjectName(_fromUtf8("txtFoodType"))
        self.txtMeasuringUnit = QtGui.QLineEdit(EditFoodTypes)
        self.txtMeasuringUnit.setGeometry(QtCore.QRect(120, 110, 141, 31))
        self.txtMeasuringUnit.setObjectName(_fromUtf8("txtMeasuringUnit"))

        self.retranslateUi(EditFoodTypes)
        QtCore.QMetaObject.connectSlotsByName(EditFoodTypes)

    def retranslateUi(self, EditFoodTypes):
        EditFoodTypes.setWindowTitle(QtGui.QApplication.translate("EditFoodTypes", "Edit Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditFoodTypes", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditFoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditFoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditFoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditFoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))

