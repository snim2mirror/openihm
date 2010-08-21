# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_databasemessage.ui'
#
# Created: Sat Aug 21 21:55:48 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DatabaseMessage(object):
    def setupUi(self, DatabaseMessage):
        DatabaseMessage.setObjectName("DatabaseMessage")
        DatabaseMessage.resize(424, 153)
        self.cmdOk = QtGui.QPushButton(DatabaseMessage)
        self.cmdOk.setGeometry(QtCore.QRect(160, 110, 101, 31))
        self.cmdOk.setObjectName("cmdOk")
        self.lblMessage = QtGui.QLabel(DatabaseMessage)
        self.lblMessage.setGeometry(QtCore.QRect(10, 10, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMessage.setFont(font)
        self.lblMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")

        self.retranslateUi(DatabaseMessage)
        QtCore.QMetaObject.connectSlotsByName(DatabaseMessage)

    def retranslateUi(self, DatabaseMessage):
        DatabaseMessage.setWindowTitle(QtGui.QApplication.translate("DatabaseMessage", "Problem with Database Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("DatabaseMessage", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMessage.setText(QtGui.QApplication.translate("DatabaseMessage", "{msg}", None, QtGui.QApplication.UnicodeUTF8))

