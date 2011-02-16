# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manage_standardofliving.ui'
#
# Created: Tue Dec 07 09:25:56 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_StandardOfLivingManager(object):
    def setupUi(self, StandardOfLivingManager):
        StandardOfLivingManager.setObjectName("StandardOfLivingManager")
        StandardOfLivingManager.resize(659, 334)
        StandardOfLivingManager.setMinimumSize(QtCore.QSize(659, 334))
        self.tblStandardOfLiving = QtGui.QTableView(StandardOfLivingManager)
        self.tblStandardOfLiving.setGeometry(QtCore.QRect(10, 30, 351, 291))
        self.tblStandardOfLiving.setObjectName("tblStandardOfLiving")
        self.cmdDelete = QtGui.QPushButton(StandardOfLivingManager)
        self.cmdDelete.setGeometry(QtCore.QRect(370, 290, 81, 31))
        self.cmdDelete.setObjectName("cmdDelete")
        self.cmdClose = QtGui.QPushButton(StandardOfLivingManager)
        self.cmdClose.setGeometry(QtCore.QRect(560, 290, 81, 31))
        self.cmdClose.setObjectName("cmdClose")
        self.groupBox = QtGui.QGroupBox(StandardOfLivingManager)
        self.groupBox.setGeometry(QtCore.QRect(370, 30, 281, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtItem = QtGui.QLineEdit(self.groupBox)
        self.txtItem.setGeometry(QtCore.QRect(50, 30, 221, 20))
        self.txtItem.setObjectName("txtItem")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setObjectName("label")
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setGeometry(QtCore.QRect(190, 100, 81, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.cmbItemType = QtGui.QComboBox(self.groupBox)
        self.cmbItemType.setGeometry(QtCore.QRect(50, 70, 221, 22))
        self.cmbItemType.setObjectName("cmbItemType")
        self.cmbItemType.addItem("")
        self.cmbItemType.addItem("")
        self.cmbItemType.addItem("")
        self.label_4 = QtGui.QLabel(StandardOfLivingManager)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(StandardOfLivingManager)
        QtCore.QMetaObject.connectSlotsByName(StandardOfLivingManager)

    def retranslateUi(self, StandardOfLivingManager):
        StandardOfLivingManager.setWindowTitle(QtGui.QApplication.translate("StandardOfLivingManager", "Manage Standard of Living Items", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbItemType.setItemText(0, QtGui.QApplication.translate("StandardOfLivingManager", "Person", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbItemType.setItemText(1, QtGui.QApplication.translate("StandardOfLivingManager", "Household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbItemType.setItemText(2, QtGui.QApplication.translate("StandardOfLivingManager", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Standard of Livng Items", None, QtGui.QApplication.UnicodeUTF8))

