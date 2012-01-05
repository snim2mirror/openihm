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

class StandardOfLivingManager(TableViewMixin):
     def getExpenseItems(self):
         ''' Retrieve Expense Items and display them in a combobox '''
         # select query to items
         itemtype = self.cmbScope.currentText()
         query = '''SELECT item FROM  setup_standardofliving WHERE type='%s' OR type='Both' ''' % ( itemtype )

         rows = self.executeResultsQuery(query)
         
         self.cmbExpenseItem.clear()
         for row in rows:
             item = row[0]
             self.cmbExpenseItem.addItem( item )
         
         # disable or enable gender and age fields depending on scope         
         enabled = True if itemtype != 'Household' else False
         self.cmbGender.setEnabled(  enabled )
         self.cmbAgeBottom.setEnabled(  enabled )
         self.cmbAgeTop.setEnabled(  enabled )
         
     def adjustTopList(self):
         ''' fill an age combobox with ages ranging from min to max '''
         min = int( self.cmbAgeBottom.currentText() ) + 1
         self.cmbAgeTop.clear()
         for age in range( min, 102 ):
             self.cmbAgeTop.addItem( "%i"  % (age) )
     
     def getAgeRange(self, obj, min, max):
         ''' fill an age combobox with ages ranging from min to max '''
         for age in range( min, max + 1 ):
             obj.addItem( "%i"  % (age) )
    
     def displayStandardOfLiving(self):
         ''' List standard of living items '''
         # get standard of living items
         entries = self.project.getStandardOfLivingEntries()
         
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Description'))
         model.setHorizontalHeaderItem(1,QStandardItem('Scope'))
         model.setHorizontalHeaderItem(2,QStandardItem('Gender'))
         model.setHorizontalHeaderItem(3,QStandardItem('Age Bottom'))
         model.setHorizontalHeaderItem(4,QStandardItem('Age Top'))
         model.setHorizontalHeaderItem(5, QStandardItem('Item'))
         model.setHorizontalHeaderItem(6,QStandardItem('Cost/Year'))
         
         # add  data rows
         num = 0
         
         for entry in entries:
             qtSummary = QStandardItem( entry.summary )
             qtScope = QStandardItem( entry.scope )	
             qtGender = QStandardItem( entry.gender )
             
             qtAgeBottom = QStandardItem( "%i" %   entry.agebottom )
             qtAgeTop = QStandardItem( "%i" %   entry.agetop )
             qtItem = QStandardItem( entry.item )
             qtCost = QStandardItem( "%.2f" %   entry.costperyear )
             			
             model.setItem( num, 0, qtSummary )
             model.setItem( num, 1, qtScope )
             model.setItem( num, 2, qtGender )
             model.setItem( num, 3, qtAgeBottom )
             model.setItem( num, 4, qtAgeTop )
             model.setItem( num, 5, qtItem )
             model.setItem( num, 6, qtCost )
             num = num + 1
         
         self.tblStandardOfLiving.setModel(model)
         self.tblStandardOfLiving.resizeColumnsToContents()
         self.tblStandardOfLiving.hideColumn(3)
         self.tblStandardOfLiving.hideColumn(4)
         self.tblStandardOfLiving.hideColumn(5)
         self.tblStandardOfLiving.show()
         
     def showStandardOfLivingItem(self, index):
         ''' show details of a selected item for editing '''
         self.currentItem = self.tblStandardOfLiving.model().item(index.row(),0).text()
         scope = self.tblStandardOfLiving.model().item(index.row(),1).text()
         gender = self.tblStandardOfLiving.model().item(index.row(),2).text()
         agebottom = self.tblStandardOfLiving.model().item(index.row(),3).text()
         agetop = self.tblStandardOfLiving.model().item(index.row(),4).text()
         item = self.tblStandardOfLiving.model().item(index.row(),5).text()
         cost = self.tblStandardOfLiving.model().item(index.row(),6).text()
         
         self.cmbScope.setCurrentIndex(self.cmbScope.findText( scope ))
         self.getExpenseItems()
         self.cmbGender.setCurrentIndex(self.cmbGender.findText( gender ))
         self.cmbAgeBottom.setCurrentIndex(self.cmbAgeBottom.findText( agebottom ))
         self.cmbAgeTop.setCurrentIndex(self.cmbAgeTop.findText( agetop ))
         self.cmbExpenseItem.setCurrentIndex(self.cmbExpenseItem.findText( item ))
         self.txtCostPerYear.setText(cost)
         
     def saveStandardOfLivingItem(self):
         ''' Save the currency details of a currency being added or edited '''
         currentItem = self.currentItem
         scope = self.cmbScope.currentText()
         if ( scope == "Person" ):
             gender = self.cmbGender.currentText()
             agebottom = self.cmbAgeBottom.currentText()
             agetop = self.cmbAgeTop.currentText()
         else:
             gender = "All"
             agebottom = 0
             agetop = 0
         item = self.cmbExpenseItem.currentText()
         costperyear = self.txtCostPerYear.text()
         summary = "%s - %s - [%s to %s years]" % (item,  gender,  agebottom,  agetop) if scope == "Person" else "%s - %s" % (item, scope)
         
         # add or update currently selected item
         if (self.currentItem == ""):
             self.project.addStandardOfLivingEntry(summary, scope, gender, agebottom, agetop, item, costperyear)
         else:
             entry = self.project.getStandardOfLivingEntry(self.currentItem)
             entry.editData(summary, scope, gender, agebottom, agetop, item, costperyear)
         
         # clear text boxes and refresh list
         self.resetStandardOfLivingFields()
         self.displayStandardOfLiving()
     
     def resetStandardOfLivingFields(self):
         ''' Resets data entry fields for standard of lving items '''
         self.txtCostPerYear.setText("")
         self.currentItem = ""
         self.cmbScope.setCurrentIndex( self.cmbScope.findText( "Person" ) )
         self.cmbGender.setCurrentIndex( self.cmbGender.findText( "Female" ) )
         self.cmbAgeBottom.setCurrentIndex( self.cmbAgeBottom.findText( "0" ) )
         self.cmbAgeTop.setCurrentIndex( self.cmbAgeTop.findText( "1" ) )
         
     def delStandardOfLivingItems(self):
         ''' Delete a selected Items '''
         numSelected = self.countRowsSelected(self.tblStandardOfLiving)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected item?"
             else:
                 msg = "Are you sure you want to delete the selected items?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get the member id of the selected currencies
             selectedRows = self.getSelectedRows(self.tblStandardOfLiving)
             
             for row in selectedRows:
                 item = self.tblStandardOfLiving.model().item(row,0).text()
                 self.project.delStandardOfLivingEntry(item)
                 
             self.resetStandardOfLivingFields()
             self.displayStandardOfLiving()

         else:
             QMessageBox.information(self,"Delete Standard of Living Items","Please select the rows containing items to be deleted.")
