# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managelivestock.ui'
#
# Created: Sun Feb 28 13:25:33 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LivestockDetails(object):
    def setupUi(self, LivestockDetails):
        LivestockDetails.setObjectName("LivestockDetails")
        LivestockDetails.resize(QtCore.QSize(QtCore.QRect(0,0,369,238).size()).expandedTo(LivestockDetails.minimumSizeHint()))
        LivestockDetails.setMinimumSize(QtCore.QSize(369,238))

        self.btnManageLiveStockClose = QtGui.QPushButton(LivestockDetails)
        self.btnManageLiveStockClose.setGeometry(QtCore.QRect(270,200,80,28))
        self.btnManageLiveStockClose.setObjectName("btnManageLiveStockClose")

        self.pushButton_3 = QtGui.QPushButton(LivestockDetails)
        self.pushButton_3.setGeometry(QtCore.QRect(40,200,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(LivestockDetails)
        self.comboBox.setGeometry(QtCore.QRect(120,20,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(LivestockDetails)
        self.label.setGeometry(QtCore.QRect(10,20,54,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(LivestockDetails)
        self.comboBox_3.setGeometry(QtCore.QRect(120,60,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(LivestockDetails)
        self.label_3.setGeometry(QtCore.QRect(10,70,91,18))
        self.label_3.setObjectName("label_3")

        self.comboBox_4 = QtGui.QComboBox(LivestockDetails)
        self.comboBox_4.setGeometry(QtCore.QRect(120,100,131,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtGui.QLabel(LivestockDetails)
        self.label_4.setGeometry(QtCore.QRect(10,100,101,18))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtGui.QLineEdit(LivestockDetails)
        self.lineEdit.setGeometry(QtCore.QRect(120,140,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(LivestockDetails)
        self.label_5.setGeometry(QtCore.QRect(10,150,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(LivestockDetails)
        self.pushButton.setGeometry(QtCore.QRect(160,200,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LivestockDetails)
        QtCore.QMetaObject.connectSlotsByName(LivestockDetails)

    def retranslateUi(self, LivestockDetails):
        LivestockDetails.setWindowTitle(QtGui.QApplication.translate("LivestockDetails", "Manage Livestock ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageLiveStockClose.setText(QtGui.QApplication.translate("LivestockDetails", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("LivestockDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LivestockDetails", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LivestockDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LivestockDetails", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("LivestockDetails", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LivestockDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))

