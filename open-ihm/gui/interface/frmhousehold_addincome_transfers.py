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
		
		self.getTransferTypes()
		
		if ( incomeid != 0 ):
			self.displayIncomeDetails()
			self.setWindowTitle( "Edit Income Item" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveIncome)
        
    def getTransferTypes(self):
		''' Retrieve Transfer Types and display them in a combobox '''
		# select query to Transfer Types
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
		query = '''SELECT *
				   FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    assistancetype = row[2]
		    self.cboAssistanceType.setCurrentIndex( self.cboAssistanceType.findText( assistancetype ) )
		    unitofmeasure = row[3]
		    self.txtUnitOfMeasure.setText( unitofmeasure )
		    foodperdist = row[5]
		    self.txtFoodPerDist.setText( str(foodperdist) )
		    numreceived = row[6]
		    self.txtNumReceived.setText( str(numreceived) )
		    cashperdist = row[7]
		    self.txtCashPerDist.setText( str(cashperdist) )
		    cashperyear = row[9]
		    self.txtCashPerYear.setText( str(cashperyear) )
		 
		cursor.close()   
		db.close()
        
    def saveIncome(self):
		''' Saves transfer income to database '''    	
		
		# get the data entered by user
		assistancetype  = self.cboAssistanceType.currentText()
		unitofmeasure	= self.txtUnitOfMeasure.text()
		sourcetype		= "External"
		foodperdist		= self.txtFoodPerDist.text()
		numreceived		= self.txtNumReceived.text()
		cashperdist		= self.txtCashPerDist.text()
		cashperyear		= self.txtCashPerYear.text()
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO transfers (hhid, assistancetype, unitofmeasure, sourcetype, foodperdistribution,
			           cashperdistribution, numberoftimesreceived, cashperyear, pid ) VALUES(%s,'%s','%s','%s',%s,%s,%s,%s,%s)
					''' % (self.hhid, assistancetype, unitofmeasure, sourcetype, foodperdist, cashperdist, numreceived, cashperyear, self.pid)
		else:
			query = ''' UPDATE transfers 
					    SET assistancetype='%s', unitofmeasure='%s', sourcetype='%s', foodperdistribution=%s, cashperdistribution=%s,
					    numberoftimesreceived=%s, cashperyear=%s
						WHERE hhid=%s AND pid=%s AND id=%s 
					''' % ( assistancetype, unitofmeasure, sourcetype, foodperdist, cashperdist, numreceived, cashperyear, self.hhid, self.pid,  self.incomeid)
		
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
