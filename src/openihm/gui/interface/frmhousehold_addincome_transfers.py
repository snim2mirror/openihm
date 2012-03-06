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

from data.config import Config
Ui_AddHouseholdIncomeTransfers, base_class = uic.loadUiType("gui/designs/ui_household_income_transfers.ui")

from mixins import MySQLMixin, MDIDialogMixin

class FrmHouseholdTransferIncome(QDialog, Ui_AddHouseholdIncomeTransfers, MySQLMixin, MDIDialogMixin):	
     ''' Form to add or edit a Household Transfers Income  '''	
     def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent 	= parent
         self.hhid 		= hhid
         self.pid = parent.parent.projectid
         self.incomeid 	= incomeid

         self.config = Config.dbinfo().copy()

         self.getGiftsTypes()
         self.getCropTypes()

         if ( incomeid != 0 ):
             self.displayIncomeDetails()
             self.setWindowTitle( "Edit Income Item" )

         # display household name
         self.lblHouseholdName.setText(hhname)

     def getGiftsTypes(self):
         ''' Retrieve Gifts Types and display them in a combobox '''
         # select query to Gifts Types
         query = '''SELECT assistancetype FROM setup_transfers'''
         rows = self.executeResultsQuery(query)
         for row in rows:
             assistancetype = row[0]
             self.cmbSourceOfTransfer.addItem(assistancetype)
        
     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cmbFoodType.itemData( self.cmbFoodType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
         
     def getCropTypes(self):
         ''' Retrieve Crop Types and display them in a combobox '''
         # select query to Crop Types
         query = '''SELECT name, unitofmeasure FROM setup_foods_crops'''
         rows = self.executeResultsQuery(query)
         for row in rows:
             croptype = row[0]
             measuringunit = row[1]
             self.cmbFoodType.addItem(croptype, QVariant(measuringunit))

         unitofmeasure = self.cmbFoodType.itemData( self.cmbFoodType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
        
     def displayIncomeDetails(self):
         ''' Retrieve and display Household Income details '''
         query = '''SELECT sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsconsumed , unitssold, priceperunit  
                  FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )

         rows = self.executeResultsQuery(query)
         for row in rows:
             sourceoftransfer = row[0]
             self.cmbSourceOfTransfer.setCurrentIndex( self.cmbSourceOfTransfer.findText( sourceoftransfer ) )
             cashperyear = row[1]
             self.txtCash.setText( "%.2f" % cashperyear )
             foodtype = row[2]
             self.cmbFoodType.setCurrentIndex( self.cmbFoodType.findText(foodtype) )
             unitofmeasure = row[3]
             self.txtUnitOfMeasure.setText(unitofmeasure)
             unitsconsumed = row[4]
             self.txtUnitsConsumed.setText( "%.2f" % unitsconsumed )
             unitssold = row[5]
             self.txtUnitsSold.setText( "%.2f" % unitssold )
             unitprice = row[6]
             self.txtUnitPrice.setText( "%.2f" % unitprice )

     def saveIncome(self):
         ''' Saves transfer from org income to database '''    	
         
         # get the data entered by user
         sourceoftransfer  = self.cmbSourceOfTransfer.currentText()
         sourcetype		= "External"
         cash                 = self.txtCash.text() if self.txtCash.text() != "" else "0"
         foodtype           = self.cmbFoodType.currentText()
         unitofmeasure	= self.txtUnitOfMeasure.text()
         unitsconsumed	= self.txtUnitsConsumed.text() if self.txtUnitsConsumed.text() != "" else "0"
         unitssold           = self.txtUnitsSold.text() if self.txtUnitsSold.text() != "" else "0"
         unitprice           = self.txtUnitPrice.text() if self.txtUnitPrice.text() != "" else "0"

         # create UPDATE query
         if (self.incomeid == 0):
             query = '''INSERT INTO transfers (hhid, pid, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsconsumed, unitssold, 
                 priceperunit, sourcetype ) VALUES(%s,%s,'%s',%s,'%s','%s',%s,%s, %s,  
                 '%s') ''' % ( self.hhid, self.pid, sourceoftransfer, cash, foodtype, unitofmeasure,  unitsconsumed,  unitssold,  unitprice,  sourcetype )
         else:
             query = ''' UPDATE transfers SET sourceoftransfer='%s',  cashperyear=%s, foodtype='%s', unitofmeasure='%s', unitsconsumed=%s, 
                         unitssold='%s', priceperunit=%s, sourcetype='%s' WHERE hhid=%s AND pid=%s AND 
                         id=%s ''' % ( sourceoftransfer, cash, foodtype, unitofmeasure,  unitsconsumed,  unitssold,  unitprice, sourcetype, self.hhid, self.pid,  self.incomeid)

         self.executeUpdateQuery(query)
         # close new project window
         self.parent.retrieveHouseholdTransferIncome()
         self.mdiClose()
