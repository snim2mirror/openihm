# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findprojectresults.ui'
#
# Created: Wed Jun 09 11:07:15 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FindProjectResults(object):
    def setupUi(self, FindProjectResults):
        FindProjectResults.setObjectName("FindProjectResults")
        FindProjectResults.resize(548, 424)
        FindProjectResults.setMinimumSize(QtCore.QSize(548, 424))
        self.groupBox = QtGui.QGroupBox(FindProjectResults)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 531, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 18))
        self.label.setObjectName("label")
        self.txtProjectID = QtGui.QLineEdit(self.groupBox)
        self.txtProjectID.setGeometry(QtCore.QRect(100, 50, 151, 21))
        self.txtProjectID.setObjectName("txtProjectID")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_2.setObjectName("label_2")
        self.txtProjectTitle = QtGui.QLineEdit(self.groupBox)
        self.txtProjectTitle.setGeometry(QtCore.QRect(100, 80, 301, 21))
        self.txtProjectTitle.setObjectName("txtProjectTitle")
        self.cmdSearch = QtGui.QPushButton(self.groupBox)
        self.cmdSearch.setGeometry(QtCore.QRect(430, 70, 75, 31))
        self.cmdSearch.setObjectName("cmdSearch")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 341, 31))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.tblResults = QtGui.QTableView(FindProjectResults)
        self.tblResults.setGeometry(QtCore.QRect(10, 170, 531, 201))
        self.tblResults.setObjectName("tblResults")
        self.cmdOpen = QtGui.QPushButton(FindProjectResults)
        self.cmdOpen.setGeometry(QtCore.QRect(10, 380, 81, 31))
        self.cmdOpen.setObjectName("cmdOpen")
        self.cmdClose = QtGui.QPushButton(FindProjectResults)
        self.cmdClose.setGeometry(QtCore.QRect(454, 380, 81, 31))
        self.cmdClose.setObjectName("cmdClose")
        self.label_3 = QtGui.QLabel(FindProjectResults)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 111, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(FindProjectResults)
        QtCore.QMetaObject.connectSlotsByName(FindProjectResults)

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

