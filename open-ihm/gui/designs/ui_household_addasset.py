# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addasset.ui'
#
# Created: Tue Apr 19 08:13:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdAsset(object):
    def setupUi(self, AddHouseholdAsset):
        AddHouseholdAsset.setObjectName(_fromUtf8("AddHouseholdAsset"))
        AddHouseholdAsset.resize(400, 281)
        self.label = QtGui.QLabel(AddHouseholdAsset)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdAsset)
        self.lblHouseholdName.setGeometry(QtCore.QRect(120, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.label_3 = QtGui.QLabel(AddHouseholdAsset)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cboAssetType = QtGui.QComboBox(AddHouseholdAsset)
        self.cboAssetType.setGeometry(QtCore.QRect(120, 80, 261, 22))
        self.cboAssetType.setEditable(True)
        self.cboAssetType.setObjectName(_fromUtf8("cboAssetType"))
        self.label_4 = QtGui.QLabel(AddHouseholdAsset)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 120, 261, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.txtCostPerUnit = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtCostPerUnit.setGeometry(QtCore.QRect(120, 160, 261, 20))
        self.txtCostPerUnit.setObjectName(_fromUtf8("txtCostPerUnit"))
        self.label_5 = QtGui.QLabel(AddHouseholdAsset)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtNumberOfUnits = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtNumberOfUnits.setGeometry(QtCore.QRect(120, 200, 111, 20))
        self.txtNumberOfUnits.setObjectName(_fromUtf8("txtNumberOfUnits"))
        self.label_6 = QtGui.QLabel(AddHouseholdAsset)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdAsset)
        self.cmdSave.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdAsset)
        self.cmdCancel.setGeometry(QtCore.QRect(310, 240, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label_7 = QtGui.QLabel(AddHouseholdAsset)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.cboAssetCategory = QtGui.QComboBox(AddHouseholdAsset)
        self.cboAssetCategory.setGeometry(QtCore.QRect(120, 40, 261, 22))
        self.cboAssetCategory.setEditable(True)
        self.cboAssetCategory.setObjectName(_fromUtf8("cboAssetCategory"))

        self.retranslateUi(AddHouseholdAsset)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdAsset.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdAsset.saveAsset)
        QtCore.QObject.connect(self.cboAssetCategory, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdAsset.getAssetTypes)
        QtCore.QObject.connect(self.cboAssetType, QtCore.SIGNAL(_fromUtf8("activated(int)")), AddHouseholdAsset.displayUnitOfMeasure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdAsset)
        AddHouseholdAsset.setTabOrder(self.cboAssetCategory, self.cboAssetType)
        AddHouseholdAsset.setTabOrder(self.cboAssetType, self.txtUnitOfMeasure)
        AddHouseholdAsset.setTabOrder(self.txtUnitOfMeasure, self.txtCostPerUnit)
        AddHouseholdAsset.setTabOrder(self.txtCostPerUnit, self.txtNumberOfUnits)
        AddHouseholdAsset.setTabOrder(self.txtNumberOfUnits, self.cmdSave)
        AddHouseholdAsset.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdAsset):
        AddHouseholdAsset.setWindowTitle(QtGui.QApplication.translate("AddHouseholdAsset", "Add Household Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdAsset", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Asset Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Cost per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Number of Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Asset Category:", None, QtGui.QApplication.UnicodeUTF8))

