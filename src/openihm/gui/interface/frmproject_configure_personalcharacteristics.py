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

class PersonalCharacteristicsManager(TableViewMixin):
     def getProjectPersonalCharacteristics(self):
         chars = []
         row = 0
         while (self.tblSelectedPersonalCharacteristics.model().item(row,0)):
             val = self.tblSelectedPersonalCharacteristics.model().item(row,0).text()
             chars.append(val)
             row = row + 1
            
         return chars
        
     def displayAvailablePersonalCharacteristics(self):
         ''' Retrieve and display available Personal Characteristics ''' 
         controller = Controller()
         chars = controller.getGlobalCharacteristics("Personal")
        
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
        
         self.tblAvailablePersonalCharacteristics.setModel(model)
         self.tblAvailablePersonalCharacteristics.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailablePersonalCharacteristics.resizeColumnsToContents()
        
     def displaySelectedPersonalCharacteristics(self):
         ''' Retrieve and display Project Personal Characteristics '''
         # select query to retrieve selected characteristics
         chars = self.project.getProjectCharacteristics("Personal")

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

         self.tblSelectedPersonalCharacteristics.setModel(model)
         self.tblSelectedPersonalCharacteristics.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedPersonalCharacteristics.resizeColumnsToContents()
        
     def moveAllPersonalCharacteristics(self):
         ''' Add all available Personal Characteristics to Project'''
         row = 0
         controller = Controller()
         globalchars = controller.getGlobalCharacteristics("Personal")
         for char in globalchars:
             if self.project.existsProjectCharacteristic(char.name):
                 msg = "The personal characteristic labelled, %s, has already been added to project" % (char.name)
                 QMessageBox.information(self,"Project Configuration",msg)
             else:
                 self.project.addProjectCharacteristic(char.name, char.chartype, char.datatype)
         self.displaySelectedPersonalCharacteristics()   
        
     def removeAllPersonalCharacteristics(self):
         ''' remove all listed personal characteristics from Project'''
         msg = "Are you sure you want to remove all selected characteristics from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         controller = Controller()
         chars = controller.getGlobalCharacteristics("Personal")
         for char in chars:
             self.project.delProjectCharacteristic(char.name)
             
         self.displaySelectedPersonalCharacteristics() 
        
     def moveSelectedPersonalCharacteristics(self):
        ''' Add selected available personal characteristics to Project'''
        numSelected = self.countRowsSelected(self.tblAvailablePersonalCharacteristics)
        if  numSelected != 0:
             selectedRows = self.getSelectedRows(self.tblAvailablePersonalCharacteristics)
             for row in selectedRows:
                 charname = self.tblAvailablePersonalCharacteristics.model().item(row,0).text()
                
                 if not self.project.existsProjectCharacteristic(charname):
                     controller = Controller()
                     char = controller.getGlobalCharacteristic(charname)
                     self.project.addProjectCharacteristic(char.name, char.chartype, char.datatype)
                 else:
                     msg = "The personal characteristic labelled, %s, has already been added to project" % (charname)
                     QMessageBox.information(self,"Project Configuration",msg)
                     
             self.displaySelectedPersonalCharacteristics()
        else:
            msg = "Please select the personal characteristics you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedPersonalCharacteristics(self):
         ''' remove selected personal characteristics from Project'''
         numSelected = self.countRowsSelected(self.tblSelectedPersonalCharacteristics)
         
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected personal characteristics from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             selectedRows = self.getSelectedRows(self.tblSelectedPersonalCharacteristics)
             
             for row in selectedRows:
                 charname = self.tblSelectedPersonalCharacteristics.model().item(row,0).text()
                 self.project.delProjectCharacteristic( charname )
                 
             self.displaySelectedPersonalCharacteristics()
             
         else:
             msg = "Please select the personal characteristics you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
