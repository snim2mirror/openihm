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

from control.controller import Controller

from mixins import TableViewMixin

class HouseholdCharacteristicsManager(TableViewMixin):
     def getProjectHouseholdCharacteristics(self):
         chars = []
         row = 0
         while (self.tblSelectedHouseholdCharacteristics.model().item(row,0)):
             val = self.tblSelectedHouseholdCharacteristics.model().item(row,0).text()
             chars.append(val)
             row = row + 1
            
         return chars
        
     def displayAvailableHouseholdCharacteristics(self):
         ''' Retrieve and display available Household Characteristics ''' 
         controller = Controller()
         chars = controller.getGlobalCharacteristics("Household")
        
         model = QStandardItemModel(1,2)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
         model.setHorizontalHeaderItem(1,QStandardItem('Data Type'))
        
         # add  data rows
         num = 0
        
         for char in chars:
             qtCharacteristic = QStandardItem( char.name )
             qtDataType = QStandardItem( char.datatypestr )		
             model.setItem( num, 0, qtCharacteristic )
             model.setItem( num, 1, qtDataType )
             num = num + 1
        
         self.tblAvailableHouseholdCharacteristics.setModel(model)
         self.tblAvailableHouseholdCharacteristics.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableHouseholdCharacteristics.resizeColumnsToContents()
        
     def displaySelectedHouseholdCharacteristics(self):
         ''' Retrieve and display Project Household Characteristics '''
         # select query to retrieve selected characteristics
         chars = self.project.getProjectCharacteristics("Household")

         model = QStandardItemModel(1,1)

         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
         model.setHorizontalHeaderItem(1,QStandardItem('Data Type'))

         # add  data rows
         num = 0

         for char in chars:
             qtCharacteristic = QStandardItem( char.name )	
             qtDataType = QStandardItem( char.datatypestr )		
             model.setItem( num, 0, qtCharacteristic )
             model.setItem( num, 1, qtDataType )
             num = num + 1

         self.tblSelectedHouseholdCharacteristics.setModel(model)
         self.tblSelectedHouseholdCharacteristics.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedHouseholdCharacteristics.resizeColumnsToContents()
        
     def moveAllHouseholdCharacteristics(self):
         ''' Add all available Household Characteristics to Project'''
         row = 0
         controller = Controller()
         globalchars = controller.getGlobalCharacteristics("Household")
         for char in globalchars:
             if self.project.existsProjectCharacteristic(char.name):
                 msg = "The household characteristic labelled, %s, has already been added to project" % (char.name)
                 QMessageBox.information(self,"Project Configuration",msg)
             else:
                 self.project.addProjectCharacteristic(char.name, char.chartype, char.datatype)
         self.displaySelectedHouseholdCharacteristics()   
        
     def removeAllHouseholdCharacteristics(self):
         ''' remove all listed household characteristics from Project'''
         msg = "Are you sure you want to remove all selected characteristics from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         controller = Controller()
         chars = controller.getGlobalCharacteristics("Household")
         for char in chars:
             self.project.delProjectCharacteristic(char.name)
             
         self.displaySelectedHouseholdCharacteristics() 
        
     def moveSelectedHouseholdCharacteristics(self):
        ''' Add selected available household characteristics to Project'''
        numSelected = self.countRowsSelected(self.tblAvailableHouseholdCharacteristics)
        if  numSelected != 0:
             selectedRows = self.getSelectedRows(self.tblAvailableHouseholdCharacteristics)
             for row in selectedRows:
                 charname = self.tblAvailableHouseholdCharacteristics.model().item(row,0).text()
                
                 if not self.project.existsProjectCharacteristic(charname):
                     controller = Controller()
                     char = controller.getGlobalCharacteristic(charname)
                     self.project.addProjectCharacteristic(char.name, char.chartype, char.datatype)
                 else:
                     msg = "The household characteristic labelled, %s, has already been added to project" % (charname)
                     QMessageBox.information(self,"Project Configuration",msg)
                     
             self.displaySelectedHouseholdCharacteristics()
        else:
            msg = "Please select the household characteristics you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedHouseholdCharacteristics(self):
         ''' remove selected household characteristics from Project'''
         numSelected = self.countRowsSelected(self.tblSelectedHouseholdCharacteristics)
         
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected characteristics from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             selectedRows = self.getSelectedRows(self.tblSelectedHouseholdCharacteristics)
             
             for row in selectedRows:
                 charname = self.tblSelectedHouseholdCharacteristics.model().item(row,0).text()
                 self.project.delProjectCharacteristic( charname )
                 
             self.displaySelectedHouseholdCharacteristics()
             
         else:
             msg = "Please select the household characteristics you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
