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

from data.config import Config
import includes.mysql.connector as connector

from gui.designs.ui_foodenergy_requirements import Ui_FoodEnergyRequirements
from frmfoodenergyrequirement_add import FrmAddEnergyRequirement
from frmfoodenergyrequirement_edit import FrmEditEnergyRequirement
from data.foodenergyrequirement import FoodEnergyRequirement

from mixins import MDIDialogMixin

class FrmFoodEnergyRequirements(QDialog, Ui_FoodEnergyRequirements, MDIDialogMixin):	
	''' Creates the view food energy requirements form '''	
	def __init__(self, parent):
	    ''' Set up the dialog box interface '''
	    self.parent = parent
	    QDialog.__init__(self)
	    self.setupUi(self)
	    self.parent = parent
	    self.config = Config.dbinfo().copy()
	    
	    # get food energy requirement details by sex and age
	    self.getFoodEnergyRequirements()

	def getFoodEnergyRequirements(self):
		# connect to mysql database
		db = connector.Connect(**self.config)
		cursor = db.cursor()
		
		# select query to retrieve project households
                query = '''SELECT age, kCalNeedM, kCalNeedF FROM lookup_energy_needs'''
                
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
				
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('''Person's Age'''))
		model.setHorizontalHeaderItem(1,QStandardItem('Energy Requirement - Males'))
		model.setHorizontalHeaderItem(2,QStandardItem('Energy Requirement - Females'))
		
		# add  data rows
		num = 0
	    
		for row in cursor.fetchall():
		    qtAge = QStandardItem( "%i" % row[0])
		    qtAge.setTextAlignment( Qt.AlignCenter )
		    
		    qtEnergyRequirementMales = QStandardItem( "%i" % row[1] )
		    qtEnergyRequirementMales.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    qtEnergyRequirementFemales = QStandardItem( "%i" % row[2] )
		    qtEnergyRequirementFemales.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    model.setItem( num, 0, qtAge )
		    model.setItem( num, 1, qtEnergyRequirementMales )
		    model.setItem( num, 2, qtEnergyRequirementFemales )
		    num = num + 1
	    
		self.tableView.setModel(model)
		#self.tableView.verticalHeader().hide()
                self.tableView.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
		self.tableView.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
		self.tableView.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
		self.tableView.show()
		
		cursor.close()
		db.close()
		


	def addFoodEnergyRequirement(self):
		''' Show the Add Food Energy Requirement form '''
		
		form = FrmAddEnergyRequirement(self)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
                form.exec_()
		self.getFoodEnergyRequirements()

	def editFoodEnergyRequirement(self):
		if self.countRowsSelected(self.tableView) != 0:
			# get the age of the selected record
			selectedRow = self.getCurrentRow(self.tableView)
			selectedage = self.tableView.model().item(selectedRow,0).text()
			energyreqmale = self.tableView.model().item(selectedRow,1).text()
			energyreqfemale = self.tableView.model().item(selectedRow,2).text()

			# show edit food energy requirement form
			form = FrmEditEnergyRequirement(self.parent,selectedage,energyreqmale,energyreqfemale)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			self.getFoodEnergyRequirements()
			
		else:
			QMessageBox.information(self,"Edit Food Energy Requirement","Please select the row containing food energy requirements to be edited.")


	def deleteSelectedEnergyRequirements(self):

		numSelected = self.countRowsSelected(self.tableView)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected record?"
			else:
				msg = "Are you sure you want to delete the selected records?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the age of the selected records
			selectedRows = self.getSelectedRows(self.tableView)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tableView.model().item(row,0).text() )
			 
			# delete record with selected age
			
			db = connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for myage in selectedIds:
				query = '''DELETE FROM lookup_energy_needs WHERE age=%s ''' % (myage)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
			self.getFoodEnergyRequirements()

		else:
			QMessageBox.information(self,"Delete Food Energy Requirements","Please select the rows containing food energy requirements to be deleted.")

	def countRowsSelected(self, tblVw):
		selectedRows = self.getSelectedRows(tblVw)
		return len(selectedRows)
		
	def getSelectedRows(self, tblVw):
		
		selectedRows = []
		selectedIndexes = tblVw.selectedIndexes()
		
		for indexVal in selectedIndexes:
			if indexVal.row() not in selectedRows:
				selectedRows.append(indexVal.row())
				
		return selectedRows
	
	def getCurrentRow(self, tblVw):
		indexVal = tblVw.currentIndex()
		return indexVal.row()

