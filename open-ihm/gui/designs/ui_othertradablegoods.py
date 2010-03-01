# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_othertradablegoods.ui'
#
# Created: Sun Feb 28 12:26:05 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_OtherTradableGoods(object):
    def setupUi(self, OtherTradableGoods):
        OtherTradableGoods.setObjectName("OtherTradableGoods")
        OtherTradableGoods.resize(QtCore.QSize(QtCore.QRect(0,0,371,204).size()).expandedTo(OtherTradableGoods.minimumSizeHint()))
        OtherTradableGoods.setMinimumSize(QtCore.QSize(369,204))

        self.btnOtherTradableGoodsClose = QtGui.QPushButton(OtherTradableGoods)
        self.btnOtherTradableGoodsClose.setGeometry(QtCore.QRect(280,160,80,28))
        self.btnOtherTradableGoodsClose.setObjectName("btnOtherTradableGoodsClose")

        self.pushButton_3 = QtGui.QPushButton(OtherTradableGoods)
        self.pushButton_3.setGeometry(QtCore.QRect(50,160,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(OtherTradableGoods)
        self.comboBox.setGeometry(QtCore.QRect(120,10,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(OtherTradableGoods)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(OtherTradableGoods)
        self.comboBox_3.setGeometry(QtCore.QRect(120,60,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(OtherTradableGoods)
        self.label_3.setGeometry(QtCore.QRect(10,70,91,18))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtGui.QLineEdit(OtherTradableGoods)
        self.lineEdit.setGeometry(QtCore.QRect(120,110,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(OtherTradableGoods)
        self.label_5.setGeometry(QtCore.QRect(10,110,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(OtherTradableGoods)
        self.pushButton.setGeometry(QtCore.QRect(170,160,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(OtherTradableGoods)
        QtCore.QMetaObject.connectSlotsByName(OtherTradableGoods)

    def retranslateUi(self, OtherTradableGoods):
        OtherTradableGoods.setWindowTitle(QtGui.QApplication.translate("OtherTradableGoods", "Manage Other Tradable Goods", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOtherTradableGoodsClose.setText(QtGui.QApplication.translate("OtherTradableGoods", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("OtherTradableGoods", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OtherTradableGoods", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OtherTradableGoods", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OtherTradableGoods", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("OtherTradableGoods", "Delete", None, QtGui.QApplication.UnicodeUTF8))

