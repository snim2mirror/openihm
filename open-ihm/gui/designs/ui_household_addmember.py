# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addmember.ui'
#
# Created: Sat Oct 16 19:05:17 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdMember(object):
    def setupUi(self, AddHouseholdMember):
        AddHouseholdMember.setObjectName("AddHouseholdMember")
        AddHouseholdMember.setWindowModality(QtCore.Qt.NonModal)
        AddHouseholdMember.resize(392, 248)
        self.chkHeadHousehold = QtGui.QCheckBox(AddHouseholdMember)
        self.chkHeadHousehold.setGeometry(QtCore.QRect(20, 180, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkHeadHousehold.setFont(font)
        self.chkHeadHousehold.setObjectName("chkHeadHousehold")
        self.cmdSave = QtGui.QPushButton(AddHouseholdMember)
        self.cmdSave.setGeometry(QtCore.QRect(10, 210, 91, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdMember)
        self.lblHouseholdName.setGeometry(QtCore.QRect(130, 10, 251, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHouseholdName.sizePolicy().hasHeightForWidth())
        self.lblHouseholdName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblHouseholdName.setFont(font)
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label = QtGui.QLabel(AddHouseholdMember)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cboSex = QtGui.QComboBox(AddHouseholdMember)
        self.cboSex.setGeometry(QtCore.QRect(200, 40, 121, 22))
        self.cboSex.setObjectName("cboSex")
        self.cboSex.addItem("")
        self.cboSex.addItem("")
        self.label_4 = QtGui.QLabel(AddHouseholdMember)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdMember)
        self.cmdCancel.setGeometry(QtCore.QRect(280, 210, 91, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.groupBox = QtGui.QGroupBox(AddHouseholdMember)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 371, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cmbYearOfBirth = QtGui.QComboBox(self.groupBox)
        self.cmbYearOfBirth.setGeometry(QtCore.QRect(190, 60, 121, 22))
        self.cmbYearOfBirth.setObjectName("cmbYearOfBirth")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtAge = QtGui.QLineEdit(self.groupBox)
        self.txtAge.setGeometry(QtCore.QRect(190, 30, 121, 20))
        self.txtAge.setObjectName("txtAge")

        self.retranslateUi(AddHouseholdMember)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdMember)
        AddHouseholdMember.setTabOrder(self.chkHeadHousehold, self.cboSex)
        AddHouseholdMember.setTabOrder(self.cboSex, self.txtAge)
        AddHouseholdMember.setTabOrder(self.txtAge, self.cmbYearOfBirth)
        AddHouseholdMember.setTabOrder(self.cmbYearOfBirth, self.cmdSave)
        AddHouseholdMember.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdMember):
        AddHouseholdMember.setWindowTitle(QtGui.QApplication.translate("AddHouseholdMember", "Add Household Member", None, QtGui.QApplication.UnicodeUTF8))
        self.chkHeadHousehold.setText(QtGui.QApplication.translate("AddHouseholdMember", "This member is head of household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdMember", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdMember", "{name}", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdMember", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSex.setItemText(0, QtGui.QApplication.translate("AddHouseholdMember", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSex.setItemText(1, QtGui.QApplication.translate("AddHouseholdMember", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdMember", "Sex:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdMember", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AddHouseholdMember", "Household Member\'s Age or Year of Birth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdMember", "Year of Birth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdMember", "Age of Household Member:", None, QtGui.QApplication.UnicodeUTF8))

