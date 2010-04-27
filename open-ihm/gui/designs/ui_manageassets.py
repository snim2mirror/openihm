# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manageassets.ui'
#
# Created: Mon Apr 26 21:34:38 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ManageAssetDetails(object):
    def setupUi(self, ManageAssetDetails):
        ManageAssetDetails.setObjectName("ManageAssetDetails")
        ManageAssetDetails.resize(QtCore.QSize(QtCore.QRect(0,0,572,380).size()).expandedTo(ManageAssetDetails.minimumSizeHint()))
        ManageAssetDetails.setMinimumSize(QtCore.QSize(572,380))

        self.tabWidget = QtGui.QTabWidget(ManageAssetDetails)
        self.tabWidget.setGeometry(QtCore.QRect(0,0,571,341))
        self.tabWidget.setMinimumSize(QtCore.QSize(0,0))
        self.tabWidget.setObjectName("tabWidget")

        self.tabCashSavings = QtGui.QWidget()
        self.tabCashSavings.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabCashSavings.setObjectName("tabCashSavings")

        self.label_23 = QtGui.QLabel(self.tabCashSavings)
        self.label_23.setGeometry(QtCore.QRect(260,60,121,18))
        self.label_23.setObjectName("label_23")

        self.pushButton_15 = QtGui.QPushButton(self.tabCashSavings)
        self.pushButton_15.setGeometry(QtCore.QRect(480,150,80,28))
        self.pushButton_15.setObjectName("pushButton_15")

        self.lineEdit_14 = QtGui.QLineEdit(self.tabCashSavings)
        self.lineEdit_14.setGeometry(QtCore.QRect(372,60,181,28))
        self.lineEdit_14.setObjectName("lineEdit_14")

        self.label_25 = QtGui.QLabel(self.tabCashSavings)
        self.label_25.setGeometry(QtCore.QRect(290,10,241,18))
        self.label_25.setObjectName("label_25")

        self.listWidget_6 = QtGui.QListWidget(self.tabCashSavings)
        self.listWidget_6.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_6.setObjectName("listWidget_6")

        self.label_26 = QtGui.QLabel(self.tabCashSavings)
        self.label_26.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_26.setObjectName("label_26")

        self.pushButton_16 = QtGui.QPushButton(self.tabCashSavings)
        self.pushButton_16.setGeometry(QtCore.QRect(370,150,80,28))
        self.pushButton_16.setObjectName("pushButton_16")

        self.comboBox_5 = QtGui.QComboBox(self.tabCashSavings)
        self.comboBox_5.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_5.setObjectName("comboBox_5")
        self.tabWidget.addTab(self.tabCashSavings,"")

        self.tabFoodStock = QtGui.QWidget()
        self.tabFoodStock.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabFoodStock.setObjectName("tabFoodStock")

        self.listWidget_2 = QtGui.QListWidget(self.tabFoodStock)
        self.listWidget_2.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_2.setObjectName("listWidget_2")

        self.comboBox = QtGui.QComboBox(self.tabFoodStock)
        self.comboBox.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox.setObjectName("comboBox")

        self.lineEdit_2 = QtGui.QLineEdit(self.tabFoodStock)
        self.lineEdit_2.setGeometry(QtCore.QRect(352,60,201,28))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtGui.QLineEdit(self.tabFoodStock)
        self.lineEdit_3.setGeometry(QtCore.QRect(350,110,201,28))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtGui.QLineEdit(self.tabFoodStock)
        self.lineEdit_4.setGeometry(QtCore.QRect(350,160,201,28))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_3 = QtGui.QPushButton(self.tabFoodStock)
        self.pushButton_3.setGeometry(QtCore.QRect(350,240,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtGui.QPushButton(self.tabFoodStock)
        self.pushButton_4.setGeometry(QtCore.QRect(460,240,80,28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_3 = QtGui.QLabel(self.tabFoodStock)
        self.label_3.setGeometry(QtCore.QRect(260,60,54,18))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtGui.QLabel(self.tabFoodStock)
        self.label_4.setGeometry(QtCore.QRect(260,170,81,18))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtGui.QLabel(self.tabFoodStock)
        self.label_5.setGeometry(QtCore.QRect(260,120,54,18))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtGui.QLabel(self.tabFoodStock)
        self.label_6.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_6.setObjectName("label_6")

        self.label_16 = QtGui.QLabel(self.tabFoodStock)
        self.label_16.setGeometry(QtCore.QRect(290,10,241,18))
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.tabFoodStock,"")

        self.tabLand = QtGui.QWidget()
        self.tabLand.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabLand.setObjectName("tabLand")

        self.lineEdit_5 = QtGui.QLineEdit(self.tabLand)
        self.lineEdit_5.setGeometry(QtCore.QRect(352,60,201,28))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton_9 = QtGui.QPushButton(self.tabLand)
        self.pushButton_9.setGeometry(QtCore.QRect(350,240,80,28))
        self.pushButton_9.setObjectName("pushButton_9")

        self.comboBox_2 = QtGui.QComboBox(self.tabLand)
        self.comboBox_2.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label_7 = QtGui.QLabel(self.tabLand)
        self.label_7.setGeometry(QtCore.QRect(260,60,54,18))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtGui.QLabel(self.tabLand)
        self.label_8.setGeometry(QtCore.QRect(260,120,91,18))
        self.label_8.setObjectName("label_8")

        self.listWidget_3 = QtGui.QListWidget(self.tabLand)
        self.listWidget_3.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_3.setObjectName("listWidget_3")

        self.lineEdit_6 = QtGui.QLineEdit(self.tabLand)
        self.lineEdit_6.setGeometry(QtCore.QRect(350,110,201,28))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_17 = QtGui.QLabel(self.tabLand)
        self.label_17.setGeometry(QtCore.QRect(290,10,241,18))
        self.label_17.setObjectName("label_17")

        self.label_9 = QtGui.QLabel(self.tabLand)
        self.label_9.setGeometry(QtCore.QRect(260,170,81,18))
        self.label_9.setObjectName("label_9")

        self.pushButton_10 = QtGui.QPushButton(self.tabLand)
        self.pushButton_10.setGeometry(QtCore.QRect(460,240,80,28))
        self.pushButton_10.setObjectName("pushButton_10")

        self.label_18 = QtGui.QLabel(self.tabLand)
        self.label_18.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_18.setObjectName("label_18")

        self.lineEdit_7 = QtGui.QLineEdit(self.tabLand)
        self.lineEdit_7.setGeometry(QtCore.QRect(350,160,201,28))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tabWidget.addTab(self.tabLand,"")

        self.tabTrees = QtGui.QWidget()
        self.tabTrees.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabTrees.setObjectName("tabTrees")

        self.label_10 = QtGui.QLabel(self.tabTrees)
        self.label_10.setGeometry(QtCore.QRect(260,60,54,18))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtGui.QLabel(self.tabTrees)
        self.label_11.setGeometry(QtCore.QRect(260,170,81,18))
        self.label_11.setObjectName("label_11")

        self.pushButton_11 = QtGui.QPushButton(self.tabTrees)
        self.pushButton_11.setGeometry(QtCore.QRect(460,240,80,28))
        self.pushButton_11.setObjectName("pushButton_11")

        self.lineEdit_8 = QtGui.QLineEdit(self.tabTrees)
        self.lineEdit_8.setGeometry(QtCore.QRect(352,60,201,28))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.lineEdit_9 = QtGui.QLineEdit(self.tabTrees)
        self.lineEdit_9.setGeometry(QtCore.QRect(350,160,201,28))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.label_19 = QtGui.QLabel(self.tabTrees)
        self.label_19.setGeometry(QtCore.QRect(290,10,241,18))
        self.label_19.setObjectName("label_19")

        self.listWidget_4 = QtGui.QListWidget(self.tabTrees)
        self.listWidget_4.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_4.setObjectName("listWidget_4")

        self.lineEdit_10 = QtGui.QLineEdit(self.tabTrees)
        self.lineEdit_10.setGeometry(QtCore.QRect(350,110,201,28))
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.label_20 = QtGui.QLabel(self.tabTrees)
        self.label_20.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_20.setObjectName("label_20")

        self.label_12 = QtGui.QLabel(self.tabTrees)
        self.label_12.setGeometry(QtCore.QRect(260,120,91,18))
        self.label_12.setObjectName("label_12")

        self.pushButton_12 = QtGui.QPushButton(self.tabTrees)
        self.pushButton_12.setGeometry(QtCore.QRect(350,240,80,28))
        self.pushButton_12.setObjectName("pushButton_12")

        self.comboBox_3 = QtGui.QComboBox(self.tabTrees)
        self.comboBox_3.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tabWidget.addTab(self.tabTrees,"")

        self.tabOtherTradableGoods = QtGui.QWidget()
        self.tabOtherTradableGoods.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabOtherTradableGoods.setObjectName("tabOtherTradableGoods")

        self.label_13 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_13.setGeometry(QtCore.QRect(260,60,54,18))
        self.label_13.setObjectName("label_13")

        self.label_14 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_14.setGeometry(QtCore.QRect(260,170,81,18))
        self.label_14.setObjectName("label_14")

        self.pushButton_13 = QtGui.QPushButton(self.tabOtherTradableGoods)
        self.pushButton_13.setGeometry(QtCore.QRect(460,240,80,28))
        self.pushButton_13.setObjectName("pushButton_13")

        self.lineEdit_11 = QtGui.QLineEdit(self.tabOtherTradableGoods)
        self.lineEdit_11.setGeometry(QtCore.QRect(352,60,201,28))
        self.lineEdit_11.setObjectName("lineEdit_11")

        self.lineEdit_12 = QtGui.QLineEdit(self.tabOtherTradableGoods)
        self.lineEdit_12.setGeometry(QtCore.QRect(350,160,201,28))
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.label_21 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_21.setGeometry(QtCore.QRect(290,10,241,18))
        self.label_21.setObjectName("label_21")

        self.listWidget_5 = QtGui.QListWidget(self.tabOtherTradableGoods)
        self.listWidget_5.setGeometry(QtCore.QRect(0,70,241,231))
        self.listWidget_5.setObjectName("listWidget_5")

        self.lineEdit_13 = QtGui.QLineEdit(self.tabOtherTradableGoods)
        self.lineEdit_13.setGeometry(QtCore.QRect(350,110,201,28))
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.label_22 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_22.setGeometry(QtCore.QRect(0,10,221,18))
        self.label_22.setObjectName("label_22")

        self.label_15 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_15.setGeometry(QtCore.QRect(260,120,91,18))
        self.label_15.setObjectName("label_15")

        self.pushButton_14 = QtGui.QPushButton(self.tabOtherTradableGoods)
        self.pushButton_14.setGeometry(QtCore.QRect(350,240,80,28))
        self.pushButton_14.setObjectName("pushButton_14")

        self.comboBox_4 = QtGui.QComboBox(self.tabOtherTradableGoods)
        self.comboBox_4.setGeometry(QtCore.QRect(0,40,241,27))
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.addTab(self.tabOtherTradableGoods,"")

        self.tabAssetsGeneral = QtGui.QWidget()
        self.tabAssetsGeneral.setGeometry(QtCore.QRect(0,0,567,313))
        self.tabAssetsGeneral.setObjectName("tabAssetsGeneral")

        self.listWidget = QtGui.QListWidget(self.tabAssetsGeneral)
        self.listWidget.setGeometry(QtCore.QRect(10,40,241,261))
        self.listWidget.setObjectName("listWidget")

        self.lineEdit = QtGui.QLineEdit(self.tabAssetsGeneral)
        self.lineEdit.setGeometry(QtCore.QRect(280,40,281,28))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtGui.QPushButton(self.tabAssetsGeneral)
        self.pushButton.setGeometry(QtCore.QRect(280,120,80,28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtGui.QPushButton(self.tabAssetsGeneral)
        self.pushButton_2.setGeometry(QtCore.QRect(480,120,80,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtGui.QLabel(self.tabAssetsGeneral)
        self.label.setGeometry(QtCore.QRect(10,10,271,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(self.tabAssetsGeneral)
        self.label_2.setGeometry(QtCore.QRect(280,10,251,18))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tabAssetsGeneral,"")

        self.btnAssetsClose = QtGui.QPushButton(ManageAssetDetails)
        self.btnAssetsClose.setGeometry(QtCore.QRect(490,350,80,28))
        self.btnAssetsClose.setObjectName("btnAssetsClose")

        self.retranslateUi(ManageAssetDetails)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(ManageAssetDetails)

    def retranslateUi(self, ManageAssetDetails):
        ManageAssetDetails.setWindowTitle(QtGui.QApplication.translate("ManageAssetDetails", "Manage Asset Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("ManageAssetDetails", "Cash Saving Type", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Cash Saving Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Cash Saving Type", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCashSavings), QtGui.QApplication.translate("ManageAssetDetails", "Cash Savings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageAssetDetails", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ManageAssetDetails", "KCalories", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Food Stock Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Food Stock Details", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFoodStock), QtGui.QApplication.translate("ManageAssetDetails", "Food Stock", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Land Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ManageAssetDetails", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Land Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLand), QtGui.QApplication.translate("ManageAssetDetails", "Land", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ManageAssetDetails", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Tree Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Tree Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTrees), QtGui.QApplication.translate("ManageAssetDetails", "Trees", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ManageAssetDetails", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Good Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Good", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOtherTradableGoods), QtGui.QApplication.translate("ManageAssetDetails", "Tradable Goods", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageAssetDetails", "Existing Asset Categories", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/Edit Asset Category", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAssetsGeneral), QtGui.QApplication.translate("ManageAssetDetails", "Manage Category Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAssetsClose.setText(QtGui.QApplication.translate("ManageAssetDetails", "Close", None, QtGui.QApplication.UnicodeUTF8))

