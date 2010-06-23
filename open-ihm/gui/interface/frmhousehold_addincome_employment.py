#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_employment.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_employment import Ui_AddHouseholdIncomeEmployment

class FrmHouseholdEmploymentIncome(QDialog, Ui_AddHouseholdIncomeEmployment):	
	''' Form to add or edit a Household Employment Income  '''	
	def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.hhid 		= hhid
		self.incomeid 	= incomeid
		
		self.config = Config.dbinfo().copy()
		
		self.getEmploymentTypes()
		self.getFoodTypes()
		
		if ( incomeid != 0 ):
			self.displayIncomeDetails()
			self.setWindowTitle( "Edit Income Item" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveIncome)
	    
	def getEmploymentTypes(self):
		''' Retrieve Employment Types and display them in a combobox '''
		# select query to Employment Types
		query = '''SELECT incomesource FROM setup_employment'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    employmenttype = row[0]
		    self.cboEmploymentType.addItem(employmenttype)
		 
		cursor.close()   
		db.close()
	
	def getFoodTypes(self):
		''' Retrieve Food Types and display them in a combobox listing type of food payments '''
		self.cboFoodType.addItem("None")
		# select query to Food Types
		query = '''SELECT foodtype FROM setup_crops'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    foodtype = row[0]
		    self.cboFoodType.addItem(foodtype)
		 
		cursor.close()   
		db.close()
	    
	def displayIncomeDetails(self):
		''' Retrieve and display Household Income details '''
		query = '''SELECT *
				   FROM employmentincome WHERE hhid=%s AND id=%s ''' % ( self.hhid, self.incomeid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    employmenttype = row[2]
		    self.cboEmploymentType.setCurrentIndex( self.cboEmploymentType.findText( employmenttype ) )
		    foodtype = row[3]
		    self.cboFoodType.setCurrentIndex( self.cboFoodType.findText( foodtype ) )
		    unitofmeasure = row[4]
		    self.txtUnitOfMeasure.setText( str(unitofmeasure) )
		    unitspaid = row[5]
		    self.txtUnitsPaid.setText( str(unitspaid) )
		    incomekcal = row[6]
		    self.txtTotalEnergyValue.setText( str(incomekcal) )
		    cashincome = row[7]
		    self.txtCashPaid.setText( str(cashincome) )
		 
		cursor.close()   
		db.close()
	    
	def saveIncome(self):
		''' Saves employment income to database '''    	
		
		# get the data entered by user
		employmenttype  = self.cboEmploymentType.currentText()
		foodtype		= self.cboFoodType.currentText()
		if (foodtype != "None"):
			unitofmeasure	= self.txtUnitOfMeasure.text() if self.txtUnitOfMeasure.text() != "" else "n/a"
			unitspaid		= self.txtUnitsPaid.text() if self.txtUnitsPaid.text() != "" else "0"
			incomekcal		= self.txtTotalEnergyValue.text() if self.txtTotalEnergyValue.text() != "" else "0"
		else:
			unitofmeasure  	= "n/a"
			unitspaid		= "0"
			incomekcal		= "0"
		cashpaid		= self.txtCashPaid.text() if self.txtCashPaid.text() != "" else "0"
		
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO employmentincome (hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid,
			           incomekcal, cashincome ) VALUES(%s,'%s','%s','%s',%s,%s,%s)
					''' % (self.hhid, employmenttype, foodtype, unitofmeasure, unitspaid, incomekcal, cashpaid)
		else:
			query = ''' UPDATE employmentincome 
					    SET incomesource='%s', foodtypepaid='%s', unitofmeasure='%s', unitspaid=%s, incomekcal=%s,
					    cashincome=%s
						WHERE hhid=%s AND id=%s 
					''' % ( employmenttype, foodtype, unitofmeasure, unitspaid, incomekcal, cashpaid, self.hhid, self.incomeid)
		
		# execute query and commit changes
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdEmploymentIncome()
		self.close()