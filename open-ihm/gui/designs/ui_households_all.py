# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_households_all.ui'
#
# Created: Tue Apr 19 08:13:16 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AllHouseholds(object):
    def setupUi(self, AllHouseholds):
        AllHouseholds.setObjectName(_fromUtf8("AllHouseholds"))
        AllHouseholds.resize(792, 621)
        AllHouseholds.setMinimumSize(QtCore.QSize(792, 621))
        self.groupBox = QtGui.QGroupBox(AllHouseholds)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 771, 531))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 751, 461))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.cmdAdd = QtGui.QPushButton(self.groupBox)
        self.cmdAdd.setGeometry(QtCore.QRect(10, 490, 91, 31))
        self.cmdAdd.setObjectName(_fromUtf8("cmdAdd"))
        self.cmdEdit = QtGui.QPushButton(self.groupBox)
        self.cmdEdit.setGeometry(QtCore.QRect(110, 490, 91, 31))
        self.cmdEdit.setObjectName(_fromUtf8("cmdEdit"))
        self.cmdData = QtGui.QPushButton(self.groupBox)
        self.cmdData.setGeometry(QtCore.QRect(310, 490, 151, 31))
        self.cmdData.setObjectName(_fromUtf8("cmdData"))
        self.cmdDel = QtGui.QPushButton(self.groupBox)
        self.cmdDel.setGeometry(QtCore.QRect(210, 490, 91, 31))
        self.cmdDel.setObjectName(_fromUtf8("cmdDel"))
        self.cmdClose = QtGui.QPushButton(AllHouseholds)
        self.cmdClose.setGeometry(QtCore.QRect(680, 580, 91, 31))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.label = QtGui.QLabel(AllHouseholds)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lblProjectName = QtGui.QLabel(AllHouseholds)
        self.lblProjectName.setGeometry(QtCore.QRect(100, 10, 391, 16))
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))

        self.retranslateUi(AllHouseholds)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), AllHouseholds.mdiClose)
        QtCore.QObject.connect(self.cmdAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), AllHouseholds.addHousehold)
        QtCore.QObject.connect(self.cmdEdit, QtCore.SIGNAL(_fromUtf8("clicked()")), AllHouseholds.editHousehold)
        QtCore.QObject.connect(self.cmdDel, QtCore.SIGNAL(_fromUtf8("clicked()")), AllHouseholds.delHouseholds)
        QtCore.QObject.connect(self.cmdData, QtCore.SIGNAL(_fromUtf8("clicked()")), AllHouseholds.viewHouseholdData)
        QtCore.QMetaObject.connectSlotsByName(AllHouseholds)
        AllHouseholds.setTabOrder(self.tableView, self.cmdAdd)
        AllHouseholds.setTabOrder(self.cmdAdd, self.cmdEdit)
        AllHouseholds.setTabOrder(self.cmdEdit, self.cmdDel)
        AllHouseholds.setTabOrder(self.cmdDel, self.cmdData)
        AllHouseholds.setTabOrder(self.cmdData, self.cmdClose)

    def retranslateUi(self, AllHouseholds):
        AllHouseholds.setWindowTitle(QtGui.QApplication.translate("AllHouseholds", "Project Households", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AllHouseholds", "Households", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setText(QtGui.QApplication.translate("AllHouseholds", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEdit.setText(QtGui.QApplication.translate("AllHouseholds", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdData.setText(QtGui.QApplication.translate("AllHouseholds", "View|Edit Household Data", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDel.setText(QtGui.QApplication.translate("AllHouseholds", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("AllHouseholds", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AllHouseholds", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("AllHouseholds", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))

