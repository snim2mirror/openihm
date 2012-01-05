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

class DietManager(TableViewMixin):
     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cmbFoodItem.itemData( self.cmbFoodItem.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
         
     def getCropTypes(self):
         ''' Retrieve Crop Types and display them in a combobox '''
         # select query to Crop Types
         query = '''SELECT name, unitofmeasure FROM setup_foods_crops'''
         rows = self.executeResultsQuery(query)
         for row in rows:
             croptype = row[0]
             measuringunit = row[1]
             self.cmbFoodItem.addItem(croptype, QVariant(measuringunit))

         unitofmeasure = self.cmbFoodItem.itemData( self.cmbFoodItem.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
    
     def listDiets(self):
         ''' List project diet items '''
         diets = self.project.getProjectDietItems()
         
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Id.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Food Item'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit Of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Percentage'))
         model.setHorizontalHeaderItem(4,QStandardItem('Price per Unit'))
         
         # add  data rows
         num = 0
         
         for diet in diets:
             qtID = QStandardItem("%i" % diet.itemid)
             qtID.setTextAlignment( Qt.AlignCenter )
             qtFoodItem = QStandardItem(diet.fooditem )	
             qtUnit = QStandardItem( diet.unitofmeasure )
             
             qtPercentage = QStandardItem( "%.2f" %   diet.percentage )
             qtPrice = QStandardItem( "%.2f" %   diet.priceperunit )
             			
             model.setItem( num, 0, qtID )
             model.setItem( num, 1, qtFoodItem )
             model.setItem( num, 2, qtUnit )
             model.setItem( num, 3, qtPercentage )
             model.setItem( num, 4, qtPrice )
             num = num + 1
         
         self.tblDiets.setModel(model)
         self.tblDiets.resizeColumnsToContents()
         self.tblDiets.hideColumn(0)
         self.tblDiets.show()
         
     def showSelectedDiet(self, index):
         ''' show details of a selected currency for editing '''
         self.dietid = self.tblDiets.model().item(index.row(),0).text()
         fooditem = self.tblDiets.model().item(index.row(),1).text()
         unitofmeasure = self.tblDiets.model().item(index.row(),2).text()
         percentage = self.tblDiets.model().item(index.row(),3).text()
         priceperunit = self.tblDiets.model().item(index.row(),4).text()
         
         self.cmbFoodItem.setCurrentIndex(self.cmbFoodItem.findText( fooditem ))
         self.txtUnitOfMeasure.setText(unitofmeasure)
         self.txtPercentage.setText(percentage)
         self.txtUnitPrice.setText(priceperunit)
         
     def saveDiet(self):
         ''' Save the currency details of a currency being added or edited '''
         pid = self.parent.projectid
         fooditem = self.cmbFoodItem.currentText()
         unitofmeasure = self.txtUnitOfMeasure.text()
         percentage = self.txtPercentage.text()
         priceperunit = self.txtUnitPrice.text()
         
         # create INSERT or UPDATE query
         if (self.dietid == 0):
             self.project.addProjectDietItem(fooditem, unitofmeasure, percentage, priceperunit)
         else:
             dietitem = self.project.getProjectDietItem(self.dietid)
             dietitem.editData(fooditem, unitofmeasure, percentage, priceperunit)
         
         # clear text boxes and refresh list
         self.txtPercentage.setText("")
         self.txtUnitPrice.setText("")
         self.dietid = 0
         self.listDiets()
         
     def delDiets(self):
         ''' Delete a selected diet items '''
         numSelected = self.countRowsSelected(self.tblDiets)
         if  numSelected != 0:
             # confirm deletion
             if numSelected == 1:
                 msg = "Are you sure you want to delete the selected diet item?"
             else:
                 msg = "Are you sure you want to delete the selected diet items?"
             
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             # get the member id of the selected currencies
             selectedRows = self.getSelectedRows(self.tblDiets)
             selectedIds = []
             for row in selectedRows:
                 itemid = self.tblDiets.model().item(row,0).text()
                 self.project.delProjectDietItem(itemid)

             self.dietid = 0
             self.listDiets()

         else:
             QMessageBox.information(self,"Delete Diet Items","Please select the rows containing diet items to be deleted.")
