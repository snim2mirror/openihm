# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findprojectresults.ui'
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

class Ui_FindProjectResults(object):
    def setupUi(self, FindProjectResults):
        FindProjectResults.setObjectName(_fromUtf8("FindProjectResults"))
        FindProjectResults.resize(548, 424)
        FindProjectResults.setMinimumSize(QtCore.QSize(548, 424))
        self.groupBox = QtGui.QGroupBox(FindProjectResults)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 531, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtProjectID = QtGui.QLineEdit(self.groupBox)
        self.txtProjectID.setGeometry(QtCore.QRect(100, 50, 151, 21))
        self.txtProjectID.setObjectName(_fromUtf8("txtProjectID"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtProjectTitle = QtGui.QLineEdit(self.groupBox)
        self.txtProjectTitle.setGeometry(QtCore.QRect(100, 80, 301, 21))
        self.txtProjectTitle.setObjectName(_fromUtf8("txtProjectTitle"))
        self.cmdSearch = QtGui.QPushButton(self.groupBox)
        self.cmdSearch.setGeometry(QtCore.QRect(430, 70, 75, 31))
        self.cmdSearch.setObjectName(_fromUtf8("cmdSearch"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 341, 31))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tblResults = QtGui.QTableView(FindProjectResults)
        self.tblResults.setGeometry(QtCore.QRect(10, 170, 531, 201))
        self.tblResults.setObjectName(_fromUtf8("tblResults"))
        self.cmdOpen = QtGui.QPushButton(FindProjectResults)
        self.cmdOpen.setGeometry(QtCore.QRect(10, 380, 81, 31))
        self.cmdOpen.setObjectName(_fromUtf8("cmdOpen"))
        self.cmdClose = QtGui.QPushButton(FindProjectResults)
        self.cmdClose.setGeometry(QtCore.QRect(454, 380, 81, 31))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.label_3 = QtGui.QLabel(FindProjectResults)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(FindProjectResults)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProjectResults.mdiClose)
        QtCore.QObject.connect(self.cmdOpen, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProjectResults.openProject)
        QtCore.QObject.connect(self.cmdSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), FindProjectResults.showResults)
        QtCore.QMetaObject.connectSlotsByName(FindProjectResults)
        FindProjectResults.setTabOrder(self.txtProjectID, self.txtProjectTitle)
        FindProjectResults.setTabOrder(self.txtProjectTitle, self.cmdSearch)
        FindProjectResults.setTabOrder(self.cmdSearch, self.tblResults)
        FindProjectResults.setTabOrder(self.tblResults, self.cmdOpen)
        FindProjectResults.setTabOrder(self.cmdOpen, self.cmdClose)

    def retranslateUi(self, FindProjectResults):
        FindProjectResults.setWindowTitle(QtGui.QApplication.translate("FindProjectResults", "Project Search Results", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FindProjectResults", "Search Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindProjectResults", "Project ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindProjectResults", "Project Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSearch.setText(QtGui.QApplication.translate("FindProjectResults", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FindProjectResults", "Enter Project ID or Project Title [entering nothing will list all projects]", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOpen.setText(QtGui.QApplication.translate("FindProjectResults", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("FindProjectResults", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindProjectResults", "Found Projects", None, QtGui.QApplication.UnicodeUTF8))

