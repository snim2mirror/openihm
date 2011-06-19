#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_crop.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_crops import Ui_AddHouseholdIncomeCrops

from mixins import MDIDialogMixin

class FrmHouseholdCropIncome(QDialog, Ui_AddHouseholdIncomeCrops, MDIDialogMixin):	
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
         
         self.getCropTypes()
         
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
         
     def getCropTypes(self):
         ''' Retrieve Crop Types and display them in a combobox '''
         # select query to Crop Types
         query = '''SELECT name, unitofmeasure FROM setup_foods_crops WHERE category='crops' '''

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
             croptype = row[0]
             measuringunit = row[1]
             self.cboIncomeType.addItem(croptype, QVariant(measuringunit))

         unitofmeasure = self.cboIncomeType.itemData( self.cboIncomeType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )

         cursor.close()   
         db.close()
        
     def displayIncomeDetails(self):
         ''' Retrieve and display Household Income details '''
         query = '''SELECT incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed  
             FROM cropincome WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
         
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
         ''' Saves crop income to database '''    	

         # get the data entered by user
         croptype      	= self.cboIncomeType.currentText()
         unitofmeasure	= self.txtUnitOfMeasure.text()
         unitsproduced    = self.txtUnitsProduced.text() if self.txtUnitsProduced.text() != "" else "0"
         unitsconsumed	= self.txtUnitsConsumed.text() if self.txtUnitsConsumed.text() != "" else "0"
         unitssold		= self.txtUnitsSold.text() if self.txtUnitsSold.text() != "" else "0"
         unitprice		= self.txtUnitPrice.text() if self.txtUnitPrice.text() != "" else "0"
         otheruses       = self.txtUnitsOtherUses.text() if self.txtUnitsOtherUses.text() != "" else "0"

         db = data.mysql.connector.Connect(**self.config)

         # create UPDATE query
         if (self.incomeid == 0):
             query = '''INSERT INTO cropincome (hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, 
                 otheruses, unitsconsumed, pid ) VALUES(%s,'%s','%s',%s,%s,%s, %s, %s, 
                 %s) ''' % ( self.hhid, croptype, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.pid )
         else:
             query = ''' UPDATE cropincome SET incomesource='%s', unitofmeasure='%s', unitsproduced=%s, unitssold=%s,
                  unitprice=%s, otheruses=%s, unitsconsumed=%s WHERE hhid=%s AND pid=%s AND  
                  id=%s ''' % ( croptype, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.hhid, self.pid,  self.incomeid)

         # execute query and commit changes
         cursor =  db.cursor()
         cursor.execute(query)
         db.commit()

         # close database connection
         cursor.close()
         db.close()

         # close new project window
         self.parent.retrieveHouseholdCropIncome()
         self.mdiClose()
