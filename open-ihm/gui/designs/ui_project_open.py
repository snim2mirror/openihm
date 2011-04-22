# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_project_open.ui'
#
# Created: Fri Apr 22 15:23:22 2011
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
        self.formLayout = QtGui.QFormLayout(OpenProject)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(OpenProject)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cboProjectName = QtGui.QComboBox(OpenProject)
        self.cboProjectName.setObjectName(_fromUtf8("cboProjectName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboProjectName)
        self.groupBox = QtGui.QGroupBox(OpenProject)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOk = QtGui.QPushButton(self.groupBox)
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.horizontalLayout.addWidget(self.cmdOk)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(OpenProject)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), OpenProject.mdiClose)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), OpenProject.openProject)
        QtCore.QMetaObject.connectSlotsByName(OpenProject)

    def retranslateUi(self, OpenProject):
        OpenProject.setWindowTitle(QtGui.QApplication.translate("OpenProject", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OpenProject", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("OpenProject", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("OpenProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

