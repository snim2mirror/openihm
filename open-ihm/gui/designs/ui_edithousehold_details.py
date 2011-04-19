# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edithousehold_details.ui'
#
# Created: Tue Apr 19 03:45:23 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditHousehold(object):
    def setupUi(self, EditHousehold):
        EditHousehold.setObjectName(_fromUtf8("EditHousehold"))
        EditHousehold.resize(380, 175)
        EditHousehold.setMinimumSize(QtCore.QSize(380, 175))
        self.txtShortHouseHoldName = QtGui.QLineEdit(EditHousehold)
        self.txtShortHouseHoldName.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.txtShortHouseHoldName.setObjectName(_fromUtf8("txtShortHouseHoldName"))
        self.label_2 = QtGui.QLabel(EditHousehold)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(EditHousehold)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblProjectName = QtGui.QLabel(EditHousehold)
        self.lblProjectName.setGeometry(QtCore.QRect(130, 10, 101, 16))
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.label_5 = QtGui.QLabel(EditHousehold)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dtpDateVisted = QtGui.QDateEdit(EditHousehold)
        self.dtpDateVisted.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.dtpDateVisted.setObjectName(_fromUtf8("dtpDateVisted"))
        self.cmdSave = QtGui.QPushButton(EditHousehold)
        self.cmdSave.setGeometry(QtCore.QRect(10, 132, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmdCancel = QtGui.QPushButton(EditHousehold)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 132, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label_6 = QtGui.QLabel(EditHousehold)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtHouseholdName = QtGui.QLineEdit(EditHousehold)
        self.txtHouseholdName.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))

        self.retranslateUi(EditHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHousehold.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHousehold.saveHousehold)
        QtCore.QMetaObject.connectSlotsByName(EditHousehold)
        EditHousehold.setTabOrder(self.txtShortHouseHoldName, self.txtHouseholdName)
        EditHousehold.setTabOrder(self.txtHouseholdName, self.dtpDateVisted)
        EditHousehold.setTabOrder(self.dtpDateVisted, self.cmdSave)
        EditHousehold.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, EditHousehold):
        EditHousehold.setWindowTitle(QtGui.QApplication.translate("EditHousehold", "Edit Household Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditHousehold", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("EditHousehold", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditHousehold", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditHousehold", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditHousehold", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))

