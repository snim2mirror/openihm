# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newproject.ui'
#
# Created: Tue Apr 19 03:45:26 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName(_fromUtf8("NewProject"))
        NewProject.resize(389, 309)
        NewProject.setMinimumSize(QtCore.QSize(389, 309))
        self.cmdSave = QtGui.QPushButton(NewProject)
        self.cmdSave.setGeometry(QtCore.QRect(20, 260, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmdCancel = QtGui.QPushButton(NewProject)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 260, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.txtProjectName = QtGui.QLineEdit(NewProject)
        self.txtProjectName.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.txtProjectName.setObjectName(_fromUtf8("txtProjectName"))
        self.label_2 = QtGui.QLabel(NewProject)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(NewProject)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dtpStartDate = QtGui.QDateEdit(NewProject)
        self.dtpStartDate.setGeometry(QtCore.QRect(100, 60, 111, 22))
        self.dtpStartDate.setObjectName(_fromUtf8("dtpStartDate"))
        self.label_4 = QtGui.QLabel(NewProject)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dtpEndDate = QtGui.QDateEdit(NewProject)
        self.dtpEndDate.setGeometry(QtCore.QRect(100, 100, 110, 22))
        self.dtpEndDate.setObjectName(_fromUtf8("dtpEndDate"))
        self.label_5 = QtGui.QLabel(NewProject)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtDescription = QtGui.QTextEdit(NewProject)
        self.txtDescription.setGeometry(QtCore.QRect(100, 180, 271, 64))
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.label_6 = QtGui.QLabel(NewProject)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cmbCurrency = QtGui.QComboBox(NewProject)
        self.cmbCurrency.setGeometry(QtCore.QRect(100, 140, 231, 22))
        self.cmbCurrency.setObjectName(_fromUtf8("cmbCurrency"))

        self.retranslateUi(NewProject)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), NewProject.saveProject)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), NewProject.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(NewProject)
        NewProject.setTabOrder(self.txtProjectName, self.dtpStartDate)
        NewProject.setTabOrder(self.dtpStartDate, self.dtpEndDate)
        NewProject.setTabOrder(self.dtpEndDate, self.cmbCurrency)
        NewProject.setTabOrder(self.cmbCurrency, self.txtDescription)
        NewProject.setTabOrder(self.txtDescription, self.cmdSave)
        NewProject.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(QtGui.QApplication.translate("NewProject", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("NewProject", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("NewProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewProject", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewProject", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewProject", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("NewProject", "Currency", None, QtGui.QApplication.UnicodeUTF8))

