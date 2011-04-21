# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_edit.ui'
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

class Ui_EditFoodTypes(object):
    def setupUi(self, EditFoodTypes):
        EditFoodTypes.setObjectName(_fromUtf8("EditFoodTypes"))
        EditFoodTypes.resize(350, 228)
        EditFoodTypes.setMinimumSize(QtCore.QSize(350, 204))
        self.formLayout = QtGui.QFormLayout(EditFoodTypes)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(EditFoodTypes)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtFoodType = QtGui.QLineEdit(EditFoodTypes)
        self.txtFoodType.setObjectName(_fromUtf8("txtFoodType"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtFoodType)
        self.label_2 = QtGui.QLabel(EditFoodTypes)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbCategory = QtGui.QComboBox(EditFoodTypes)
        self.cmbCategory.setObjectName(_fromUtf8("cmbCategory"))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cmbCategory)
        self.label_4 = QtGui.QLabel(EditFoodTypes)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtKCalories = QtGui.QLineEdit(EditFoodTypes)
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtKCalories)
        self.label_3 = QtGui.QLabel(EditFoodTypes)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtMeasuringUnit = QtGui.QLineEdit(EditFoodTypes)
        self.txtMeasuringUnit.setObjectName(_fromUtf8("txtMeasuringUnit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtMeasuringUnit)
        self.groupBox = QtGui.QGroupBox(EditFoodTypes)
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

        self.retranslateUi(EditFoodTypes)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodTypes.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodTypes.saveDetails)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodTypes.close)
        QtCore.QMetaObject.connectSlotsByName(EditFoodTypes)
        EditFoodTypes.setTabOrder(self.txtFoodType, self.cmbCategory)
        EditFoodTypes.setTabOrder(self.cmbCategory, self.txtKCalories)
        EditFoodTypes.setTabOrder(self.txtKCalories, self.txtMeasuringUnit)
        EditFoodTypes.setTabOrder(self.txtMeasuringUnit, self.cmdSave)
        EditFoodTypes.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, EditFoodTypes):
        EditFoodTypes.setWindowTitle(QtGui.QApplication.translate("EditFoodTypes", "Edit Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditFoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditFoodTypes", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(0, QtGui.QApplication.translate("EditFoodTypes", "crops", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(1, QtGui.QApplication.translate("EditFoodTypes", "livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(2, QtGui.QApplication.translate("EditFoodTypes", "wildfoods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditFoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditFoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditFoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditFoodTypes", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

