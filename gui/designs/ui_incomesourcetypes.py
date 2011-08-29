# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_incomesourcetypes.ui'
#
# Created: Thu Apr 21 19:28:07 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_IncomeSourcesTypes(object):
    def setupUi(self, IncomeSourcesTypes):
        IncomeSourcesTypes.setObjectName(_fromUtf8("IncomeSourcesTypes"))
        IncomeSourcesTypes.resize(563, 297)
        IncomeSourcesTypes.setMinimumSize(QtCore.QSize(450, 297))
        IncomeSourcesTypes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout_2 = QtGui.QVBoxLayout(IncomeSourcesTypes)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(IncomeSourcesTypes)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(IncomeSourcesTypes)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(IncomeSourcesTypes)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.btnIncomeSourcesClose = QtGui.QPushButton(self.groupBox)
        self.btnIncomeSourcesClose.setObjectName(_fromUtf8("btnIncomeSourcesClose"))
        self.horizontalLayout.addWidget(self.btnIncomeSourcesClose)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(IncomeSourcesTypes)
        QtCore.QObject.connect(self.btnIncomeSourcesClose, QtCore.SIGNAL(_fromUtf8("clicked()")), IncomeSourcesTypes.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(IncomeSourcesTypes)

    def retranslateUi(self, IncomeSourcesTypes):
        IncomeSourcesTypes.setWindowTitle(QtGui.QApplication.translate("IncomeSourcesTypes", "Manage Income Source Types", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("IncomeSourcesTypes", "Income Type", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("IncomeSourcesTypes", "Income Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIncomeSourcesClose.setText(QtGui.QApplication.translate("IncomeSourcesTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))

