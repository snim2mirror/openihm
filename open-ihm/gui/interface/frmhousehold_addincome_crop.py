#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_crop.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_crops import Ui_AddHouseholdIncomeCrops

class FrmHouseholdCropIncome(QDialog, Ui_AddHouseholdIncomeCrops):	
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
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveIncome)
        
    def getCropTypes(self):
		''' Retrieve Crop Types and display them in a combobox '''
		# select query to Crop Types
		query = '''SELECT foodtype FROM setup_crops'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    croptype = row[0]
		    self.cboIncomeType.addItem(croptype)
		 
		cursor.close()   
		db.close()
        
    def displayIncomeDetails(self):
		''' Retrieve and display Household Income details '''
		query = '''SELECT * FROM cropincome WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    croptype = row[2]
		    self.cboIncomeType.setCurrentIndex( self.cboIncomeType.findText( croptype ) )
		    unitofmeasure = row[3]
		    self.txtUnitOfMeasure.setText( unitofmeasure )
		    unitsconsumed = row[4]
		    self.txtUnitsConsumed.setText( str(unitsconsumed) )
		    unitssold = row[5]
		    self.txtUnitsSold.setText( str(unitssold) )
		    unitprice = row[6]
		    self.txtUnitPrice.setText( str(unitprice) )
		 
		cursor.close()   
		db.close()
        
    def saveIncome(self):
		''' Saves crop income to database '''    	
		
		# get the data entered by user
		croptype      	= self.cboIncomeType.currentText()
		unitofmeasure	= self.txtUnitOfMeasure.text()
		unitsconsumed	= self.txtUnitsConsumed.text()
		unitssold		= self.txtUnitsSold.text()
		unitprice		= self.txtUnitPrice.text()
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO cropincome (hhid, incomesource, unitofmeasure, unitsconsumed, unitssold, unitprice, pid )
			    VALUES(%s,'%s','%s',%s,%s,%s, %s) ''' % ( self.hhid, croptype, unitofmeasure, unitsconsumed, unitssold, unitprice,  self.pid )
		else:
			query = ''' UPDATE cropincome SET incomesource='%s', unitofmeasure='%s', unitsconsumed=%s, unitssold=%s,
						unitprice=%s WHERE hhid=%s AND pid=%s 
						AND id=%s ''' % ( croptype, unitofmeasure, unitsconsumed, unitssold, unitprice, self.hhid, self.pid,  self.incomeid)
		
		# execute query and commit changes
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdCropIncome()
		self.close()
