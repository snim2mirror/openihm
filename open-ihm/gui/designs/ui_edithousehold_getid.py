# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edithousehold_getid.ui'
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

class Ui_EditHouseholdGetID(object):
    def setupUi(self, EditHouseholdGetID):
        EditHouseholdGetID.setObjectName(_fromUtf8("EditHouseholdGetID"))
        EditHouseholdGetID.resize(393, 114)
        EditHouseholdGetID.setMinimumSize(QtCore.QSize(393, 114))
        self.cmdOk = QtGui.QPushButton(EditHouseholdGetID)
        self.cmdOk.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.cmdCancel = QtGui.QPushButton(EditHouseholdGetID)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 60, 81, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label = QtGui.QLabel(EditHouseholdGetID)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.cboHouseholdName = QtGui.QComboBox(EditHouseholdGetID)
        self.cboHouseholdName.setGeometry(QtCore.QRect(100, 20, 281, 22))
        self.cboHouseholdName.setObjectName(_fromUtf8("cboHouseholdName"))

        self.retranslateUi(EditHouseholdGetID)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHouseholdGetID.showDetails)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHouseholdGetID.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(EditHouseholdGetID)
        EditHouseholdGetID.setTabOrder(self.cboHouseholdName, self.cmdOk)
        EditHouseholdGetID.setTabOrder(self.cmdOk, self.cmdCancel)

    def retranslateUi(self, EditHouseholdGetID):
        EditHouseholdGetID.setWindowTitle(QtGui.QApplication.translate("EditHouseholdGetID", "Edit Household - Select Household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))

