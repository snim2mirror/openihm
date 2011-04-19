#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_livestock.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_livestock import Ui_AddHouseholdIncomeLivestock

class FrmHouseholdLivestockIncome(QDialog, Ui_AddHouseholdIncomeLivestock):	
     ''' Form to add or edit a Household Livestock Income  '''	
     def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent 	= parent
         self.hhid 		= hhid
         self.pid = parent.parent.projectid
         self.incomeid 	= incomeid
         
         self.config = Config.dbinfo().copy()
         
         self.getLivestockTypes()
         
         if ( incomeid != 0 ):
             self.displayIncomeDetails()
             self.setWindowTitle( "Edit Income Item" )
             
         # display household name
         self.lblHouseholdName.setText(hhname)
         
         # lock editing of income source and unit of measure
         self.cboIncomeType.setEditable( False )
         self.txtUnitOfMeasure.setReadOnly( True )
         
     def mdiClose(self):
          self.parent.mdi.closeActiveSubWindow()

     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cboIncomeType.itemData( self.cboIncomeType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
        
     def getLivestockTypes(self):
         ''' Retrieve Livestock Types and display them in a combobox '''
         # select query to Livestock Types
         query = '''SELECT name, unitofmeasure FROM setup_foods_crops WHERE category='livestock' '''

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)
         
         rows = cursor.fetchall()
         
         for row in rows:
             incometype = row[0]
             measuringunit = row[1]
             self.cboIncomeType.addItem(incometype, QVariant(measuringunit))

         unitofmeasure = self.cboIncomeType.itemData( self.cboIncomeType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )

         cursor.close()   
         db.close()
        
     def displayIncomeDetails(self):
         ''' Retrieve and display Household Income details '''
         query = '''SELECT incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed  
             FROM livestockincome WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
         
         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
             croptype = row[0]
             self.cboIncomeType.setCurrentIndex( self.cboIncomeType.findText( croptype ) )
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

         cursor.close()   
         db.close()

     def saveIncome(self):
         ''' Saves livestock income to database '''    	

         # get the data entered by user
         incometype      	= self.cboIncomeType.currentText()
         unitofmeasure	= self.txtUnitOfMeasure.text()
         unitsproduced    = self.txtUnitsProduced.text() if self.txtUnitsProduced.text() != "" else "0"
         unitsconsumed	= self.txtUnitsConsumed.text() if self.txtUnitsConsumed.text() != "" else "0"
         unitssold		= self.txtUnitsSold.text() if self.txtUnitsSold.text() != "" else "0"
         unitprice		= self.txtUnitPrice.text() if self.txtUnitPrice.text() != "" else "0"
         otheruses       = self.txtUnitsOtherUses.text() if self.txtUnitsOtherUses.text() != "" else "0"

         db = data.mysql.connector.Connect(**self.config)

         # create UPDATE query
         if (self.incomeid == 0):
             query = '''INSERT INTO livestockincome (hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, 
                 otheruses, unitsconsumed, pid ) VALUES(%s,'%s','%s',%s,%s,%s, %s, %s, 
                 %s) ''' % ( self.hhid, incometype, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.pid )
         else:
             query = ''' UPDATE livestockincome SET incomesource='%s', unitofmeasure='%s', unitsproduced=%s, unitssold=%s,
                  unitprice=%s, otheruses=%s, unitsconsumed=%s WHERE hhid=%s AND pid=%s AND  
                  id=%s ''' % ( incometype, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.hhid, self.pid,  self.incomeid)

         # execute query and commit changes
         cursor =  db.cursor()
         cursor.execute(query)
         db.commit()

         # close database connection
         cursor.close()
         db.close()

         # close new project window
         self.parent.retrieveHouseholdLivestockIncome()
         self.close()
