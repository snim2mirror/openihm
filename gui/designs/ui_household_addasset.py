# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_addasset.ui'
#
# Created: Fri Apr 22 21:52:27 2011
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
        self.formLayout = QtGui.QFormLayout(AddHouseholdAsset)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AddHouseholdAsset)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdAsset)
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblHouseholdName)
        self.label_7 = QtGui.QLabel(AddHouseholdAsset)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.cboAssetCategory = QtGui.QComboBox(AddHouseholdAsset)
        self.cboAssetCategory.setEditable(True)
        self.cboAssetCategory.setObjectName(_fromUtf8("cboAssetCategory"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboAssetCategory)
        self.label_3 = QtGui.QLabel(AddHouseholdAsset)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cboAssetType = QtGui.QComboBox(AddHouseholdAsset)
        self.cboAssetType.setEditable(True)
        self.cboAssetType.setObjectName(_fromUtf8("cboAssetType"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboAssetType)
        self.label_4 = QtGui.QLabel(AddHouseholdAsset)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtUnitOfMeasure)
        self.label_5 = QtGui.QLabel(AddHouseholdAsset)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtCostPerUnit = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtCostPerUnit.setObjectName(_fromUtf8("txtCostPerUnit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtCostPerUnit)
        self.label_6 = QtGui.QLabel(AddHouseholdAsset)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtNumberOfUnits = QtGui.QLineEdit(AddHouseholdAsset)
        self.txtNumberOfUnits.setObjectName(_fromUtf8("txtNumberOfUnits"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtNumberOfUnits)
        self.groupBox = QtGui.QGroupBox(AddHouseholdAsset)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label_7.setBuddy(self.cboAssetCategory)
        self.label_3.setBuddy(self.cboAssetType)
        self.label_4.setBuddy(self.txtUnitOfMeasure)
        self.label_5.setBuddy(self.txtCostPerUnit)
        self.label_6.setBuddy(self.txtNumberOfUnits)

        self.retranslateUi(AddHouseholdAsset)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdAsset.close)
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
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Asset Category:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Asset Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Cost per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Number of Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdAsset", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

