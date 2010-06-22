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
		self.incomeid 	= incomeid
		
		self.config = Config.dbinfo().copy()
		
		self.getLivestockTypes()
		
		if ( incomeid != 0 ):
			self.displayIncomeDetails()
			self.setWindowTitle( "Edit Income Item" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveIncome)
        
    def getLivestockTypes(self):
		''' Retrieve Livestock Types and display them in a combobox '''
		# select query to Livestock Types
		query = '''SELECT incomesource FROM setup_livestock'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    incometype = row[0]
		    self.cboIncomeType.addItem(incometype)
		 
		cursor.close()   
		db.close()
        
    def displayIncomeDetails(self):
		''' Retrieve and display Household Income details '''
		query = '''SELECT * FROM livestockincome WHERE hhid=%s AND id=%s ''' % ( self.hhid, self.incomeid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    incometype = row[2]
		    self.cboIncomeType.setCurrentIndex( self.cboIncomeType.findText( incometype ) )
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
		''' Saves livestock income to database '''    	
		
		# get the data entered by user
		incometype   	= self.cboIncomeType.currentText()
		unitofmeasure	= self.txtUnitOfMeasure.text()
		unitsconsumed	= self.txtUnitsConsumed.text()
		unitssold		= self.txtUnitsSold.text()
		unitprice		= self.txtUnitPrice.text()
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO livestockincome (hhid, incomesource, unitofmeasure, unitsconsumed, unitssold, unitprice )
			    VALUES(%s,'%s','%s',%s,%s,%s) ''' % ( self.hhid, incometype, unitofmeasure, unitsconsumed, unitssold, unitprice )
		else:
			query = ''' UPDATE livestockincome SET incomesource='%s', unitofmeasure='%s', unitsconsumed=%s, unitssold=%s,
						unitprice=%s WHERE hhid=%s 
						AND id=%s ''' % ( incometype, unitofmeasure, unitsconsumed, unitssold, unitprice, self.hhid, self.incomeid)
		
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