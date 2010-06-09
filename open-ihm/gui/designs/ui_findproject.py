# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_findproject.ui'
#
# Created: Wed Jun 09 10:01:35 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FindProject(object):
    def setupUi(self, FindProject):
        FindProject.setObjectName("FindProject")
        FindProject.resize(400, 160)
        FindProject.setMinimumSize(QtCore.QSize(400, 160))
        self.cmdOk = QtGui.QPushButton(FindProject)
        self.cmdOk.setGeometry(QtCore.QRect(10, 120, 80, 28))
        self.cmdOk.setObjectName("cmdOk")
        self.cmdCancel = QtGui.QPushButton(FindProject)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 120, 80, 28))
        self.cmdCancel.setObjectName("cmdCancel")
        self.txtProjectID = QtGui.QLineEdit(FindProject)
        self.txtProjectID.setGeometry(QtCore.QRect(90, 40, 151, 21))
        self.txtProjectID.setObjectName("txtProjectID")
        self.label = QtGui.QLabel(FindProject)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(FindProject)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.label_2.setObjectName("label_2")
        self.txtProjectTitle = QtGui.QLineEdit(FindProject)
        self.txtProjectTitle.setGeometry(QtCore.QRect(90, 80, 301, 21))
        self.txtProjectTitle.setObjectName("txtProjectTitle")
        self.label_3 = QtGui.QLabel(FindProject)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 401, 31))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(FindProject)
        QtCore.QMetaObject.connectSlotsByName(FindProject)

    def retranslateUi(self, FindProject):
        FindProject.setWindowTitle(QtGui.QApplication.translate("FindProject", "Find Project", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("FindProject", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("FindProject", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FindProject", "Project ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FindProject", "Project Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FindProject", "Enter Project ID or Project Title [entering nothing will list all projects]", None, QtGui.QApplication.UnicodeUTF8))

