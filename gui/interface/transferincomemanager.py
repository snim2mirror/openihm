#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
from data.controller import Controller

from mixins import TableViewMixin

class TransferIncomeManager(TableViewMixin):
     def getProjectTransfers(self):
         incomes = []
         row = 0
         while (self.tblSelectedTransfers.model().item(row,0)):
             val = self.tblSelectedTransfers.model().item(row,0).text()
             incomes.append(val)
             row = row + 1
            
         return incomes
        
     def displayAvailableTransfers(self):
         ''' Retrieve and display available transfers ''' 
         incomes = self.project.getTransferIncomes() 
        
         model = QStandardItemModel(1,1)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
        
         # add  data rows
         num = 0
        
         for income in incomes:
             qtIncome = QStandardItem( income)
             
             model.setItem( num, 0, qtIncome )
             num = num + 1
        
         self.tblAvailableTransfers.setModel(model)
         self.tblAvailableTransfers.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableTransfers.resizeColumnsToContents()
        
     def displaySelectedTransfers(self):
         ''' Retrieve and display Project Transfer Incomes'''
        
         incomes = self.project.getIncomeSources("transfers") 

         model = QStandardItemModel(1,1)

         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))

         # add  data rows
         num = 0

         for income in incomes:
             qtIncome = QStandardItem( income.name )	
             model.setItem( num, 0, qtIncome )
             num = num + 1

         self.tblSelectedTransfers.setModel(model)
         self.tblSelectedTransfers.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedTransfers.resizeColumnsToContents()
        
     def moveAllTransfers(self):
         ''' Add all available transfers to Project'''
         row = 0
         while( self.tblAvailableTransfers.model().item(row,0)):
             income 		= self.tblAvailableTransfers.model().item(row,0).text()
            
             currentProjectTransfers = self.getProjectTransfers()
             if income not in currentProjectTransfers:
                 self.project.addIncomeSource(income, "transfers")
             else:
                 msg = "The income source labelled, %s, has already been added to project" % (income)
                 QMessageBox.information(self,"Project Configuration",msg)
             row = row + 1
         self.displaySelectedTransfers()   
        
        
     def removeAllTransfers(self):
         ''' remove all listed household or person characteristics from Project'''
         msg = "Are you sure you want to remove all selected transfers from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         incomes = self.getProjectTransfers()
         self.project.deleteIncomeSources( incomes )
         self.displaySelectedTransfers() 
        
     def moveSelectedTransfers(self):
        ''' Add selected available transfers to Project'''
        numSelected = self.countRowsSelected(self.tblAvailableTransfers)
        if  numSelected != 0:
             selectedRows = self.getSelectedRows(self.tblAvailableTransfers)
             for row in selectedRows:
                 income 		= self.tblAvailableTransfers.model().item(row,0).text()
                
                 currentProjectTransfers = self.getProjectTransfers()
                 if income not in currentProjectTransfers:
                     self.project.addIncomeSource(income, "transfers")
                 else:
                     msg = "The income source labelled, %s, has already been added to project" % (income)
                     QMessageBox.information(self,"Project Configuration",msg)
             self.displaySelectedTransfers()
        else:
            msg = "Please select the transfers you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedTransfers(self):
         ''' remove selected transfers from Project'''
         numSelected = self.countRowsSelected(self.tblSelectedTransfers)
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected transfer(s) from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             selectedRows = self.getSelectedRows(self.tblSelectedTransfers)
             incomes = []
             for row in selectedRows:
                 income = self.tblSelectedTransfers.model().item(row,0).text()
                 incomes.append(income)
                 
             self.project.deleteIncomeSources( incomes )
             self.displaySelectedTransfers()
             
         else:
             msg = "Please select the transfers you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
