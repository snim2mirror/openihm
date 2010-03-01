# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managetrees.ui'
#
# Created: Sun Feb 28 13:03:15 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Trees(object):
    def setupUi(self, Trees):
        Trees.setObjectName("Trees")
        Trees.resize(QtCore.QSize(QtCore.QRect(0,0,371,204).size()).expandedTo(Trees.minimumSizeHint()))
        Trees.setMinimumSize(QtCore.QSize(369,204))

        self.btnOtherTradableGoodsClose = QtGui.QPushButton(Trees)
        self.btnOtherTradableGoodsClose.setGeometry(QtCore.QRect(280,160,80,28))
        self.btnOtherTradableGoodsClose.setObjectName("btnOtherTradableGoodsClose")

        self.pushButton_3 = QtGui.QPushButton(Trees)
        self.pushButton_3.setGeometry(QtCore.QRect(50,160,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(Trees)
        self.comboBox.setGeometry(QtCore.QRect(120,10,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(Trees)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(Trees)
        self.comboBox_3.setGeometry(QtCore.QRect(120,60,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(Trees)
        self.label_3.setGeometry(QtCore.QRect(10,70,91,18))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtGui.QLineEdit(Trees)
        self.lineEdit.setGeometry(QtCore.QRect(120,110,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(Trees)
        self.label_5.setGeometry(QtCore.QRect(10,110,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(Trees)
        self.pushButton.setGeometry(QtCore.QRect(170,160,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Trees)
        QtCore.QMetaObject.connectSlotsByName(Trees)

    def retranslateUi(self, Trees):
        Trees.setWindowTitle(QtGui.QApplication.translate("Trees", "Manage Asset Trees", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOtherTradableGoodsClose.setText(QtGui.QApplication.translate("Trees", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Trees", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Trees", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Trees", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Trees", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Trees", "Delete", None, QtGui.QApplication.UnicodeUTF8))

