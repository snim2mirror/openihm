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

Ui_AddHouseholdIncomeEmployment, base_class = uic.loadUiType("gui/designs/ui_household_income_employment.ui")

from mixins import MDIDialogMixin, MySQLMixin

class FrmHouseholdEmploymentIncome(QDialog, Ui_AddHouseholdIncomeEmployment, MySQLMixin, MDIDialogMixin):	
	''' Form to add or edit a Household Employment Income  '''	
	def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.hhid 		= hhid
		self.pid = parent.parent.projectid
		self.incomeid 	= incomeid
		
		self.config = Config.dbinfo().copy()
		
		self.getEmploymentTypes()
		self.getFoodTypes()
		
		if ( incomeid != 0 ):
			self.displayIncomeDetails()
			self.setWindowTitle( "Edit Income Item" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)

	def getEmploymentTypes(self):
		''' Retrieve Employment Types and display them in a combobox '''
		# select query to Employment Types
		query = '''SELECT incomesource FROM setup_employment'''
		
		rows = self.executeResultsQuery(query)
		
		for row in rows:
		    employmenttype = row[0]
		    self.cboEmploymentType.addItem(employmenttype)
	
	def getFoodTypes(self):
		''' Retrieve Food Types and display them in a combobox listing type of food payments '''
		self.cboFoodType.addItem("None")
		# select query to Food Types
		query = '''SELECT name FROM setup_foods_crops '''
		rows = self.executeResultsQuery(query)
		
		for row in rows:
		    foodtype = row[0]
		    self.cboFoodType.addItem(foodtype)

	def displayIncomeDetails(self):
		''' Retrieve and display Household Income details '''
		query = '''SELECT *
				   FROM employmentincome WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
		
		rows = self.executeResultsQuery(query)
		for row in rows:
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
		
			
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO employmentincome (hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid,
			           incomekcal, cashincome, pid ) VALUES(%s,'%s','%s','%s',%s,%s,%s,%s)
					''' % (self.hhid, employmenttype, foodtype, unitofmeasure, unitspaid, incomekcal, cashpaid, self.pid)
		else:
			query = ''' UPDATE employmentincome 
					    SET incomesource='%s', foodtypepaid='%s', unitofmeasure='%s', unitspaid=%s, incomekcal=%s,
					    cashincome=%s
						WHERE hhid=%s AND pid=%s AND id=%s 
					''' % ( employmenttype, foodtype, unitofmeasure, unitspaid, incomekcal, cashpaid, self.hhid, self.pid, self.incomeid)
		
		self.executeUpdate(query)
		
		# close new project window
		self.parent.retrieveHouseholdEmploymentIncome()
		self.mdiClose()
