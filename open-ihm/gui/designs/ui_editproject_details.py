# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editproject_details.ui'
#
# Created: Fri Apr 22 21:52:27 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditProject(object):
    def setupUi(self, EditProject):
        EditProject.setObjectName(_fromUtf8("EditProject"))
        EditProject.resize(389, 333)
        EditProject.setMinimumSize(QtCore.QSize(389, 333))
        self.formLayout = QtGui.QFormLayout(EditProject)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(EditProject)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblProjectID = QtGui.QLabel(EditProject)
        self.lblProjectID.setObjectName(_fromUtf8("lblProjectID"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblProjectID)
        self.label_2 = QtGui.QLabel(EditProject)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtProjectName = QtGui.QLineEdit(EditProject)
        self.txtProjectName.setObjectName(_fromUtf8("txtProjectName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtProjectName)
        self.label_3 = QtGui.QLabel(EditProject)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dtpStartDate = QtGui.QDateEdit(EditProject)
        self.dtpStartDate.setObjectName(_fromUtf8("dtpStartDate"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dtpStartDate)
        self.label_4 = QtGui.QLabel(EditProject)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dtpEndDate = QtGui.QDateEdit(EditProject)
        self.dtpEndDate.setObjectName(_fromUtf8("dtpEndDate"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dtpEndDate)
        self.label_6 = QtGui.QLabel(EditProject)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.cmbCurrency = QtGui.QComboBox(EditProject)
        self.cmbCurrency.setObjectName(_fromUtf8("cmbCurrency"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.cmbCurrency)
        self.label_5 = QtGui.QLabel(EditProject)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtDescription = QtGui.QTextEdit(EditProject)
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtDescription)
        self.groupBox = QtGui.QGroupBox(EditProject)
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
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label_2.setBuddy(self.txtProjectName)
        self.label_3.setBuddy(self.dtpStartDate)
        self.label_4.setBuddy(self.dtpEndDate)
        self.label_6.setBuddy(self.cmbCurrency)
        self.label_5.setBuddy(self.txtDescription)

        self.retranslateUi(EditProject)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditProject.saveProject)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditProject.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(EditProject)
        EditProject.setTabOrder(self.txtProjectName, self.dtpStartDate)
        EditProject.setTabOrder(self.dtpStartDate, self.dtpEndDate)
        EditProject.setTabOrder(self.dtpEndDate, self.cmbCurrency)
        EditProject.setTabOrder(self.cmbCurrency, self.txtDescription)

    def retranslateUi(self, EditProject):
        EditProject.setWindowTitle(QtGui.QApplication.translate("EditProject", "Edit Project Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditProject", "Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectID.setText(QtGui.QApplication.translate("EditProject", "{projectid}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditProject", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditProject", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditProject", "Currency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditProject", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditProject", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

