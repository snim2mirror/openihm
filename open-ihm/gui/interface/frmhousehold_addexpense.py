#-------------------------------------------------------------------	
#	Filename: frmhousehold_addexpense.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_addexpense import Ui_AddHouseholdExpense

class FrmHouseholdExpense(QDialog, Ui_AddHouseholdExpense):	
    ''' Form to add or edit Household Expenditure  '''	
    def __init__(self, parent,  hhid, hhname, expid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.pid  = parent.parent.projectid
		self.hhid 		= hhid
		self.expid 		= expid
		
		self.config = Config.dbinfo().copy()
		
		self.getExpenditureTypes()
		
		if ( expid != 0 ):
			self.displayExpenditureDetails()
			self.setWindowTitle( "Edit Household Expenditure" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
    def mdiClose(self):
        self.parent.mdi.closeActiveSubWindow()

                
    def getExpenditureTypes(self):
		''' Retrieve Expenditure Types and display them in a combobox '''
		# select query to Asset Types
		query = '''SELECT expendituretype FROM setup_expendituretypes'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    exptype = row[0]
		    self.cboExpenditure.addItem(exptype)
		 
		cursor.close()   
		db.close()
        
    def displayExpenditureDetails(self):
		''' Retrieve and display Household Expenditure details '''
		query = '''SELECT * FROM expenditure WHERE hhid=%s AND pid=%s AND expid=%s ''' % ( self.hhid, self.pid, self.expid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
			exptype = row[2]
			self.cboExpenditure.setCurrentIndex( self.cboExpenditure.findText( exptype ) )
			unitofmeasure = row[3]
			self.txtUnitOfMeasure.setText( unitofmeasure )
			costperunit = row[4]
			self.txtCostPerUnit.setText( str(costperunit) )
			kcalperunit = row[5]
			if ( kcalperunit == None ):
				kcalperunit = ""
			self.txtKCalPerUnit.setText( str(kcalperunit) )
			numunits = row[6]
			self.txtNumberOfUnits.setText( str(numunits) )
		 
		cursor.close()   
		db.close()
        
    def saveExpenditure(self):
		''' Saves expenditure to database '''    	
		
		# get the data entered by user
		exptype       = self.cboExpenditure.currentText()
		unitofmeasure = self.txtUnitOfMeasure.text()
		costperunit   = self.txtCostPerUnit.text()
		kcalperunit	  = self.txtKCalPerUnit.text()
		numunits      = self.txtNumberOfUnits.text()
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		expid 	= self.expid
		hhid 	= self.hhid
		if (kcalperunit == ""):
			kcalperunit = "NULL"
			
		if (expid == 0):
			query = '''INSERT INTO expenditure (hhid, exptype, unitofmeasure, priceperunit, kcalperunit, totalunits, pid )
			    VALUES(%s,'%s','%s',%s,%s,%s,%s) ''' % ( hhid, exptype, unitofmeasure, costperunit, kcalperunit, numunits,  self.pid )
		else:
			query = ''' UPDATE expenditure SET exptype='%s', unitofmeasure='%s', priceperunit=%s, kcalperunit=%s,
						totalunits=%s WHERE hhid=%s AND pid=%s 
						AND expid=%s ''' % ( exptype, unitofmeasure, costperunit, kcalperunit, numunits, hhid, self.pid,  expid )
                        
#		QMessageBox.information(self,"Edit Member",query)
		
		# execute query and commit changes
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdExpenses()
		self.close()
