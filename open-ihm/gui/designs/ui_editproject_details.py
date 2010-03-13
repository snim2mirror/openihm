# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editproject_details.ui'
#
# Created: Fri Mar 12 16:26:12 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditProject(object):
    def setupUi(self, EditProject):
        EditProject.setObjectName("EditProject")
        EditProject.resize(389, 333)
        EditProject.setMinimumSize(QtCore.QSize(389, 333))
        self.cmdSave = QtGui.QPushButton(EditProject)
        self.cmdSave.setGeometry(QtCore.QRect(20, 280, 75, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.cmdCancel = QtGui.QPushButton(EditProject)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 280, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        self.label = QtGui.QLabel(EditProject)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.txtProjectName = QtGui.QLineEdit(EditProject)
        self.txtProjectName.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.txtProjectName.setObjectName("txtProjectName")
        self.label_2 = QtGui.QLabel(EditProject)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(EditProject)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_3.setObjectName("label_3")
        self.dtpStartDate = QtGui.QDateEdit(EditProject)
        self.dtpStartDate.setGeometry(QtCore.QRect(100, 80, 111, 22))
        self.dtpStartDate.setObjectName("dtpStartDate")
        self.label_4 = QtGui.QLabel(EditProject)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 46, 13))
        self.label_4.setObjectName("label_4")
        self.dtpEndDate = QtGui.QDateEdit(EditProject)
        self.dtpEndDate.setGeometry(QtCore.QRect(100, 120, 110, 22))
        self.dtpEndDate.setObjectName("dtpEndDate")
        self.label_5 = QtGui.QLabel(EditProject)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtDescription = QtGui.QTextEdit(EditProject)
        self.txtDescription.setGeometry(QtCore.QRect(100, 200, 271, 64))
        self.txtDescription.setObjectName("txtDescription")
        self.lblProjectID = QtGui.QLabel(EditProject)
        self.lblProjectID.setGeometry(QtCore.QRect(100, 10, 61, 16))
        self.lblProjectID.setObjectName("lblProjectID")
        self.label_6 = QtGui.QLabel(EditProject)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 46, 13))
        self.label_6.setObjectName("label_6")
        self.cmbCurrency = QtGui.QComboBox(EditProject)
        self.cmbCurrency.setGeometry(QtCore.QRect(100, 160, 111, 22))
        self.cmbCurrency.setObjectName("cmbCurrency")
        self.cmbCurrency.addItem("")
        self.cmbCurrency.addItem("")

        self.retranslateUi(EditProject)
        QtCore.QMetaObject.connectSlotsByName(EditProject)

    def retranslateUi(self, EditProject):
        EditProject.setWindowTitle(QtGui.QApplication.translate("EditProject", "Edit Project Details", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditProject", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditProject", "Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditProject", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditProject", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EditProject", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectID.setText(QtGui.QApplication.translate("EditProject", "{projectid}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditProject", "Currency", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCurrency.setItemText(0, QtGui.QApplication.translate("EditProject", "MK", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCurrency.setItemText(1, QtGui.QApplication.translate("EditProject", "USD", None, QtGui.QApplication.UnicodeUTF8))

