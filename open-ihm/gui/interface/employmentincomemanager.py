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

from mixins import TableViewMixin

class EmploymentIncomeManager(TableViewMixin):
     def getProjectEmployment(self):
         incomes = []
         row = 0
         while (self.tblSelectedEmployment.model().item(row,0)):
             val = self.tblSelectedEmployment.model().item(row,0).text()
             incomes.append(val)
             row = row + 1
            
         return incomes
        
     def displayAvailableEmployment(self):
         ''' Retrieve and display available employment ''' 
         incomes = self.project.getEmploymentIncomes() 
        
         model = QStandardItemModel(1,1)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))
        
         # add  data rows
         num = 0
        
         for income in incomes:
             qtIncome = QStandardItem( income)
             
             model.setItem( num, 0, qtIncome )
             num = num + 1
        
         self.tblAvailableEmployment.setModel(model)
         self.tblAvailableEmployment.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableEmployment.resizeColumnsToContents()
        
     def displaySelectedEmployment(self):
         ''' Retrieve and display Project employment Incomes'''
        
         incomes = self.project.getIncomeSources("employment") 

         model = QStandardItemModel(1,1)

         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income Source'))

         # add  data rows
         num = 0

         for income in incomes:
             qtIncome = QStandardItem( income.name )	
             model.setItem( num, 0, qtIncome )
             num = num + 1

         self.tblSelectedEmployment.setModel(model)
         self.tblSelectedEmployment.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedEmployment.resizeColumnsToContents()
        
     def moveAllEmployment(self):
         ''' Add all available employment to Project'''
         row = 0
         while( self.tblAvailableEmployment.model().item(row,0)):
             income 		= self.tblAvailableEmployment.model().item(row,0).text()
            
             currentProjectEmployment = self.getProjectEmployment()
             if income not in currentProjectEmployment:
                 self.project.addIncomeSource(income, "employment")
             else:
                 msg = "The income source labelled, %s, has already been added to project" % (income)
                 QMessageBox.information(self,"Project Configuration",msg)
             row = row + 1
         self.displaySelectedEmployment()   
        
        
     def removeAllEmployment(self):
         ''' remove all listed household or person characteristics from Project'''
         msg = "Are you sure you want to remove all selected employment from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         incomes = self.getProjectEmployment()
         self.project.deleteIncomeSources( incomes )
         self.displaySelectedEmployment() 
        
     def moveSelectedEmployment(self):
        ''' Add selected available employment to Project'''
        numSelected = self.countRowsSelected(self.tblAvailableEmployment)
        if  numSelected != 0:
             selectedRows = self.getSelectedRows(self.tblAvailableEmployment)
             for row in selectedRows:
                 income 		= self.tblAvailableEmployment.model().item(row,0).text()
                
                 currentProjectEmployment = self.getProjectEmployment()
                 if income not in currentProjectEmployment:
                     self.project.addIncomeSource(income, "employment")
                 else:
                     msg = "The income source labelled, %s, has already been added to project" % (income)
                     QMessageBox.information(self,"Project Configuration",msg)
             self.displaySelectedEmployment()
        else:
            msg = "Please select the employment you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedEmployment(self):
         ''' remove selected employment from Project'''
         numSelected = self.countRowsSelected(self.tblSelectedEmployment)
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected employment(s) from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             selectedRows = self.getSelectedRows(self.tblSelectedEmployment)
             incomes = []
             for row in selectedRows:
                 income = self.tblSelectedEmployment.model().item(row,0).text()
                 incomes.append(income)
                 
             self.project.deleteIncomeSources( incomes )
             self.displaySelectedEmployment()
             
         else:
             msg = "Please select the employment you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
