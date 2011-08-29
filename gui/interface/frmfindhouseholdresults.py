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

# import the Create Project Dialog design class
from gui.designs.ui_findhouseholdresults import Ui_FindHouseholdResults
from frmhouseholds_add import FrmAddHousehold
from frmhouseholds_edit import FrmEditHousehold
from frmhousehold_data import FrmHouseholdData

from mixins import MDIDialogMixin

class FrmFindHouseholdResults(QDialog, Ui_FindHouseholdResults, MDIDialogMixin):
	''' Creates the Find Household Results form. '''	
	def __init__(self, parent, hhid = "", hhname = ""):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent = parent
		self.config = Config.dbinfo().copy()
		
		self.lblProjectName.setText( self.parent.projectname ) 
		self.txtHouseholdNo.setText( hhid )
		self.txtHouseholdName.setText ( hhname )
		
		self.getHouseholds()
		
	def getHouseholds(self):
		''' display households matching the criteria entered by user '''
		hhid 			= self.txtHouseholdNo.text()
		hhname 			= self.txtHouseholdName.text()
	
		SQLcondition 	= ""
		if ( hhid != "" ):
			SQLcondition = " hhid='%s'" % ( hhid )
		
		if ( hhname != "" ):
			if ( SQLcondition == "" ):
				SQLcondition = "householdname LIKE '%" + "%s" % ( hhname ) + "%'" 
			else:
				SQLcondition = "(" + SQLcondition + " OR householdname LIKE '%" + "%s" % ( hhname ) + "%' )" 
		
		if ( SQLcondition != "" ):		 
			query = ''' SELECT hhid, householdname, dateofcollection 
					FROM households WHERE pid=%i AND %s ''' % ( self.parent.projectid, SQLcondition )
		else:
			query = ''' SELECT hhid, householdname, dateofcollection 
					FROM households WHERE pid=%i ''' % ( self.parent.projectid )
		
		rows = self.executeResultsQuery(query)
		count = len( rows )
		
		self.setWindowTitle("%i matching household(s) found." % (count) )
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Household No.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Household Name'))
		model.setHorizontalHeaderItem(2,QStandardItem('Date of Collection'))
		
		# add  data rows
		num = 0
	    
		for row in rows:
		    qtHouseholdNo = QStandardItem( "%i" % row[0])
		    qtHouseholdNo.setTextAlignment( Qt.AlignCenter )
		    
		    qtHouseholdName = QStandardItem( row[1] )
		    
		    qtDateCollected = QStandardItem( QDate(row[2]).toString("dd/MM/yyyy") )
		    qtDateCollected.setTextAlignment( Qt.AlignCenter )
		    
		    model.setItem( num, 0, qtHouseholdNo )
		    model.setItem( num, 1, qtHouseholdName )
		    model.setItem( num, 2, qtDateCollected )

		    num = num + 1
	    
		self.tblResults.setModel(model)
		self.tblResults.resizeColumnsToContents()
		self.tblResults.show()
		
	def addHousehold(self):
		''' Show the Add Household form '''
		# get project id and name
		projectid	= self.parent.projectid
		projectname = self.parent.projectname
		
		# show the add household  form
		form = FrmAddHousehold(self, projectid, projectname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		form.exec_()
		
	def editHousehold(self):
		''' Show the Edit Household form '''
		if self.countRowsSelected(self.tblResults) != 0:
			# get the hhid of the selected household
			selectedRow = self.getCurrentRow(self.tblResults)
			hhid = self.tblResults.model().item(selectedRow,0).text()
			# get project id and name
			projectid	= self.parent.projectid
			projectname = self.parent.projectname
			# show edit household member form
			form = FrmEditHousehold(self, projectid, projectname, hhid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			QMessageBox.information(self,"Edit Household","Please select the row containing a household to be editted.")
		
	def delHouseholds(self):
		''' Delete selected households '''
		numSelected = self.countRowsSelected( self.tblResults )
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household?"
			else:
				msg = "Are you sure you want to delete the selected households?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the hhid of the selected households
			selectedRows = self.getSelectedRows(self.tblResults)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblResults.model().item(row,0).text() )
			 
			# delete selected households
			
			for hhid in selectedIds:
				query = '''DELETE FROM households WHERE hhid=%s ''' % (hhid)	
				self.executeUpdateQuery(query)
    			
			self.getHouseholds()

		else:
			QMessageBox.information(self,"Delete Households","Please select the rows containing households to be deleted.")
		
	def viewHouseholdData(self):
		''' show the household data for the selected household '''
		if self.countRowsSelected(self.tblResults) != 0:
			# get the hhid of the selected household
			selectedRow = self.getCurrentRow(self.tblResults)
			hhid = self.tblResults.model().item(selectedRow,0).text()
		
			# show household data form
			form = FrmHouseholdData(self.parent,hhid)
			subWin = self.parent.mdi.addSubWindow(form)
			self.parent.centerSubWindow(subWin)
			form.show()
		else:
			msg = "Please select the row containing a household whose data you want to view or edit."
			QMessageBox.information(self,"View|Edit Household Data",msg)
		
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
		
			
