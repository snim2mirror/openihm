#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_gifts.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_gifts import Ui_AddHouseholdIncomeGifts

class FrmHouseholdGiftsIncome(QDialog, Ui_AddHouseholdIncomeGifts):	
    ''' Form to add or edit a Household Gifts Income  '''	
    def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.hhid 		= hhid
		self.incomeid 	= incomeid
		
		self.config = Config.dbinfo().copy()
		
		self.getGiftsTypes()
		
		if ( incomeid != 0 ):
			self.displayIncomeDetails()
			self.setWindowTitle( "Edit Income Item" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveIncome)
        
    def getGiftsTypes(self):
		''' Retrieve Gifts Types and display them in a combobox '''
		# select query to Gifts Types
		query = '''SELECT assistancetype FROM setup_transfers'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    assistancetype = row[0]
		    self.cboAssistanceType.addItem(assistancetype)
		 
		cursor.close()   
		db.close()
        
    def displayIncomeDetails(self):
		''' Retrieve and display Household Income details '''
		query = '''SELECT assistancetype, unitofmeasure, unitsconsumed 
				   FROM transfers WHERE hhid=%s AND id=%s ''' % ( self.hhid, self.incomeid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    assistancetype = row[0]
		    self.cboAssistanceType.setCurrentIndex( self.cboAssistanceType.findText( assistancetype ) )
		    unitofmeasure = row[1]
		    self.txtUnitOfMeasure.setText( unitofmeasure )
		    unitsconsumed = row[2]
		    self.txtUnitsConsumed.setText( str(unitsconsumed) )
		 
		cursor.close()   
		db.close()
        
    def saveIncome(self):
		''' Saves gifts income to database '''    	
		
		# get the data entered by user
		assistancetype  = self.cboAssistanceType.currentText()
		unitofmeasure	= self.txtUnitOfMeasure.text()
		unitsconsumed	= self.txtUnitsConsumed.text()
		sourcetype		= "Internal"
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO transfers (hhid, assistancetype, unitofmeasure, unitsconsumed, sourcetype )
			    VALUES(%s,'%s','%s',%s,'%s') ''' % ( self.hhid, assistancetype, unitofmeasure, unitsconsumed, sourcetype )
		else:
			query = ''' UPDATE transfers SET assistancetype='%s', unitofmeasure='%s', unitsconsumed=%s, sourcetype='%s'
						WHERE hhid=%s 
						AND id=%s ''' % ( assistancetype, unitofmeasure, unitsconsumed, sourcetype, self.hhid, self.incomeid)
		
		# execute query and commit changes
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdGiftsIncome()
		self.close()