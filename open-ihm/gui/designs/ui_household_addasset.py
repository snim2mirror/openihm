# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addasset.ui'
#
# Created: Fri Jun 18 08:06:10 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddHouseholdAsset(object):
    def setupUi(self, AddHouseholdAsset):
        AddHouseholdAsset.setObjectName("AddHouseholdAsset")
        AddHouseholdAsset.resize(400, 242)
        self.label = QtGui.QLabel(AddHouseholdAsset)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdAsset)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName("lblHouseholdName")
        self.label_3 = QtGui.QLabel(AddHouseholdAsset)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.label_3.setObjectName("label_3")
        self.cboAssetType = QtGui.QComboBox(AddHouseholdAsset)
        self.cboAssetType.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboAssetType.setEditable(True)
        self.cboAssetType.setObjectName("cboAssetType")
        self.label_4 = QtGui.QLabel(AddHouseholdAsset)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.txtCostPerUnit = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtCostPerUnit.setGeometry(QtCore.QRect(120, 120, 261, 20))
        self.txtCostPerUnit.setObjectName("txtCostPerUnit")
        self.label_5 = QtGui.QLabel(AddHouseholdAsset)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 91, 21))
        self.label_5.setObjectName("label_5")
        self.txtNumberOfUnits = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtNumberOfUnits.setGeometry(QtCore.QRect(120, 160, 111, 20))
        self.txtNumberOfUnits.setObjectName("txtNumberOfUnits")
        self.label_6 = QtGui.QLabel(AddHouseholdAsset)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_6.setObjectName("label_6")
        self.cmdSave = QtGui.QPushButton(AddHouseholdAsset)
        self.cmdSave.setGeometry(QtCore.QRect(20, 200, 75, 31))
        self.cmdSave.setObjectName("cmdSave")
        self.cmdCancel = QtGui.QPushButton(AddHouseholdAsset)
        self.cmdCancel.setGeometry(QtCore.QRect(300, 200, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")

        self.retranslateUi(AddHouseholdAsset)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdAsset)

    def retranslateUi(self, AddHouseholdAsset):
        AddHouseholdAsset.setWindowTitle(QtGui.QApplication.translate("AddHouseholdAsset", "Add Household Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdAsset", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Asset Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Unit of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Cost per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Number of Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
