# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes.ui'
#
# Created: Tue Apr 19 03:45:26 2011
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
        FoodTypes.resize(384, 204)
        FoodTypes.setMinimumSize(QtCore.QSize(384, 204))
        self.cmdManageFoodClose = QtGui.QPushButton(FoodTypes)
        self.cmdManageFoodClose.setGeometry(QtCore.QRect(300, 170, 80, 28))
        self.cmdManageFoodClose.setObjectName(_fromUtf8("cmdManageFoodClose"))
        self.cmdSave = QtGui.QPushButton(FoodTypes)
        self.cmdSave.setGeometry(QtCore.QRect(70, 170, 80, 28))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmbFoodType = QtGui.QComboBox(FoodTypes)
        self.cmbFoodType.setGeometry(QtCore.QRect(120, 10, 221, 27))
        self.cmbFoodType.setEditable(True)
        self.cmbFoodType.setObjectName(_fromUtf8("cmbFoodType"))
        self.label = QtGui.QLabel(FoodTypes)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmbUnitOfMeasure = QtGui.QComboBox(FoodTypes)
        self.cmbUnitOfMeasure.setGeometry(QtCore.QRect(120, 110, 131, 27))
        self.cmbUnitOfMeasure.setEditable(True)
        self.cmbUnitOfMeasure.setObjectName(_fromUtf8("cmbUnitOfMeasure"))
        self.label_3 = QtGui.QLabel(FoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(FoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cmdDelete = QtGui.QPushButton(FoodTypes)
        self.cmdDelete.setGeometry(QtCore.QRect(190, 170, 80, 28))
        self.cmdDelete.setObjectName(_fromUtf8("cmdDelete"))
        self.txtKCalories = QtGui.QLineEdit(FoodTypes)
        self.txtKCalories.setGeometry(QtCore.QRect(120, 60, 131, 31))
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))

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
        self.cmdManageFoodClose.setText(QtGui.QApplication.translate("FoodTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("FoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("FoodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))

