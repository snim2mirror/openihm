# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editmembercharacteristic.ui'
#
# Created: Sat Oct 16 11:29:07 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditMemberCharacteristics(object):
    def setupUi(self, EditMemberCharacteristics):
        EditMemberCharacteristics.setObjectName("EditMemberCharacteristics")
        EditMemberCharacteristics.resize(390, 415)
        self.label = QtGui.QLabel(EditMemberCharacteristics)
        self.label.setGeometry(QtCore.QRect(9, 9, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblHouseholdName = QtGui.QLabel(EditMemberCharacteristics)
        self.lblHouseholdName.setGeometry(QtCore.QRect(130, 10, 44, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblHouseholdName.setFont(font)
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label_2 = QtGui.QLabel(EditMemberCharacteristics)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 112, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblHeadOfHousehold = QtGui.QLabel(EditMemberCharacteristics)
        self.lblHeadOfHousehold.setGeometry(QtCore.QRect(130, 40, 109, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblHeadOfHousehold.setFont(font)
        self.lblHeadOfHousehold.setObjectName("lblHeadOfHousehold")
        self.lblMemberAge = QtGui.QLabel(EditMemberCharacteristics)
        self.lblMemberAge.setGeometry(QtCore.QRect(130, 70, 46, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMemberAge.setFont(font)
        self.lblMemberAge.setObjectName("lblMemberAge")
        self.label_3 = QtGui.QLabel(EditMemberCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtGui.QLabel(EditMemberCharacteristics)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lblMemberSex = QtGui.QLabel(EditMemberCharacteristics)
        self.lblMemberSex.setGeometry(QtCore.QRect(130, 100, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMemberSex.setFont(font)
        self.lblMemberSex.setObjectName("lblMemberSex")
        self.groupBox = QtGui.QGroupBox(EditMemberCharacteristics)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 371, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tblPersonalChars = QtGui.QTableView(self.groupBox)
        self.tblPersonalChars.setGeometry(QtCore.QRect(10, 20, 351, 201))
        self.tblPersonalChars.setObjectName("tblPersonalChars")
        self.cmdEdit = QtGui.QPushButton(self.groupBox)
        self.cmdEdit.setGeometry(QtCore.QRect(10, 230, 91, 31))
        self.cmdEdit.setObjectName("cmdEdit")
        self.cmdClose = QtGui.QPushButton(self.groupBox)
        self.cmdClose.setGeometry(QtCore.QRect(274, 230, 81, 31))
        self.cmdClose.setObjectName("cmdClose")

        self.retranslateUi(EditMemberCharacteristics)
        QtCore.QMetaObject.connectSlotsByName(EditMemberCharacteristics)

    def retranslateUi(self, EditMemberCharacteristics):
        EditMemberCharacteristics.setWindowTitle(QtGui.QApplication.translate("EditMemberCharacteristics", "Edit Household Member Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "{name}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "Head of Household:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHeadOfHousehold.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "{headofhousehold}", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMemberAge.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "{age}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "Member\'s Age:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "Sex:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMemberSex.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "{sex}", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("EditMemberCharacteristics", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEdit.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("EditMemberCharacteristics", "Close", None, QtGui.QApplication.UnicodeUTF8))
