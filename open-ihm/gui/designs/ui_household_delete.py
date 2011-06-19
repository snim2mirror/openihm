# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_delete.ui'
#
# Created: Fri Apr 22 21:52:27 2011
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
        DeleteHousehold.resize(400, 116)
        self.formLayout = QtGui.QFormLayout(DeleteHousehold)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DeleteHousehold)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cboHouseholdName = QtGui.QComboBox(DeleteHousehold)
        self.cboHouseholdName.setObjectName(_fromUtf8("cboHouseholdName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboHouseholdName)
        self.groupBox = QtGui.QGroupBox(DeleteHousehold)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdDel = QtGui.QPushButton(self.groupBox)
        self.cmdDel.setObjectName(_fromUtf8("cmdDel"))
        self.horizontalLayout.addWidget(self.cmdDel)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label.setBuddy(self.cboHouseholdName)

        self.retranslateUi(DeleteHousehold)
        QtCore.QObject.connect(self.cmdDel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteHousehold.delHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteHousehold.mdiClose)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteHousehold.close)
        QtCore.QMetaObject.connectSlotsByName(DeleteHousehold)
        DeleteHousehold.setTabOrder(self.cboHouseholdName, self.cmdDel)
        DeleteHousehold.setTabOrder(self.cmdDel, self.cmdCancel)

    def retranslateUi(self, DeleteHousehold):
        DeleteHousehold.setWindowTitle(QtGui.QApplication.translate("DeleteHousehold", "Delete Household ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DeleteHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDel.setText(QtGui.QApplication.translate("DeleteHousehold", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("DeleteHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

