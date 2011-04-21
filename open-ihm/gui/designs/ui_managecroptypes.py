# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managecroptypes.ui'
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

class Ui_CropTypes(object):
    def setupUi(self, CropTypes):
        CropTypes.setObjectName(_fromUtf8("CropTypes"))
        CropTypes.resize(479, 261)
        CropTypes.setMinimumSize(QtCore.QSize(389, 261))
        self.formLayout = QtGui.QFormLayout(CropTypes)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(CropTypes)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox = QtGui.QComboBox(CropTypes)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtGui.QLabel(CropTypes)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox_2 = QtGui.QComboBox(CropTypes)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.label_3 = QtGui.QLabel(CropTypes)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox_3 = QtGui.QComboBox(CropTypes)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_3)
        self.label_4 = QtGui.QLabel(CropTypes)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox_4 = QtGui.QComboBox(CropTypes)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_4)
        self.label_5 = QtGui.QLabel(CropTypes)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit = QtGui.QLineEdit(CropTypes)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.groupBox = QtGui.QGroupBox(CropTypes)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.btnManageCropsClose = QtGui.QPushButton(self.groupBox)
        self.btnManageCropsClose.setObjectName(_fromUtf8("btnManageCropsClose"))
        self.horizontalLayout.addWidget(self.btnManageCropsClose)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(CropTypes)
        QtCore.QObject.connect(self.btnManageCropsClose, QtCore.SIGNAL(_fromUtf8("clicked()")), CropTypes.mdiClose)
        QtCore.QMetaObject.connectSlotsByName(CropTypes)
        CropTypes.setTabOrder(self.comboBox, self.comboBox_2)
        CropTypes.setTabOrder(self.comboBox_2, self.comboBox_3)
        CropTypes.setTabOrder(self.comboBox_3, self.comboBox_4)
        CropTypes.setTabOrder(self.comboBox_4, self.lineEdit)
        CropTypes.setTabOrder(self.lineEdit, self.pushButton_3)
        CropTypes.setTabOrder(self.pushButton_3, self.pushButton)
        CropTypes.setTabOrder(self.pushButton, self.btnManageCropsClose)

    def retranslateUi(self, CropTypes):
        CropTypes.setWindowTitle(QtGui.QApplication.translate("CropTypes", "Manage Crop Types", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CropTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CropTypes", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CropTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CropTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CropTypes", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("CropTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("CropTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageCropsClose.setText(QtGui.QApplication.translate("CropTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))

