#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_transfers.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_transfers import Ui_AddHouseholdIncomeTransfers

class FrmHouseholdTransferIncome(QDialog, Ui_AddHouseholdIncomeTransfers):	
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

     def mdiClose(self):
          self.parent.mdi.closeActiveSubWindow()

     def getGiftsTypes(self):
         ''' Retrieve Gifts Types and display them in a combobox '''
         # select query to Gifts Types
         query = '''SELECT assistancetype FROM setup_transfers'''

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
             assistancetype = row[0]
             self.cmbSourceOfTransfer.addItem(assistancetype)

         cursor.close()   
         db.close()
        
     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cmbFoodType.itemData( self.cmbFoodType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
         
     def getCropTypes(self):
         ''' Retrieve Crop Types and display them in a combobox '''
         # select query to Crop Types
         query = '''SELECT name, unitofmeasure FROM setup_foods_crops'''

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
             croptype = row[0]
             measuringunit = row[1]
             self.cmbFoodType.addItem(croptype, QVariant(measuringunit))

         unitofmeasure = self.cmbFoodType.itemData( self.cmbFoodType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )

         cursor.close()   
         db.close()
        
     def displayIncomeDetails(self):
         ''' Retrieve and display Household Income details '''
         query = '''SELECT sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsconsumed , unitssold, priceperunit  
                  FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         for row in cursor.fetchall():
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

         cursor.close()   
         db.close()

     def saveIncome(self):
         ''' Saves transfer from org income to database '''    	
         
         # get the data entered by user
         sourceoftransfer  = self.cmbSourceOfTransfer.currentText()
         sourcetype		= "External"
         cash                 = self.txtCash.text()
         foodtype           = self.cmbFoodType.currentText()
         unitofmeasure	= self.txtUnitOfMeasure.text()
         unitsconsumed	= self.txtUnitsConsumed.text()
         unitssold           = self.txtUnitsSold.text()
         unitprice           = self.txtUnitPrice.text()

         db = data.mysql.connector.Connect(**self.config)

         # create UPDATE query
         if (self.incomeid == 0):
             query = '''INSERT INTO transfers (hhid, pid, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsconsumed, unitssold, 
                 priceperunit, sourcetype ) VALUES(%s,%s,'%s',%s,'%s','%s',%s,%s, %s,  
                 '%s') ''' % ( self.hhid, self.pid, sourceoftransfer, cash, foodtype, unitofmeasure,  unitsconsumed,  unitssold,  unitprice,  sourcetype )
         else:
             query = ''' UPDATE transfers SET sourceoftransfer='%s',  cashperyear=%s, foodtype='%s', unitofmeasure='%s', unitsconsumed=%s, 
                         unitssold='%s', priceperunit=%s, sourcetype='%s' WHERE hhid=%s AND pid=%s AND 
                         id=%s ''' % ( sourceoftransfer, cash, foodtype, unitofmeasure,  unitsconsumed,  unitssold,  unitprice, sourcetype, self.hhid, self.pid,  self.incomeid)

         # execute query and commit changes
         cursor =  db.cursor()
         cursor.execute(query)
         db.commit()
         
         # close database connection
         cursor.close()
         db.close()
         
         # close new project window
         self.parent.retrieveHouseholdTransferIncome()
         self.close()
