# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newproject.ui'
#
# Created: Fri Mar 05 11:16:02 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(389, 226)
        NewProject.setMinimumSize(QtCore.QSize(389, 226))
        self.cmdSave = QtGui.QPushButton(NewProject)
        self.cmdSave.setGeometry(QtCore.QRect(20, 180, 81, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.cmdCancel = QtGui.QPushButton(NewProject)
        self.cmdCancel.setGeometry(QtCore.QRect(290, 180, 81, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.txtProjectName = QtGui.QLineEdit(NewProject)
        self.txtProjectName.setGeometry(QtCore.QRect(100, 10, 113, 20))
        self.txtProjectName.setObjectName("txtProjectName")
        self.label_2 = QtGui.QLabel(NewProject)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(NewProject)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.label_3.setObjectName("label_3")
        self.dtpStartDate = QtGui.QDateEdit(NewProject)
        self.dtpStartDate.setGeometry(QtCore.QRect(100, 40, 111, 22))
        self.dtpStartDate.setObjectName("dtpStartDate")
        self.label_4 = QtGui.QLabel(NewProject)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 46, 13))
        self.label_4.setObjectName("label_4")
        self.dtpEndDate = QtGui.QDateEdit(NewProject)
        self.dtpEndDate.setGeometry(QtCore.QRect(100, 70, 110, 22))
        self.dtpEndDate.setObjectName("dtpEndDate")
        self.label_5 = QtGui.QLabel(NewProject)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtDescription = QtGui.QTextEdit(NewProject)
        self.txtDescription.setGeometry(QtCore.QRect(100, 100, 241, 64))
        self.txtDescription.setObjectName("txtDescription")

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(QtGui.QApplication.translate("NewProject", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("NewProject", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("NewProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewProject", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewProject", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewProject", "Description", None, QtGui.QApplication.UnicodeUTF8))

