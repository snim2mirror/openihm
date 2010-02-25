# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_housecharacteristics.ui'
#
# Created: Wed Feb 24 17:40:54 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HouseCharacteristics(object):
    def setupUi(self, HouseCharacteristics):
        HouseCharacteristics.setObjectName("HouseCharacteristics")
        HouseCharacteristics.resize(QtCore.QSize(QtCore.QRect(0,0,389,261).size()).expandedTo(HouseCharacteristics.minimumSizeHint()))
        HouseCharacteristics.setMinimumSize(QtCore.QSize(389,261))

        self.btnHouseClose = QtGui.QPushButton(HouseCharacteristics)
        self.btnHouseClose.setGeometry(QtCore.QRect(280,180,80,28))
        self.btnHouseClose.setObjectName("btnHouseClose")

        self.pushButton_2 = QtGui.QPushButton(HouseCharacteristics)
        self.pushButton_2.setGeometry(QtCore.QRect(180,180,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtGui.QPushButton(HouseCharacteristics)
        self.pushButton_3.setGeometry(QtCore.QRect(80,180,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(HouseCharacteristics)
        self.comboBox.setGeometry(QtCore.QRect(100,10,251,27))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtGui.QComboBox(HouseCharacteristics)
        self.comboBox_2.setGeometry(QtCore.QRect(100,60,251,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label = QtGui.QLabel(HouseCharacteristics)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(HouseCharacteristics)
        self.label_2.setGeometry(QtCore.QRect(10,60,61,18))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtGui.QLineEdit(HouseCharacteristics)
        self.lineEdit.setGeometry(QtCore.QRect(100,110,251,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtGui.QLabel(HouseCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(10,120,61,18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(HouseCharacteristics)
        QtCore.QMetaObject.connectSlotsByName(HouseCharacteristics)

    def retranslateUi(self, HouseCharacteristics):
        HouseCharacteristics.setWindowTitle(QtGui.QApplication.translate("HouseCharacteristics", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHouseClose.setText(QtGui.QApplication.translate("HouseCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("HouseCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("HouseCharacteristics", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HouseCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))

