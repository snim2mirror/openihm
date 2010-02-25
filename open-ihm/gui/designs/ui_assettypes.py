# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_assettypes.ui'
#
# Created: Wed Feb 24 18:17:18 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AssetTypes(object):
    def setupUi(self, AssetTypes):
        AssetTypes.setObjectName("AssetTypes")
        AssetTypes.resize(QtCore.QSize(QtCore.QRect(0,0,419,297).size()).expandedTo(AssetTypes.minimumSizeHint()))
        AssetTypes.setMinimumSize(QtCore.QSize(419,297))
        AssetTypes.setMaximumSize(QtCore.QSize(419,16777215))

        self.listWidget = QtGui.QListWidget(AssetTypes)
        self.listWidget.setGeometry(QtCore.QRect(0,40,191,251))
        self.listWidget.setObjectName("listWidget")

        self.lineEdit = QtGui.QLineEdit(AssetTypes)
        self.lineEdit.setGeometry(QtCore.QRect(210,40,201,28))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtGui.QPushButton(AssetTypes)
        self.pushButton.setGeometry(QtCore.QRect(320,90,91,28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtGui.QPushButton(AssetTypes)
        self.pushButton_2.setGeometry(QtCore.QRect(210,90,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.btnAssetTypesClose = QtGui.QPushButton(AssetTypes)
        self.btnAssetTypesClose.setGeometry(QtCore.QRect(330,260,80,28))
        self.btnAssetTypesClose.setObjectName("btnAssetTypesClose")

        self.label = QtGui.QLabel(AssetTypes)
        self.label.setGeometry(QtCore.QRect(0,10,161,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(AssetTypes)
        self.label_2.setGeometry(QtCore.QRect(210,10,111,18))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AssetTypes)
        QtCore.QMetaObject.connectSlotsByName(AssetTypes)

    def retranslateUi(self, AssetTypes):
        AssetTypes.setWindowTitle(QtGui.QApplication.translate("AssetTypes", "Manage Asset Types", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AssetTypes", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("AssetTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAssetTypesClose.setText(QtGui.QApplication.translate("AssetTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AssetTypes", "List of Existing Asset Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AssetTypes", "Asset Name", None, QtGui.QApplication.UnicodeUTF8))

