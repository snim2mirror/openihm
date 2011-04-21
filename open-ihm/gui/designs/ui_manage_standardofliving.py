# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manage_standardofliving.ui'
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

class Ui_StandardOfLivingManager(object):
    def setupUi(self, StandardOfLivingManager):
        StandardOfLivingManager.setObjectName(_fromUtf8("StandardOfLivingManager"))
        StandardOfLivingManager.resize(659, 334)
        StandardOfLivingManager.setMinimumSize(QtCore.QSize(659, 334))
        self.gridLayout = QtGui.QGridLayout(StandardOfLivingManager)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(StandardOfLivingManager)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tblStandardOfLiving = QtGui.QTableView(self.groupBox_3)
        self.tblStandardOfLiving.setAlternatingRowColors(True)
        self.tblStandardOfLiving.setSortingEnabled(True)
        self.tblStandardOfLiving.setObjectName(_fromUtf8("tblStandardOfLiving"))
        self.verticalLayout.addWidget(self.tblStandardOfLiving)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 2, 1)
        self.groupBox = QtGui.QGroupBox(StandardOfLivingManager)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtItem = QtGui.QLineEdit(self.groupBox)
        self.txtItem.setObjectName(_fromUtf8("txtItem"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtItem)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbItemType = QtGui.QComboBox(self.groupBox)
        self.cmbItemType.setObjectName(_fromUtf8("cmbItemType"))
        self.cmbItemType.addItem(_fromUtf8(""))
        self.cmbItemType.addItem(_fromUtf8(""))
        self.cmbItemType.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cmbItemType)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(StandardOfLivingManager)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox_2)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdDelete = QtGui.QPushButton(self.groupBox_2)
        self.cmdDelete.setObjectName(_fromUtf8("cmdDelete"))
        self.horizontalLayout.addWidget(self.cmdDelete)
        self.cmdClose = QtGui.QPushButton(self.groupBox_2)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

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
        self.groupBox_3.setTitle(QtGui.QApplication.translate("StandardOfLivingManager", "Standard of Living", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbItemType.setItemText(0, QtGui.QApplication.translate("StandardOfLivingManager", "Person", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbItemType.setItemText(1, QtGui.QApplication.translate("StandardOfLivingManager", "Household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbItemType.setItemText(2, QtGui.QApplication.translate("StandardOfLivingManager", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("StandardOfLivingManager", "Close", None, QtGui.QApplication.UnicodeUTF8))

