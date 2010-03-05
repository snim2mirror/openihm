# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manageincomedetails.ui'
#
# Created: Fri Mar  5 17:07:16 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ManageIncome(object):
    def setupUi(self, ManageIncome):
        ManageIncome.setObjectName("ManageIncome")
        ManageIncome.resize(QtCore.QSize(QtCore.QRect(0,0,572,380).size()).expandedTo(ManageIncome.minimumSizeHint()))
        ManageIncome.setMinimumSize(QtCore.QSize(572,380))

        self.tabWidget = QtGui.QTabWidget(ManageIncome)
        self.tabWidget.setGeometry(QtCore.QRect(0,0,571,341))
        self.tabWidget.setMinimumSize(QtCore.QSize(0,0))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setGeometry(QtCore.QRect(0,0,567,313))
        self.tab.setObjectName("tab")

        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(270,40,281,28))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270,120,80,28))
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(270,10,251,18))
        self.label_2.setObjectName("label_2")

        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0,10,271,18))
        self.label.setObjectName("label")

        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(470,120,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0,40,241,261))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab,"")

        self.tabIncomeCrops = QtGui.QWidget()
        self.tabIncomeCrops.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabIncomeCrops.setObjectName("tabIncomeCrops")

        self.label_26 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_26.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_26.setObjectName("label_26")

        self.comboBox_5 = QtGui.QComboBox(self.tabIncomeCrops)
        self.comboBox_5.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_5.setObjectName("comboBox_5")

        self.listWidget_6 = QtGui.QListWidget(self.tabIncomeCrops)
        self.listWidget_6.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_6.setObjectName("listWidget_6")

        self.comboBox_4 = QtGui.QComboBox(self.tabIncomeCrops)
        self.comboBox_4.setGeometry(QtCore.QRect(370,120,191,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_3 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_3.setGeometry(QtCore.QRect(280,90,91,18))
        self.label_3.setObjectName("label_3")

        self.label_5 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_5.setGeometry(QtCore.QRect(280,170,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton_3 = QtGui.QPushButton(self.tabIncomeCrops)
        self.pushButton_3.setGeometry(QtCore.QRect(480,210,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.lineEdit_2 = QtGui.QLineEdit(self.tabIncomeCrops)
        self.lineEdit_2.setGeometry(QtCore.QRect(370,160,151,28))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_4 = QtGui.QPushButton(self.tabIncomeCrops)
        self.pushButton_4.setGeometry(QtCore.QRect(360,210,80,28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.comboBox_3 = QtGui.QComboBox(self.tabIncomeCrops)
        self.comboBox_3.setGeometry(QtCore.QRect(370,80,191,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_4 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_4.setGeometry(QtCore.QRect(280,50,54,18))
        self.label_4.setObjectName("label_4")

        self.label_6 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_6.setGeometry(QtCore.QRect(280,130,101,18))
        self.label_6.setObjectName("label_6")

        self.label_25 = QtGui.QLabel(self.tabIncomeCrops)
        self.label_25.setGeometry(QtCore.QRect(280,10,241,18))
        self.label_25.setObjectName("label_25")

        self.lineEdit_7 = QtGui.QLineEdit(self.tabIncomeCrops)
        self.lineEdit_7.setGeometry(QtCore.QRect(370,40,191,28))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tabWidget.addTab(self.tabIncomeCrops,"")

        self.tabEmployment = QtGui.QWidget()
        self.tabEmployment.setGeometry(QtCore.QRect(0,0,640,320))
        self.tabEmployment.setObjectName("tabEmployment")

        self.pushButton_11 = QtGui.QPushButton(self.tabEmployment)
        self.pushButton_11.setGeometry(QtCore.QRect(360,200,80,28))
        self.pushButton_11.setObjectName("pushButton_11")

        self.label_15 = QtGui.QLabel(self.tabEmployment)
        self.label_15.setGeometry(QtCore.QRect(260,50,111,18))
        self.label_15.setObjectName("label_15")

        self.label_16 = QtGui.QLabel(self.tabEmployment)
        self.label_16.setGeometry(QtCore.QRect(260,140,91,18))
        self.label_16.setObjectName("label_16")

        self.label_17 = QtGui.QLabel(self.tabEmployment)
        self.label_17.setGeometry(QtCore.QRect(260,90,101,18))
        self.label_17.setObjectName("label_17")

        self.groupBox_2 = QtGui.QGroupBox(self.tabEmployment)
        self.groupBox_2.setGeometry(QtCore.QRect(370,80,191,41))
        self.groupBox_2.setObjectName("groupBox_2")

        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10,10,80,24))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(90,10,80,24))
        self.checkBox_2.setObjectName("checkBox_2")

        self.pushButton_12 = QtGui.QPushButton(self.tabEmployment)
        self.pushButton_12.setGeometry(QtCore.QRect(480,200,80,28))
        self.pushButton_12.setObjectName("pushButton_12")

        self.label_33 = QtGui.QLabel(self.tabEmployment)
        self.label_33.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_33.setObjectName("label_33")

        self.comboBox_16 = QtGui.QComboBox(self.tabEmployment)
        self.comboBox_16.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_16.setObjectName("comboBox_16")

        self.listWidget_10 = QtGui.QListWidget(self.tabEmployment)
        self.listWidget_10.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_10.setObjectName("listWidget_10")

        self.lineEdit_14 = QtGui.QLineEdit(self.tabEmployment)
        self.lineEdit_14.setGeometry(QtCore.QRect(370,40,191,28))
        self.lineEdit_14.setObjectName("lineEdit_14")

        self.lineEdit_6 = QtGui.QLineEdit(self.tabEmployment)
        self.lineEdit_6.setGeometry(QtCore.QRect(370,140,191,28))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_34 = QtGui.QLabel(self.tabEmployment)
        self.label_34.setGeometry(QtCore.QRect(260,10,241,18))
        self.label_34.setObjectName("label_34")
        self.tabWidget.addTab(self.tabEmployment,"")

        self.tabIncomeLivestock = QtGui.QWidget()
        self.tabIncomeLivestock.setGeometry(QtCore.QRect(0,0,640,320))
        self.tabIncomeLivestock.setObjectName("tabIncomeLivestock")

        self.comboBox_6 = QtGui.QComboBox(self.tabIncomeLivestock)
        self.comboBox_6.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_6.setObjectName("comboBox_6")

        self.label_7 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_7.setGeometry(QtCore.QRect(280,110,91,18))
        self.label_7.setObjectName("label_7")

        self.label_27 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_27.setGeometry(QtCore.QRect(280,10,271,18))
        self.label_27.setObjectName("label_27")

        self.listWidget_7 = QtGui.QListWidget(self.tabIncomeLivestock)
        self.listWidget_7.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_7.setObjectName("listWidget_7")

        self.comboBox_7 = QtGui.QComboBox(self.tabIncomeLivestock)
        self.comboBox_7.setGeometry(QtCore.QRect(370,100,151,27))
        self.comboBox_7.setObjectName("comboBox_7")

        self.comboBox_2 = QtGui.QComboBox(self.tabIncomeLivestock)
        self.comboBox_2.setGeometry(QtCore.QRect(370,50,191,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.pushButton_5 = QtGui.QPushButton(self.tabIncomeLivestock)
        self.pushButton_5.setGeometry(QtCore.QRect(360,240,80,28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label_28 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_28.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_28.setObjectName("label_28")

        self.label_8 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_8.setGeometry(QtCore.QRect(280,50,54,18))
        self.label_8.setObjectName("label_8")

        self.lineEdit_3 = QtGui.QLineEdit(self.tabIncomeLivestock)
        self.lineEdit_3.setGeometry(QtCore.QRect(370,180,151,28))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_9 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_9.setGeometry(QtCore.QRect(280,140,101,18))
        self.label_9.setObjectName("label_9")

        self.pushButton_6 = QtGui.QPushButton(self.tabIncomeLivestock)
        self.pushButton_6.setGeometry(QtCore.QRect(480,240,80,28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.comboBox_8 = QtGui.QComboBox(self.tabIncomeLivestock)
        self.comboBox_8.setGeometry(QtCore.QRect(370,140,151,27))
        self.comboBox_8.setObjectName("comboBox_8")

        self.label_10 = QtGui.QLabel(self.tabIncomeLivestock)
        self.label_10.setGeometry(QtCore.QRect(280,190,81,18))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tabIncomeLivestock,"")

        self.tabIncomeTransfers = QtGui.QWidget()
        self.tabIncomeTransfers.setGeometry(QtCore.QRect(0,0,640,320))
        self.tabIncomeTransfers.setObjectName("tabIncomeTransfers")

        self.comboBox_13 = QtGui.QComboBox(self.tabIncomeTransfers)
        self.comboBox_13.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_13.setObjectName("comboBox_13")

        self.listWidget_9 = QtGui.QListWidget(self.tabIncomeTransfers)
        self.listWidget_9.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_9.setObjectName("listWidget_9")

        self.label_31 = QtGui.QLabel(self.tabIncomeTransfers)
        self.label_31.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_31.setObjectName("label_31")

        self.label_32 = QtGui.QLabel(self.tabIncomeTransfers)
        self.label_32.setGeometry(QtCore.QRect(280,10,271,18))
        self.label_32.setObjectName("label_32")

        self.pushButton_9 = QtGui.QPushButton(self.tabIncomeTransfers)
        self.pushButton_9.setGeometry(QtCore.QRect(280,120,80,28))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtGui.QPushButton(self.tabIncomeTransfers)
        self.pushButton_10.setGeometry(QtCore.QRect(480,120,80,28))
        self.pushButton_10.setObjectName("pushButton_10")

        self.lineEdit_5 = QtGui.QLineEdit(self.tabIncomeTransfers)
        self.lineEdit_5.setGeometry(QtCore.QRect(280,40,281,28))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.tabWidget.addTab(self.tabIncomeTransfers,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setGeometry(QtCore.QRect(0,0,567,313))
        self.tab_2.setObjectName("tab_2")

        self.comboBox_9 = QtGui.QComboBox(self.tab_2)
        self.comboBox_9.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_9.setObjectName("comboBox_9")

        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(280,110,91,18))
        self.label_11.setObjectName("label_11")

        self.label_29 = QtGui.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(280,10,241,18))
        self.label_29.setObjectName("label_29")

        self.listWidget_8 = QtGui.QListWidget(self.tab_2)
        self.listWidget_8.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_8.setObjectName("listWidget_8")

        self.comboBox_10 = QtGui.QComboBox(self.tab_2)
        self.comboBox_10.setGeometry(QtCore.QRect(370,100,151,27))
        self.comboBox_10.setObjectName("comboBox_10")

        self.comboBox_11 = QtGui.QComboBox(self.tab_2)
        self.comboBox_11.setGeometry(QtCore.QRect(370,50,191,27))
        self.comboBox_11.setObjectName("comboBox_11")

        self.pushButton_7 = QtGui.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(360,240,80,28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.label_30 = QtGui.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_30.setObjectName("label_30")

        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(280,50,54,18))
        self.label_12.setObjectName("label_12")

        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(370,180,151,28))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(280,140,101,18))
        self.label_13.setObjectName("label_13")

        self.pushButton_8 = QtGui.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(480,240,80,28))
        self.pushButton_8.setObjectName("pushButton_8")

        self.comboBox_12 = QtGui.QComboBox(self.tab_2)
        self.comboBox_12.setGeometry(QtCore.QRect(370,140,151,27))
        self.comboBox_12.setObjectName("comboBox_12")

        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(280,190,81,18))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_2,"")

        self.btnManageIncomeClose = QtGui.QPushButton(ManageIncome)
        self.btnManageIncomeClose.setGeometry(QtCore.QRect(490,350,80,28))
        self.btnManageIncomeClose.setObjectName("btnManageIncomeClose")

        self.retranslateUi(ManageIncome)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ManageIncome)

    def retranslateUi(self, ManageIncome):
        ManageIncome.setWindowTitle(QtGui.QApplication.translate("ManageIncome", "Manage Income Details", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ManageIncome", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageIncome", "Add/Edit Asset Category", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageIncome", "Existing Asset Categories", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ManageIncome", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ManageIncome", "Select Crop Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ManageIncome", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageIncome", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ManageIncome", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Crop Details", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomeCrops), QtGui.QApplication.translate("ManageIncome", "Crops", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ManageIncome", "Employment Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ManageIncome", "Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ManageIncome", "Payment Type", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("ManageIncome", "Cash", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("ManageIncome", "Food", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("ManageIncome", "Select Employment Type", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.clear()

        item = QtGui.QListWidgetItem(self.listWidget_10)
        item.setText(QtGui.QApplication.translate("ManageIncome", "Men", None, QtGui.QApplication.UnicodeUTF8))

        item1 = QtGui.QListWidgetItem(self.listWidget_10)
        item1.setText(QtGui.QApplication.translate("ManageIncome", "Women", None, QtGui.QApplication.UnicodeUTF8))

        item2 = QtGui.QListWidgetItem(self.listWidget_10)
        item2.setText(QtGui.QApplication.translate("ManageIncome", "Children", None, QtGui.QApplication.UnicodeUTF8))

        item3 = QtGui.QListWidgetItem(self.listWidget_10)
        item3.setText(QtGui.QApplication.translate("ManageIncome", "Family", None, QtGui.QApplication.UnicodeUTF8))

        item4 = QtGui.QListWidgetItem(self.listWidget_10)
        item4.setText(QtGui.QApplication.translate("ManageIncome", "Contract", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Employment Types Details", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEmployment), QtGui.QApplication.translate("ManageIncome", "Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Livestock/Livestock Products Details", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("ManageIncome", "Select Livestock/Livestock Product", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ManageIncome", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ManageIncome", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ManageIncome", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomeLivestock), QtGui.QApplication.translate("ManageIncome", "Livestock and Livestock Products", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("ManageIncome", "Select Transfer Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Transfer Type", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("ManageIncome", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIncomeTransfers), QtGui.QApplication.translate("ManageIncome", "Transfers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ManageIncome", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("ManageIncome", "Add/ Edit Foods Details", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("ManageIncome", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("ManageIncome", "Select Food Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManageIncome", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ManageIncome", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("ManageIncome", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ManageIncome", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ManageIncome", "Wild Foods, Hunting, Fishing", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageIncomeClose.setText(QtGui.QApplication.translate("ManageIncome", "Close", None, QtGui.QApplication.UnicodeUTF8))

