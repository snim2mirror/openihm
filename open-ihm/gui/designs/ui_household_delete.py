# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_delete.ui'
#
# Created: Tue Apr 19 03:45:24 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeleteHousehold(object):
    def setupUi(self, DeleteHousehold):
        DeleteHousehold.setObjectName(_fromUtf8("DeleteHousehold"))
        DeleteHousehold.resize(400, 108)
        self.cmdDel = QtGui.QPushButton(DeleteHousehold)
        self.cmdDel.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.cmdDel.setObjectName(_fromUtf8("cmdDel"))
        self.label = QtGui.QLabel(DeleteHousehold)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cboHouseholdName = QtGui.QComboBox(DeleteHousehold)
        self.cboHouseholdName.setGeometry(QtCore.QRect(120, 20, 261, 22))
        self.cboHouseholdName.setObjectName(_fromUtf8("cboHouseholdName"))
        self.cmdCancel = QtGui.QPushButton(DeleteHousehold)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 60, 81, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))

        self.retranslateUi(DeleteHousehold)
        QtCore.QObject.connect(self.cmdDel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteHousehold.delHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteHousehold.mdiClose)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteHousehold.close)
        QtCore.QMetaObject.connectSlotsByName(DeleteHousehold)
        DeleteHousehold.setTabOrder(self.cboHouseholdName, self.cmdDel)
        DeleteHousehold.setTabOrder(self.cmdDel, self.cmdCancel)

    def retranslateUi(self, DeleteHousehold):
        DeleteHousehold.setWindowTitle(QtGui.QApplication.translate("DeleteHousehold", "Delete Household ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDel.setText(QtGui.QApplication.translate("DeleteHousehold", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DeleteHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("DeleteHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

