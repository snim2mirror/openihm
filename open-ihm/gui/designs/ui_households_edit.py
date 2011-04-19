# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_households_edit.ui'
#
# Created: Tue Apr 19 08:09:03 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Households_Edit(object):
    def setupUi(self, Households_Edit):
        Households_Edit.setObjectName(_fromUtf8("Households_Edit"))
        Households_Edit.resize(384, 175)
        self.lblProjectName = QtGui.QLabel(Households_Edit)
        self.lblProjectName.setGeometry(QtCore.QRect(130, 10, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblProjectName.setFont(font)
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.label_5 = QtGui.QLabel(Households_Edit)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cmdCancel = QtGui.QPushButton(Households_Edit)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.dtpDateVisted = QtGui.QDateEdit(Households_Edit)
        self.dtpDateVisted.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.dtpDateVisted.setObjectName(_fromUtf8("dtpDateVisted"))
        self.label_6 = QtGui.QLabel(Households_Edit)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cmdSave = QtGui.QPushButton(Households_Edit)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.txtShortHouseHoldName = QtGui.QLineEdit(Households_Edit)
        self.txtShortHouseHoldName.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.txtShortHouseHoldName.setObjectName(_fromUtf8("txtShortHouseHoldName"))
        self.label_2 = QtGui.QLabel(Households_Edit)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtHouseholdName = QtGui.QLineEdit(Households_Edit)
        self.txtHouseholdName.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))
        self.label_3 = QtGui.QLabel(Households_Edit)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Households_Edit)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Households_Edit.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), Households_Edit.saveHousehold)
        QtCore.QMetaObject.connectSlotsByName(Households_Edit)
        Households_Edit.setTabOrder(self.txtShortHouseHoldName, self.txtHouseholdName)
        Households_Edit.setTabOrder(self.txtHouseholdName, self.dtpDateVisted)
        Households_Edit.setTabOrder(self.dtpDateVisted, self.cmdSave)
        Households_Edit.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, Households_Edit):
        Households_Edit.setWindowTitle(QtGui.QApplication.translate("Households_Edit", "Edit Household", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("Households_Edit", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Households_Edit", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("Households_Edit", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Households_Edit", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("Households_Edit", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Households_Edit", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Households_Edit", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))

