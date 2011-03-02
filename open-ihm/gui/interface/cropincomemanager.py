from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 
from data.controller import Controller
import common

class CropIncomeManager:
     def getProjectCrops(self):
         incomes = []
         row = 0
         while (self.tblSelectedCrops.model().item(row,0)):
             val = self.tblSelectedCrops.model().item(row,0).text()
             incomes.append(val)
             row = row + 1
            
         return incomes
        
     def displayAvailableCrops(self):
         ''' Retrieve and display available crops ''' 
         incomes = self.project.getFoodIncomes("crops") 
        
         model = QStandardItemModel(1,1)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
        
         # add  data rows
         num = 0
        
         for income in incomes:
             qtIncome = QStandardItem( income)
             
             model.setItem( num, 0, qtIncome )
             num = num + 1
        
         self.tblAvailableCrops.setModel(model)
         self.tblAvailableCrops.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableCrops.resizeColumnsToContents()
        
     def displaySelectedCrops(self):
         ''' Retrieve and display Project Crop Incomes'''
        
         incomes = self.project.getIncomeSources("crops") 

         model = QStandardItemModel(1,1)

         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))

         # add  data rows
         num = 0

         for income in incomes:
             qtIncome = QStandardItem( income.name )	
             model.setItem( num, 0, qtIncome )
             num = num + 1

         self.tblSelectedCrops.setModel(model)
         self.tblSelectedCrops.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedCrops.resizeColumnsToContents()
        
     def moveAllCrops(self):
         ''' Add all available crops to Project'''
         row = 0
         while( self.tblAvailableCrops.model().item(row,0)):
             income 		= self.tblAvailableCrops.model().item(row,0).text()
            
             currentProjectCrops = self.getProjectCrops()
             if income not in currentProjectCrops:
                 self.project.addIncomeSource(income, "crops")
             else:
                 msg = "The income source labelled, %s, has already been added to project" % (income)
                 QMessageBox.information(self,"Project Configuration",msg)
             row = row + 1
         self.displaySelectedCrops()   
        
        
     def removeAllCrops(self):
         ''' remove all listed household or person characteristics from Project'''
         msg = "Are you sure you want to remove all selected crops from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         incomes = self.getProjectCrops()
         self.project.deleteIncomeSources( incomes )
         self.displaySelectedCrops() 
        
     def moveSelectedCrops(self):
        ''' Add selected available crops to Project'''
        numSelected = common.countRowsSelected(self.tblAvailableCrops)
        if  numSelected != 0:
             selectedRows = common.getSelectedRows(self.tblAvailableCrops)
             for row in selectedRows:
                 income 		= self.tblAvailableCrops.model().item(row,0).text()
                
                 currentProjectCrops = self.getProjectCrops()
                 if income not in currentProjectCrops:
                     self.project.addIncomeSource(income, "crops")
                 else:
                     msg = "The income source labelled, %s, has already been added to project" % (income)
                     QMessageBox.information(self,"Project Configuration",msg)
             self.displaySelectedCrops()
        else:
            msg = "Please select the crops you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedCrops(self):
         ''' remove selected crops from Project'''
         numSelected = common.countRowsSelected(self.tblSelectedCrops)
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected crop(s) from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             selectedRows = common.getSelectedRows(self.tblSelectedCrops)
             incomes = []
             for row in selectedRows:
                 income = self.tblSelectedCrops.model().item(row,0).text()
                 incomes.append(income)
                 
             self.project.deleteIncomeSources( incomes )
             self.displaySelectedCrops()
             
         else:
             msg = "Please select the crops you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
