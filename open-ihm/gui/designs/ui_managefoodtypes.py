# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes.ui'
#
# Created: Sun Feb 21 17:53:36 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_foodTypes(object):
    def setupUi(self, foodTypes):
        foodTypes.setObjectName("foodTypes")
        foodTypes.resize(QtCore.QSize(QtCore.QRect(0,0,389,270).size()).expandedTo(foodTypes.minimumSizeHint()))
        foodTypes.setMinimumSize(QtCore.QSize(389,261))

        self.btnManageFoodCancel = QtGui.QPushButton(foodTypes)
        self.btnManageFoodCancel.setGeometry(QtCore.QRect(270,220,80,28))
        self.btnManageFoodCancel.setObjectName("btnManageFoodCancel")

        self.pushButton_3 = QtGui.QPushButton(foodTypes)
        self.pushButton_3.setGeometry(QtCore.QRect(40,220,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(foodTypes)
        self.comboBox.setGeometry(QtCore.QRect(120,10,221,27))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtGui.QComboBox(foodTypes)
        self.comboBox_2.setGeometry(QtCore.QRect(120,50,221,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label = QtGui.QLabel(foodTypes)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(foodTypes)
        self.label_2.setGeometry(QtCore.QRect(10,60,61,18))
        self.label_2.setObjectName("label_2")

        self.comboBox_3 = QtGui.QComboBox(foodTypes)
        self.comboBox_3.setGeometry(QtCore.QRect(120,90,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(foodTypes)
        self.label_3.setGeometry(QtCore.QRect(10,100,91,18))
        self.label_3.setObjectName("label_3")

        self.comboBox_4 = QtGui.QComboBox(foodTypes)
        self.comboBox_4.setGeometry(QtCore.QRect(120,130,131,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtGui.QLabel(foodTypes)
        self.label_4.setGeometry(QtCore.QRect(10,130,101,18))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtGui.QLineEdit(foodTypes)
        self.lineEdit.setGeometry(QtCore.QRect(120,170,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(foodTypes)
        self.label_5.setGeometry(QtCore.QRect(10,180,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(foodTypes)
        self.pushButton.setGeometry(QtCore.QRect(160,220,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(foodTypes)
        QtCore.QMetaObject.connectSlotsByName(foodTypes)

    def retranslateUi(self, foodTypes):
        foodTypes.setWindowTitle(QtGui.QApplication.translate("foodTypes", "Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageFoodCancel.setText(QtGui.QApplication.translate("foodTypes", "Cacel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("foodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("foodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("foodTypes", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("foodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("foodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("foodTypes", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("foodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))

