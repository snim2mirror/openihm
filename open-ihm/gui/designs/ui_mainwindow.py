# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Fri Mar  5 17:05:29 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,800,600).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,26,800,551))
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,26))
        self.menubar.setObjectName("menubar")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")

        self.menuHousehold = QtGui.QMenu(self.menuProject)
        self.menuHousehold.setObjectName("menuHousehold")

        self.menuData_Management = QtGui.QMenu(self.menubar)
        self.menuData_Management.setObjectName("menuData_Management")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,577,800,23))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew_Project = QtGui.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")

        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")

        self.actionClose_Project = QtGui.QAction(MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionDelete_Project = QtGui.QAction(MainWindow)
        self.actionDelete_Project.setObjectName("actionDelete_Project")

        self.actionExport_Project_Data = QtGui.QAction(MainWindow)
        self.actionExport_Project_Data.setObjectName("actionExport_Project_Data")

        self.actionFind_Project = QtGui.QAction(MainWindow)
        self.actionFind_Project.setObjectName("actionFind_Project")

        self.actionFind_Project_2 = QtGui.QAction(MainWindow)
        self.actionFind_Project_2.setObjectName("actionFind_Project_2")

        self.actionEdit_Project = QtGui.QAction(MainWindow)
        self.actionEdit_Project.setObjectName("actionEdit_Project")

        self.actionAdd_Household = QtGui.QAction(MainWindow)
        self.actionAdd_Household.setObjectName("actionAdd_Household")

        self.actionOpen_Household = QtGui.QAction(MainWindow)
        self.actionOpen_Household.setObjectName("actionOpen_Household")

        self.actionConfigure_Project = QtGui.QAction(MainWindow)
        self.actionConfigure_Project.setObjectName("actionConfigure_Project")

        self.actionMembers = QtGui.QAction(MainWindow)
        self.actionMembers.setObjectName("actionMembers")

        self.actionExpenditure = QtGui.QAction(MainWindow)
        self.actionExpenditure.setObjectName("actionExpenditure")

        self.actionIncome = QtGui.QAction(MainWindow)
        self.actionIncome.setObjectName("actionIncome")

        self.actionAssets = QtGui.QAction(MainWindow)
        self.actionAssets.setObjectName("actionAssets")

        self.actionHousehold_Characteristics = QtGui.QAction(MainWindow)
        self.actionHousehold_Characteristics.setObjectName("actionHousehold_Characteristics")

        self.actionHousehold_Characteristics_2 = QtGui.QAction(MainWindow)
        self.actionHousehold_Characteristics_2.setObjectName("actionHousehold_Characteristics_2")

        self.actionPersonal_Characteristics = QtGui.QAction(MainWindow)
        self.actionPersonal_Characteristics.setObjectName("actionPersonal_Characteristics")

        self.actionAsset_Details = QtGui.QAction(MainWindow)
        self.actionAsset_Details.setObjectName("actionAsset_Details")

        self.actionIncome_Source_Details = QtGui.QAction(MainWindow)
        self.actionIncome_Source_Details.setObjectName("actionIncome_Source_Details")

        self.actionCrop_Types = QtGui.QAction(MainWindow)
        self.actionCrop_Types.setObjectName("actionCrop_Types")

        self.actionLand_Types = QtGui.QAction(MainWindow)
        self.actionLand_Types.setObjectName("actionLand_Types")

        self.actionExpenditure_Types = QtGui.QAction(MainWindow)
        self.actionExpenditure_Types.setObjectName("actionExpenditure_Types")

        self.actionContents = QtGui.QAction(MainWindow)
        self.actionContents.setObjectName("actionContents")

        self.actionIndex = QtGui.QAction(MainWindow)
        self.actionIndex.setObjectName("actionIndex")

        self.actionImport_Project_Data = QtGui.QAction(MainWindow)
        self.actionImport_Project_Data.setObjectName("actionImport_Project_Data")

        self.actionLivestock = QtGui.QAction(MainWindow)
        self.actionLivestock.setObjectName("actionLivestock")

        self.actionLivestock_Products = QtGui.QAction(MainWindow)
        self.actionLivestock_Products.setObjectName("actionLivestock_Products")

        self.actionTrees = QtGui.QAction(MainWindow)
        self.actionTrees.setObjectName("actionTrees")

        self.actionEmployment = QtGui.QAction(MainWindow)
        self.actionEmployment.setObjectName("actionEmployment")

        self.actionGifts = QtGui.QAction(MainWindow)
        self.actionGifts.setObjectName("actionGifts")

        self.actionExternal_Aid = QtGui.QAction(MainWindow)
        self.actionExternal_Aid.setObjectName("actionExternal_Aid")

        self.actionWild_Foods = QtGui.QAction(MainWindow)
        self.actionWild_Foods.setObjectName("actionWild_Foods")

        self.actionHunting_and_Fishing = QtGui.QAction(MainWindow)
        self.actionHunting_and_Fishing.setObjectName("actionHunting_and_Fishing")

        self.actionOther_Tradable_Goods = QtGui.QAction(MainWindow)
        self.actionOther_Tradable_Goods.setObjectName("actionOther_Tradable_Goods")
        self.menu_File.addAction(self.actionNew_Project)
        self.menu_File.addAction(self.actionOpen_Project)
        self.menu_File.addAction(self.actionDelete_Project)
        self.menu_File.addAction(self.actionClose_Project)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionImport_Project_Data)
        self.menu_File.addAction(self.actionExport_Project_Data)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFind_Project)
        self.menuEdit.addAction(self.actionFind_Project_2)
        self.menuHousehold.addAction(self.actionMembers)
        self.menuHousehold.addAction(self.actionExpenditure)
        self.menuHousehold.addAction(self.actionIncome)
        self.menuHousehold.addAction(self.actionAssets)
        self.menuHousehold.addAction(self.actionHousehold_Characteristics)
        self.menuProject.addAction(self.actionEdit_Project)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionAdd_Household)
        self.menuProject.addAction(self.actionOpen_Household)
        self.menuProject.addAction(self.menuHousehold.menuAction())
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionConfigure_Project)
        self.menuData_Management.addAction(self.actionAsset_Details)
        self.menuData_Management.addAction(self.actionExpenditure_Types)
        self.menuData_Management.addAction(self.actionCrop_Types)
        self.menuData_Management.addAction(self.actionHousehold_Characteristics_2)
        self.menuData_Management.addAction(self.actionIncome_Source_Details)
        self.menuData_Management.addAction(self.actionPersonal_Characteristics)
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionIndex)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuData_Management.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Open IHM", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProject.setTitle(QtGui.QApplication.translate("MainWindow", "&Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHousehold.setTitle(QtGui.QApplication.translate("MainWindow", "View Household", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData_Management.setTitle(QtGui.QApplication.translate("MainWindow", "Data &Management", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Project.setText(QtGui.QApplication.translate("MainWindow", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Project.setText(QtGui.QApplication.translate("MainWindow", "Close Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Project.setText(QtGui.QApplication.translate("MainWindow", "Delete Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Project_Data.setText(QtGui.QApplication.translate("MainWindow", "Export Project Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Project.setText(QtGui.QApplication.translate("MainWindow", "Find Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Project_2.setText(QtGui.QApplication.translate("MainWindow", "Find Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Project_2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Project.setText(QtGui.QApplication.translate("MainWindow", "Edit Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Household.setText(QtGui.QApplication.translate("MainWindow", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Household.setText(QtGui.QApplication.translate("MainWindow", "Edit Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure_Project.setText(QtGui.QApplication.translate("MainWindow", "Configure Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMembers.setText(QtGui.QApplication.translate("MainWindow", "Members", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExpenditure.setText(QtGui.QApplication.translate("MainWindow", "Expenditure", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncome.setText(QtGui.QApplication.translate("MainWindow", "Income", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAssets.setText(QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHousehold_Characteristics.setText(QtGui.QApplication.translate("MainWindow", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHousehold_Characteristics_2.setText(QtGui.QApplication.translate("MainWindow", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPersonal_Characteristics.setText(QtGui.QApplication.translate("MainWindow", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAsset_Details.setText(QtGui.QApplication.translate("MainWindow", "Asset Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncome_Source_Details.setText(QtGui.QApplication.translate("MainWindow", "Income Source Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCrop_Types.setText(QtGui.QApplication.translate("MainWindow", "Crop Type Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLand_Types.setText(QtGui.QApplication.translate("MainWindow", "Land Types", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExpenditure_Types.setText(QtGui.QApplication.translate("MainWindow", "Expenditure Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionContents.setText(QtGui.QApplication.translate("MainWindow", "Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionContents.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndex.setText(QtGui.QApplication.translate("MainWindow", "About Open IHM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Project_Data.setText(QtGui.QApplication.translate("MainWindow", "Import Project Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLivestock.setText(QtGui.QApplication.translate("MainWindow", "Livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLivestock_Products.setText(QtGui.QApplication.translate("MainWindow", "Livestock Products", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrees.setText(QtGui.QApplication.translate("MainWindow", "Trees", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEmployment.setText(QtGui.QApplication.translate("MainWindow", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGifts.setText(QtGui.QApplication.translate("MainWindow", "Gifts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExternal_Aid.setText(QtGui.QApplication.translate("MainWindow", "External Aid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWild_Foods.setText(QtGui.QApplication.translate("MainWindow", "Wild Foods", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHunting_and_Fishing.setText(QtGui.QApplication.translate("MainWindow", "Hunting and Fishing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOther_Tradable_Goods.setText(QtGui.QApplication.translate("MainWindow", "Other Tradable Goods", None, QtGui.QApplication.UnicodeUTF8))

