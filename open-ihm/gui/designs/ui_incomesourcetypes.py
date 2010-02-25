# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_incomesourcetypes.ui'
#
# Created: Wed Feb 24 18:40:59 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_IncomeSourcesTypes(object):
    def setupUi(self, IncomeSourcesTypes):
        IncomeSourcesTypes.setObjectName("IncomeSourcesTypes")
        IncomeSourcesTypes.resize(QtCore.QSize(QtCore.QRect(0,0,419,297).size()).expandedTo(IncomeSourcesTypes.minimumSizeHint()))
        IncomeSourcesTypes.setMinimumSize(QtCore.QSize(419,297))
        IncomeSourcesTypes.setMaximumSize(QtCore.QSize(419,16777215))

        self.listWidget = QtGui.QListWidget(IncomeSourcesTypes)
        self.listWidget.setGeometry(QtCore.QRect(0,40,191,251))
        self.listWidget.setObjectName("listWidget")

        self.lineEdit = QtGui.QLineEdit(IncomeSourcesTypes)
        self.lineEdit.setGeometry(QtCore.QRect(210,40,201,28))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtGui.QPushButton(IncomeSourcesTypes)
        self.pushButton.setGeometry(QtCore.QRect(320,90,91,28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtGui.QPushButton(IncomeSourcesTypes)
        self.pushButton_2.setGeometry(QtCore.QRect(210,90,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.btnIncomeSourcesClose = QtGui.QPushButton(IncomeSourcesTypes)
        self.btnIncomeSourcesClose.setGeometry(QtCore.QRect(330,260,80,28))
        self.btnIncomeSourcesClose.setObjectName("btnIncomeSourcesClose")

        self.label = QtGui.QLabel(IncomeSourcesTypes)
        self.label.setGeometry(QtCore.QRect(0,10,161,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(IncomeSourcesTypes)
        self.label_2.setGeometry(QtCore.QRect(210,10,111,18))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(IncomeSourcesTypes)
        QtCore.QMetaObject.connectSlotsByName(IncomeSourcesTypes)

    def retranslateUi(self, IncomeSourcesTypes):
        IncomeSourcesTypes.setWindowTitle(QtGui.QApplication.translate("IncomeSourcesTypes", "Manage Income Source Types", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIncomeSourcesClose.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "List of Existing Income Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Income Type", None, QtGui.QApplication.UnicodeUTF8))

