# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Sun Apr 17 21:36:07 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("#centralwidget {\n"
"    background : white;\n"
"    background-image : url(:/images/images/EfDChancoComposite.jpg);\n"
"    background-repeat : no-repeat;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        self.menuData_Management = QtGui.QMenu(self.menubar)
        self.menuData_Management.setObjectName(_fromUtf8("menuData_Management"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuHousehold = QtGui.QMenu(self.menubar)
        self.menuHousehold.setObjectName(_fromUtf8("menuHousehold"))
        self.menuOutputs = QtGui.QMenu(self.menubar)
        self.menuOutputs.setObjectName(_fromUtf8("menuOutputs"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionDelete_Project = QtGui.QAction(MainWindow)
        self.actionDelete_Project.setObjectName(_fromUtf8("actionDelete_Project"))
        self.actionEdit_Project = QtGui.QAction(MainWindow)
        self.actionEdit_Project.setObjectName(_fromUtf8("actionEdit_Project"))
        self.actionOpen_Household = QtGui.QAction(MainWindow)
        self.actionOpen_Household.setObjectName(_fromUtf8("actionOpen_Household"))
        self.actionConfigure_Project = QtGui.QAction(MainWindow)
        self.actionConfigure_Project.setObjectName(_fromUtf8("actionConfigure_Project"))
        self.actionMembers = QtGui.QAction(MainWindow)
        self.actionMembers.setObjectName(_fromUtf8("actionMembers"))
        self.actionExpenditure = QtGui.QAction(MainWindow)
        self.actionExpenditure.setObjectName(_fromUtf8("actionExpenditure"))
        self.actionIncome = QtGui.QAction(MainWindow)
        self.actionIncome.setObjectName(_fromUtf8("actionIncome"))
        self.actionAssets = QtGui.QAction(MainWindow)
        self.actionAssets.setObjectName(_fromUtf8("actionAssets"))
        self.actionHousehold_Characteristics = QtGui.QAction(MainWindow)
        self.actionHousehold_Characteristics.setObjectName(_fromUtf8("actionHousehold_Characteristics"))
        self.actionHousehold_Characteristics_2 = QtGui.QAction(MainWindow)
        self.actionHousehold_Characteristics_2.setObjectName(_fromUtf8("actionHousehold_Characteristics_2"))
        self.actionPersonal_Characteristics = QtGui.QAction(MainWindow)
        self.actionPersonal_Characteristics.setObjectName(_fromUtf8("actionPersonal_Characteristics"))
        self.actionAsset_Details = QtGui.QAction(MainWindow)
        self.actionAsset_Details.setObjectName(_fromUtf8("actionAsset_Details"))
        self.actionIncome_Source_Details = QtGui.QAction(MainWindow)
        self.actionIncome_Source_Details.setObjectName(_fromUtf8("actionIncome_Source_Details"))
        self.actionFood_Types = QtGui.QAction(MainWindow)
        self.actionFood_Types.setObjectName(_fromUtf8("actionFood_Types"))
        self.actionLand_Types = QtGui.QAction(MainWindow)
        self.actionLand_Types.setObjectName(_fromUtf8("actionLand_Types"))
        self.actionExpenditure_Types = QtGui.QAction(MainWindow)
        self.actionExpenditure_Types.setObjectName(_fromUtf8("actionExpenditure_Types"))
        self.actionContents = QtGui.QAction(MainWindow)
        self.actionContents.setObjectName(_fromUtf8("actionContents"))
        self.actionAboutOpenIHM = QtGui.QAction(MainWindow)
        self.actionAboutOpenIHM.setObjectName(_fromUtf8("actionAboutOpenIHM"))
        self.actionLivestock = QtGui.QAction(MainWindow)
        self.actionLivestock.setObjectName(_fromUtf8("actionLivestock"))
        self.actionLivestock_Products = QtGui.QAction(MainWindow)
        self.actionLivestock_Products.setObjectName(_fromUtf8("actionLivestock_Products"))
        self.actionTrees = QtGui.QAction(MainWindow)
        self.actionTrees.setObjectName(_fromUtf8("actionTrees"))
        self.actionEmployment = QtGui.QAction(MainWindow)
        self.actionEmployment.setObjectName(_fromUtf8("actionEmployment"))
        self.actionGifts = QtGui.QAction(MainWindow)
        self.actionGifts.setObjectName(_fromUtf8("actionGifts"))
        self.actionExternal_Aid = QtGui.QAction(MainWindow)
        self.actionExternal_Aid.setObjectName(_fromUtf8("actionExternal_Aid"))
        self.actionWild_Foods = QtGui.QAction(MainWindow)
        self.actionWild_Foods.setObjectName(_fromUtf8("actionWild_Foods"))
        self.actionHunting_and_Fishing = QtGui.QAction(MainWindow)
        self.actionHunting_and_Fishing.setObjectName(_fromUtf8("actionHunting_and_Fishing"))
        self.actionOther_Tradable_Goods = QtGui.QAction(MainWindow)
        self.actionOther_Tradable_Goods.setObjectName(_fromUtf8("actionOther_Tradable_Goods"))
        self.actionView_All_Households = QtGui.QAction(MainWindow)
        self.actionView_All_Households.setObjectName(_fromUtf8("actionView_All_Households"))
        self.actionHousehold_Data = QtGui.QAction(MainWindow)
        self.actionHousehold_Data.setObjectName(_fromUtf8("actionHousehold_Data"))
        self.actionFind_Project = QtGui.QAction(MainWindow)
        self.actionFind_Project.setObjectName(_fromUtf8("actionFind_Project"))
        self.actionCreate_Project = QtGui.QAction(MainWindow)
        self.actionCreate_Project.setObjectName(_fromUtf8("actionCreate_Project"))
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionClose_Project = QtGui.QAction(MainWindow)
        self.actionClose_Project.setObjectName(_fromUtf8("actionClose_Project"))
        self.actionImport_Project_Data = QtGui.QAction(MainWindow)
        self.actionImport_Project_Data.setObjectName(_fromUtf8("actionImport_Project_Data"))
        self.actionExport_Project_Data = QtGui.QAction(MainWindow)
        self.actionExport_Project_Data.setObjectName(_fromUtf8("actionExport_Project_Data"))
        self.actionAdd_Household = QtGui.QAction(MainWindow)
        self.actionAdd_Household.setObjectName(_fromUtf8("actionAdd_Household"))
        self.actionEdit_Household = QtGui.QAction(MainWindow)
        self.actionEdit_Household.setObjectName(_fromUtf8("actionEdit_Household"))
        self.actionDelete_Household = QtGui.QAction(MainWindow)
        self.actionDelete_Household.setObjectName(_fromUtf8("actionDelete_Household"))
        self.actionEnter_Household_Data = QtGui.QAction(MainWindow)
        self.actionEnter_Household_Data.setObjectName(_fromUtf8("actionEnter_Household_Data"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionFind_Household = QtGui.QAction(MainWindow)
        self.actionFind_Household.setObjectName(_fromUtf8("actionFind_Household"))
        self.actionView_All_Households_2 = QtGui.QAction(MainWindow)
        self.actionView_All_Households_2.setObjectName(_fromUtf8("actionView_All_Households_2"))
        self.actionEnergy_Requirements = QtGui.QAction(MainWindow)
        self.actionEnergy_Requirements.setObjectName(_fromUtf8("actionEnergy_Requirements"))
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionHousehold_by_Characteristics = QtGui.QAction(MainWindow)
        self.actionHousehold_by_Characteristics.setObjectName(_fromUtf8("actionHousehold_by_Characteristics"))
        self.actionManage_Currencies = QtGui.QAction(MainWindow)
        self.actionManage_Currencies.setObjectName(_fromUtf8("actionManage_Currencies"))
        self.actionIncome_By_Source = QtGui.QAction(MainWindow)
        self.actionIncome_By_Source.setObjectName(_fromUtf8("actionIncome_By_Source"))
        self.actionInitialise_Food_Energy_Table = QtGui.QAction(MainWindow)
        self.actionInitialise_Food_Energy_Table.setObjectName(_fromUtf8("actionInitialise_Food_Energy_Table"))
        self.actionGenerate_Data_Entry_Sheets = QtGui.QAction(MainWindow)
        self.actionGenerate_Data_Entry_Sheets.setObjectName(_fromUtf8("actionGenerate_Data_Entry_Sheets"))
        self.actionManage_Standard_of_Living_Items = QtGui.QAction(MainWindow)
        self.actionManage_Standard_of_Living_Items.setObjectName(_fromUtf8("actionManage_Standard_of_Living_Items"))
        self.actionConfigure_Project_Income = QtGui.QAction(MainWindow)
        self.actionConfigure_Project_Income.setObjectName(_fromUtf8("actionConfigure_Project_Income"))
        self.actionDisposable_Income = QtGui.QAction(MainWindow)
        self.actionDisposable_Income.setObjectName(_fromUtf8("actionDisposable_Income"))
        self.actionInitialise_Energy_Requirement_Table = QtGui.QAction(MainWindow)
        self.actionInitialise_Energy_Requirement_Table.setObjectName(_fromUtf8("actionInitialise_Energy_Requirement_Table"))
        self.actionLiving_Threshold = QtGui.QAction(MainWindow)
        self.actionLiving_Threshold.setObjectName(_fromUtf8("actionLiving_Threshold"))
        self.menuProject.addAction(self.actionCreate_Project)
        self.menuProject.addAction(self.actionOpen_Project)
        self.menuProject.addAction(self.actionFind_Project)
        self.menuProject.addAction(self.actionClose_Project)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionEdit_Project)
        self.menuProject.addAction(self.actionConfigure_Project)
        self.menuProject.addAction(self.actionConfigure_Project_Income)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionGenerate_Data_Entry_Sheets)
        self.menuProject.addAction(self.actionImport_Project_Data)
        self.menuProject.addAction(self.actionExport_Project_Data)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuData_Management.addAction(self.actionAsset_Details)
        self.menuData_Management.addAction(self.actionExpenditure_Types)
        self.menuData_Management.addAction(self.actionIncome_Source_Details)
        self.menuData_Management.addSeparator()
        self.menuData_Management.addAction(self.actionHousehold_Characteristics_2)
        self.menuData_Management.addAction(self.actionPersonal_Characteristics)
        self.menuData_Management.addSeparator()
        self.menuData_Management.addAction(self.actionFood_Types)
        self.menuData_Management.addAction(self.actionEnergy_Requirements)
        self.menuData_Management.addSeparator()
        self.menuData_Management.addAction(self.actionManage_Currencies)
        self.menuData_Management.addAction(self.actionManage_Standard_of_Living_Items)
        self.menuData_Management.addSeparator()
        self.menuData_Management.addAction(self.actionInitialise_Energy_Requirement_Table)
        self.menuData_Management.addAction(self.actionInitialise_Food_Energy_Table)
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionAboutOpenIHM)
        self.menuHousehold.addAction(self.actionAdd_Household)
        self.menuHousehold.addAction(self.actionEdit_Household)
        self.menuHousehold.addAction(self.actionDelete_Household)
        self.menuHousehold.addSeparator()
        self.menuHousehold.addAction(self.actionEnter_Household_Data)
        self.menuHousehold.addSeparator()
        self.menuHousehold.addAction(self.actionFind_Household)
        self.menuHousehold.addAction(self.actionView_All_Households_2)
        self.menuOutputs.addAction(self.actionDisposable_Income)
        self.menuOutputs.addAction(self.actionHousehold_by_Characteristics)
        self.menuOutputs.addAction(self.actionIncome_By_Source)
        self.menuOutputs.addAction(self.actionLiving_Threshold)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuHousehold.menuAction())
        self.menubar.addAction(self.menuData_Management.menuAction())
        self.menubar.addAction(self.menuOutputs.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionCreate_Project)
        self.toolBar.addAction(self.actionOpen_Project)
        self.toolBar.addAction(self.actionFind_Project)
        self.toolBar.addAction(self.actionClose_Project)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionCreate_Project, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.newProject)
        QtCore.QObject.connect(self.actionOpen_Project, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.openProject)
        QtCore.QObject.connect(self.actionFind_Project, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.findProject)
        QtCore.QObject.connect(self.actionClose_Project, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.closeProject)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionAsset_Details, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageAssetDetails)
        QtCore.QObject.connect(self.actionIncome_Source_Details, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageIncomeDetails)
        QtCore.QObject.connect(self.actionExpenditure_Types, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageBaseExpenditureDetails)
        QtCore.QObject.connect(self.actionEdit_Project, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.editProject)
        QtCore.QObject.connect(self.actionConfigure_Project, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.configureProject)
        QtCore.QObject.connect(self.actionEdit_Household, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.editProjectHousehold)
        QtCore.QObject.connect(self.actionEnter_Household_Data, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.viewHouseholdData)
        QtCore.QObject.connect(self.actionFind_Household, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.findHousehold)
        QtCore.QObject.connect(self.actionView_All_Households_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.viewAllHouseholds)
        QtCore.QObject.connect(self.actionFood_Types, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageFoodTypes)
        QtCore.QObject.connect(self.actionAdd_Household, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.addHousehold)
        QtCore.QObject.connect(self.actionDelete_Household, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.delHousehold)
        QtCore.QObject.connect(self.actionHousehold_Characteristics_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageHouseholdCharacteristics)
        QtCore.QObject.connect(self.actionPersonal_Characteristics, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.managePersonalCharacteristics)
        QtCore.QObject.connect(self.actionAboutOpenIHM, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.aboutOpenIHM)
        QtCore.QObject.connect(self.actionEnergy_Requirements, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.viewFoodEnergyRequirements)
        QtCore.QObject.connect(self.actionManage_Currencies, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageCurrencies)
        QtCore.QObject.connect(self.actionManage_Standard_of_Living_Items, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.manageStandardOfLiving)
        QtCore.QObject.connect(self.actionHousehold_by_Characteristics, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.reportHouseholdsByCharacteristics)
        QtCore.QObject.connect(self.actionIncome_By_Source, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.reportHouseholdsByIncomeSource)
        QtCore.QObject.connect(self.actionInitialise_Food_Energy_Table, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.initialiseFoodEnergyLookupTable)
        QtCore.QObject.connect(self.actionGenerate_Data_Entry_Sheets, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.createDataEntrySheets)
        QtCore.QObject.connect(self.actionImport_Project_Data, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.importData)
        QtCore.QObject.connect(self.actionDisposable_Income, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.setReporttypeDI)
        QtCore.QObject.connect(self.actionInitialise_Energy_Requirement_Table, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.initialiseFoodRequirementTable)
        QtCore.QObject.connect(self.actionLiving_Threshold, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.setReporttypeAsLivingThreshold)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Open IHM", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProject.setTitle(QtGui.QApplication.translate("MainWindow", "&Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData_Management.setTitle(QtGui.QApplication.translate("MainWindow", "Data &Management", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHousehold.setTitle(QtGui.QApplication.translate("MainWindow", "Household", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOutputs.setTitle(QtGui.QApplication.translate("MainWindow", "Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Project.setText(QtGui.QApplication.translate("MainWindow", "Delete Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Project.setText(QtGui.QApplication.translate("MainWindow", "Edit Project", None, QtGui.QApplication.UnicodeUTF8))
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
        self.actionFood_Types.setText(QtGui.QApplication.translate("MainWindow", "View Food Type Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLand_Types.setText(QtGui.QApplication.translate("MainWindow", "Land Types", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExpenditure_Types.setText(QtGui.QApplication.translate("MainWindow", "Expenditure Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionContents.setText(QtGui.QApplication.translate("MainWindow", "Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionContents.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutOpenIHM.setText(QtGui.QApplication.translate("MainWindow", "About Open IHM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLivestock.setText(QtGui.QApplication.translate("MainWindow", "Livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLivestock_Products.setText(QtGui.QApplication.translate("MainWindow", "Livestock Products", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrees.setText(QtGui.QApplication.translate("MainWindow", "Trees", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEmployment.setText(QtGui.QApplication.translate("MainWindow", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGifts.setText(QtGui.QApplication.translate("MainWindow", "Gifts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExternal_Aid.setText(QtGui.QApplication.translate("MainWindow", "External Aid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWild_Foods.setText(QtGui.QApplication.translate("MainWindow", "Wild Foods", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHunting_and_Fishing.setText(QtGui.QApplication.translate("MainWindow", "Hunting and Fishing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOther_Tradable_Goods.setText(QtGui.QApplication.translate("MainWindow", "Other Tradable Goods", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_All_Households.setText(QtGui.QApplication.translate("MainWindow", "View All Households", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHousehold_Data.setText(QtGui.QApplication.translate("MainWindow", "Household Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Project.setText(QtGui.QApplication.translate("MainWindow", "Find Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Project.setText(QtGui.QApplication.translate("MainWindow", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Project.setText(QtGui.QApplication.translate("MainWindow", "Close Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Project_Data.setText(QtGui.QApplication.translate("MainWindow", "Import Project Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Project_Data.setText(QtGui.QApplication.translate("MainWindow", "Export Project Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Household.setText(QtGui.QApplication.translate("MainWindow", "Add Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Household.setText(QtGui.QApplication.translate("MainWindow", "Edit Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Household.setText(QtGui.QApplication.translate("MainWindow", "Delete Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnter_Household_Data.setText(QtGui.QApplication.translate("MainWindow", "Enter Household Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Household.setText(QtGui.QApplication.translate("MainWindow", "Find Household", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_All_Households_2.setText(QtGui.QApplication.translate("MainWindow", "View All Households", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnergy_Requirements.setText(QtGui.QApplication.translate("MainWindow", "View Food Energy Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHousehold_by_Characteristics.setText(QtGui.QApplication.translate("MainWindow", "Households List by Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_Currencies.setText(QtGui.QApplication.translate("MainWindow", "Manage Currencies", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncome_By_Source.setText(QtGui.QApplication.translate("MainWindow", "Income By Source", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInitialise_Food_Energy_Table.setText(QtGui.QApplication.translate("MainWindow", "Initialise Food Energy Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate_Data_Entry_Sheets.setText(QtGui.QApplication.translate("MainWindow", "Create Data Entry Sheets", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_Standard_of_Living_Items.setText(QtGui.QApplication.translate("MainWindow", "Manage Standard of Living Items", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure_Project_Income.setText(QtGui.QApplication.translate("MainWindow", "Select Project Income", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisposable_Income.setText(QtGui.QApplication.translate("MainWindow", "Disposable Income", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInitialise_Energy_Requirement_Table.setText(QtGui.QApplication.translate("MainWindow", "Initialise Energy Requirements Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLiving_Threshold.setText(QtGui.QApplication.translate("MainWindow", "Living Threshold", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
import resimages_rc
