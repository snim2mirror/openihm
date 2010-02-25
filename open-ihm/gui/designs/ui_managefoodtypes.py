# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes.ui'
#
# Created: Wed Feb 24 17:31:55 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FoodTypes(object):
    def setupUi(self, FoodTypes):
        FoodTypes.setObjectName("FoodTypes")
        FoodTypes.resize(QtCore.QSize(QtCore.QRect(0,0,389,270).size()).expandedTo(FoodTypes.minimumSizeHint()))
        FoodTypes.setMinimumSize(QtCore.QSize(389,261))

        self.btnManageFoodClose = QtGui.QPushButton(FoodTypes)
        self.btnManageFoodClose.setGeometry(QtCore.QRect(270,220,80,28))
        self.btnManageFoodClose.setObjectName("btnManageFoodClose")

        self.pushButton_3 = QtGui.QPushButton(FoodTypes)
        self.pushButton_3.setGeometry(QtCore.QRect(40,220,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(FoodTypes)
        self.comboBox.setGeometry(QtCore.QRect(120,10,221,27))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtGui.QComboBox(FoodTypes)
        self.comboBox_2.setGeometry(QtCore.QRect(120,50,221,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label = QtGui.QLabel(FoodTypes)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(FoodTypes)
        self.label_2.setGeometry(QtCore.QRect(10,60,61,18))
        self.label_2.setObjectName("label_2")

        self.comboBox_3 = QtGui.QComboBox(FoodTypes)
        self.comboBox_3.setGeometry(QtCore.QRect(120,90,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(FoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10,100,91,18))
        self.label_3.setObjectName("label_3")

        self.comboBox_4 = QtGui.QComboBox(FoodTypes)
        self.comboBox_4.setGeometry(QtCore.QRect(120,130,131,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtGui.QLabel(FoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10,130,101,18))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtGui.QLineEdit(FoodTypes)
        self.lineEdit.setGeometry(QtCore.QRect(120,170,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(FoodTypes)
        self.label_5.setGeometry(QtCore.QRect(10,180,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(FoodTypes)
        self.pushButton.setGeometry(QtCore.QRect(160,220,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FoodTypes)
        QtCore.QMetaObject.connectSlotsByName(FoodTypes)

    def retranslateUi(self, FoodTypes):
        FoodTypes.setWindowTitle(QtGui.QApplication.translate("FoodTypes", "Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageFoodClose.setText(QtGui.QApplication.translate("FoodTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("FoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FoodTypes", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FoodTypes", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("FoodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))

