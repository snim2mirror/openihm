# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managelivestockproducts.ui'
#
# Created: Sun Feb 28 13:34:21 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LivestockProducts(object):
    def setupUi(self, LivestockProducts):
        LivestockProducts.setObjectName("LivestockProducts")
        LivestockProducts.resize(QtCore.QSize(QtCore.QRect(0,0,369,238).size()).expandedTo(LivestockProducts.minimumSizeHint()))
        LivestockProducts.setMinimumSize(QtCore.QSize(369,238))

        self.btnLiveStockProductsClose = QtGui.QPushButton(LivestockProducts)
        self.btnLiveStockProductsClose.setGeometry(QtCore.QRect(270,200,80,28))
        self.btnLiveStockProductsClose.setObjectName("btnLiveStockProductsClose")

        self.pushButton_3 = QtGui.QPushButton(LivestockProducts)
        self.pushButton_3.setGeometry(QtCore.QRect(40,200,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(LivestockProducts)
        self.comboBox.setGeometry(QtCore.QRect(120,20,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(LivestockProducts)
        self.label.setGeometry(QtCore.QRect(10,20,54,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(LivestockProducts)
        self.comboBox_3.setGeometry(QtCore.QRect(120,60,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(LivestockProducts)
        self.label_3.setGeometry(QtCore.QRect(10,70,91,18))
        self.label_3.setObjectName("label_3")

        self.comboBox_4 = QtGui.QComboBox(LivestockProducts)
        self.comboBox_4.setGeometry(QtCore.QRect(120,100,131,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtGui.QLabel(LivestockProducts)
        self.label_4.setGeometry(QtCore.QRect(10,100,101,18))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtGui.QLineEdit(LivestockProducts)
        self.lineEdit.setGeometry(QtCore.QRect(120,140,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(LivestockProducts)
        self.label_5.setGeometry(QtCore.QRect(10,150,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(LivestockProducts)
        self.pushButton.setGeometry(QtCore.QRect(160,200,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LivestockProducts)
        QtCore.QMetaObject.connectSlotsByName(LivestockProducts)

    def retranslateUi(self, LivestockProducts):
        LivestockProducts.setWindowTitle(QtGui.QApplication.translate("LivestockProducts", "Manage Livestock Products", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLiveStockProductsClose.setText(QtGui.QApplication.translate("LivestockProducts", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("LivestockProducts", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LivestockProducts", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LivestockProducts", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LivestockProducts", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("LivestockProducts", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LivestockProducts", "Delete", None, QtGui.QApplication.UnicodeUTF8))

