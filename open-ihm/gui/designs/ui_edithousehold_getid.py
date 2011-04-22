# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edithousehold_getid.ui'
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

class Ui_EditHouseholdGetID(object):
    def setupUi(self, EditHouseholdGetID):
        EditHouseholdGetID.setObjectName(_fromUtf8("EditHouseholdGetID"))
        EditHouseholdGetID.resize(393, 114)
        EditHouseholdGetID.setMinimumSize(QtCore.QSize(393, 114))
        self.formLayout = QtGui.QFormLayout(EditHouseholdGetID)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(EditHouseholdGetID)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cboHouseholdName = QtGui.QComboBox(EditHouseholdGetID)
        self.cboHouseholdName.setObjectName(_fromUtf8("cboHouseholdName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboHouseholdName)
        self.groupBox = QtGui.QGroupBox(EditHouseholdGetID)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOk = QtGui.QPushButton(self.groupBox)
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.horizontalLayout.addWidget(self.cmdOk)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label.setBuddy(self.cboHouseholdName)

        self.retranslateUi(EditHouseholdGetID)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHouseholdGetID.showDetails)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditHouseholdGetID.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(EditHouseholdGetID)
        EditHouseholdGetID.setTabOrder(self.cboHouseholdName, self.cmdOk)
        EditHouseholdGetID.setTabOrder(self.cmdOk, self.cmdCancel)

    def retranslateUi(self, EditHouseholdGetID):
        EditHouseholdGetID.setWindowTitle(QtGui.QApplication.translate("EditHouseholdGetID", "Edit Household - Select Household", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditHouseholdGetID", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

