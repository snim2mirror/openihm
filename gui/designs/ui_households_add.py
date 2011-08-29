# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_households_add.ui'
#
# Created: Fri Apr 22 21:52:28 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Households_Add(object):
    def setupUi(self, Households_Add):
        Households_Add.setObjectName(_fromUtf8("Households_Add"))
        Households_Add.resize(420, 211)
        self.formLayout = QtGui.QFormLayout(Households_Add)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(Households_Add)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lblProjectName = QtGui.QLabel(Households_Add)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblProjectName.setFont(font)
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblProjectName)
        self.label_6 = QtGui.QLabel(Households_Add)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtShortHouseHoldName = QtGui.QLineEdit(Households_Add)
        self.txtShortHouseHoldName.setObjectName(_fromUtf8("txtShortHouseHoldName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtShortHouseHoldName)
        self.label_2 = QtGui.QLabel(Households_Add)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtHouseholdName = QtGui.QLineEdit(Households_Add)
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtHouseholdName)
        self.label_5 = QtGui.QLabel(Households_Add)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.dtpDateVisted = QtGui.QDateEdit(Households_Add)
        self.dtpDateVisted.setObjectName(_fromUtf8("dtpDateVisted"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dtpDateVisted)
        self.groupBox = QtGui.QGroupBox(Households_Add)
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

        self.retranslateUi(Households_Add)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), Households_Add.saveHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Households_Add.mdiClose)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Households_Add.close)
        QtCore.QMetaObject.connectSlotsByName(Households_Add)
        Households_Add.setTabOrder(self.txtShortHouseHoldName, self.txtHouseholdName)
        Households_Add.setTabOrder(self.txtHouseholdName, self.dtpDateVisted)

    def retranslateUi(self, Households_Add):
        Households_Add.setWindowTitle(QtGui.QApplication.translate("Households_Add", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Households_Add", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("Households_Add", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Households_Add", "Household Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Households_Add", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Households_Add", "Date Visited:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("Households_Add", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("Households_Add", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

