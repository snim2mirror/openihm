# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managewildfoods.ui'
#
# Created: Sun Feb 28 13:17:14 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WildFoods(object):
    def setupUi(self, WildFoods):
        WildFoods.setObjectName("WildFoods")
        WildFoods.resize(QtCore.QSize(QtCore.QRect(0,0,369,238).size()).expandedTo(WildFoods.minimumSizeHint()))
        WildFoods.setMinimumSize(QtCore.QSize(369,238))

        self.btnManageWildFoodsClose = QtGui.QPushButton(WildFoods)
        self.btnManageWildFoodsClose.setGeometry(QtCore.QRect(270,200,80,28))
        self.btnManageWildFoodsClose.setObjectName("btnManageWildFoodsClose")

        self.pushButton_3 = QtGui.QPushButton(WildFoods)
        self.pushButton_3.setGeometry(QtCore.QRect(40,200,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(WildFoods)
        self.comboBox.setGeometry(QtCore.QRect(120,20,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(WildFoods)
        self.label.setGeometry(QtCore.QRect(10,20,54,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(WildFoods)
        self.comboBox_3.setGeometry(QtCore.QRect(120,60,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(WildFoods)
        self.label_3.setGeometry(QtCore.QRect(10,70,91,18))
        self.label_3.setObjectName("label_3")

        self.comboBox_4 = QtGui.QComboBox(WildFoods)
        self.comboBox_4.setGeometry(QtCore.QRect(120,100,131,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtGui.QLabel(WildFoods)
        self.label_4.setGeometry(QtCore.QRect(10,100,101,18))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtGui.QLineEdit(WildFoods)
        self.lineEdit.setGeometry(QtCore.QRect(120,140,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(WildFoods)
        self.label_5.setGeometry(QtCore.QRect(10,150,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(WildFoods)
        self.pushButton.setGeometry(QtCore.QRect(160,200,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(WildFoods)
        QtCore.QMetaObject.connectSlotsByName(WildFoods)

    def retranslateUi(self, WildFoods):
        WildFoods.setWindowTitle(QtGui.QApplication.translate("WildFoods", "Manage Wild Foods", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageWildFoodsClose.setText(QtGui.QApplication.translate("WildFoods", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("WildFoods", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WildFoods", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("WildFoods", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("WildFoods", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("WildFoods", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("WildFoods", "Delete", None, QtGui.QApplication.UnicodeUTF8))

