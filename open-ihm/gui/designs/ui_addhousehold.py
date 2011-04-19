# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addhousehold.ui'
#
# Created: Tue Apr 19 14:51:30 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHousehold(object):
    def setupUi(self, AddHousehold):
        AddHousehold.setObjectName(_fromUtf8("AddHousehold"))
        AddHousehold.resize(380, 175)
        AddHousehold.setMinimumSize(QtCore.QSize(380, 175))
        self.txtShortHouseHoldName = QtGui.QLineEdit(AddHousehold)
        self.txtShortHouseHoldName.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.txtShortHouseHoldName.setObjectName(_fromUtf8("txtShortHouseHoldName"))
        self.label_2 = QtGui.QLabel(AddHousehold)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(AddHousehold)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblProjectName = QtGui.QLabel(AddHousehold)
        self.lblProjectName.setGeometry(QtCore.QRect(130, 10, 101, 16))
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.label_5 = QtGui.QLabel(AddHousehold)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dtpDateVisted = QtGui.QDateEdit(AddHousehold)
        self.dtpDateVisted.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.dtpDateVisted.setObjectName(_fromUtf8("dtpDateVisted"))
        self.cmdSave = QtGui.QPushButton(AddHousehold)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmdCancel = QtGui.QPushButton(AddHousehold)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label_6 = QtGui.QLabel(AddHousehold)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtHouseholdName = QtGui.QLineEdit(AddHousehold)
        self.txtHouseholdName.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))

        self.retranslateUi(AddHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHousehold.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHousehold.saveHousehold)
        QtCore.QMetaObject.connectSlotsByName(AddHousehold)
        AddHousehold.setTabOrder(self.txtShortHouseHoldName, self.txtHouseholdName)
        AddHousehold.setTabOrder(self.txtHouseholdName, self.dtpDateVisted)
        AddHousehold.setTabOrder(self.dtpDateVisted, self.cmdSave)
        AddHousehold.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHousehold):
        AddHousehold.setWindowTitle(QtGui.QApplication.translate("AddHousehold", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHousehold", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("AddHousehold", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHousehold", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHousehold", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHousehold", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))

