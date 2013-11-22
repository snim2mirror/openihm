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

Ui_AddHouseholdIncomeWildfoods, base_class = uic.loadUiType("gui/designs/ui_household_income_wildfoods.ui")


from mixins import MDIDialogMixin, MySQLMixin

class FrmHouseholdWildfoodsIncome(QDialog, Ui_AddHouseholdIncomeWildfoods, MySQLMixin, MDIDialogMixin):	
     ''' Form to add or edit a Household Crop Income  '''	
     def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent 	= parent
         self.hhid 		= hhid
         self.pid = parent.parent.projectid
         self.incomeid 	= incomeid
         
         self.config = Config.dbinfo().copy()
         
         self.getWildfoodsTypes()
         
         if ( incomeid != 0 ):
             self.displayIncomeDetails()
             self.setWindowTitle( "Edit Income Item" )
             
         # display household name
         self.lblHouseholdName.setText(hhname)
         
         # lock editing of income source and unit of measure
         self.cboIncomeType.setEditable( False )
         self.txtUnitOfMeasure.setReadOnly( True )
         
     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cboIncomeType.itemData( self.cboIncomeType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
        
     def getWildfoodsTypes(self):
         ''' Retrieve Crop Types and display them in a combobox '''
         # select query to wildfood Types
         query = '''SELECT name, unitofmeasure FROM setup_foods_crops WHERE category='wildfoods' '''

         rows = self.executeResultsQuery(query)
         for row in rows:
             incomesource = row[0]
             measuringunit = row[1]
             self.cboIncomeType.addItem(incomesource, QVariant(measuringunit))

         unitofmeasure = self.cboIncomeType.itemData( self.cboIncomeType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
        
     def displayIncomeDetails(self):
         ''' Retrieve and display Household Income details '''
         query = '''SELECT incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed  
             FROM wildfoods WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
         
         rows = self.executeResultsQuery(query)

         for row in rows:
             incometype = row[0]
             self.cboIncomeType.setCurrentIndex( self.cboIncomeType.findText( incometype ) )
             unitofmeasure = row[1]
             self.txtUnitOfMeasure.setText( unitofmeasure )
             unitsproduced = row[2]
             self.txtUnitsProduced.setText( str(unitsproduced) )
             unitssold = row[3]
             self.txtUnitsSold.setText( str(unitssold) )
             unitprice = row[4]
             self.txtUnitPrice.setText( str(unitprice) )
             otheruses = row[5]
             self.txtUnitsOtherUses.setText( str(otheruses) )
             unitsconsumed = row[6]
             self.txtUnitsConsumed.setText( str(unitsconsumed) )
        
     def saveIncome(self):
         ''' Saves wildfoods income to database '''    	

         # get the data entered by user
         incometype      	= self.cboIncomeType.currentText()
         unitofmeasure	= self.txtUnitOfMeasure.text()
         unitsproduced    = self.txtUnitsProduced.text() if self.txtUnitsProduced.text() != "" else "0"
         unitsconsumed	= self.txtUnitsConsumed.text() if self.txtUnitsConsumed.text() != "" else "0"
         unitssold		= self.txtUnitsSold.text() if self.txtUnitsSold.text() != "" else "0"
         unitprice		= self.txtUnitPrice.text() if self.txtUnitPrice.text() != "" else "0"
         otheruses       = self.txtUnitsOtherUses.text() if self.txtUnitsOtherUses.text() != "" else "0"
         
         totalusage = float(unitsconsumed) + float(unitssold) + float(otheruses)
         totalproduced = float(unitsproduced)
         
         if totalproduced < totalusage:
             msg = "The total of units consumed, units sold and units for otheruses should not exceed units produced."
             QMessageBox.information(self,"Add Wildfood Income", msg)	
             return

         # create UPDATE query
         if (self.incomeid == 0):
             query = '''INSERT INTO wildfoods (hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, 
                 otheruses, unitsconsumed, pid ) VALUES(%s,'%s','%s',%s,%s,%s, %s, %s, 
                 %s) ''' % ( self.hhid, incometype, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.pid )
         else:
             query = ''' UPDATE wildfoods SET incomesource='%s', unitofmeasure='%s', unitsproduced=%s, unitssold=%s,
                  unitprice=%s, otheruses=%s, unitsconsumed=%s WHERE hhid=%s AND pid=%s AND  
                  id=%s ''' % ( incometype, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.hhid, self.pid,  self.incomeid)

         self.executeUpdateQuery(query)
         # close new project window
         self.parent.retrieveHouseholdWildfoodsIncome()
         self.mdiClose()
