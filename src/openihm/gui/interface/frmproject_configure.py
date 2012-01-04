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

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

from control.controller import Controller

# import the Create Project Dialog design class
Ui_ProjectConfiguration, base_class = uic.loadUiType("gui/designs/ui_projectconfiguration.ui")


from cropincomemanager import CropIncomeManager
from livestockincomemanager import LivestockIncomeManager
from wildfoodincomemanager import WildfoodIncomeManager
from employmentincomemanager import EmploymentIncomeManager
from transferincomemanager import TransferIncomeManager
from frmproject_configure_householdcharacteristics import HouseholdCharacteristicsManager
from frmproject_configure_personalcharacteristics import PersonalCharacteristicsManager

from mixins import MDIDialogMixin, MySQLMixin, TableViewMixin

class FrmConfigureProject(QDialog, Ui_ProjectConfiguration, PersonalCharacteristicsManager,  HouseholdCharacteristicsManager,  CropIncomeManager, LivestockIncomeManager, WildfoodIncomeManager, EmploymentIncomeManager, TransferIncomeManager, TableViewMixin, MySQLMixin, MDIDialogMixin):	
     ''' Creates the Edit Project form. '''	
     def __init__(self, parent):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.parent = parent
         self.dietid = 0                     # selected diet item
         self.currentItem = ""           # selected standard of living item
         self.setupUi(self)
        
         controller = Controller()
         self.project = controller.getProject( self.parent.projectid )
        
         # show first tab first
         self.tabProject.setCurrentIndex(0)
        
         # display project name
         self.lblProjectName.setText(self.parent.projectname)
        
         # display Available and Selected Household Characteristics
         self.displayAvailableHouseholdCharacteristics()
         self.displaySelectedHouseholdCharacteristics()
         
         self.displayAvailablePersonalCharacteristics()
         self.displaySelectedPersonalCharacteristics()
         
         self.listDiets()
         self.getCropTypes()
         self.displayStandardOfLiving()
         self.getExpenseItems()
         self.getAgeRange(self.cmbAgeBottom, 0, 100)
         self.getAgeRange(self.cmbAgeTop, 1, 101)
         
         self.displayAvailableCrops()
         self.displaySelectedCrops()
         
         self.displayAvailableLivestock()
         self.displaySelectedLivestock()
         
         self.displayAvailableWildfoods()
         self.displaySelectedWildfoods()
         
         self.displayAvailableEmployment()
         self.displaySelectedEmployment()
         
         self.displayAvailableTransfers()
         self.displaySelectedTransfers()
        
        
     #--------------------------------------------------------------------------------------------------------------------------
     #  Standard of Living
     #-------------------------------------------------------------------------------------------------------------------------
         
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
         # select query to retrieve items
         pid = self.parent.projectid
         query = '''SELECT summary, scope, gender, agebottom, agetop, item, costperyear 
                     FROM standardofliving WHERE pid=%s ORDER BY scope''' % ( pid )
         
         rows = self.executeResultsQuery(query)
         
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
         
         for row in rows:
             qtSummary = QStandardItem( row[0] )
             qtScope = QStandardItem( row[1] )	
             qtGender = QStandardItem( row[2] )
             
             qtAgeBottom = QStandardItem( "%i" %   row[3] )
             qtAgeTop = QStandardItem( "%i" %   row[4] )
             qtItem = QStandardItem( row[5] )
             qtCost = QStandardItem( "%.2f" %   row[6] )
             			
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
         pid = self.parent.projectid
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
         summary = "%s %s [%s to %s years]" % (gender,  item,  agebottom,  agetop) if scope == "Person" else "%s %s" % (scope, item)
         
         # create INSERT or UPDATE query
         if (self.currentItem == ""):
             query = '''INSERT INTO standardofliving (pid, summary,scope,gender, agebottom,agetop,item,costperyear )
                         VALUES(%s,'%s','%s','%s',%s,%s,'%s',%s) ''' % ( pid, summary,scope,gender, agebottom,agetop,item,costperyear  )
         else:
             query = ''' UPDATE standardofliving SET summary='%s', scope='%s', gender='%s', agebottom=%s, agetop=%s, item='%s',
                            costperyear=%s
                         WHERE summary='%s' AND pid=%s ''' % ( summary,scope,gender, agebottom,agetop,item,costperyear, currentItem, pid)
         
         self.executeUpdateQuery(query)
         
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
         pid = self.parent.projectid
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
             selectedItems = []
             for row in selectedRows:
                 selectedItems.append( self.tblStandardOfLiving.model().item(row,0).text() )
             # delete selected currencies
             queries = []
             for item in selectedItems:
                  queries.append('''DELETE FROM standardofliving WHERE summary='%s' AND pid=%s ''' % (item,  pid))
             self.executeMultipleUpdateQueries(queries)
             self.resetStandardOfLivingFields()
             self.displayStandardOfLiving()

         else:
             QMessageBox.information(self,"Delete Standard of Living Items","Please select the rows containing items to be deleted.")
       
        
     #--------------------------------------------------------------------------------------------------------------------------
     #  Diets
     #-------------------------------------------------------------------------------------------------------------------------
    
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
         ''' List available currencies '''
         # select query to retrieve currencies
         pid = self.parent.projectid
         query = '''SELECT id, fooditem, unitofmeasure, percentage, priceperunit FROM diet WHERE pid=%s ''' % pid
         
         rows = self.executeResultsQuery(query)
         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Id.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Food Item'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit Of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Percentage'))
         model.setHorizontalHeaderItem(4,QStandardItem('Price per Unit'))
         
         # add  data rows
         num = 0
         
         for row in rows:
             qtID = QStandardItem("%i" % row[0])
             qtID.setTextAlignment( Qt.AlignCenter )
             qtFoodItem = QStandardItem( row[1] )	
             qtUnit = QStandardItem(row[2] )
             
             qtPercentage = QStandardItem( "%.2f" %   row[3] )
             qtPrice = QStandardItem( "%.2f" %   row[4] )
             			
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
             query = '''INSERT INTO diet (pid, fooditem,unitofmeasure,percentage, priceperunit )
                         VALUES(%s,'%s','%s',%s,%s) ''' % ( pid, fooditem,unitofmeasure,percentage, priceperunit  )
         else:
             query = ''' UPDATE diet SET fooditem='%s', unitofmeasure='%s', percentage=%s, priceperunit=%s
                         WHERE id=%s AND pid=%s ''' % ( fooditem,unitofmeasure,percentage, priceperunit, self.dietid, pid)
         
         self.executeUpdateQuery(query)
         
         # clear text boxes and refresh list
         self.txtPercentage.setText("")
         self.txtUnitPrice.setText("")
         self.dietid = 0
         self.listDiets()
         
     def delDiets(self):
         ''' Delete a selected currencies '''
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
                 selectedIds.append( self.tblDiets.model().item(row,0).text() )
             # delete selected currencies
             queries = []
             for dietid in selectedIds:
                 queries.append('''DELETE FROM diet WHERE id='%s' ''' % (dietid))
             self.executeMultipleUpdateQuery(queries)

             self.dietid = 0
             self.listDiets()

         else:
             QMessageBox.information(self,"Delete Diet Items","Please select the rows containing diet items to be deleted.")
