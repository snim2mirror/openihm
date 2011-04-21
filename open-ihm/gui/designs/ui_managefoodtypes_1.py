# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managefoodtypes_1.ui'
#
# Created: Thu Apr 21 19:28:08 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FoodTypes(object):
    def setupUi(self, FoodTypes):
        FoodTypes.setObjectName(_fromUtf8("FoodTypes"))
        FoodTypes.resize(456, 400)
        FoodTypes.setMinimumSize(QtCore.QSize(456, 400))
        self.verticalLayout = QtGui.QVBoxLayout(FoodTypes)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(FoodTypes)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.txtSearchCrop = QtGui.QLineEdit(self.groupBox_2)
        self.txtSearchCrop.setObjectName(_fromUtf8("txtSearchCrop"))
        self.horizontalLayout_2.addWidget(self.txtSearchCrop)
        self.cmdSearch = QtGui.QPushButton(self.groupBox_2)
        self.cmdSearch.setObjectName(_fromUtf8("cmdSearch"))
        self.horizontalLayout_2.addWidget(self.cmdSearch)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tableView = QtGui.QTableView(FoodTypes)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.groupBox = QtGui.QGroupBox(FoodTypes)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdAddRow = QtGui.QPushButton(self.groupBox)
        self.cmdAddRow.setObjectName(_fromUtf8("cmdAddRow"))
        self.horizontalLayout.addWidget(self.cmdAddRow)
        self.cmdEditRow = QtGui.QPushButton(self.groupBox)
        self.cmdEditRow.setObjectName(_fromUtf8("cmdEditRow"))
        self.horizontalLayout.addWidget(self.cmdEditRow)
        self.cmdDeleteRows = QtGui.QPushButton(self.groupBox)
        self.cmdDeleteRows.setObjectName(_fromUtf8("cmdDeleteRows"))
        self.horizontalLayout.addWidget(self.cmdDeleteRows)
        self.cmdClose = QtGui.QPushButton(self.groupBox)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FoodTypes)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodTypes.mdiClose)
        QtCore.QObject.connect(self.cmdDeleteRows, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodTypes.deleteSelectedCropTypes)
        QtCore.QObject.connect(self.cmdEditRow, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodTypes.editCropType)
        QtCore.QObject.connect(self.cmdAddRow, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodTypes.saveCropType)
        QtCore.QObject.connect(self.cmdSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), FoodTypes.searchCropType)
        QtCore.QMetaObject.connectSlotsByName(FoodTypes)
        FoodTypes.setTabOrder(self.txtSearchCrop, self.cmdSearch)
        FoodTypes.setTabOrder(self.cmdSearch, self.tableView)
        FoodTypes.setTabOrder(self.tableView, self.cmdAddRow)
        FoodTypes.setTabOrder(self.cmdAddRow, self.cmdEditRow)
        FoodTypes.setTabOrder(self.cmdEditRow, self.cmdDeleteRows)
        FoodTypes.setTabOrder(self.cmdDeleteRows, self.cmdClose)

    def retranslateUi(self, FoodTypes):
        FoodTypes.setWindowTitle(QtGui.QApplication.translate("FoodTypes", "Food Energy Values", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FoodTypes", "Search for Food Type", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSearch.setText(QtGui.QApplication.translate("FoodTypes", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddRow.setText(QtGui.QApplication.translate("FoodTypes", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditRow.setText(QtGui.QApplication.translate("FoodTypes", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDeleteRows.setText(QtGui.QApplication.translate("FoodTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("FoodTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))

