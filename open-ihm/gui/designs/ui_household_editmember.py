# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_editmember.ui'
#
# Created: Sun May 16 20:05:31 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditHouseholdMember(object):
    def setupUi(self, EditHouseholdMember):
        EditHouseholdMember.setObjectName("EditHouseholdMember")
        EditHouseholdMember.resize(390, 243)
        self.cmdSave = QtGui.QPushButton(EditHouseholdMember)
        self.cmdSave.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.chkHeadHousehold = QtGui.QCheckBox(EditHouseholdMember)
        self.chkHeadHousehold.setGeometry(QtCore.QRect(260, 40, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkHeadHousehold.setFont(font)
        self.chkHeadHousehold.setObjectName("chkHeadHousehold")
        self.label = QtGui.QLabel(EditHouseholdMember)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dtpDOB = QtGui.QDateEdit(EditHouseholdMember)
        self.dtpDOB.setGeometry(QtCore.QRect(130, 80, 121, 22))
        self.dtpDOB.setObjectName("dtpDOB")
        self.label_3 = QtGui.QLabel(EditHouseholdMember)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtGui.QLabel(EditHouseholdMember)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtMemberID = QtGui.QLineEdit(EditHouseholdMember)
        self.txtMemberID.setGeometry(QtCore.QRect(130, 40, 121, 20))
        self.txtMemberID.setObjectName("txtMemberID")
        self.label_4 = QtGui.QLabel(EditHouseholdMember)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cboSex = QtGui.QComboBox(EditHouseholdMember)
        self.cboSex.setGeometry(QtCore.QRect(130, 120, 121, 22))
        self.cboSex.setObjectName("cboSex")
        self.cboSex.addItem("")
        self.cboSex.addItem("")
        self.lblHouseholdName = QtGui.QLabel(EditHouseholdMember)
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
        self.label_5 = QtGui.QLabel(EditHouseholdMember)
        self.label_5.setGeometry(QtCore.QRect(50, 160, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtEducation = QtGui.QLineEdit(EditHouseholdMember)
        self.txtEducation.setGeometry(QtCore.QRect(130, 160, 251, 20))
        self.txtEducation.setObjectName("txtEducation")
        self.cmdCancel = QtGui.QPushButton(EditHouseholdMember)
        self.cmdCancel.setGeometry(QtCore.QRect(290, 200, 91, 31))
        self.cmdCancel.setObjectName("cmdCancel")

        self.retranslateUi(EditHouseholdMember)
        QtCore.QMetaObject.connectSlotsByName(EditHouseholdMember)

    def retranslateUi(self, EditHouseholdMember):
        EditHouseholdMember.setWindowTitle(QtGui.QApplication.translate("EditHouseholdMember", "Edit Household Member", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditHouseholdMember", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.chkHeadHousehold.setText(QtGui.QApplication.translate("EditHouseholdMember", "Household Head", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditHouseholdMember", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditHouseholdMember", "Date of Birth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditHouseholdMember", "Member ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditHouseholdMember", "Sex:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSex.setItemText(0, QtGui.QApplication.translate("EditHouseholdMember", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSex.setItemText(1, QtGui.QApplication.translate("EditHouseholdMember", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("EditHouseholdMember", "{name}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditHouseholdMember", "Education:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHouseholdMember", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

