# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manageemployment.ui'
#
# Created: Sun Feb 28 23:05:09 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ManageEmployment(object):
    def setupUi(self, ManageEmployment):
        ManageEmployment.setObjectName("ManageEmployment")
        ManageEmployment.resize(QtCore.QSize(QtCore.QRect(0,0,389,270).size()).expandedTo(ManageEmployment.minimumSizeHint()))
        ManageEmployment.setMinimumSize(QtCore.QSize(389,261))

        self.btnManageEmploymentClose = QtGui.QPushButton(ManageEmployment)
        self.btnManageEmploymentClose.setGeometry(QtCore.QRect(270,230,80,28))
        self.btnManageEmploymentClose.setObjectName("btnManageEmploymentClose")

        self.pushButton_3 = QtGui.QPushButton(ManageEmployment)
        self.pushButton_3.setGeometry(QtCore.QRect(40,230,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(ManageEmployment)
        self.comboBox.setGeometry(QtCore.QRect(140,20,221,27))
        self.comboBox.setObjectName("comboBox")

        self.label = QtGui.QLabel(ManageEmployment)
        self.label.setGeometry(QtCore.QRect(10,30,111,18))
        self.label.setObjectName("label")

        self.comboBox_3 = QtGui.QComboBox(ManageEmployment)
        self.comboBox_3.setGeometry(QtCore.QRect(140,180,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(ManageEmployment)
        self.label_3.setGeometry(QtCore.QRect(10,190,91,18))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtGui.QPushButton(ManageEmployment)
        self.pushButton.setGeometry(QtCore.QRect(160,230,80,28))
        self.pushButton.setObjectName("pushButton")

        self.groupBox = QtGui.QGroupBox(ManageEmployment)
        self.groupBox.setGeometry(QtCore.QRect(140,60,221,41))
        self.groupBox.setObjectName("groupBox")

        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10,10,91,24))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(100,10,91,24))
        self.radioButton_2.setObjectName("radioButton_2")

        self.label_2 = QtGui.QLabel(ManageEmployment)
        self.label_2.setGeometry(QtCore.QRect(10,70,111,18))
        self.label_2.setObjectName("label_2")

        self.groupBox_2 = QtGui.QGroupBox(ManageEmployment)
        self.groupBox_2.setGeometry(QtCore.QRect(140,120,221,41))
        self.groupBox_2.setObjectName("groupBox_2")

        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10,10,80,24))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(100,10,80,24))
        self.checkBox_2.setObjectName("checkBox_2")

        self.label_4 = QtGui.QLabel(ManageEmployment)
        self.label_4.setGeometry(QtCore.QRect(10,130,101,18))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ManageEmployment)
        QtCore.QMetaObject.connectSlotsByName(ManageEmployment)

    def retranslateUi(self, ManageEmployment):
        ManageEmployment.setWindowTitle(QtGui.QApplication.translate("ManageEmployment", "Manage Employment Details", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageEmploymentClose.setText(QtGui.QApplication.translate("ManageEmployment", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("ManageEmployment", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageEmployment", "Type of Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageEmployment", "Daily Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ManageEmployment", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("ManageEmployment", "Males", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("ManageEmployment", "Females", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageEmployment", "Work is Done By?", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("ManageEmployment", "Cash", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("ManageEmployment", "Kind", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageEmployment", "Payment Type", None, QtGui.QApplication.UnicodeUTF8))

