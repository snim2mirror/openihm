# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manageincomedetails.ui'
#
# Created: Fri Apr 22 21:52:29 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManageIncome(object):
    def setupUi(self, ManageIncome):
        ManageIncome.setObjectName(_fromUtf8("ManageIncome"))
        ManageIncome.resize(623, 394)
        ManageIncome.setMinimumSize(QtCore.QSize(611, 380))
        self.tabWidget = QtGui.QTabWidget(ManageIncome)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 611, 341))
        self.tabWidget.setMinimumSize(QtCore.QSize(611, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabIncomeCrops = QtGui.QWidget()
        self.tabIncomeCrops.setObjectName(_fromUtf8("tabIncomeCrops"))
        self.label_26 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_26.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_3 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_3.setGeometry(QtCore.QRect(280, 90, 91, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnCropDelete = QtGui.QPushButton(self.tabIncomeCrops)
        self.btnCropDelete.setGeometry(QtCore.QRect(510, 210, 80, 28))
        self.btnCropDelete.setObjectName(_fromUtf8("btnCropDelete"))
        self.btnCropSave = QtGui.QPushButton(self.tabIncomeCrops)
        self.btnCropSave.setGeometry(QtCore.QRect(300, 210, 80, 28))
        self.btnCropSave.setObjectName(_fromUtf8("btnCropSave"))
        self.label_4 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 54, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_6.setGeometry(QtCore.QRect(280, 140, 101, 18))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_25 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_25.setGeometry(QtCore.QRect(280, 10, 241, 18))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.txtCropTypeName = QtGui.QLineEdit(self.tabIncomeCrops)
        self.txtCropTypeName.setGeometry(QtCore.QRect(370, 40, 211, 28))
        self.txtCropTypeName.setObjectName(_fromUtf8("txtCropTypeName"))
        self.txtEnergyValue = QtGui.QLineEdit(self.tabIncomeCrops)
        self.txtEnergyValue.setGeometry(QtCore.QRect(370, 130, 211, 31))
        self.txtEnergyValue.setObjectName(_fromUtf8("txtEnergyValue"))
        self.txtMeasuringUnit = QtGui.QLineEdit(self.tabIncomeCrops)
        self.txtMeasuringUnit.setGeometry(QtCore.QRect(370, 80, 211, 31))
        self.txtMeasuringUnit.setObjectName(_fromUtf8("txtMeasuringUnit"))
        self.cropListView = QtGui.QListView(self.tabIncomeCrops)
        self.cropListView.setGeometry(QtCore.QRect(5, 40, 251, 192))
        self.cropListView.setAlternatingRowColors(True)
        self.cropListView.setObjectName(_fromUtf8("cropListView"))
        self.btnCropsClear = QtGui.QPushButton(self.tabIncomeCrops)
        self.btnCropsClear.setGeometry(QtCore.QRect(410, 210, 81, 28))
        self.btnCropsClear.setObjectName(_fromUtf8("btnCropsClear"))
        self.tabWidget.addTab(self.tabIncomeCrops, _fromUtf8(""))
        self.tabEmployment = QtGui.QWidget()
        self.tabEmployment.setObjectName(_fromUtf8("tabEmployment"))
        self.btnEmplomentTypeSave = QtGui.QPushButton(self.tabEmployment)
        self.btnEmplomentTypeSave.setGeometry(QtCore.QRect(360, 200, 80, 28))
        self.btnEmplomentTypeSave.setObjectName(_fromUtf8("btnEmplomentTypeSave"))
        self.label_15 = QtGui.QLabel(self.tabEmployment)
        self.label_15.setGeometry(QtCore.QRect(260, 40, 111, 18))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.btnEmplomentTypeDelete = QtGui.QPushButton(self.tabEmployment)
        self.btnEmplomentTypeDelete.setGeometry(QtCore.QRect(480, 200, 80, 28))
        self.btnEmplomentTypeDelete.setObjectName(_fromUtf8("btnEmplomentTypeDelete"))
        self.label_33 = QtGui.QLabel(self.tabEmployment)
        self.label_33.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.txtEmploymentType = QtGui.QLineEdit(self.tabEmployment)
        self.txtEmploymentType.setGeometry(QtCore.QRect(370, 40, 191, 28))
        self.txtEmploymentType.setObjectName(_fromUtf8("txtEmploymentType"))
        self.label_34 = QtGui.QLabel(self.tabEmployment)
        self.label_34.setGeometry(QtCore.QRect(260, 10, 241, 18))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.employmentListView = QtGui.QListView(self.tabEmployment)
        self.employmentListView.setGeometry(QtCore.QRect(5, 40, 241, 192))
        self.employmentListView.setAlternatingRowColors(True)
        self.employmentListView.setObjectName(_fromUtf8("employmentListView"))
        self.tabWidget.addTab(self.tabEmployment, _fromUtf8(""))
        self.tabIncomeLivestock = QtGui.QWidget()
        self.tabIncomeLivestock.setObjectName(_fromUtf8("tabIncomeLivestock"))
        self.label_7 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_7.setGeometry(QtCore.QRect(280, 110, 91, 18))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_27 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_27.setGeometry(QtCore.QRect(280, 10, 271, 18))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.btnLivestockSave = QtGui.QPushButton(self.tabIncomeLivestock)
        self.btnLivestockSave.setGeometry(QtCore.QRect(300, 240, 81, 28))
        self.btnLivestockSave.setObjectName(_fromUtf8("btnLivestockSave"))
        self.label_28 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_28.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_8 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_8.setGeometry(QtCore.QRect(280, 50, 54, 18))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_9.setGeometry(QtCore.QRect(280, 160, 101, 18))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.btnLivestockDelete = QtGui.QPushButton(self.tabIncomeLivestock)
        self.btnLivestockDelete.setGeometry(QtCore.QRect(500, 240, 81, 28))
        self.btnLivestockDelete.setObjectName(_fromUtf8("btnLivestockDelete"))
        self.txtLivestockPType = QtGui.QLineEdit(self.tabIncomeLivestock)
        self.txtLivestockPType.setGeometry(QtCore.QRect(360, 50, 211, 31))
        self.txtLivestockPType.setObjectName(_fromUtf8("txtLivestockPType"))
        self.txtLivestockUnit = QtGui.QLineEdit(self.tabIncomeLivestock)
        self.txtLivestockUnit.setGeometry(QtCore.QRect(360, 100, 211, 31))
        self.txtLivestockUnit.setObjectName(_fromUtf8("txtLivestockUnit"))
        self.txtLivestockEnergyValue = QtGui.QLineEdit(self.tabIncomeLivestock)
        self.txtLivestockEnergyValue.setGeometry(QtCore.QRect(360, 150, 211, 31))
        self.txtLivestockEnergyValue.setObjectName(_fromUtf8("txtLivestockEnergyValue"))
        self.livestockListView = QtGui.QListView(self.tabIncomeLivestock)
        self.livestockListView.setGeometry(QtCore.QRect(5, 40, 251, 192))
        self.livestockListView.setAlternatingRowColors(True)
        self.livestockListView.setObjectName(_fromUtf8("livestockListView"))
        self.btnLivestockClear = QtGui.QPushButton(self.tabIncomeLivestock)
        self.btnLivestockClear.setGeometry(QtCore.QRect(400, 240, 81, 28))
        self.btnLivestockClear.setObjectName(_fromUtf8("btnLivestockClear"))
        self.tabWidget.addTab(self.tabIncomeLivestock, _fromUtf8(""))
        self.tabIncomeTransfers = QtGui.QWidget()
        self.tabIncomeTransfers.setObjectName(_fromUtf8("tabIncomeTransfers"))
        self.tabTransferDetails = QtGui.QTabWidget(self.tabIncomeTransfers)
        self.tabTransferDetails.setGeometry(QtCore.QRect(0, 10, 601, 301))
        self.tabTransferDetails.setObjectName(_fromUtf8("tabTransferDetails"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_32 = QtGui.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(300, 10, 271, 18))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.transferTypesListView = QtGui.QListView(self.tab)
        self.transferTypesListView.setGeometry(QtCore.QRect(5, 40, 241, 192))
        self.transferTypesListView.setAlternatingRowColors(True)
        self.transferTypesListView.setObjectName(_fromUtf8("transferTypesListView"))
        self.btnTransferTypeDelete = QtGui.QPushButton(self.tab)
        self.btnTransferTypeDelete.setGeometry(QtCore.QRect(480, 140, 80, 28))
        self.btnTransferTypeDelete.setObjectName(_fromUtf8("btnTransferTypeDelete"))
        self.label_31 = QtGui.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.btnTransferTypeSave = QtGui.QPushButton(self.tab)
        self.btnTransferTypeSave.setGeometry(QtCore.QRect(280, 140, 80, 28))
        self.btnTransferTypeSave.setObjectName(_fromUtf8("btnTransferTypeSave"))
        self.txtTransferType = QtGui.QLineEdit(self.tab)
        self.txtTransferType.setGeometry(QtCore.QRect(340, 40, 221, 28))
        self.txtTransferType.setObjectName(_fromUtf8("txtTransferType"))
        self.txtTransferUnitofMeasure = QtGui.QLineEdit(self.tab)
        self.txtTransferUnitofMeasure.setGeometry(QtCore.QRect(340, 90, 221, 28))
        self.txtTransferUnitofMeasure.setObjectName(_fromUtf8("txtTransferUnitofMeasure"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 100, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(260, 50, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabTransferDetails.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_35 = QtGui.QLabel(self.tab_3)
        self.label_35.setGeometry(QtCore.QRect(280, 10, 271, 18))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.transferSourcesListView = QtGui.QListView(self.tab_3)
        self.transferSourcesListView.setGeometry(QtCore.QRect(5, 40, 251, 192))
        self.transferSourcesListView.setAlternatingRowColors(True)
        self.transferSourcesListView.setObjectName(_fromUtf8("transferSourcesListView"))
        self.btnTransferSourcesDelete = QtGui.QPushButton(self.tab_3)
        self.btnTransferSourcesDelete.setGeometry(QtCore.QRect(480, 120, 80, 28))
        self.btnTransferSourcesDelete.setObjectName(_fromUtf8("btnTransferSourcesDelete"))
        self.label_36 = QtGui.QLabel(self.tab_3)
        self.label_36.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.btnTransferSourcesSave = QtGui.QPushButton(self.tab_3)
        self.btnTransferSourcesSave.setGeometry(QtCore.QRect(280, 120, 80, 28))
        self.btnTransferSourcesSave.setObjectName(_fromUtf8("btnTransferSourcesSave"))
        self.txtTransferSources = QtGui.QLineEdit(self.tab_3)
        self.txtTransferSources.setGeometry(QtCore.QRect(280, 40, 281, 28))
        self.txtTransferSources.setObjectName(_fromUtf8("txtTransferSources"))
        self.tabTransferDetails.addTab(self.tab_3, _fromUtf8(""))
        self.tabWidget.addTab(self.tabIncomeTransfers, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(280, 110, 91, 18))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_29 = QtGui.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(280, 10, 241, 18))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.btnWildFoodSave = QtGui.QPushButton(self.tab_2)
        self.btnWildFoodSave.setGeometry(QtCore.QRect(300, 240, 80, 28))
        self.btnWildFoodSave.setObjectName(_fromUtf8("btnWildFoodSave"))
        self.label_30 = QtGui.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(280, 50, 54, 18))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(280, 160, 101, 18))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.btnWildFoodDelete = QtGui.QPushButton(self.tab_2)
        self.btnWildFoodDelete.setGeometry(QtCore.QRect(500, 240, 80, 28))
        self.btnWildFoodDelete.setObjectName(_fromUtf8("btnWildFoodDelete"))
        self.txtWildFoodType = QtGui.QLineEdit(self.tab_2)
        self.txtWildFoodType.setGeometry(QtCore.QRect(360, 50, 211, 31))
        self.txtWildFoodType.setObjectName(_fromUtf8("txtWildFoodType"))
        self.txtWildFoodUnit = QtGui.QLineEdit(self.tab_2)
        self.txtWildFoodUnit.setGeometry(QtCore.QRect(360, 100, 211, 31))
        self.txtWildFoodUnit.setObjectName(_fromUtf8("txtWildFoodUnit"))
        self.txtWildFoodEnergyValue = QtGui.QLineEdit(self.tab_2)
        self.txtWildFoodEnergyValue.setGeometry(QtCore.QRect(360, 150, 211, 31))
        self.txtWildFoodEnergyValue.setObjectName(_fromUtf8("txtWildFoodEnergyValue"))
        self.wildFoodsListView = QtGui.QListView(self.tab_2)
        self.wildFoodsListView.setGeometry(QtCore.QRect(5, 50, 251, 192))
        self.wildFoodsListView.setAlternatingRowColors(True)
        self.wildFoodsListView.setObjectName(_fromUtf8("wildFoodsListView"))
        self.btnWildFoodsClear = QtGui.QPushButton(self.tab_2)
        self.btnWildFoodsClear.setGeometry(QtCore.QRect(400, 240, 81, 28))
        self.btnWildFoodsClear.setObjectName(_fromUtf8("btnWildFoodsClear"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.btnManageIncomeClose = QtGui.QPushButton(ManageIncome)
        self.btnManageIncomeClose.setGeometry(QtCore.QRect(530, 350, 80, 28))
        self.btnManageIncomeClose.setObjectName(_fromUtf8("btnManageIncomeClose"))
        self.label_26.setBuddy(self.cropListView)
        self.label_3.setBuddy(self.txtMeasuringUnit)
        self.label_4.setBuddy(self.txtCropTypeName)
        self.label_6.setBuddy(self.txtEnergyValue)

        self.retranslateUi(ManageIncome)
        self.tabWidget.setCurrentIndex(0)
        self.tabTransferDetails.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnManageIncomeClose, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.mdiClose)
        QtCore.QObject.connect(self.btnCropSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.saveCropType)
        QtCore.QObject.connect(self.btnCropsClear, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.clearCropTextboxes)
        QtCore.QObject.connect(self.btnCropDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.deleteCropType)
        QtCore.QObject.connect(self.cropListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageIncome.pickselectedCropItem)
        QtCore.QObject.connect(self.employmentListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageIncome.pickSelectedEmployment)
        QtCore.QObject.connect(self.btnEmplomentTypeSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.saveEmploymentType)
        QtCore.QObject.connect(self.btnEmplomentTypeDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.deleteEmploymentType)
        QtCore.QObject.connect(self.livestockListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageIncome.pickselectedLivestockItem)
        QtCore.QObject.connect(self.btnLivestockSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.saveLivestockType)
        QtCore.QObject.connect(self.btnLivestockClear, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.clearLivestockTextboxes)
        QtCore.QObject.connect(self.btnLivestockDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.deleteLivestockType)
        QtCore.QObject.connect(self.transferTypesListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageIncome.pickSelectedTransfer)
        QtCore.QObject.connect(self.btnTransferTypeSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.saveTransferType)
        QtCore.QObject.connect(self.btnTransferTypeDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.deleteTransferType)
        QtCore.QObject.connect(self.wildFoodsListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageIncome.pickselectedWildFoodItem)
        QtCore.QObject.connect(self.btnWildFoodSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.saveWildFoodType)
        QtCore.QObject.connect(self.btnWildFoodDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.deleteWildFoodType)
        QtCore.QObject.connect(self.btnWildFoodsClear, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.clearWildFoodTextboxes)
        QtCore.QObject.connect(self.transferSourcesListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageIncome.pickSelectedTransferSource)
        QtCore.QObject.connect(self.btnTransferSourcesSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.saveTransferSourceType)
        QtCore.QObject.connect(self.btnTransferSourcesDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageIncome.deleteTransferSourceType)
        QtCore.QMetaObject.connectSlotsByName(ManageIncome)

    def retranslateUi(self, ManageIncome):
        ManageIncome.setWindowTitle(QtGui.QApplication.translate("ManageIncome", "Manage Income Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ManageIncome", "Select Crop Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCropDelete.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCropSave.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageIncome", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ManageIncome", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Crop Details", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCropsClear.setText(QtGui.QApplication.translate("ManageIncome", "Clear Text", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomeCrops), QtGui.QApplication.translate("ManageIncome", "Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEmplomentTypeSave.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ManageIncome", "Employment Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEmplomentTypeDelete.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("ManageIncome", "Select Employment Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Employment Types Details", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEmployment), QtGui.QApplication.translate("ManageIncome", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Livestock/Livestock Products Details", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLivestockSave.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("ManageIncome", "Select Livestock/Livestock Product", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ManageIncome", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ManageIncome", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLivestockDelete.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLivestockClear.setText(QtGui.QApplication.translate("ManageIncome", "Clear Text", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomeLivestock), QtGui.QApplication.translate("ManageIncome", "Livestock and Livestock Products", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Transfer Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransferTypeDelete.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("ManageIncome", "Select Transfer Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransferTypeSave.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageIncome", "Transfer Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTransferDetails.setTabText(self.tabTransferDetails.indexOf(self.tab), QtGui.QApplication.translate("ManageIncome", "Assistance Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Transfer Source", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransferSourcesDelete.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("ManageIncome", "Select Transfer Source", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransferSourcesSave.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.txtTransferSources.setToolTip(QtGui.QApplication.translate("ManageIncome", "Transfer Source should be \'Internal\' or \'External\'", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTransferDetails.setTabText(self.tabTransferDetails.indexOf(self.tab_3), QtGui.QApplication.translate("ManageIncome", "Assistance Source(External or Internal?)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomeTransfers), QtGui.QApplication.translate("ManageIncome", "Transfers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Foods Details", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWildFoodSave.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("ManageIncome", "Select Food Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManageIncome", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ManageIncome", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWildFoodDelete.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWildFoodsClear.setText(QtGui.QApplication.translate("ManageIncome", "Clear Text", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ManageIncome", "Wild Foods, Hunting, Fishing", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageIncomeClose.setText(QtGui.QApplication.translate("ManageIncome", "Close", None, QtGui.QApplication.UnicodeUTF8))

