# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findhousehold.ui'
#
# Created: Thu Apr 21 19:52:06 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindHousehold(object):
    def setupUi(self, FindHousehold):
        FindHousehold.setObjectName(_fromUtf8("FindHousehold"))
        FindHousehold.resize(431, 191)
        FindHousehold.setMinimumSize(QtCore.QSize(414, 160))
        self.formLayout = QtGui.QFormLayout(FindHousehold)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(FindHousehold)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_3)
        self.label = QtGui.QLabel(FindHousehold)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.txtHouseholdNo = QtGui.QLineEdit(FindHousehold)
        self.txtHouseholdNo.setObjectName(_fromUtf8("txtHouseholdNo"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtHouseholdNo)
        self.label_2 = QtGui.QLabel(FindHousehold)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtHouseholdName = QtGui.QLineEdit(FindHousehold)
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtHouseholdName)
        self.groupBox = QtGui.QGroupBox(FindHousehold)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOk = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdOk.sizePolicy().hasHeightForWidth())
        self.cmdOk.setSizePolicy(sizePolicy)
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.horizontalLayout.addWidget(self.cmdOk)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdCancel.sizePolicy().hasHeightForWidth())
        self.cmdCancel.setSizePolicy(sizePolicy)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(FindHousehold)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHousehold.findHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHousehold.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(FindHousehold)
        FindHousehold.setTabOrder(self.txtHouseholdNo, self.txtHouseholdName)

    def retranslateUi(self, FindHousehold):
        FindHousehold.setWindowTitle(QtGui.QApplication.translate("FindHousehold", "Find Household", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindHousehold", "Enter Household No. or Household Name [entering nothing will list all Households]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindHousehold", "Household No.:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("FindHousehold", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("FindHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

