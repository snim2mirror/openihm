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
import includes.mysql.connector as connector # FIXME: Do we need this?
from data.controller import Controller

from mixins import TableViewMixin

class WildfoodIncomeManager(TableViewMixin):
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
        numSelected = self.countRowsSelected(self.tblAvailableWildfoods)
        if  numSelected != 0:
             selectedRows = self.getSelectedRows(self.tblAvailableWildfoods)
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
         numSelected = self.countRowsSelected(self.tblSelectedWildfoods)
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected wildfood(s) from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
             selectedRows = self.getSelectedRows(self.tblSelectedWildfoods)
             incomes = []
             for row in selectedRows:
                 income = self.tblSelectedWildfoods.model().item(row,0).text()
                 incomes.append(income)
                 
             self.project.deleteIncomeSources( incomes )
             self.displaySelectedWildfoods()
             
         else:
             msg = "Please select the wildfoods you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
