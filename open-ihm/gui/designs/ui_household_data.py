# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_data.ui'
#
# Created: Fri Apr 22 21:52:27 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HouseholdData(object):
    def setupUi(self, HouseholdData):
        HouseholdData.setObjectName(_fromUtf8("HouseholdData"))
        HouseholdData.resize(797, 620)
        HouseholdData.setMinimumSize(QtCore.QSize(797, 620))
        self.tabHouseHold = QtGui.QTabWidget(HouseholdData)
        self.tabHouseHold.setGeometry(QtCore.QRect(10, 40, 781, 531))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabHouseHold.setFont(font)
        self.tabHouseHold.setObjectName(_fromUtf8("tabHouseHold"))
        self.tabHouseHoldMembers = QtGui.QWidget()
        self.tabHouseHoldMembers.setObjectName(_fromUtf8("tabHouseHoldMembers"))
        self.tblMembers = QtGui.QTableView(self.tabHouseHoldMembers)
        self.tblMembers.setGeometry(QtCore.QRect(10, 30, 371, 431))
        self.tblMembers.setAlternatingRowColors(True)
        self.tblMembers.setSortingEnabled(True)
        self.tblMembers.setObjectName(_fromUtf8("tblMembers"))
        self.cmdAddMember = QtGui.QPushButton(self.tabHouseHoldMembers)
        self.cmdAddMember.setGeometry(QtCore.QRect(10, 470, 91, 31))
        self.cmdAddMember.setObjectName(_fromUtf8("cmdAddMember"))
        self.cmdEditMember = QtGui.QPushButton(self.tabHouseHoldMembers)
        self.cmdEditMember.setGeometry(QtCore.QRect(110, 470, 91, 31))
        self.cmdEditMember.setObjectName(_fromUtf8("cmdEditMember"))
        self.cmdDelMember = QtGui.QPushButton(self.tabHouseHoldMembers)
        self.cmdDelMember.setGeometry(QtCore.QRect(210, 470, 91, 31))
        self.cmdDelMember.setObjectName(_fromUtf8("cmdDelMember"))
        self.tblPersonalCharacteristics = QtGui.QTableView(self.tabHouseHoldMembers)
        self.tblPersonalCharacteristics.setGeometry(QtCore.QRect(390, 30, 371, 431))
        self.tblPersonalCharacteristics.setAlternatingRowColors(True)
        self.tblPersonalCharacteristics.setSortingEnabled(True)
        self.tblPersonalCharacteristics.setObjectName(_fromUtf8("tblPersonalCharacteristics"))
        self.cmdEditPersonalCharacteristic = QtGui.QPushButton(self.tabHouseHoldMembers)
        self.cmdEditPersonalCharacteristic.setGeometry(QtCore.QRect(390, 470, 141, 31))
        self.cmdEditPersonalCharacteristic.setObjectName(_fromUtf8("cmdEditPersonalCharacteristic"))
        self.label_8 = QtGui.QLabel(self.tabHouseHoldMembers)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblPersonalCharacteristicsHeader = QtGui.QLabel(self.tabHouseHoldMembers)
        self.lblPersonalCharacteristicsHeader.setGeometry(QtCore.QRect(400, 10, 231, 16))
        self.lblPersonalCharacteristicsHeader.setObjectName(_fromUtf8("lblPersonalCharacteristicsHeader"))
        self.tabHouseHold.addTab(self.tabHouseHoldMembers, _fromUtf8(""))
        self.tabHouseholdAssets = QtGui.QWidget()
        self.tabHouseholdAssets.setObjectName(_fromUtf8("tabHouseholdAssets"))
        self.tblAssets = QtGui.QTableView(self.tabHouseholdAssets)
        self.tblAssets.setGeometry(QtCore.QRect(10, 10, 751, 451))
        self.tblAssets.setAlternatingRowColors(True)
        self.tblAssets.setSortingEnabled(True)
        self.tblAssets.setObjectName(_fromUtf8("tblAssets"))
        self.cmdAddAsset = QtGui.QPushButton(self.tabHouseholdAssets)
        self.cmdAddAsset.setGeometry(QtCore.QRect(10, 470, 91, 31))
        self.cmdAddAsset.setObjectName(_fromUtf8("cmdAddAsset"))
        self.cmdEditAsset = QtGui.QPushButton(self.tabHouseholdAssets)
        self.cmdEditAsset.setGeometry(QtCore.QRect(110, 470, 91, 31))
        self.cmdEditAsset.setObjectName(_fromUtf8("cmdEditAsset"))
        self.cmdDelAsset = QtGui.QPushButton(self.tabHouseholdAssets)
        self.cmdDelAsset.setGeometry(QtCore.QRect(210, 470, 91, 31))
        self.cmdDelAsset.setObjectName(_fromUtf8("cmdDelAsset"))
        self.tabHouseHold.addTab(self.tabHouseholdAssets, _fromUtf8(""))
        self.tabHouseholdIncome = QtGui.QWidget()
        self.tabHouseholdIncome.setObjectName(_fromUtf8("tabHouseholdIncome"))
        self.tabWidget = QtGui.QTabWidget(self.tabHouseholdIncome)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 751, 491))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.cmdAddCrop = QtGui.QPushButton(self.tab)
        self.cmdAddCrop.setGeometry(QtCore.QRect(20, 450, 91, 31))
        self.cmdAddCrop.setObjectName(_fromUtf8("cmdAddCrop"))
        self.cmdEditCrop = QtGui.QPushButton(self.tab)
        self.cmdEditCrop.setGeometry(QtCore.QRect(120, 450, 91, 31))
        self.cmdEditCrop.setObjectName(_fromUtf8("cmdEditCrop"))
        self.cmdDelCrop = QtGui.QPushButton(self.tab)
        self.cmdDelCrop.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.cmdDelCrop.setObjectName(_fromUtf8("cmdDelCrop"))
        self.tblCropIncome = QtGui.QTableView(self.tab)
        self.tblCropIncome.setGeometry(QtCore.QRect(10, 40, 701, 401))
        self.tblCropIncome.setAlternatingRowColors(True)
        self.tblCropIncome.setSortingEnabled(True)
        self.tblCropIncome.setObjectName(_fromUtf8("tblCropIncome"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 161, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tblLivestockIncome = QtGui.QTableView(self.tab_2)
        self.tblLivestockIncome.setGeometry(QtCore.QRect(10, 40, 701, 401))
        self.tblLivestockIncome.setAlternatingRowColors(True)
        self.tblLivestockIncome.setSortingEnabled(True)
        self.tblLivestockIncome.setObjectName(_fromUtf8("tblLivestockIncome"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 121, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cmdEditLivestock = QtGui.QPushButton(self.tab_2)
        self.cmdEditLivestock.setGeometry(QtCore.QRect(120, 450, 91, 31))
        self.cmdEditLivestock.setObjectName(_fromUtf8("cmdEditLivestock"))
        self.cmdDelLivestock = QtGui.QPushButton(self.tab_2)
        self.cmdDelLivestock.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.cmdDelLivestock.setObjectName(_fromUtf8("cmdDelLivestock"))
        self.cmdAddLivestock = QtGui.QPushButton(self.tab_2)
        self.cmdAddLivestock.setGeometry(QtCore.QRect(20, 450, 91, 31))
        self.cmdAddLivestock.setObjectName(_fromUtf8("cmdAddLivestock"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 121, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tblEmploymentIncome = QtGui.QTableView(self.tab_3)
        self.tblEmploymentIncome.setGeometry(QtCore.QRect(10, 40, 701, 401))
        self.tblEmploymentIncome.setAlternatingRowColors(True)
        self.tblEmploymentIncome.setSortingEnabled(True)
        self.tblEmploymentIncome.setObjectName(_fromUtf8("tblEmploymentIncome"))
        self.cmdEditEmployment = QtGui.QPushButton(self.tab_3)
        self.cmdEditEmployment.setGeometry(QtCore.QRect(120, 450, 91, 31))
        self.cmdEditEmployment.setObjectName(_fromUtf8("cmdEditEmployment"))
        self.cmdDelEmployment = QtGui.QPushButton(self.tab_3)
        self.cmdDelEmployment.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.cmdDelEmployment.setObjectName(_fromUtf8("cmdDelEmployment"))
        self.cmdAddEmployment = QtGui.QPushButton(self.tab_3)
        self.cmdAddEmployment.setGeometry(QtCore.QRect(20, 450, 91, 31))
        self.cmdAddEmployment.setObjectName(_fromUtf8("cmdAddEmployment"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_5 = QtGui.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 151, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tblWildfoodsIncome = QtGui.QTableView(self.tab_4)
        self.tblWildfoodsIncome.setGeometry(QtCore.QRect(10, 40, 701, 401))
        self.tblWildfoodsIncome.setAlternatingRowColors(True)
        self.tblWildfoodsIncome.setSortingEnabled(True)
        self.tblWildfoodsIncome.setObjectName(_fromUtf8("tblWildfoodsIncome"))
        self.cmdEditWildfoods = QtGui.QPushButton(self.tab_4)
        self.cmdEditWildfoods.setGeometry(QtCore.QRect(120, 450, 91, 31))
        self.cmdEditWildfoods.setObjectName(_fromUtf8("cmdEditWildfoods"))
        self.cmdDelWildfoods = QtGui.QPushButton(self.tab_4)
        self.cmdDelWildfoods.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.cmdDelWildfoods.setObjectName(_fromUtf8("cmdDelWildfoods"))
        self.cmdAddWildfoods = QtGui.QPushButton(self.tab_4)
        self.cmdAddWildfoods.setGeometry(QtCore.QRect(20, 450, 91, 31))
        self.cmdAddWildfoods.setObjectName(_fromUtf8("cmdAddWildfoods"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 121, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tblGiftsIncome = QtGui.QTableView(self.tab_5)
        self.tblGiftsIncome.setGeometry(QtCore.QRect(10, 40, 701, 401))
        self.tblGiftsIncome.setAlternatingRowColors(True)
        self.tblGiftsIncome.setSortingEnabled(True)
        self.tblGiftsIncome.setObjectName(_fromUtf8("tblGiftsIncome"))
        self.cmdEditGifts = QtGui.QPushButton(self.tab_5)
        self.cmdEditGifts.setGeometry(QtCore.QRect(120, 450, 91, 31))
        self.cmdEditGifts.setObjectName(_fromUtf8("cmdEditGifts"))
        self.cmdDelGifts = QtGui.QPushButton(self.tab_5)
        self.cmdDelGifts.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.cmdDelGifts.setObjectName(_fromUtf8("cmdDelGifts"))
        self.cmdAddGifts = QtGui.QPushButton(self.tab_5)
        self.cmdAddGifts.setGeometry(QtCore.QRect(20, 450, 91, 31))
        self.cmdAddGifts.setObjectName(_fromUtf8("cmdAddGifts"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.label_7 = QtGui.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 221, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tblTransferIncome = QtGui.QTableView(self.tab_6)
        self.tblTransferIncome.setGeometry(QtCore.QRect(10, 40, 701, 401))
        self.tblTransferIncome.setAlternatingRowColors(True)
        self.tblTransferIncome.setSortingEnabled(True)
        self.tblTransferIncome.setObjectName(_fromUtf8("tblTransferIncome"))
        self.cmdEditTransfer = QtGui.QPushButton(self.tab_6)
        self.cmdEditTransfer.setGeometry(QtCore.QRect(120, 450, 91, 31))
        self.cmdEditTransfer.setObjectName(_fromUtf8("cmdEditTransfer"))
        self.cmdDelTransfer = QtGui.QPushButton(self.tab_6)
        self.cmdDelTransfer.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.cmdDelTransfer.setObjectName(_fromUtf8("cmdDelTransfer"))
        self.cmdAddTransfer = QtGui.QPushButton(self.tab_6)
        self.cmdAddTransfer.setGeometry(QtCore.QRect(20, 450, 91, 31))
        self.cmdAddTransfer.setObjectName(_fromUtf8("cmdAddTransfer"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tabHouseHold.addTab(self.tabHouseholdIncome, _fromUtf8(""))
        self.tabHouseholdExpenditure = QtGui.QWidget()
        self.tabHouseholdExpenditure.setObjectName(_fromUtf8("tabHouseholdExpenditure"))
        self.tblExpenditure = QtGui.QTableView(self.tabHouseholdExpenditure)
        self.tblExpenditure.setGeometry(QtCore.QRect(10, 10, 751, 451))
        self.tblExpenditure.setAlternatingRowColors(True)
        self.tblExpenditure.setSortingEnabled(True)
        self.tblExpenditure.setObjectName(_fromUtf8("tblExpenditure"))
        self.cmdAddExpenditure = QtGui.QPushButton(self.tabHouseholdExpenditure)
        self.cmdAddExpenditure.setGeometry(QtCore.QRect(10, 470, 91, 31))
        self.cmdAddExpenditure.setObjectName(_fromUtf8("cmdAddExpenditure"))
        self.cmdEditExpenditure = QtGui.QPushButton(self.tabHouseholdExpenditure)
        self.cmdEditExpenditure.setGeometry(QtCore.QRect(110, 470, 91, 31))
        self.cmdEditExpenditure.setObjectName(_fromUtf8("cmdEditExpenditure"))
        self.cmdDelExpenditure = QtGui.QPushButton(self.tabHouseholdExpenditure)
        self.cmdDelExpenditure.setGeometry(QtCore.QRect(210, 470, 91, 31))
        self.cmdDelExpenditure.setObjectName(_fromUtf8("cmdDelExpenditure"))
        self.tabHouseHold.addTab(self.tabHouseholdExpenditure, _fromUtf8(""))
        self.tabHouseholdCharacteristics = QtGui.QWidget()
        self.tabHouseholdCharacteristics.setObjectName(_fromUtf8("tabHouseholdCharacteristics"))
        self.tblCharacteristics = QtGui.QTableView(self.tabHouseholdCharacteristics)
        self.tblCharacteristics.setGeometry(QtCore.QRect(10, 10, 751, 451))
        self.tblCharacteristics.setAlternatingRowColors(True)
        self.tblCharacteristics.setSortingEnabled(True)
        self.tblCharacteristics.setObjectName(_fromUtf8("tblCharacteristics"))
        self.cmdEditCharacteristic = QtGui.QPushButton(self.tabHouseholdCharacteristics)
        self.cmdEditCharacteristic.setGeometry(QtCore.QRect(10, 470, 91, 31))
        self.cmdEditCharacteristic.setObjectName(_fromUtf8("cmdEditCharacteristic"))
        self.tabHouseHold.addTab(self.tabHouseholdCharacteristics, _fromUtf8(""))
        self.cmdClose = QtGui.QPushButton(HouseholdData)
        self.cmdClose.setGeometry(QtCore.QRect(694, 580, 91, 31))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.cboHouseholdNumber = QtGui.QComboBox(HouseholdData)
        self.cboHouseholdNumber.setGeometry(QtCore.QRect(140, 10, 221, 22))
        self.cboHouseholdNumber.setObjectName(_fromUtf8("cboHouseholdNumber"))
        self.label = QtGui.QLabel(HouseholdData)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setBuddy(self.cboHouseholdNumber)

        self.retranslateUi(HouseholdData)
        self.tabHouseHold.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QObject.connect(self.cmdClose, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.mdiClose)
        QtCore.QObject.connect(self.cmdAddMember, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdMember)
        QtCore.QObject.connect(self.cmdEditMember, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdMember)
        QtCore.QObject.connect(self.cmdDelMember, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdMembers)
        QtCore.QObject.connect(self.cmdEditPersonalCharacteristic, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editPersonalCharacteristic)
        QtCore.QObject.connect(self.cmdAddAsset, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdAsset)
        QtCore.QObject.connect(self.cmdEditAsset, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdAsset)
        QtCore.QObject.connect(self.cmdDelAsset, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdAssets)
        QtCore.QObject.connect(self.cmdAddCrop, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdCropIncome)
        QtCore.QObject.connect(self.cmdEditCrop, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdCropIncome)
        QtCore.QObject.connect(self.cmdDelCrop, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdCropIncome)
        QtCore.QObject.connect(self.cmdAddLivestock, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdLivestockIncome)
        QtCore.QObject.connect(self.cmdEditLivestock, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdLivestockIncome)
        QtCore.QObject.connect(self.cmdDelLivestock, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdLivestockIncome)
        QtCore.QObject.connect(self.cmdAddEmployment, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdEmploymentIncome)
        QtCore.QObject.connect(self.cmdEditEmployment, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdEmploymentIncome)
        QtCore.QObject.connect(self.cmdDelEmployment, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdEmploymentIncome)
        QtCore.QObject.connect(self.cmdAddWildfoods, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdWildfoodsIncome)
        QtCore.QObject.connect(self.cmdEditWildfoods, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdWildfoodsIncome)
        QtCore.QObject.connect(self.cmdDelWildfoods, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdWildfoodsIncome)
        QtCore.QObject.connect(self.cmdAddGifts, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdTransferIncome)
        QtCore.QObject.connect(self.cmdEditGifts, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdTransferIncome)
        QtCore.QObject.connect(self.cmdDelGifts, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdTransferIncome)
        QtCore.QObject.connect(self.cmdAddTransfer, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdTransferIncome)
        QtCore.QObject.connect(self.cmdEditTransfer, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdTransferIncome)
        QtCore.QObject.connect(self.cmdDelTransfer, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdTransferIncome)
        QtCore.QObject.connect(self.cmdAddExpenditure, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.addHouseholdExpenditure)
        QtCore.QObject.connect(self.cmdEditExpenditure, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editHouseholdExpenditure)
        QtCore.QObject.connect(self.cmdDelExpenditure, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.delHouseholdExpenses)
        QtCore.QObject.connect(self.cmdEditCharacteristic, QtCore.SIGNAL(_fromUtf8("clicked()")), HouseholdData.editCharacteristic)
        QtCore.QObject.connect(self.tblMembers, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), HouseholdData.showMemberPersonalCharacteristics)
        QtCore.QObject.connect(self.cboHouseholdNumber, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), HouseholdData.displayHouseholdData)
        QtCore.QMetaObject.connectSlotsByName(HouseholdData)

    def retranslateUi(self, HouseholdData):
        HouseholdData.setWindowTitle(QtGui.QApplication.translate("HouseholdData", "Household Data", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddMember.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditMember.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelMember.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditPersonalCharacteristic.setText(QtGui.QApplication.translate("HouseholdData", "Edit Characteristic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("HouseholdData", "Household Members", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPersonalCharacteristicsHeader.setText(QtGui.QApplication.translate("HouseholdData", "Personal Characteristics:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabHouseHold.setTabText(self.tabHouseHold.indexOf(self.tabHouseHoldMembers), QtGui.QApplication.translate("HouseholdData", "Members", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddAsset.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditAsset.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelAsset.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabHouseHold.setTabText(self.tabHouseHold.indexOf(self.tabHouseholdAssets), QtGui.QApplication.translate("HouseholdData", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddCrop.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditCrop.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelCrop.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HouseholdData", "Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("HouseholdData", "Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HouseholdData", "Livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditLivestock.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelLivestock.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddLivestock.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("HouseholdData", "Livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("HouseholdData", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditEmployment.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelEmployment.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddEmployment.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("HouseholdData", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("HouseholdData", "Wildfoods and Hunting", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditWildfoods.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelWildfoods.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddWildfoods.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("HouseholdData", "Wildfoods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("HouseholdData", "Transfers", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditGifts.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelGifts.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddGifts.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("HouseholdData", "Transfers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("HouseholdData", "Transfers from Organisations", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditTransfer.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelTransfer.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddTransfer.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("HouseholdData", "Transfers From Orgs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabHouseHold.setTabText(self.tabHouseHold.indexOf(self.tabHouseholdIncome), QtGui.QApplication.translate("HouseholdData", "Income", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddExpenditure.setText(QtGui.QApplication.translate("HouseholdData", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditExpenditure.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelExpenditure.setText(QtGui.QApplication.translate("HouseholdData", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabHouseHold.setTabText(self.tabHouseHold.indexOf(self.tabHouseholdExpenditure), QtGui.QApplication.translate("HouseholdData", "Expenditure", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditCharacteristic.setText(QtGui.QApplication.translate("HouseholdData", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabHouseHold.setTabText(self.tabHouseHold.indexOf(self.tabHouseholdCharacteristics), QtGui.QApplication.translate("HouseholdData", "Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("HouseholdData", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseholdData", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))

