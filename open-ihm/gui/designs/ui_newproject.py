# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newproject.ui'
#
# Created: Thu Feb 18 18:24:10 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(389, 261)
        NewProject.setMinimumSize(QtCore.QSize(389, 261))
        self.BtnProjectSave = QtGui.QPushButton(NewProject)
        self.BtnProjectSave.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.BtnProjectSave.setObjectName("BtnProjectSave")
        self.BtnProjectCancel = QtGui.QPushButton(NewProject)
        self.BtnProjectCancel.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.BtnProjectCancel.setObjectName("BtnProjectCancel")
        self.TxtProjectID = QtGui.QLineEdit(NewProject)
        self.TxtProjectID.setGeometry(QtCore.QRect(100, 10, 113, 20))
        self.TxtProjectID.setObjectName("TxtProjectID")
        self.label = QtGui.QLabel(NewProject)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.TxtProjectName = QtGui.QLineEdit(NewProject)
        self.TxtProjectName.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.TxtProjectName.setObjectName("TxtProjectName")
        self.label_2 = QtGui.QLabel(NewProject)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(NewProject)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.label_3.setObjectName("label_3")
        self.dtpStartDate = QtGui.QDateEdit(NewProject)
        self.dtpStartDate.setGeometry(QtCore.QRect(100, 70, 111, 22))
        self.dtpStartDate.setObjectName("dtpStartDate")
        self.label_4 = QtGui.QLabel(NewProject)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 46, 13))
        self.label_4.setObjectName("label_4")
        self.dtpEndDate = QtGui.QDateEdit(NewProject)
        self.dtpEndDate.setGeometry(QtCore.QRect(100, 100, 110, 22))
        self.dtpEndDate.setObjectName("dtpEndDate")
        self.label_5 = QtGui.QLabel(NewProject)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.label_5.setObjectName("label_5")
        self.TxtDescription = QtGui.QTextEdit(NewProject)
        self.TxtDescription.setGeometry(QtCore.QRect(100, 130, 241, 64))
        self.TxtDescription.setObjectName("TxtDescription")

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(QtGui.QApplication.translate("NewProject", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnProjectSave.setText(QtGui.QApplication.translate("NewProject", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnProjectCancel.setText(QtGui.QApplication.translate("NewProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewProject", "Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewProject", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewProject", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewProject", "Description", None, QtGui.QApplication.UnicodeUTF8))

