# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newproject.ui'
#
# Created: Fri Apr 22 21:52:29 2011
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
        self.formLayout = QtGui.QFormLayout(NewProject)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(NewProject)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtProjectName = QtGui.QLineEdit(NewProject)
        self.txtProjectName.setObjectName(_fromUtf8("txtProjectName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtProjectName)
        self.label_3 = QtGui.QLabel(NewProject)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dtpStartDate = QtGui.QDateEdit(NewProject)
        self.dtpStartDate.setObjectName(_fromUtf8("dtpStartDate"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dtpStartDate)
        self.label_4 = QtGui.QLabel(NewProject)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dtpEndDate = QtGui.QDateEdit(NewProject)
        self.dtpEndDate.setObjectName(_fromUtf8("dtpEndDate"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dtpEndDate)
        self.label_6 = QtGui.QLabel(NewProject)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.cmbCurrency = QtGui.QComboBox(NewProject)
        self.cmbCurrency.setObjectName(_fromUtf8("cmbCurrency"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmbCurrency)
        self.label_5 = QtGui.QLabel(NewProject)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtDescription = QtGui.QTextEdit(NewProject)
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtDescription)
        self.groupBox = QtGui.QGroupBox(NewProject)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label_2.setBuddy(self.txtProjectName)
        self.label_3.setBuddy(self.dtpStartDate)
        self.label_4.setBuddy(self.dtpEndDate)
        self.label_6.setBuddy(self.cmbCurrency)
        self.label_5.setBuddy(self.txtDescription)

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
        self.label_2.setText(QtGui.QApplication.translate("NewProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewProject", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewProject", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("NewProject", "Currency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewProject", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("NewProject", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("NewProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

