# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_personalcharacteristics.ui'
#
# Created: Wed Feb 24 18:06:49 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PersonalCharacteristics(object):
    def setupUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setObjectName("PersonalCharacteristics")
        PersonalCharacteristics.resize(QtCore.QSize(QtCore.QRect(0,0,389,261).size()).expandedTo(PersonalCharacteristics.minimumSizeHint()))
        PersonalCharacteristics.setMinimumSize(QtCore.QSize(389,261))

        self.btnPCharsClose = QtGui.QPushButton(PersonalCharacteristics)
        self.btnPCharsClose.setGeometry(QtCore.QRect(290,190,80,28))
        self.btnPCharsClose.setObjectName("btnPCharsClose")

        self.pushButton_2 = QtGui.QPushButton(PersonalCharacteristics)
        self.pushButton_2.setGeometry(QtCore.QRect(190,190,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtGui.QPushButton(PersonalCharacteristics)
        self.pushButton_3.setGeometry(QtCore.QRect(90,190,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(PersonalCharacteristics)
        self.comboBox.setGeometry(QtCore.QRect(90,20,281,27))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtGui.QComboBox(PersonalCharacteristics)
        self.comboBox_2.setGeometry(QtCore.QRect(90,70,281,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label = QtGui.QLabel(PersonalCharacteristics)
        self.label.setGeometry(QtCore.QRect(10,20,54,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(PersonalCharacteristics)
        self.label_2.setGeometry(QtCore.QRect(10,80,61,18))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtGui.QLabel(PersonalCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(10,120,71,18))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtGui.QLineEdit(PersonalCharacteristics)
        self.lineEdit.setGeometry(QtCore.QRect(90,120,281,28))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(PersonalCharacteristics)
        QtCore.QMetaObject.connectSlotsByName(PersonalCharacteristics)

    def retranslateUi(self, PersonalCharacteristics):
        PersonalCharacteristics.setWindowTitle(QtGui.QApplication.translate("PersonalCharacteristics", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPCharsClose.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PersonalCharacteristics", "Description", None, QtGui.QApplication.UnicodeUTF8))

