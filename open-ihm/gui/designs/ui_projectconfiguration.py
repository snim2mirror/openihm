# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_projectconfiguration.ui'
#
# Created: Wed Mar 02 22:19:42 2011
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProjectConfiguration(object):
    def setupUi(self, ProjectConfiguration):
        ProjectConfiguration.setObjectName("ProjectConfiguration")
        ProjectConfiguration.resize(678, 537)
        ProjectConfiguration.setMinimumSize(QtCore.QSize(678, 537))
        ProjectConfiguration.setSizeIncrement(QtCore.QSize(0, 0))
        self.label = QtGui.QLabel(ProjectConfiguration)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.lblProjectName = QtGui.QLabel(ProjectConfiguration)
        self.lblProjectName.setGeometry(QtCore.QRect(100, 10, 431, 16))
        self.lblProjectName.setObjectName("lblProjectName")
        self.tabProject = QtGui.QTabWidget(ProjectConfiguration)
        self.tabProject.setGeometry(QtCore.QRect(10, 40, 661, 451))
        self.tabProject.setObjectName("tabProject")
        self.tabProjectHouseholdCharacteristics = QtGui.QWidget()
        self.tabProjectHouseholdCharacteristics.setObjectName("tabProjectHouseholdCharacteristics")
        self.cmdHouseholdMoveSelected = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdHouseholdMoveSelected.setObjectName("cmdHouseholdMoveSelected")
        self.cmdHouseholdRemoveSelected = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdHouseholdRemoveSelected.setObjectName("cmdHouseholdRemoveSelected")
        self.label_5 = QtGui.QLabel(self.tabProjectHouseholdCharacteristics)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_5.setObjectName("label_5")
        self.cmdHouseholdMoveAll = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdHouseholdMoveAll.setObjectName("cmdHouseholdMoveAll")
        self.cmdHouseholdRemoveAll = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdHouseholdRemoveAll.setObjectName("cmdHouseholdRemoveAll")
        self.label_6 = QtGui.QLabel(self.tabProjectHouseholdCharacteristics)
        self.label_6.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_6.setObjectName("label_6")
        self.lstHouseholdAvailableChars = QtGui.QListView(self.tabProjectHouseholdCharacteristics)
        self.lstHouseholdAvailableChars.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.lstHouseholdAvailableChars.setObjectName("lstHouseholdAvailableChars")
        self.lstHouseholdSelectedChars = QtGui.QListView(self.tabProjectHouseholdCharacteristics)
        self.lstHouseholdSelectedChars.setGeometry(QtCore.QRect(370, 30, 261, 361))
        self.lstHouseholdSelectedChars.setObjectName("lstHouseholdSelectedChars")
        self.tabProject.addTab(self.tabProjectHouseholdCharacteristics, "")
        self.tabProjectPersonalCharacteristics = QtGui.QWidget()
        self.tabProjectPersonalCharacteristics.setObjectName("tabProjectPersonalCharacteristics")
        self.cmdPersonalRemoveSelected = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdPersonalRemoveSelected.setObjectName("cmdPersonalRemoveSelected")
        self.label_4 = QtGui.QLabel(self.tabProjectPersonalCharacteristics)
        self.label_4.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_4.setObjectName("label_4")
        self.cmdPersonalMoveSelected = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdPersonalMoveSelected.setObjectName("cmdPersonalMoveSelected")
        self.cmdPersonalMoveAll = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdPersonalMoveAll.setObjectName("cmdPersonalMoveAll")
        self.label_3 = QtGui.QLabel(self.tabProjectPersonalCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_3.setObjectName("label_3")
        self.cmdPersonalRemoveAll = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdPersonalRemoveAll.setObjectName("cmdPersonalRemoveAll")
        self.lstPersonalAvailableChars = QtGui.QListView(self.tabProjectPersonalCharacteristics)
        self.lstPersonalAvailableChars.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.lstPersonalAvailableChars.setObjectName("lstPersonalAvailableChars")
        self.lstPersonalSelectedChars = QtGui.QListView(self.tabProjectPersonalCharacteristics)
        self.lstPersonalSelectedChars.setGeometry(QtCore.QRect(370, 30, 261, 361))
        self.lstPersonalSelectedChars.setObjectName("lstPersonalSelectedChars")
        self.tabProject.addTab(self.tabProjectPersonalCharacteristics, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tblDiets = QtGui.QTableView(self.tab)
        self.tblDiets.setGeometry(QtCore.QRect(10, 10, 341, 381))
        self.tblDiets.setObjectName("tblDiets")
        self.cmdDelDiet = QtGui.QPushButton(self.tab)
        self.cmdDelDiet.setGeometry(QtCore.QRect(360, 350, 91, 31))
        self.cmdDelDiet.setObjectName("cmdDelDiet")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(360, 10, 281, 211))
        self.groupBox.setObjectName("groupBox")
        self.cmbFoodItem = QtGui.QComboBox(self.groupBox)
        self.cmbFoodItem.setGeometry(QtCore.QRect(120, 20, 141, 22))
        self.cmbFoodItem.setObjectName("cmbFoodItem")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 23, 81, 20))
        self.label_2.setObjectName("label_2")
        self.txtUnitOfMeasure = QtGui.QLineEdit(self.groupBox)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 60, 141, 20))
        self.txtUnitOfMeasure.setObjectName("txtUnitOfMeasure")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_7.setObjectName("label_7")
        self.txtPercentage = QtGui.QLineEdit(self.groupBox)
        self.txtPercentage.setGeometry(QtCore.QRect(120, 100, 91, 20))
        self.txtPercentage.setObjectName("txtPercentage")
        self.txtUnitPrice = QtGui.QLineEdit(self.groupBox)
        self.txtUnitPrice.setGeometry(QtCore.QRect(120, 140, 91, 20))
        self.txtUnitPrice.setObjectName("txtUnitPrice")
        self.cmdSaveDiet = QtGui.QPushButton(self.groupBox)
        self.cmdSaveDiet.setGeometry(QtCore.QRect(180, 170, 91, 31))
        self.cmdSaveDiet.setObjectName("cmdSaveDiet")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 91, 21))
        self.label_9.setObjectName("label_9")
        self.tabProject.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tblStandardOfLiving = QtGui.QTableView(self.tab_2)
        self.tblStandardOfLiving.setGeometry(QtCore.QRect(10, 10, 361, 381))
        self.tblStandardOfLiving.setObjectName("tblStandardOfLiving")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 251, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cmbExpenseItem = QtGui.QComboBox(self.groupBox_2)
        self.cmbExpenseItem.setGeometry(QtCore.QRect(90, 110, 151, 22))
        self.cmbExpenseItem.setObjectName("cmbExpenseItem")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 81, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_11.setObjectName("label_11")
        self.cmdSaveLivingStanItem = QtGui.QPushButton(self.groupBox_2)
        self.cmdSaveLivingStanItem.setGeometry(QtCore.QRect(150, 170, 91, 31))
        self.cmdSaveLivingStanItem.setObjectName("cmdSaveLivingStanItem")
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 140, 81, 20))
        self.label_14.setObjectName("label_14")
        self.txtCostPerYear = QtGui.QLineEdit(self.groupBox_2)
        self.txtCostPerYear.setGeometry(QtCore.QRect(90, 140, 151, 20))
        self.txtCostPerYear.setObjectName("txtCostPerYear")
        self.cmbScope = QtGui.QComboBox(self.groupBox_2)
        self.cmbScope.setGeometry(QtCore.QRect(90, 20, 151, 22))
        self.cmbScope.setObjectName("cmbScope")
        self.cmbScope.addItem("")
        self.cmbScope.addItem("")
        self.cmbGender = QtGui.QComboBox(self.groupBox_2)
        self.cmbGender.setGeometry(QtCore.QRect(90, 50, 151, 22))
        self.cmbGender.setEditable(False)
        self.cmbGender.setObjectName("cmbGender")
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbAgeBottom = QtGui.QComboBox(self.groupBox_2)
        self.cmbAgeBottom.setGeometry(QtCore.QRect(90, 80, 61, 22))
        self.cmbAgeBottom.setEditable(False)
        self.cmbAgeBottom.setObjectName("cmbAgeBottom")
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(160, 80, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.cmbAgeTop = QtGui.QComboBox(self.groupBox_2)
        self.cmbAgeTop.setGeometry(QtCore.QRect(190, 80, 51, 22))
        self.cmbAgeTop.setEditable(False)
        self.cmbAgeTop.setObjectName("cmbAgeTop")
        self.cmdDelLivingStandardItem = QtGui.QPushButton(self.tab_2)
        self.cmdDelLivingStandardItem.setGeometry(QtCore.QRect(390, 360, 91, 31))
        self.cmdDelLivingStandardItem.setObjectName("cmdDelLivingStandardItem")
        self.tabProject.addTab(self.tab_2, "")
        self.tabIncome = QtGui.QWidget()
        self.tabIncome.setObjectName("tabIncome")
        self.tabWidget = QtGui.QTabWidget(self.tabIncome)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 641, 421))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tabCrops = QtGui.QWidget()
        self.tabCrops.setObjectName("tabCrops")
        self.label_26 = QtGui.QLabel(self.tabCrops)
        self.label_26.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtGui.QLabel(self.tabCrops)
        self.label_27.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_27.setObjectName("label_27")
        self.cmdCropsRemoveAll = QtGui.QPushButton(self.tabCrops)
        self.cmdCropsRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdCropsRemoveAll.setObjectName("cmdCropsRemoveAll")
        self.cmdCropsRemoveSelected = QtGui.QPushButton(self.tabCrops)
        self.cmdCropsRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdCropsRemoveSelected.setObjectName("cmdCropsRemoveSelected")
        self.cmdCropsMoveSelected = QtGui.QPushButton(self.tabCrops)
        self.cmdCropsMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdCropsMoveSelected.setObjectName("cmdCropsMoveSelected")
        self.cmdCropsMoveAll = QtGui.QPushButton(self.tabCrops)
        self.cmdCropsMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdCropsMoveAll.setObjectName("cmdCropsMoveAll")
        self.tblAvailableCrops = QtGui.QTableView(self.tabCrops)
        self.tblAvailableCrops.setGeometry(QtCore.QRect(10, 30, 256, 361))
        self.tblAvailableCrops.setObjectName("tblAvailableCrops")
        self.tblSelectedCrops = QtGui.QTableView(self.tabCrops)
        self.tblSelectedCrops.setGeometry(QtCore.QRect(370, 30, 256, 361))
        self.tblSelectedCrops.setObjectName("tblSelectedCrops")
        self.tabWidget.addTab(self.tabCrops, "")
        self.tabEmployment = QtGui.QWidget()
        self.tabEmployment.setObjectName("tabEmployment")
        self.label_28 = QtGui.QLabel(self.tabEmployment)
        self.label_28.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_28.setObjectName("label_28")
        self.cmdEmploymentRemoveAll = QtGui.QPushButton(self.tabEmployment)
        self.cmdEmploymentRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdEmploymentRemoveAll.setObjectName("cmdEmploymentRemoveAll")
        self.cmdEmploymentMoveSelected = QtGui.QPushButton(self.tabEmployment)
        self.cmdEmploymentMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdEmploymentMoveSelected.setObjectName("cmdEmploymentMoveSelected")
        self.cmdEmploymentMoveAll = QtGui.QPushButton(self.tabEmployment)
        self.cmdEmploymentMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdEmploymentMoveAll.setObjectName("cmdEmploymentMoveAll")
        self.cmdEmploymentRemoveSelected = QtGui.QPushButton(self.tabEmployment)
        self.cmdEmploymentRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdEmploymentRemoveSelected.setObjectName("cmdEmploymentRemoveSelected")
        self.label_29 = QtGui.QLabel(self.tabEmployment)
        self.label_29.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_29.setObjectName("label_29")
        self.tblAvailableEmployment = QtGui.QTableView(self.tabEmployment)
        self.tblAvailableEmployment.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.tblAvailableEmployment.setObjectName("tblAvailableEmployment")
        self.tblSelectedEmployment = QtGui.QTableView(self.tabEmployment)
        self.tblSelectedEmployment.setGeometry(QtCore.QRect(370, 30, 256, 361))
        self.tblSelectedEmployment.setObjectName("tblSelectedEmployment")
        self.tabWidget.addTab(self.tabEmployment, "")
        self.tabLivestock = QtGui.QWidget()
        self.tabLivestock.setObjectName("tabLivestock")
        self.label_30 = QtGui.QLabel(self.tabLivestock)
        self.label_30.setGeometry(QtCore.QRect(20, 10, 181, 16))
        self.label_30.setObjectName("label_30")
        self.cmdLivestockRemoveSelected = QtGui.QPushButton(self.tabLivestock)
        self.cmdLivestockRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdLivestockRemoveSelected.setObjectName("cmdLivestockRemoveSelected")
        self.label_31 = QtGui.QLabel(self.tabLivestock)
        self.label_31.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_31.setObjectName("label_31")
        self.cmdLivestockRemoveAll = QtGui.QPushButton(self.tabLivestock)
        self.cmdLivestockRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdLivestockRemoveAll.setObjectName("cmdLivestockRemoveAll")
        self.cmdLivestockMoveSelected = QtGui.QPushButton(self.tabLivestock)
        self.cmdLivestockMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdLivestockMoveSelected.setObjectName("cmdLivestockMoveSelected")
        self.cmdLivestockMoveAll = QtGui.QPushButton(self.tabLivestock)
        self.cmdLivestockMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdLivestockMoveAll.setObjectName("cmdLivestockMoveAll")
        self.tblAvailableLivestock = QtGui.QTableView(self.tabLivestock)
        self.tblAvailableLivestock.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.tblAvailableLivestock.setObjectName("tblAvailableLivestock")
        self.tblSelectedLivestock = QtGui.QTableView(self.tabLivestock)
        self.tblSelectedLivestock.setGeometry(QtCore.QRect(370, 30, 256, 361))
        self.tblSelectedLivestock.setObjectName("tblSelectedLivestock")
        self.tabWidget.addTab(self.tabLivestock, "")
        self.tabTransfers = QtGui.QWidget()
        self.tabTransfers.setObjectName("tabTransfers")
        self.label_32 = QtGui.QLabel(self.tabTransfers)
        self.label_32.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_32.setObjectName("label_32")
        self.cmdTransfersMoveSelected = QtGui.QPushButton(self.tabTransfers)
        self.cmdTransfersMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdTransfersMoveSelected.setObjectName("cmdTransfersMoveSelected")
        self.label_33 = QtGui.QLabel(self.tabTransfers)
        self.label_33.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_33.setObjectName("label_33")
        self.cmdTransfersRemoveAll = QtGui.QPushButton(self.tabTransfers)
        self.cmdTransfersRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdTransfersRemoveAll.setObjectName("cmdTransfersRemoveAll")
        self.cmdTransfersMoveAll = QtGui.QPushButton(self.tabTransfers)
        self.cmdTransfersMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdTransfersMoveAll.setObjectName("cmdTransfersMoveAll")
        self.cmdTransfersRemoveSelected = QtGui.QPushButton(self.tabTransfers)
        self.cmdTransfersRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdTransfersRemoveSelected.setObjectName("cmdTransfersRemoveSelected")
        self.tblAvailableTransfers = QtGui.QTableView(self.tabTransfers)
        self.tblAvailableTransfers.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.tblAvailableTransfers.setObjectName("tblAvailableTransfers")
        self.tblSelectedTransfers = QtGui.QTableView(self.tabTransfers)
        self.tblSelectedTransfers.setGeometry(QtCore.QRect(370, 30, 256, 361))
        self.tblSelectedTransfers.setObjectName("tblSelectedTransfers")
        self.tabWidget.addTab(self.tabTransfers, "")
        self.tabWildFoods = QtGui.QWidget()
        self.tabWildFoods.setObjectName("tabWildFoods")
        self.label_34 = QtGui.QLabel(self.tabWildFoods)
        self.label_34.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_34.setObjectName("label_34")
        self.cmdWildfoodMoveSelected = QtGui.QPushButton(self.tabWildFoods)
        self.cmdWildfoodMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdWildfoodMoveSelected.setObjectName("cmdWildfoodMoveSelected")
        self.cmdWildfoodRemoveAll = QtGui.QPushButton(self.tabWildFoods)
        self.cmdWildfoodRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdWildfoodRemoveAll.setObjectName("cmdWildfoodRemoveAll")
        self.cmdWildfoodRemoveSelected = QtGui.QPushButton(self.tabWildFoods)
        self.cmdWildfoodRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdWildfoodRemoveSelected.setObjectName("cmdWildfoodRemoveSelected")
        self.cmdWildfoodMoveAll = QtGui.QPushButton(self.tabWildFoods)
        self.cmdWildfoodMoveAll.setGeometry(QtCore.QRect(280, 120, 81, 31))
        self.cmdWildfoodMoveAll.setObjectName("cmdWildfoodMoveAll")
        self.label_35 = QtGui.QLabel(self.tabWildFoods)
        self.label_35.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_35.setObjectName("label_35")
        self.tblAvailableWildfoods = QtGui.QTableView(self.tabWildFoods)
        self.tblAvailableWildfoods.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.tblAvailableWildfoods.setObjectName("tblAvailableWildfoods")
        self.tblSelectedWildfoods = QtGui.QTableView(self.tabWildFoods)
        self.tblSelectedWildfoods.setGeometry(QtCore.QRect(370, 30, 256, 361))
        self.tblSelectedWildfoods.setObjectName("tblSelectedWildfoods")
        self.tabWidget.addTab(self.tabWildFoods, "")
        self.tabProject.addTab(self.tabIncome, "")
        self.cmdClose = QtGui.QPushButton(ProjectConfiguration)
        self.cmdClose.setGeometry(QtCore.QRect(560, 500, 91, 31))
        self.cmdClose.setDefault(True)
        self.cmdClose.setObjectName("cmdClose")

        self.retranslateUi(ProjectConfiguration)
        self.tabProject.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectConfiguration)

    def retranslateUi(self, ProjectConfiguration):
        ProjectConfiguration.setWindowTitle(QtGui.QApplication.translate("ProjectConfiguration", "Project Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectConfiguration", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("ProjectConfiguration", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabProjectHouseholdCharacteristics), QtGui.QApplication.translate("ProjectConfiguration", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabProjectPersonalCharacteristics), QtGui.QApplication.translate("ProjectConfiguration", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelDiet.setText(QtGui.QApplication.translate("ProjectConfiguration", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProjectConfiguration", "Food Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ProjectConfiguration", "Unit Of Measure:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSaveDiet.setText(QtGui.QApplication.translate("ProjectConfiguration", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ProjectConfiguration", "Percentage:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ProjectConfiguration", "Price per Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab), QtGui.QApplication.translate("ProjectConfiguration", "Diet Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ProjectConfiguration", "Expense Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ProjectConfiguration", "Scope:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSaveLivingStanItem.setText(QtGui.QApplication.translate("ProjectConfiguration", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ProjectConfiguration", "Age Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ProjectConfiguration", "Gender:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ProjectConfiguration", "Cost per Year:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbScope.setItemText(0, QtGui.QApplication.translate("ProjectConfiguration", "Person", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbScope.setItemText(1, QtGui.QApplication.translate("ProjectConfiguration", "Household", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGender.setItemText(0, QtGui.QApplication.translate("ProjectConfiguration", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGender.setItemText(1, QtGui.QApplication.translate("ProjectConfiguration", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGender.setItemText(2, QtGui.QApplication.translate("ProjectConfiguration", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ProjectConfiguration", "to", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelLivingStandardItem.setText(QtGui.QApplication.translate("ProjectConfiguration", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tab_2), QtGui.QApplication.translate("ProjectConfiguration", "Standard of Living Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCropsRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCropsRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCropsMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCropsMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCrops), QtGui.QApplication.translate("ProjectConfiguration", "Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Employment Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEmploymentRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEmploymentMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEmploymentMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEmploymentRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Employment Types", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEmployment), QtGui.QApplication.translate("ProjectConfiguration", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Livestock & Livestock Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdLivestockRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Livestock & Livestock Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdLivestockRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdLivestockMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdLivestockMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLivestock), QtGui.QApplication.translate("ProjectConfiguration", "Livestock & Livestock Products", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Transfer Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdTransfersMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Transfer Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdTransfersRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdTransfersMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdTransfersRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTransfers), QtGui.QApplication.translate("ProjectConfiguration", "Transfers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdWildfoodMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdWildfoodRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdWildfoodRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdWildfoodMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Food Types", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWildFoods), QtGui.QApplication.translate("ProjectConfiguration", "Wild Foods", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabIncome), QtGui.QApplication.translate("ProjectConfiguration", "Income Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("ProjectConfiguration", "Close", None, QtGui.QApplication.UnicodeUTF8))

