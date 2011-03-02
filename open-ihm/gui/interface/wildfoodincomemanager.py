from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 
from data.controller import Controller
import common

class WildfoodIncomeManager:
     def getProjectWildfoods(self):
         incomes = []
         row = 0
         while (self.tblSelectedWildfoods.model().item(row,0)):
             val = self.tblSelectedWildfoods.model().item(row,0).text()
             incomes.append(val)
             row = row + 1
            
         return incomes
        
     def displayAvailableWildfoods(self):
         ''' Retrieve and display available wildfood ''' 
         incomes = self.project.getFoodIncomes("wildfoods") 
        
         model = QStandardItemModel(1,1)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
        
         # add  data rows
         num = 0
        
         for income in incomes:
             qtIncome = QStandardItem( income)
             
             model.setItem( num, 0, qtIncome )
             num = num + 1
        
         self.tblAvailableWildfoods.setModel(model)
         self.tblAvailableWildfoods.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableWildfoods.resizeColumnsToContents()
        
     def displaySelectedWildfoods(self):
         ''' Retrieve and display Project Wildfood Incomes'''
        
         incomes = self.project.getIncomeSources("wildfoods") 

         model = QStandardItemModel(1,1)

         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))

         # add  data rows
         num = 0

         for income in incomes:
             qtIncome = QStandardItem( income.name )	
             model.setItem( num, 0, qtIncome )
             num = num + 1

         self.tblSelectedWildfoods.setModel(model)
         self.tblSelectedWildfoods.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedWildfoods.resizeColumnsToContents()
        
     def moveAllWildfoods(self):
         ''' Add all available wildfoods to Project'''
         row = 0
         while( self.tblAvailableWildfoods.model().item(row,0)):
             income 		= self.tblAvailableWildfoods.model().item(row,0).text()
            
             currentProjectWildfoods = self.getProjectWildfoods()
             if income not in currentProjectWildfoods:
                 self.project.addIncomeSource(income, "wildfoods")
             else:
                 msg = "The income source labelled, %s, has already been added to project" % (income)
                 QMessageBox.information(self,"Project Configuration",msg)
             row = row + 1
         self.displaySelectedWildfoods()   
        
        
     def removeAllWildfoods(self):
         ''' remove all listed household or person characteristics from Project'''
         msg = "Are you sure you want to remove all selected wildfoods from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         incomes = self.getProjectWildfoods()
         self.project.deleteIncomeSources( incomes )
         self.displaySelectedWildfoods() 
        
     def moveSelectedWildfoods(self):
        ''' Add selected available wildfoods to Project'''
        numSelected = common.countRowsSelected(self.tblAvailableWildfoods)
        if  numSelected != 0:
             selectedRows = common.getSelectedRows(self.tblAvailableWildfoods)
             for row in selectedRows:
                 income 		= self.tblAvailableWildfoods.model().item(row,0).text()
                
                 currentProjectWildfoods = self.getProjectWildfoods()
                 if income not in currentProjectWildfoods:
                     self.project.addIncomeSource(income, "wildfoods")
                 else:
                     msg = "The income source labelled, %s, has already been added to project" % (income)
                     QMessageBox.information(self,"Project Configuration",msg)
             self.displaySelectedWildfoods()
        else:
            msg = "Please select the wildfoods you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedWildfoods(self):
         ''' remove selected wildfoods from Project'''
         numSelected = common.countRowsSelected(self.tblSelectedWildfoods)
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected wildfood(s) from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             selectedRows = common.getSelectedRows(self.tblSelectedWildfoods)
             incomes = []
             for row in selectedRows:
                 income = self.tblSelectedWildfoods.model().item(row,0).text()
                 incomes.append(income)
                 
             self.project.deleteIncomeSources( incomes )
             self.displaySelectedWildfoods()
             
         else:
             msg = "Please select the wildfoods you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
