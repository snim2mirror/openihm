# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_edit.ui'
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

class Ui_EditFoodTypes(object):
    def setupUi(self, EditFoodTypes):
        EditFoodTypes.setObjectName(_fromUtf8("EditFoodTypes"))
        EditFoodTypes.resize(350, 259)
        EditFoodTypes.setMinimumSize(QtCore.QSize(350, 204))
        self.cmdCancel = QtGui.QPushButton(EditFoodTypes)
        self.cmdCancel.setGeometry(QtCore.QRect(260, 220, 80, 28))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.cmdSave = QtGui.QPushButton(EditFoodTypes)
        self.cmdSave.setGeometry(QtCore.QRect(70, 220, 80, 28))
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.label = QtGui.QLabel(EditFoodTypes)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(EditFoodTypes)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 91, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(EditFoodTypes)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 101, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtKCalories = QtGui.QLineEdit(EditFoodTypes)
        self.txtKCalories.setGeometry(QtCore.QRect(120, 110, 141, 31))
        self.txtKCalories.setObjectName(_fromUtf8("txtKCalories"))
        self.txtFoodType = QtGui.QLineEdit(EditFoodTypes)
        self.txtFoodType.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.txtFoodType.setObjectName(_fromUtf8("txtFoodType"))
        self.txtMeasuringUnit = QtGui.QLineEdit(EditFoodTypes)
        self.txtMeasuringUnit.setGeometry(QtCore.QRect(120, 160, 141, 31))
        self.txtMeasuringUnit.setObjectName(_fromUtf8("txtMeasuringUnit"))
        self.cmbCategory = QtGui.QComboBox(EditFoodTypes)
        self.cmbCategory.setGeometry(QtCore.QRect(120, 50, 221, 31))
        self.cmbCategory.setObjectName(_fromUtf8("cmbCategory"))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.cmbCategory.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(EditFoodTypes)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(EditFoodTypes)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodTypes.close)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), EditFoodTypes.saveDetails)
        QtCore.QMetaObject.connectSlotsByName(EditFoodTypes)
        EditFoodTypes.setTabOrder(self.txtFoodType, self.cmbCategory)
        EditFoodTypes.setTabOrder(self.cmbCategory, self.txtKCalories)
        EditFoodTypes.setTabOrder(self.txtKCalories, self.txtMeasuringUnit)
        EditFoodTypes.setTabOrder(self.txtMeasuringUnit, self.cmdSave)
        EditFoodTypes.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, EditFoodTypes):
        EditFoodTypes.setWindowTitle(QtGui.QApplication.translate("EditFoodTypes", "Edit Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("EditFoodTypes", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("EditFoodTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditFoodTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditFoodTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EditFoodTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(0, QtGui.QApplication.translate("EditFoodTypes", "crops", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(1, QtGui.QApplication.translate("EditFoodTypes", "livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCategory.setItemText(2, QtGui.QApplication.translate("EditFoodTypes", "wildfoods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditFoodTypes", "Category", None, QtGui.QApplication.UnicodeUTF8))

