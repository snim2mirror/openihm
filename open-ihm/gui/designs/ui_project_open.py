# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_project_open.ui'
#
# Created: Tue Apr 19 08:13:17 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OpenProject(object):
    def setupUi(self, OpenProject):
        OpenProject.setObjectName(_fromUtf8("OpenProject"))
        OpenProject.resize(393, 114)
        OpenProject.setMinimumSize(QtCore.QSize(393, 114))
        self.cmdOk = QtGui.QPushButton(OpenProject)
        self.cmdOk.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.cmdCancel = QtGui.QPushButton(OpenProject)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 60, 81, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label = QtGui.QLabel(OpenProject)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.cboProjectName = QtGui.QComboBox(OpenProject)
        self.cboProjectName.setGeometry(QtCore.QRect(100, 20, 281, 22))
        self.cboProjectName.setObjectName(_fromUtf8("cboProjectName"))

        self.retranslateUi(OpenProject)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), OpenProject.mdiclose)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), OpenProject.openProject)
        QtCore.QMetaObject.connectSlotsByName(OpenProject)

    def retranslateUi(self, OpenProject):
        OpenProject.setWindowTitle(QtGui.QApplication.translate("OpenProject", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("OpenProject", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("OpenProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OpenProject", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))

