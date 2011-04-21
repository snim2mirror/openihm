# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_databasemessage.ui'
#
# Created: Thu Apr 21 19:28:05 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DatabaseMessage(object):
    def setupUi(self, DatabaseMessage):
        DatabaseMessage.setObjectName(_fromUtf8("DatabaseMessage"))
        DatabaseMessage.resize(424, 153)
        self.lblMessage = QtGui.QLabel(DatabaseMessage)
        self.lblMessage.setGeometry(QtCore.QRect(9, 9, 44, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMessage.setFont(font)
        self.lblMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.cmdOk = QtGui.QPushButton(DatabaseMessage)
        self.cmdOk.setGeometry(QtCore.QRect(320, 110, 85, 28))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))

        self.retranslateUi(DatabaseMessage)
        QtCore.QObject.connect(self.cmdOk, QtCore.SIGNAL(_fromUtf8("clicked()")), DatabaseMessage.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(DatabaseMessage)

    def retranslateUi(self, DatabaseMessage):
        DatabaseMessage.setWindowTitle(QtGui.QApplication.translate("DatabaseMessage", "Problem with Database Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMessage.setText(QtGui.QApplication.translate("DatabaseMessage", "{msg}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOk.setText(QtGui.QApplication.translate("DatabaseMessage", "Ok", None, QtGui.QApplication.UnicodeUTF8))

