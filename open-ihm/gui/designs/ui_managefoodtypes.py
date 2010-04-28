# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes.ui'
#
# Created: Wed Apr 28 13:51:42 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FoodTypes(object):
    def setupUi(self, FoodTypes):
        FoodTypes.setObjectName("FoodTypes")
        FoodTypes.resize(QtCore.QSize(QtCore.QRect(0,0,384,224).size()).expandedTo(FoodTypes.minimumSizeHint()))
        FoodTypes.setMinimumSize(QtCore.QSize(384,224))

        self.btnManageFoodClose = QtGui.QPushButton(FoodTypes)
        self.btnManageFoodClose.setGeometry(QtCore.QRect(300,190,80,28))
        self.btnManageFoodClose.setObjectName("btnManageFoodClose")

        self.pushButton_3 = QtGui.QPushButton(FoodTypes)
        self.pushButton_3.setGeometry(QtCore.QRect(70,190,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.cmbFoodType = QtGui.QComboBox(FoodTypes)
        self.cmbFoodType.setGeometry(QtCore.QRect(120,10,221,27))
        self.cmbFoodType.setObjectName("cmbFoodType")

        self.label = QtGui.QLabel(FoodTypes)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.cmbUnitOfMeasure = QtGui.QComboBox(FoodTypes)
        self.cmbUnitOfMeasure.setGeometry(QtCore.QRect(120,50,131,27))
        self.cmbUnitOfMeasure.setObjectName("cmbUnitOfMeasure")

        self.label_3 = QtGui.QLabel(FoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10,60,91,18))
        self.label_3.setObjectName("label_3")

        self.cmbKCalories = QtGui.QComboBox(FoodTypes)
        self.cmbKCalories.setGeometry(QtCore.QRect(120,90,131,27))
        self.cmbKCalories.setObjectName("cmbKCalories")

        self.label_4 = QtGui.QLabel(FoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10,90,101,18))
        self.label_4.setObjectName("label_4")

        self.txtUnitPrice = QtGui.QLineEdit(FoodTypes)
        self.txtUnitPrice.setGeometry(QtCore.QRect(120,130,131,28))
        self.txtUnitPrice.setObjectName("txtUnitPrice")

        self.label_5 = QtGui.QLabel(FoodTypes)
        self.label_5.setGeometry(QtCore.QRect(10,140,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(FoodTypes)
        self.pushButton.setGeometry(QtCore.QRect(190,190,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FoodTypes)
        QtCore.QMetaObject.connectSlotsByName(FoodTypes)

    def retranslateUi(self, FoodTypes):
        FoodTypes.setWindowTitle(QtGui.QApplication.translate("FoodTypes", "Manage Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageFoodClose.setText(QtGui.QApplication.translate("FoodTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("FoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FoodTypes", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("FoodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))

