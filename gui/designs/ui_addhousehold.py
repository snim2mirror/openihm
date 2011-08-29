# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addhousehold.ui'
#
# Created: Fri Apr 22 21:52:26 2011
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
        AddHousehold.resize(428, 214)
        AddHousehold.setMinimumSize(QtCore.QSize(380, 175))
        self.formLayout = QtGui.QFormLayout(AddHousehold)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(AddHousehold)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lblProjectName = QtGui.QLabel(AddHousehold)
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblProjectName)
        self.label_6 = QtGui.QLabel(AddHousehold)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtShortHouseHoldName = QtGui.QLineEdit(AddHousehold)
        self.txtShortHouseHoldName.setObjectName(_fromUtf8("txtShortHouseHoldName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtShortHouseHoldName)
        self.label_2 = QtGui.QLabel(AddHousehold)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtHouseholdName = QtGui.QLineEdit(AddHousehold)
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtHouseholdName)
        self.label_5 = QtGui.QLabel(AddHousehold)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.dtpDateVisted = QtGui.QDateEdit(AddHousehold)
        self.dtpDateVisted.setObjectName(_fromUtf8("dtpDateVisted"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dtpDateVisted)
        self.groupBox = QtGui.QGroupBox(AddHousehold)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label_6.setBuddy(self.txtShortHouseHoldName)
        self.label_2.setBuddy(self.txtHouseholdName)
        self.label_5.setBuddy(self.dtpDateVisted)

        self.retranslateUi(AddHousehold)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHousehold.saveHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHousehold.mdiClose)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHousehold.close)
        QtCore.QMetaObject.connectSlotsByName(AddHousehold)
        AddHousehold.setTabOrder(self.txtShortHouseHoldName, self.txtHouseholdName)
        AddHousehold.setTabOrder(self.txtHouseholdName, self.dtpDateVisted)
        AddHousehold.setTabOrder(self.dtpDateVisted, self.cmdSave)

    def retranslateUi(self, AddHousehold):
        AddHousehold.setWindowTitle(QtGui.QApplication.translate("AddHousehold", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHousehold", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("AddHousehold", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHousehold", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHousehold", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHousehold", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

