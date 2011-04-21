# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_add.ui'
#
# Created: Thu Apr 21 20:27:57 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddFoodTypes(object):
    def setupUi(self, AddFoodTypes):
        AddFoodTypes.setObjectName(_fromUtf8("AddFoodTypes"))
        AddFoodTypes.resize(350, 216)
        AddFoodTypes.setMinimumSize(QtCore.QSize(350, 204))
        self.formLayout = QtGui.QFormLayout(AddFoodTypes)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AddFoodTypes)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtFoodType = QtGui.QLineEdit(AddFoodTypes)
        self.txtFoodType.setObjectName(_fromUtf8("txtFoodType"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtFoodType)
        self.label_2 = QtGui.QLabel(AddFoodTypes)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbCategory = QtGui.QComboBox(AddFoodTypes)
        self.cmbCategory.setObjectName(_fromUtf8("cmbCategory"))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cmbCategory)
        self.label_4 = QtGui.QLabel(AddFoodTypes)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtKCalories = QtGui.QLineEdit(AddFoodTypes)
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtKCalories)
        self.label_3 = QtGui.QLabel(AddFoodTypes)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cmbUnitOfMeasure = QtGui.QComboBox(AddFoodTypes)
        self.cmbUnitOfMeasure.setEditable(True)
        self.cmbUnitOfMeasure.setObjectName(_fromUtf8("cmbUnitOfMeasure"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cmbUnitOfMeasure)
        self.groupBox = QtGui.QGroupBox(AddFoodTypes)
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
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(AddFoodTypes)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodTypes.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodTypes.saveDetails)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodTypes.close)
        QtCore.QMetaObject.connectSlotsByName(AddFoodTypes)
        AddFoodTypes.setTabOrder(self.txtFoodType, self.cmbCategory)
        AddFoodTypes.setTabOrder(self.cmbCategory, self.txtKCalories)
        AddFoodTypes.setTabOrder(self.txtKCalories, self.cmbUnitOfMeasure)
        AddFoodTypes.setTabOrder(self.cmbUnitOfMeasure, self.cmdSave)
        AddFoodTypes.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddFoodTypes):
        AddFoodTypes.setWindowTitle(QtGui.QApplication.translate("AddFoodTypes", "Add Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddFoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddFoodTypes", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(0, QtGui.QApplication.translate("AddFoodTypes", "crops", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(1, QtGui.QApplication.translate("AddFoodTypes", "livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(2, QtGui.QApplication.translate("AddFoodTypes", "wildfoods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddFoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddFoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddFoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddFoodTypes", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

