# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_add.ui'
#
# Created: Tue Apr 19 08:09:04 2011
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
        AddFoodTypes.resize(350, 239)
        AddFoodTypes.setMinimumSize(QtCore.QSize(350, 204))
        self.cmdCancel = QtGui.QPushButton(AddFoodTypes)
        self.cmdCancel.setGeometry(QtCore.QRect(260, 200, 80, 28))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.cmdSave = QtGui.QPushButton(AddFoodTypes)
        self.cmdSave.setGeometry(QtCore.QRect(70, 200, 80, 28))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label = QtGui.QLabel(AddFoodTypes)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmbUnitOfMeasure = QtGui.QComboBox(AddFoodTypes)
        self.cmbUnitOfMeasure.setGeometry(QtCore.QRect(120, 160, 131, 27))
        self.cmbUnitOfMeasure.setEditable(True)
        self.cmbUnitOfMeasure.setObjectName(_fromUtf8("cmbUnitOfMeasure"))
        self.label_3 = QtGui.QLabel(AddFoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 91, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AddFoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 101, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtKCalories = QtGui.QLineEdit(AddFoodTypes)
        self.txtKCalories.setGeometry(QtCore.QRect(120, 110, 131, 31))
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.txtFoodType = QtGui.QLineEdit(AddFoodTypes)
        self.txtFoodType.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.txtFoodType.setObjectName(_fromUtf8("txtFoodType"))
        self.label_2 = QtGui.QLabel(AddFoodTypes)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cmbCategory = QtGui.QComboBox(AddFoodTypes)
        self.cmbCategory.setGeometry(QtCore.QRect(120, 60, 221, 31))
        self.cmbCategory.setObjectName(_fromUtf8("cmbCategory"))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))

        self.retranslateUi(AddFoodTypes)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodTypes.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddFoodTypes.saveDetails)
        QtCore.QMetaObject.connectSlotsByName(AddFoodTypes)
        AddFoodTypes.setTabOrder(self.txtFoodType, self.cmbCategory)
        AddFoodTypes.setTabOrder(self.cmbCategory, self.txtKCalories)
        AddFoodTypes.setTabOrder(self.txtKCalories, self.cmbUnitOfMeasure)
        AddFoodTypes.setTabOrder(self.cmbUnitOfMeasure, self.cmdSave)
        AddFoodTypes.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddFoodTypes):
        AddFoodTypes.setWindowTitle(QtGui.QApplication.translate("AddFoodTypes", "Add Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddFoodTypes", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddFoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddFoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddFoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddFoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddFoodTypes", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(0, QtGui.QApplication.translate("AddFoodTypes", "crops", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(1, QtGui.QApplication.translate("AddFoodTypes", "livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(2, QtGui.QApplication.translate("AddFoodTypes", "wildfoods", None, QtGui.QApplication.UnicodeUTF8))

