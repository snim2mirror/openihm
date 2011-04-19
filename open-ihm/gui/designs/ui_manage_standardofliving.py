# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manage_standardofliving.ui'
#
# Created: Tue Apr 19 07:27:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StandardOfLivingManager(object):
    def setupUi(self, StandardOfLivingManager):
        StandardOfLivingManager.setObjectName(_fromUtf8("StandardOfLivingManager"))
        StandardOfLivingManager.resize(659, 334)
        StandardOfLivingManager.setMinimumSize(QtCore.QSize(659, 334))
        self.tblStandardOfLiving = QtGui.QTableView(StandardOfLivingManager)
        self.tblStandardOfLiving.setGeometry(QtCore.QRect(10, 30, 351, 291))
        self.tblStandardOfLiving.setObjectName(_fromUtf8("tblStandardOfLiving"))
        self.cmdDelete = QtGui.QPushButton(StandardOfLivingManager)
        self.cmdDelete.setGeometry(QtCore.QRect(370, 290, 81, 31))
        self.cmdDelete.setObjectName(_fromUtf8("cmdDelete"))
        self.cmdClose = QtGui.QPushButton(StandardOfLivingManager)
        self.cmdClose.setGeometry(QtCore.QRect(560, 290, 81, 31))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.groupBox = QtGui.QGroupBox(StandardOfLivingManager)
        self.groupBox.setGeometry(QtCore.QRect(370, 30, 281, 141))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtItem = QtGui.QLineEdit(self.groupBox)
        self.txtItem.setGeometry(QtCore.QRect(50, 30, 221, 20))
        self.txtItem.setObjectName(_fromUtf8("txtItem"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setGeometry(QtCore.QRect(190, 100, 81, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmbItemType = QtGui.QComboBox(self.groupBox)
        self.cmbItemType.setGeometry(QtCore.QRect(50, 70, 221, 22))
        self.cmbItemType.setObjectName(_fromUtf8("cmbItemType"))
        self.cmbItemType.addItem(_fromUtf8(""))
        self.cmbItemType.addItem(_fromUtf8(""))
        self.cmbItemType.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(StandardOfLivingManager)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(StandardOfLivingManager)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), StandardOfLivingManager.mdiClose)
        QtCore.QObject.connect(self.cmdDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), StandardOfLivingManager.delItems)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), StandardOfLivingManager.saveItem)
        QtCore.QMetaObject.connectSlotsByName(StandardOfLivingManager)
        StandardOfLivingManager.setTabOrder(self.tblStandardOfLiving, self.txtItem)
        StandardOfLivingManager.setTabOrder(self.txtItem, self.cmbItemType)
        StandardOfLivingManager.setTabOrder(self.cmbItemType, self.cmdSave)
        StandardOfLivingManager.setTabOrder(self.cmdSave, self.cmdDelete)
        StandardOfLivingManager.setTabOrder(self.cmdDelete, self.cmdClose)

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

