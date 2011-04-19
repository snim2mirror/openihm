# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findhousehold.ui'
#
# Created: Tue Apr 19 08:13:15 2011
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
        FindHousehold.resize(414, 160)
        FindHousehold.setMinimumSize(QtCore.QSize(414, 160))
        self.cmdOk = QtGui.QPushButton(FindHousehold)
        self.cmdOk.setGeometry(QtCore.QRect(10, 120, 80, 28))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.cmdCancel = QtGui.QPushButton(FindHousehold)
        self.cmdCancel.setGeometry(QtCore.QRect(320, 120, 80, 28))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.txtHouseholdNo = QtGui.QLineEdit(FindHousehold)
        self.txtHouseholdNo.setGeometry(QtCore.QRect(110, 40, 131, 21))
        self.txtHouseholdNo.setObjectName(_fromUtf8("txtHouseholdNo"))
        self.label = QtGui.QLabel(FindHousehold)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(FindHousehold)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtHouseholdName = QtGui.QLineEdit(FindHousehold)
        self.txtHouseholdName.setGeometry(QtCore.QRect(110, 80, 291, 21))
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))
        self.label_3 = QtGui.QLabel(FindHousehold)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 401, 31))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(FindHousehold)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHousehold.mdiClose)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHousehold.findHousehold)
        QtCore.QMetaObject.connectSlotsByName(FindHousehold)
        FindHousehold.setTabOrder(self.txtHouseholdNo, self.txtHouseholdName)
        FindHousehold.setTabOrder(self.txtHouseholdName, self.cmdOk)
        FindHousehold.setTabOrder(self.cmdOk, self.cmdCancel)

    def retranslateUi(self, FindHousehold):
        FindHousehold.setWindowTitle(QtGui.QApplication.translate("FindHousehold", "Find Household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("FindHousehold", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("FindHousehold", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindHousehold", "Household No.:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindHousehold", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindHousehold", "Enter Household No. or Household Name [entering nothing will list all Households]", None, QtGui.QApplication.UnicodeUTF8))

