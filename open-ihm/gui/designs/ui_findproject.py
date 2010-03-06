# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findproject.ui'
#
# Created: Sat Mar  6 09:32:25 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FindProject(object):
    def setupUi(self, FindProject):
        FindProject.setObjectName("FindProject")
        FindProject.resize(QtCore.QSize(QtCore.QRect(0,0,400,160).size()).expandedTo(FindProject.minimumSizeHint()))
        FindProject.setMinimumSize(QtCore.QSize(400,160))

        self.pushButton = QtGui.QPushButton(FindProject)
        self.pushButton.setGeometry(QtCore.QRect(0,130,80,28))
        self.pushButton.setObjectName("pushButton")

        self.btnFindProjectClose = QtGui.QPushButton(FindProject)
        self.btnFindProjectClose.setGeometry(QtCore.QRect(310,130,80,28))
        self.btnFindProjectClose.setObjectName("btnFindProjectClose")

        self.lineEdit = QtGui.QLineEdit(FindProject)
        self.lineEdit.setGeometry(QtCore.QRect(80,40,151,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtGui.QLabel(FindProject)
        self.label.setGeometry(QtCore.QRect(0,40,151,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(FindProject)
        self.label_2.setGeometry(QtCore.QRect(0,80,151,18))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtGui.QLineEdit(FindProject)
        self.lineEdit_2.setGeometry(QtCore.QRect(80,80,311,28))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtGui.QLabel(FindProject)
        self.label_3.setGeometry(QtCore.QRect(0,10,371,18))
        self.label_3.setObjectName("label_3")

        self.pushButton_3 = QtGui.QPushButton(FindProject)
        self.pushButton_3.setGeometry(QtCore.QRect(160,130,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(FindProject)
        QtCore.QMetaObject.connectSlotsByName(FindProject)

    def retranslateUi(self, FindProject):
        FindProject.setWindowTitle(QtGui.QApplication.translate("FindProject", "Find Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("FindProject", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindProjectClose.setText(QtGui.QApplication.translate("FindProject", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindProject", "Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindProject", "Project Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindProject", "Type in Project ID or Project Title", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("FindProject", "Help", None, QtGui.QApplication.UnicodeUTF8))

