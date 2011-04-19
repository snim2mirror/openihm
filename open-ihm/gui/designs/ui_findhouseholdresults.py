# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findhouseholdresults.ui'
#
# Created: Tue Apr 19 10:36:38 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindHouseholdResults(object):
    def setupUi(self, FindHouseholdResults):
        FindHouseholdResults.setObjectName(_fromUtf8("FindHouseholdResults"))
        FindHouseholdResults.resize(551, 620)
        FindHouseholdResults.setMinimumSize(QtCore.QSize(548, 620))
        self.groupBox = QtGui.QGroupBox(FindHouseholdResults)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 531, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 81, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtHouseholdNo = QtGui.QLineEdit(self.groupBox)
        self.txtHouseholdNo.setGeometry(QtCore.QRect(120, 50, 161, 21))
        self.txtHouseholdNo.setObjectName(_fromUtf8("txtHouseholdNo"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtHouseholdName = QtGui.QLineEdit(self.groupBox)
        self.txtHouseholdName.setGeometry(QtCore.QRect(120, 80, 281, 21))
        self.txtHouseholdName.setObjectName(_fromUtf8("txtHouseholdName"))
        self.cmdSearch = QtGui.QPushButton(self.groupBox)
        self.cmdSearch.setGeometry(QtCore.QRect(440, 70, 75, 31))
        self.cmdSearch.setObjectName(_fromUtf8("cmdSearch"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 511, 31))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_2 = QtGui.QGroupBox(FindHouseholdResults)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 531, 411))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tblResults = QtGui.QTableView(self.groupBox_2)
        self.tblResults.setGeometry(QtCore.QRect(10, 20, 511, 341))
        self.tblResults.setAlternatingRowColors(True)
        self.tblResults.setSortingEnabled(True)
        self.tblResults.setObjectName(_fromUtf8("tblResults"))
        self.cmdEdit = QtGui.QPushButton(self.groupBox_2)
        self.cmdEdit.setGeometry(QtCore.QRect(110, 370, 91, 31))
        self.cmdEdit.setObjectName(_fromUtf8("cmdEdit"))
        self.cmdDel = QtGui.QPushButton(self.groupBox_2)
        self.cmdDel.setGeometry(QtCore.QRect(210, 370, 91, 31))
        self.cmdDel.setObjectName(_fromUtf8("cmdDel"))
        self.cmdAdd = QtGui.QPushButton(self.groupBox_2)
        self.cmdAdd.setGeometry(QtCore.QRect(10, 370, 91, 31))
        self.cmdAdd.setObjectName(_fromUtf8("cmdAdd"))
        self.cmdData = QtGui.QPushButton(self.groupBox_2)
        self.cmdData.setGeometry(QtCore.QRect(310, 370, 151, 31))
        self.cmdData.setObjectName(_fromUtf8("cmdData"))
        self.label_3 = QtGui.QLabel(FindHouseholdResults)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblProjectName = QtGui.QLabel(FindHouseholdResults)
        self.lblProjectName.setGeometry(QtCore.QRect(110, 10, 431, 21))
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.cmdClose = QtGui.QPushButton(FindHouseholdResults)
        self.cmdClose.setGeometry(QtCore.QRect(440, 580, 81, 31))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))

        self.retranslateUi(FindHouseholdResults)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHouseholdResults.mdiClose)
        QtCore.QObject.connect(self.cmdSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHouseholdResults.getHouseholds)
        QtCore.QObject.connect(self.cmdAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHouseholdResults.addHousehold)
        QtCore.QObject.connect(self.cmdEdit, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHouseholdResults.editHousehold)
        QtCore.QObject.connect(self.cmdDel, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHouseholdResults.delHouseholds)
        QtCore.QObject.connect(self.cmdData, QtCore.SIGNAL(_fromUtf8("clicked()")), FindHouseholdResults.viewHouseholdData)
        QtCore.QMetaObject.connectSlotsByName(FindHouseholdResults)
        FindHouseholdResults.setTabOrder(self.txtHouseholdNo, self.txtHouseholdName)
        FindHouseholdResults.setTabOrder(self.txtHouseholdName, self.cmdSearch)
        FindHouseholdResults.setTabOrder(self.cmdSearch, self.tblResults)
        FindHouseholdResults.setTabOrder(self.tblResults, self.cmdAdd)
        FindHouseholdResults.setTabOrder(self.cmdAdd, self.cmdEdit)
        FindHouseholdResults.setTabOrder(self.cmdEdit, self.cmdDel)
        FindHouseholdResults.setTabOrder(self.cmdDel, self.cmdData)
        FindHouseholdResults.setTabOrder(self.cmdData, self.cmdClose)

    def retranslateUi(self, FindHouseholdResults):
        FindHouseholdResults.setWindowTitle(QtGui.QApplication.translate("FindHouseholdResults", "Household Search Results", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FindHouseholdResults", "Search Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindHouseholdResults", "Household No:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindHouseholdResults", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSearch.setText(QtGui.QApplication.translate("FindHouseholdResults", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FindHouseholdResults", "Enter Household No. or Household Name [entering nothing will list all households in the current project]", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FindHouseholdResults", "Households", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEdit.setText(QtGui.QApplication.translate("FindHouseholdResults", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDel.setText(QtGui.QApplication.translate("FindHouseholdResults", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setText(QtGui.QApplication.translate("FindHouseholdResults", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdData.setText(QtGui.QApplication.translate("FindHouseholdResults", "View|Edit Household Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindHouseholdResults", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("FindHouseholdResults", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("FindHouseholdResults", "Close", None, QtGui.QApplication.UnicodeUTF8))

