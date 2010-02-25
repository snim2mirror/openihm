# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_expendituretypes.ui'
#
# Created: Thu Feb 25 14:47:49 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ExpenditureTypes(object):
    def setupUi(self, ExpenditureTypes):
        ExpenditureTypes.setObjectName("ExpenditureTypes")
        ExpenditureTypes.resize(QtCore.QSize(QtCore.QRect(0,0,419,297).size()).expandedTo(ExpenditureTypes.minimumSizeHint()))
        ExpenditureTypes.setMinimumSize(QtCore.QSize(419,297))
        ExpenditureTypes.setMaximumSize(QtCore.QSize(419,16777215))

        self.listWidget = QtGui.QListWidget(ExpenditureTypes)
        self.listWidget.setGeometry(QtCore.QRect(0,40,191,251))
        self.listWidget.setObjectName("listWidget")

        self.lineEdit = QtGui.QLineEdit(ExpenditureTypes)
        self.lineEdit.setGeometry(QtCore.QRect(210,40,201,28))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtGui.QPushButton(ExpenditureTypes)
        self.pushButton.setGeometry(QtCore.QRect(320,90,91,28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtGui.QPushButton(ExpenditureTypes)
        self.pushButton_2.setGeometry(QtCore.QRect(210,90,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.btnExpenditureTypesClose = QtGui.QPushButton(ExpenditureTypes)
        self.btnExpenditureTypesClose.setGeometry(QtCore.QRect(330,260,80,28))
        self.btnExpenditureTypesClose.setObjectName("btnExpenditureTypesClose")

        self.label = QtGui.QLabel(ExpenditureTypes)
        self.label.setGeometry(QtCore.QRect(0,10,191,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(ExpenditureTypes)
        self.label_2.setGeometry(QtCore.QRect(210,10,111,18))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ExpenditureTypes)
        QtCore.QMetaObject.connectSlotsByName(ExpenditureTypes)

    def retranslateUi(self, ExpenditureTypes):
        ExpenditureTypes.setWindowTitle(QtGui.QApplication.translate("ExpenditureTypes", "Manage Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ExpenditureTypes", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ExpenditureTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExpenditureTypesClose.setText(QtGui.QApplication.translate("ExpenditureTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExpenditureTypes", "List of Existing Expenditure Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExpenditureTypes", "Expenditure Type", None, QtGui.QApplication.UnicodeUTF8))

