# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_households_all.ui'
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

class Ui_AllHouseholds(object):
    def setupUi(self, AllHouseholds):
        AllHouseholds.setObjectName(_fromUtf8("AllHouseholds"))
        AllHouseholds.resize(792, 550)
        AllHouseholds.setMinimumSize(QtCore.QSize(792, 550))
        self.formLayout = QtGui.QFormLayout(AllHouseholds)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AllHouseholds)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblProjectName = QtGui.QLabel(AllHouseholds)
        self.lblProjectName.setObjectName(_fromUtf8("lblProjectName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblProjectName)
        self.groupBox = QtGui.QGroupBox(AllHouseholds)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 400))
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(AllHouseholds)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdAdd = QtGui.QPushButton(self.groupBox_2)
        self.cmdAdd.setObjectName(_fromUtf8("cmdAdd"))
        self.horizontalLayout.addWidget(self.cmdAdd)
        self.cmdEdit = QtGui.QPushButton(self.groupBox_2)
        self.cmdEdit.setObjectName(_fromUtf8("cmdEdit"))
        self.horizontalLayout.addWidget(self.cmdEdit)
        self.cmdDel = QtGui.QPushButton(self.groupBox_2)
        self.cmdDel.setObjectName(_fromUtf8("cmdDel"))
        self.horizontalLayout.addWidget(self.cmdDel)
        self.cmdData = QtGui.QPushButton(self.groupBox_2)
        self.cmdData.setObjectName(_fromUtf8("cmdData"))
        self.horizontalLayout.addWidget(self.cmdData)
        self.cmdClose = QtGui.QPushButton(self.groupBox_2)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox_2)

        self.retranslateUi(AllHouseholds)
        QtCore.QMetaObject.connectSlotsByName(AllHouseholds)

    def retranslateUi(self, AllHouseholds):
        AllHouseholds.setWindowTitle(QtGui.QApplication.translate("AllHouseholds", "Project Households", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AllHouseholds", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("AllHouseholds", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AllHouseholds", "Households", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setText(QtGui.QApplication.translate("AllHouseholds", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEdit.setText(QtGui.QApplication.translate("AllHouseholds", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDel.setText(QtGui.QApplication.translate("AllHouseholds", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdData.setText(QtGui.QApplication.translate("AllHouseholds", "View|Edit Household Data", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("AllHouseholds", "Close", None, QtGui.QApplication.UnicodeUTF8))

