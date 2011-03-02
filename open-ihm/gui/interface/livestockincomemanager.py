from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 
from data.controller import Controller
import common

class LivestockIncomeManager:
     def getProjectLivestock(self):
         incomes = []
         row = 0
         while (self.tblSelectedLivestock.model().item(row,0)):
             val = self.tblSelectedLivestock.model().item(row,0).text()
             incomes.append(val)
             row = row + 1
            
         return incomes
        
     def displayAvailableLivestock(self):
         ''' Retrieve and display available livestock ''' 
         incomes = self.project.getFoodIncomes("livestock") 
        
         model = QStandardItemModel(1,1)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
        
         # add  data rows
         num = 0
        
         for income in incomes:
             qtIncome = QStandardItem( income)
             
             model.setItem( num, 0, qtIncome )
             num = num + 1
        
         self.tblAvailableLivestock.setModel(model)
         self.tblAvailableLivestock.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableLivestock.resizeColumnsToContents()
        
     def displaySelectedLivestock(self):
         ''' Retrieve and display Project Livestock Incomes'''
        
         incomes = self.project.getIncomeSources("livestock") 

         model = QStandardItemModel(1,1)

         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))

         # add  data rows
         num = 0

         for income in incomes:
             qtIncome = QStandardItem( income.name )	
             model.setItem( num, 0, qtIncome )
             num = num + 1

         self.tblSelectedLivestock.setModel(model)
         self.tblSelectedLivestock.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedLivestock.resizeColumnsToContents()
        
     def moveAllLivestock(self):
         ''' Add all available livestocks to Project'''
         row = 0
         while( self.tblAvailableLivestock.model().item(row,0)):
             income 		= self.tblAvailableLivestock.model().item(row,0).text()
            
             currentProjectLivestock = self.getProjectLivestock()
             if income not in currentProjectLivestock:
                 self.project.addIncomeSource(income, "livestock")
             else:
                 msg = "The income source labelled, %s, has already been added to project" % (income)
                 QMessageBox.information(self,"Project Configuration",msg)
             row = row + 1
         self.displaySelectedLivestock()   
        
        
     def removeAllLivestock(self):
         ''' remove all listed household or person characteristics from Project'''
         msg = "Are you sure you want to remove all selected livestocks from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         incomes = self.getProjectLivestock()
         self.project.deleteIncomeSources( incomes )
         self.displaySelectedLivestock() 
        
     def moveSelectedLivestock(self):
        ''' Add selected available livestocks to Project'''
        numSelected = common.countRowsSelected(self.tblAvailableLivestock)
        if  numSelected != 0:
             selectedRows = common.getSelectedRows(self.tblAvailableLivestock)
             for row in selectedRows:
                 income 		= self.tblAvailableLivestock.model().item(row,0).text()
                
                 currentProjectLivestock = self.getProjectLivestock()
                 if income not in currentProjectLivestock:
                     self.project.addIncomeSource(income, "livestock")
                 else:
                     msg = "The income source labelled, %s, has already been added to project" % (income)
                     QMessageBox.information(self,"Project Configuration",msg)
             self.displaySelectedLivestock()
        else:
            msg = "Please select the livestocks you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedLivestock(self):
         ''' remove selected livestocks from Project'''
         numSelected = common.countRowsSelected(self.tblSelectedLivestock)
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected livestock(s) from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             selectedRows = common.getSelectedRows(self.tblSelectedLivestock)
             incomes = []
             for row in selectedRows:
                 income = self.tblSelectedLivestock.model().item(row,0).text()
                 incomes.append(income)
                 
             self.project.deleteIncomeSources( incomes )
             self.displaySelectedLivestock()
             
         else:
             msg = "Please select the livestocks you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
