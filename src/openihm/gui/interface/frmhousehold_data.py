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
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from data.config import Config
from control.controller import Controller
from data.db import session_scope
from model.alchemy_schema import Householdmember
import alchemy.household_members as household_members


Ui_HouseholdData, base_class = uic.loadUiType("gui/designs/ui_household_data.ui")


from frmhousehold_addmember import FrmAddHouseholdMember
from frmhousehold_editmember import FrmEditHouseholdMember
from frmhousehold_editcharacteristic import FrmEditHouseholdCharacteristic
from frmhousehold_editpersonalcharacteristic import FrmEditPersonalCharacteristic
from frmhousehold_addasset import FrmHouseholdAsset
from frmhousehold_addexpense import FrmHouseholdExpense
from frmhousehold_addincome_crop import FrmHouseholdCropIncome
from frmhousehold_addincome_livestock import FrmHouseholdLivestockIncome
from frmhousehold_addincome_wildfoods import FrmHouseholdWildfoodsIncome
from frmhousehold_addincome_gifts import FrmHouseholdGiftsIncome
from frmhousehold_addincome_transfers import FrmHouseholdTransferIncome
from frmhousehold_addincome_employment import FrmHouseholdEmploymentIncome

from mixins import MDIDialogMixin, MySQLMixin, TableViewMixin

class FrmHouseholdData(QDialog, Ui_HouseholdData, MySQLMixin, TableViewMixin, MDIDialogMixin):	
	''' Creates the household data (income, assets, expenditure, etc) form '''	
	def __init__(self, parent, hhid=0):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent = parent
		
		self.hhCharacteristicsTable = "p%iHouseholdCharacteristics" % (self.parent.projectid )
		self.psCharacteristicsTable = "p%iPersonalCharacteristics" % (self.parent.projectid )
		# connect to database
		self.config = Config.dbinfo().copy()
		
		# get house holds
		self.getHouseholds()
		
		# set current house hold
		if hhid != 0:
			self.cboHouseholdNumber.setCurrentIndex(self.cboHouseholdNumber.findData(QVariant(hhid)))
		
		# retrieve members
		self.displayHouseholdData()

	def displayHouseholdData(self):
		self.setWindowTitle("Household Data - " + self.cboHouseholdNumber.currentText())
		self.retrieveHouseholdMembers()
		self.retrieveHouseholdAssets()
		self.retrieveHouseholdExpenses()
		self.retrieveHouseholdCropIncome()
		self.retrieveHouseholdLivestockIncome()
		self.retrieveHouseholdWildfoodsIncome()
		self.retrieveHouseholdGiftsIncome()
		self.retrieveHouseholdTransferIncome()
		self.retrieveHouseholdEmploymentIncome()
		self.retrieveHouseholdCharacteristics()
		
		self.tabHouseHold.setCurrentIndex(0)
		
	def getHouseholds(self):
		# select query to retrieve project data
		query = '''SELECT hhid, householdname 
		             FROM households WHERE pid=%i''' % (self.parent.projectid)
		
		rows = self.executeResultsQuery(query)
		for row in rows:
		    hhid = row[0]
		    householdname = row[1]
		    self.cboHouseholdNumber.addItem(householdname, QVariant(hhid))
		
	#-----------------------------------------------------------------------------------
	#	Household Members
	#-----------------------------------------------------------------------------------
	
	def addHouseholdMember(self):
		''' Show the Add Household Member form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmAddHouseholdMember(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household member form
		form.exec_()
		
	def editHouseholdMember(self):
		if self.countRowsSelected(self.tblMembers) != 0:
			# get the member id of the selected member
			selectedRow = self.getCurrentRow(self.tblMembers)
			if ( self.tblMembers.model().item(selectedRow, 0) != None ):
			     memberid = self.tblMembers.model().item(selectedRow,0).text()
			else:
			     memberid = ""
			if ( memberid == "" ):
			     return
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household member form
			form = FrmEditHouseholdMember(self, hhid, hhname, memberid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			QMessageBox.information(self,"Edit Member","Please select the row containing a member to be editted.")
			
	def delHouseholdMembers(self):
		numSelected = self.countRowsSelected(self.tblMembers)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household member?"
			else:
				msg = "Are you sure you want to delete the selected household members?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the member id of the selected members
			selectedRows = self.getSelectedRows(self.tblMembers)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblMembers.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			# delete selected members
			
			with session_scope() as session:
			    projectid = self.parent.projectid
			    household_members.remove_members(session, hhid, projectid, selectedIds)

			self.retrieveHouseholdMembers()

		else:
			QMessageBox.information(self,"Delete Members","Please select the rows containing members to be deleted.")
		
	def retrieveHouseholdMembers(self):
		''' retrieves and shows a list of household members '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0] 
		pid = self.parent.projectid
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Member ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Head of Household'))
		model.setHorizontalHeaderItem(2,QStandardItem('Age'))
		model.setHorizontalHeaderItem(3,QStandardItem('Sex'))
		model.setHorizontalHeaderItem(4,QStandardItem('Months Absent'))        
		
		# add  data rows
		num = 0
		# select query to retrieve household members
		query = '''SELECT personid, headofhousehold, yearofbirth, sex, periodaway 
		             FROM householdmembers WHERE hhid=%i and pid=%i ORDER BY yearofbirth ''' % (hhid,  pid)
		
		rows = self.executeResultsQuery(query)
		for row in rows:
			qtMemberID = QStandardItem(row[0])
			qtMemberID.setTextAlignment( Qt.AlignCenter )
			qtHouseholdHead = QStandardItem( row[1] )
			age = date.today().year - row[2]
			qtAge = QStandardItem( "%i" % age )
			
			qtSex = QStandardItem( row[3] )
			qtMonthsAbsent = QStandardItem( "%i" % row[4] )
			qtMonthsAbsent.setTextAlignment( Qt.AlignCenter)
			
			model.setItem( num, 0, qtMemberID )
			model.setItem( num, 1, qtHouseholdHead )
			model.setItem( num, 2, qtAge )
			model.setItem( num, 3, qtSex )
			model.setItem( num, 4, qtMonthsAbsent )            
			num = num + 1
		
		self.tblMembers.setModel(model)
		self.tblMembers.resizeColumnsToContents()
		# display personal characteristics
		personid = "0"
		if ( num > 0 ):
		     self.tblMembers.selectRow(0)
		     selectedRow = self.getCurrentRow(self.tblMembers)
		     personid = self.tblMembers.model().item(selectedRow,0).text()
		     self.cmdEditMember.setEnabled( True )
		     self.cmdDelMember.setEnabled( True )
		else:
		     self.cmdEditMember.setEnabled( False )
		     self.cmdDelMember.setEnabled( False )
		     self.cmdEditPersonalCharacteristic.setEnabled( False )
		
		if (num > 0):
		     self.retrievePersonalCharacteristics(personid)
		
	def showMemberPersonalCharacteristics(self):
         ''' show personal characteristics of selected household member '''
         selectedRow = self.getCurrentRow(self.tblMembers)
         if ( self.tblMembers.model().item(selectedRow, 0) != None ):
             personid = self.tblMembers.model().item(selectedRow,0).text()
             self.retrievePersonalCharacteristics(personid)
         else:
             personid = "0"
         
         
	#-----------------------------------------------------------------------------------
	#	Personal Characteristics
	#-----------------------------------------------------------------------------------
	
	def getPersonalCharacteristicDataType(self, charName):
		controller = Controller()
		char = controller.getGlobalCharacteristic(charName)
		if char.name != "": 
		     return char.datatype
		else:
		     return 3
	
	def retrievePersonalCharacteristics( self,  personid ):
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]

		controller = Controller()
		project = controller.getProject(self.parent.projectid)
		household = project.getHousehold(hhid)
		member = household.getMember(personid)
		chars = member.getAllCharacteristics()    # get set and unset characteristics
		
		model = QStandardItemModel(1,1)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
		model.setHorizontalHeaderItem(1,QStandardItem('Value'))
		
		# add  data rows
		num = 0
		
		for char in chars:
			qtChar 	= QStandardItem( char.name )
			if ( ( self.getPersonalCharacteristicDataType( char.name ) == 2 ) and (char.charvalue != "Not Set") ):
				qtVal	= QStandardItem( "%i" % int( char.charvalue))
			else:
				qtVal	= QStandardItem( "%s" % char.charvalue )
				
			model.setItem( num, 0, qtChar )
			model.setItem( num, 1, qtVal )
				
			num = num + 1
		
		self.tblPersonalCharacteristics.setModel(model)
		self.tblPersonalCharacteristics.resizeColumnsToContents()
		self.tblPersonalCharacteristics.show()
		
		header = "Personal Characteristics for %s" % personid if personid != "0" else "Personal Characteristics"
		self.lblPersonalCharacteristicsHeader.setText( header )
		if ( ( personid != "0" ) and ( num != 0 ) ):
		     self.cmdEditPersonalCharacteristic.setEnabled( True )
		else:
		     self.cmdEditPersonalCharacteristic.setEnabled( False )
		
	def editPersonalCharacteristic(self):
		if self.countRowsSelected(self.tblPersonalCharacteristics) != 0:
			# get member id
			selectedRow = self.getCurrentRow(self.tblMembers)
			if ( self.tblMembers.model().item(selectedRow, 0) != None ):
			     personid = self.tblMembers.model().item(selectedRow,0).text()
			else:
			     personid = "0"
			# get current details of the selected characteristics
			selectedRow = self.getCurrentRow(self.tblPersonalCharacteristics)
			charName = self.tblPersonalCharacteristics.model().item(selectedRow,0).text()
			charVal	 = self.tblPersonalCharacteristics.model().item(selectedRow,1).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			# show edit household member form
			form = FrmEditPersonalCharacteristic(self, self.parent.projectid, hhid, personid, charName, charVal)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing a characteristic to be editted."
			QMessageBox.information(self,"Edit Characteristic", msg)	
	
	#-----------------------------------------------------------------------------------
	#	Household Characteristics
	#-----------------------------------------------------------------------------------
	
	def getCharacteristicDataType(self, charName):
		controller = Controller()
		char = controller.getGlobalCharacteristic(charName)
		if char.name != "": 
		     return char.datatype
		else:
		     return 3
	
	def retrieveHouseholdCharacteristics( self ):
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		controller = Controller()
		project = controller.getProject(self.parent.projectid)
		household = project.getHousehold(hhid)
		chars = household.getAllCharacteristics()    # get set and unset characteristics
		
		model = QStandardItemModel(1,1)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
		model.setHorizontalHeaderItem(1,QStandardItem('Value'))
		
		# add  data rows
		num = 0
		
		for char in chars:
			qtChar 	= QStandardItem( char.name )
			if ( ( self.getCharacteristicDataType( char.name ) == 2 ) and (char.charvalue != "Not Set") ):
				qtVal	= QStandardItem( "%i" % int( char.charvalue))
			else:
				qtVal	= QStandardItem( "%s" % char.charvalue )
				
			model.setItem( num, 0, qtChar )
			model.setItem( num, 1, qtVal )
				
			num = num + 1
		
		self.tblCharacteristics.setModel(model)
		self.tblCharacteristics.resizeColumnsToContents()
		self.tblCharacteristics.show()
		
	def editCharacteristic(self):
		if self.countRowsSelected(self.tblCharacteristics) != 0:
			# get the member id of the selected member
			selectedRow = self.getCurrentRow(self.tblCharacteristics)
			charName = self.tblCharacteristics.model().item(selectedRow,0).text()
			charVal	 = self.tblCharacteristics.model().item(selectedRow,1).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			# show edit household member form
			form = FrmEditHouseholdCharacteristic(self, self.parent.projectid, hhid, charName, charVal)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing a characteristic to be editted."
			QMessageBox.information(self,"Edit Characteristic", msg)	
		
	#-------------------------------------------------------------------------------------------------------
	# Assets
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdAsset(self):
		''' Show the Add Household Member form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdAsset(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household asset form
		form.exec_()
		
	def editHouseholdAsset(self):
		if self.countRowsSelected(self.tblAssets) != 0:
			# get the asset id of the selected asset
			selectedRow = self.getCurrentRow(self.tblAssets)
			assetid = self.tblAssets.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household asset form
			form = FrmHouseholdAsset(self, hhid, hhname, assetid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			QMessageBox.information(self,"Edit Member","Please select the row containing an asset to be editted.")
			
	def delHouseholdAssets(self):
		numSelected = self.countRowsSelected(self.tblAssets)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household asset?"
			else:
				msg = "Are you sure you want to delete the selected household assets?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the asset id of the selected assets
			selectedRows = self.getSelectedRows(self.tblAssets)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblAssets.model().item(row,0).text() )
			 
			# get household id and pid
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected assets

			queries = []
			for assetid in selectedIds:
				queries.append('''DELETE FROM assets WHERE hhid=%s AND pid=%s AND assetid='%s' ''' % (hhid, pid,  assetid))
			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdAssets()

		else:
			QMessageBox.information(self,"Delete Assets","Please select the rows containing assets to be deleted.")
		
	def retrieveHouseholdAssets(self):
		 ''' retrieves and shows a list of household asset '''
		 temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		 hhid = temp[0]
		 pid = self.parent.projectid
		 # select query to retrieve household assets
		 query = '''SELECT assetid, assetcategory, assettype, unitofmeasure, unitcost, totalunits 
		 FROM assets WHERE hhid=%i AND pid=%s''' % (hhid, pid)
		 
		 rows = self.executeResultsQuery(query)
		 model = QStandardItemModel(1,2)
		 # set model headers
		 model.setHorizontalHeaderItem(0,QStandardItem('Asset ID.'))
		 model.setHorizontalHeaderItem(1,QStandardItem('Category'))
		 model.setHorizontalHeaderItem(2,QStandardItem('Asset Type'))
		 model.setHorizontalHeaderItem(3,QStandardItem('Unit'))
		 model.setHorizontalHeaderItem(4,QStandardItem('Cost Per Unit'))
		 model.setHorizontalHeaderItem(5,QStandardItem('Number of Units'))
		 
		 # add  data rows
		 num = 0

		 for row in rows:
		     qtAssetID = QStandardItem( "%i" % row[0])
		     qtAssetID.setTextAlignment( Qt.AlignCenter )
		     qtAssetCategory = QStandardItem( row[1] )
		     qtAssetType = QStandardItem( row[2] )	
		     qtUnitOfMeasure = QStandardItem( row[3] )
		     qtCostPerUnit = QStandardItem( "%.2f" % row[4] )
		     qtNumUnits = QStandardItem( "%.2f" % row[5] )
		 
		     model.setItem( num, 0, qtAssetID )
		     model.setItem( num, 1, qtAssetCategory )
		     model.setItem( num, 2, qtAssetType )
		     model.setItem( num, 3, qtUnitOfMeasure )
		     model.setItem( num, 4, qtCostPerUnit )
		     model.setItem( num, 5, qtNumUnits )
		     num = num + 1
		 self.tblAssets.setModel(model)
		 self.tblAssets.resizeColumnsToContents()
		 self.tblAssets.hideColumn(0)
		 self.tblAssets.show()

	#-------------------------------------------------------------------------------------------------------
	# Income: Crops
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdCropIncome(self):
		''' Show the Add Household Crop Income form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdCropIncome(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household crop income form
		form.exec_()
		
	def editHouseholdCropIncome(self):
		if self.countRowsSelected(self.tblCropIncome) != 0:
			# get the income id of the selected crop item
			selectedRow = self.getCurrentRow(self.tblCropIncome)
			incomeid = self.tblCropIncome.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household crop income form
			form = FrmHouseholdCropIncome(self, hhid, hhname, incomeid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing the income item to be editted."
			QMessageBox.information( self, "Edit Crop Income", msg )
			
	def delHouseholdCropIncome(self):
		numSelected = self.countRowsSelected(self.tblCropIncome)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household income item?"
			else:
				msg = "Are you sure you want to delete the selected household income items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the income id of the selected crop items
			selectedRows = self.getSelectedRows(self.tblCropIncome)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblCropIncome.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected crops

			queries = []
			for incomeid in selectedIds:
				queries.append('''DELETE FROM cropincome WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid))
			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdCropIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Crop Income", msg )
		
	def retrieveHouseholdCropIncome(self):
         ''' retrieves and shows a list of household crop income items '''
         temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
         hhid = temp[0]
         pid = self.parent.projectid 

         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit'))
         model.setHorizontalHeaderItem(3,QStandardItem('Units Produced'))
         model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
         model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
         model.setHorizontalHeaderItem(6,QStandardItem('Other Uses'))
         model.setHorizontalHeaderItem(7,QStandardItem('Units Consumed'))
         
         # select query to retrieve household crop income
         query = '''SELECT id, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed 
                 FROM cropincome WHERE hhid=%i AND pid=%s ''' % (hhid, pid)

	 rows = self.executeResultsQuery(query)
         # add  data rows
         num = 0
         
         for row in rows:
             qtIncomeID = QStandardItem( "%i" % row[0])
             qtIncomeID.setTextAlignment( Qt.AlignCenter )
             qtIncomeType = QStandardItem( row[1] )	
             qtUnitOfMeasure = QStandardItem( row[2] )
             qtUnitsProduced = QStandardItem( "%.2f" % row[3] )
             qtUnitsSold 	= QStandardItem( "%.2f" % row[4] )
             qtUnitPrice 	= QStandardItem( "%.2f" % row[5] )
             qtOtherUses 	= QStandardItem( "%.2f" % row[6] )
             qtUnitConsumed 	= QStandardItem( "%.2f" % row[7] )

             model.setItem( num, 0, qtIncomeID )
             model.setItem( num, 1, qtIncomeType )
             model.setItem( num, 2, qtUnitOfMeasure )
             model.setItem( num, 3, qtUnitsProduced )
             model.setItem( num, 4, qtUnitsSold )
             model.setItem( num, 5, qtUnitPrice )
             model.setItem( num, 6, qtOtherUses )
             model.setItem( num, 7, qtUnitConsumed )
             num = num + 1

         self.tblCropIncome.setModel(model)
         self.tblCropIncome.resizeColumnsToContents()
         self.tblCropIncome.hideColumn(0)
         self.tblCropIncome.show()

	#-------------------------------------------------------------------------------------------------------
	# Income: Livestock
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdLivestockIncome(self):
		''' Show the Add Household Livestock Income form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdLivestockIncome(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household livestock income form
		form.exec_()
		
	def editHouseholdLivestockIncome(self):
		if self.countRowsSelected(self.tblLivestockIncome) != 0:
			# get the income id of the selected livestock item
			selectedRow = self.getCurrentRow(self.tblLivestockIncome)
			incomeid = self.tblLivestockIncome.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household livestock income form
			form = FrmHouseholdLivestockIncome(self, hhid, hhname, incomeid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing the income item to be editted."
			QMessageBox.information( self, "Edit Livestock Income", msg )
			
	def delHouseholdLivestockIncome(self):
		numSelected = self.countRowsSelected(self.tblLivestockIncome)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household income item?"
			else:
				msg = "Are you sure you want to delete the selected household income items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the income id of the selected livestock items
			selectedRows = self.getSelectedRows(self.tblLivestockIncome)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblLivestockIncome.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected livestock items
			
			queries = []
			for incomeid in selectedIds:
				queries.append('''DELETE FROM livestockincome WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid))
			self.executeMultipleUpdateQueries(queries)
			self.retrieveHouseholdLivestockIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Livestock Income", msg )
		
	def retrieveHouseholdLivestockIncome(self):
         ''' retrieves and shows a list of household livestock income items '''
         temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
         hhid = temp[0]
         pid = self.parent.projectid 

         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit'))
         model.setHorizontalHeaderItem(3,QStandardItem('Units Produced'))
         model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
         model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
         model.setHorizontalHeaderItem(6,QStandardItem('Other Uses'))
         model.setHorizontalHeaderItem(7,QStandardItem('Units Consumed'))
         

         # select query to retrieve household crop income
         query = '''SELECT id, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed 
                 FROM livestockincome WHERE hhid=%i AND pid=%s ''' % (hhid, pid)
	 rows = self.executeResultsQuery(query)
	 # add  data rows
         num = 0
         
         for row in rows:
             qtIncomeID = QStandardItem( "%i" % row[0])
             qtIncomeID.setTextAlignment( Qt.AlignCenter )
             qtIncomeType = QStandardItem( row[1] )	
             qtUnitOfMeasure = QStandardItem( row[2] )
             qtUnitsProduced = QStandardItem( "%.2f" % row[3] )
             qtUnitsSold 	= QStandardItem( "%.2f" % row[4] )
             qtUnitPrice 	= QStandardItem( "%.2f" % row[5] )
             qtOtherUses 	= QStandardItem( "%.2f" % row[6] )
             qtUnitConsumed 	= QStandardItem( "%.2f" % row[7] )

             model.setItem( num, 0, qtIncomeID )
             model.setItem( num, 1, qtIncomeType )
             model.setItem( num, 2, qtUnitOfMeasure )
             model.setItem( num, 3, qtUnitsProduced )
             model.setItem( num, 4, qtUnitsSold )
             model.setItem( num, 5, qtUnitPrice )
             model.setItem( num, 6, qtOtherUses )
             model.setItem( num, 7, qtUnitConsumed )
             num = num + 1

         self.tblLivestockIncome.setModel(model)
         self.tblLivestockIncome.resizeColumnsToContents()
         self.tblLivestockIncome.hideColumn(0)
         self.tblLivestockIncome.show()

	
	#-------------------------------------------------------------------------------------------------------
	# Income: Gifts
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdGiftsIncome(self):
		''' Show the Add Household Gifts Income form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdGiftsIncome(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household gifts income form
		form.exec_()
		
	def editHouseholdGiftsIncome(self):
		if self.countRowsSelected(self.tblGiftsIncome) != 0:
			# get the income id of the selected gifts item
			selectedRow = self.getCurrentRow(self.tblGiftsIncome)
			incomeid = self.tblGiftsIncome.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household gifts income form
			form = FrmHouseholdGiftsIncome(self, hhid, hhname, incomeid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing the income item to be editted."
			QMessageBox.information( self, "Edit Gifts Income", msg )
			
	def delHouseholdGiftsIncome(self):
		numSelected = self.countRowsSelected(self.tblGiftsIncome)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household income item?"
			else:
				msg = "Are you sure you want to delete the selected household income items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the income id of the selected gifts items
			selectedRows = self.getSelectedRows(self.tblGiftsIncome)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblGiftsIncome.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected gifts items
			
			queries = []
			for incomeid in selectedIds:
				queries.append('''DELETE FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid))
			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdGiftsIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Gifts Income", msg )
		
	def retrieveHouseholdGiftsIncome(self):
		''' retrieves and shows a list of household gifts income items '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0] 
		pid = self.parent.projectid
		# select query to retrieve gifts income items
		query = '''SELECT id, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsconsumed , unitssold, priceperunit 
				   FROM transfers WHERE hhid=%i AND pid=%s AND sourcetype='Internal' ''' % (hhid,  pid)
		
		rows = self.executeResultsQuery(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Source of Transfer'))
		model.setHorizontalHeaderItem(2,QStandardItem('Cash Per Year'))
		model.setHorizontalHeaderItem(3,QStandardItem('Food Type'))
		model.setHorizontalHeaderItem(4,QStandardItem('Unit'))
		model.setHorizontalHeaderItem(5,QStandardItem('Units Consumed'))
		model.setHorizontalHeaderItem(6,QStandardItem('Units Sold'))
		model.setHorizontalHeaderItem(7,QStandardItem('Price per Unit'))
		
		# add  data rows
		num = 0
		
		for row in rows:
			qtIncomeID = QStandardItem( "%i" % row[0])
			qtIncomeID.setTextAlignment( Qt.AlignCenter )
			qtSource = QStandardItem( row[1] )	
			qtCashPerYear = QStandardItem( "%.2f" % row[2] )
			qtFoodType = QStandardItem( row[3] )
			qtUnitofMeasure = QStandardItem( row[4] )
			qtUnitsConsumed = QStandardItem( "%.2f" % row[5] )
			qtUnitsSold = QStandardItem( "%.2f" % row[6] )
			qtUnitPrice = QStandardItem( "%.2f" % row[7] )
						
			model.setItem( num, 0, qtIncomeID )
			model.setItem( num, 1, qtSource )
			model.setItem( num, 2, qtCashPerYear )
			model.setItem( num, 3, qtFoodType )
			model.setItem( num, 4, qtUnitofMeasure )
			model.setItem( num, 5, qtUnitsConsumed )
			model.setItem( num, 6, qtUnitsSold )
			model.setItem( num, 7, qtUnitPrice )
			
			num = num + 1
		
		self.tblGiftsIncome.setModel(model)
		self.tblGiftsIncome.hideColumn(0)
		self.tblGiftsIncome.resizeColumnsToContents()
		self.tblGiftsIncome.show()
		
	#-------------------------------------------------------------------------------------------------------
	# Income: Employment
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdEmploymentIncome(self):
		''' Show the Add Household Employment Income form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdEmploymentIncome(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household employment income form
		form.exec_()
		
	def editHouseholdEmploymentIncome(self):
		if self.countRowsSelected(self.tblEmploymentIncome) != 0:
			# get the income id of the selected employment item
			selectedRow = self.getCurrentRow(self.tblEmploymentIncome)
			incomeid = self.tblEmploymentIncome.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household employment income form
			form = FrmHouseholdEmploymentIncome(self, hhid, hhname, incomeid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing the income item to be editted."
			QMessageBox.information( self, "Edit Employment Income", msg )
			
	def delHouseholdEmploymentIncome(self):
		numSelected = self.countRowsSelected(self.tblEmploymentIncome)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household income item?"
			else:
				msg = "Are you sure you want to delete the selected household income items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the income id of the selected employment items
			selectedRows = self.getSelectedRows(self.tblEmploymentIncome)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblEmploymentIncome.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected employment items

			queries = []
			for incomeid in selectedIds:
				queries.append('''DELETE FROM employmentincome WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid))

			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdEmploymentIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Employment Income", msg )
		
	def retrieveHouseholdEmploymentIncome(self):
		''' retrieves and shows a list of household employment income items '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0] 
		pid = self.parent.projectid        
		# select query to retrieve employment income items
		query = '''SELECT *
				   FROM employmentincome WHERE hhid=%i AND pid=%s ''' % (hhid,  pid)
		
		rows = self.executeResultsQuery(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
		model.setHorizontalHeaderItem(2,QStandardItem('Type of Food Paid'))
		model.setHorizontalHeaderItem(3,QStandardItem('Unit'))
		model.setHorizontalHeaderItem(4,QStandardItem('Units Paid'))
		model.setHorizontalHeaderItem(5,QStandardItem('Energy Value (KCals)'))
		model.setHorizontalHeaderItem(6,QStandardItem('Cash Income'))

		num = 0
		
		for row in rows:
			qtIncomeID = QStandardItem( "%i" % row[0])
			qtIncomeID.setTextAlignment( Qt.AlignCenter )
			qtIncomeType = QStandardItem( row[2] )	
			qtFoodType = QStandardItem( row[3] )
			qtUnitOfMeasure = QStandardItem( row[4] )
			qtUnitsPaid = QStandardItem( "%f" % row[5] )
			qtIncomeKCal = QStandardItem( "%f" % row[6] )
			qtCashIncome = QStandardItem( "%f" % row[7] )
						
			model.setItem( num, 0, qtIncomeID )
			model.setItem( num, 1, qtIncomeType )
			model.setItem( num, 2, qtFoodType )
			model.setItem( num, 3, qtUnitOfMeasure )
			model.setItem( num, 4, qtUnitsPaid )
			model.setItem( num, 5, qtIncomeKCal )
			model.setItem( num, 6, qtCashIncome )
			
			num = num + 1
		
		self.tblEmploymentIncome.setModel(model)
		self.tblEmploymentIncome.resizeColumnsToContents()
		self.tblEmploymentIncome.show()
		
	#-------------------------------------------------------------------------------------------------------
	# Income: Transfers
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdTransferIncome(self):
		''' Show the Add Household Transfer Income form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdTransferIncome(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household transfer income form
		form.exec_()
		
	def editHouseholdTransferIncome(self):
		if self.countRowsSelected(self.tblTransferIncome) != 0:
			# get the income id of the selected transfer item
			selectedRow = self.getCurrentRow(self.tblTransferIncome)
			incomeid = self.tblTransferIncome.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household transfer income form
			form = FrmHouseholdTransferIncome(self, hhid, hhname, incomeid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing the income item to be editted."
			QMessageBox.information( self, "Edit Transfer Income", msg )
			
	def delHouseholdTransferIncome(self):
		numSelected = self.countRowsSelected(self.tblTransferIncome)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household income item?"
			else:
				msg = "Are you sure you want to delete the selected household income items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the income id of the selected transfer items
			selectedRows = self.getSelectedRows(self.tblTransferIncome)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblTransferIncome.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected transfer items

			queries = []
			for incomeid in selectedIds:
				queries.append('''DELETE FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid, incomeid))

			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdTransferIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Transfer Income", msg )
		
	def retrieveHouseholdTransferIncome(self):
		''' retrieves and shows a list of household transfer income items '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		pid = self.parent.projectid        
		# select query to retrieve transfer income items
		query = '''SELECT  id, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsconsumed , unitssold, priceperunit 
				   FROM transfers WHERE hhid=%i AND pid=%s AND sourcetype='External' ''' % (hhid, pid)
		
		# retrieve and display items
		rows = self.executeResultsQuery(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Source of Transfer'))
		model.setHorizontalHeaderItem(2,QStandardItem('Cash Per Year'))
		model.setHorizontalHeaderItem(3,QStandardItem('Food Type'))
		model.setHorizontalHeaderItem(4,QStandardItem('Unit'))
		model.setHorizontalHeaderItem(5,QStandardItem('Units Consumed'))
		model.setHorizontalHeaderItem(6,QStandardItem('Units Sold'))
		model.setHorizontalHeaderItem(7,QStandardItem('Price per Unit'))
		
		# add  data rows
		num = 0
		
		for row in rows:
			qtIncomeID = QStandardItem( "%i" % row[0])
			qtIncomeID.setTextAlignment( Qt.AlignCenter )
			qtSource = QStandardItem( row[1] )	
			qtCashPerYear = QStandardItem( "%.2f" % row[2] )
			qtFoodType = QStandardItem( row[3] )
			qtUnitofMeasure = QStandardItem( row[4] )
			qtUnitsConsumed = QStandardItem( "%.2f" % row[5] )
			qtUnitsSold = QStandardItem( "%.2f" % row[6] )
			qtUnitPrice = QStandardItem( "%.2f" % row[7] )
						
			model.setItem( num, 0, qtIncomeID )
			model.setItem( num, 1, qtSource )
			model.setItem( num, 2, qtCashPerYear )
			model.setItem( num, 3, qtFoodType )
			model.setItem( num, 4, qtUnitofMeasure )
			model.setItem( num, 5, qtUnitsConsumed )
			model.setItem( num, 6, qtUnitsSold )
			model.setItem( num, 7, qtUnitPrice )
			
			num = num + 1
		
		self.tblTransferIncome.setModel(model)
		self.tblTransferIncome.hideColumn(0)
		self.tblTransferIncome.resizeColumnsToContents()
		self.tblTransferIncome.show()
	
	#-------------------------------------------------------------------------------------------------------
	# Income: Wildfoods
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdWildfoodsIncome(self):
		''' Show the Add Household Wildfoods Income form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdWildfoodsIncome(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household wildfoods income form
		form.exec_()
		
	def editHouseholdWildfoodsIncome(self):
		if self.countRowsSelected(self.tblWildfoodsIncome) != 0:
			# get the income id of the selected wildfoods item
			selectedRow = self.getCurrentRow(self.tblWildfoodsIncome)
			incomeid = self.tblWildfoodsIncome.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household wildfoods income form
			form = FrmHouseholdWildfoodsIncome(self, hhid, hhname, incomeid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing the income item to be editted."
			QMessageBox.information( self, "Edit Wildfoods Income", msg )
			
	def delHouseholdWildfoodsIncome(self):
		numSelected = self.countRowsSelected(self.tblWildfoodsIncome)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household income item?"
			else:
				msg = "Are you sure you want to delete the selected household income items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the income id of the selected wildfoods items
			selectedRows = self.getSelectedRows(self.tblWildfoodsIncome)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblWildfoodsIncome.model().item(row,0).text() )
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			pid = self.parent.projectid
			# delete selected wildfoods items

			queries = []
			for incomeid in selectedIds:
				queries.append('''DELETE FROM wildfoods WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid))
			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdWildfoodsIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Wildfoods Income", msg )
		
	def retrieveHouseholdWildfoodsIncome(self):
         ''' retrieves and shows a list of household wildfoods income items '''
         temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
         hhid = temp[0]
         pid = self.parent.projectid 
         # select query to retrieve household crop income
         query = '''SELECT id, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed 
                 FROM wildfoods WHERE hhid=%i AND pid=%s ''' % (hhid, pid)

         # run query
	 rows = self.executeResultsQuery(query)

         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit'))
         model.setHorizontalHeaderItem(3,QStandardItem('Units Produced'))
         model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
         model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
         model.setHorizontalHeaderItem(6,QStandardItem('Other Uses'))
         model.setHorizontalHeaderItem(7,QStandardItem('Units Consumed'))
         
         # add  data rows
         num = 0
         
         for row in rows:
             qtIncomeID = QStandardItem( "%i" % row[0])
             qtIncomeID.setTextAlignment( Qt.AlignCenter )
             qtIncomeType = QStandardItem( row[1] )	
             qtUnitOfMeasure = QStandardItem( row[2] )
             qtUnitsProduced = QStandardItem( "%.2f" % row[3] )
             qtUnitsSold 	= QStandardItem( "%.2f" % row[4] )
             qtUnitPrice 	= QStandardItem( "%.2f" % row[5] )
             qtOtherUses 	= QStandardItem( "%.2f" % row[6] )
             qtUnitConsumed 	= QStandardItem( "%.2f" % row[7] )

             model.setItem( num, 0, qtIncomeID )
             model.setItem( num, 1, qtIncomeType )
             model.setItem( num, 2, qtUnitOfMeasure )
             model.setItem( num, 3, qtUnitsProduced )
             model.setItem( num, 4, qtUnitsSold )
             model.setItem( num, 5, qtUnitPrice )
             model.setItem( num, 6, qtOtherUses )
             model.setItem( num, 7, qtUnitConsumed )
             num = num + 1

         self.tblWildfoodsIncome.setModel(model)
         self.tblWildfoodsIncome.resizeColumnsToContents()
         self.tblWildfoodsIncome.hideColumn(0)
         self.tblWildfoodsIncome.show()

	#-------------------------------------------------------------------------------------------------------
	# Expenditure
	#-------------------------------------------------------------------------------------------------------
	
	def addHouseholdExpenditure(self):
		''' Show the Add Household Ependiture form '''
		# get household id and name
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		hhname = self.cboHouseholdNumber.currentText()
		form = FrmHouseholdExpense(self, hhid, hhname)
		form.setWindowIcon(QIcon('resources/images/openihm.png'))
		# show the add household expenditure form
		form.exec_()
		
	def editHouseholdExpenditure(self):
		if self.countRowsSelected(self.tblExpenditure) != 0:
			# get the expenditure id of the selected expense
			selectedRow = self.getCurrentRow(self.tblExpenditure)
			expid = self.tblExpenditure.model().item(selectedRow,0).text()
			# get household id and name
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			hhname = self.cboHouseholdNumber.currentText()
			# show edit household expense form
			form = FrmHouseholdExpense(self, hhid, hhname, expid)
			form.setWindowIcon(QIcon('resources/images/openihm.png'))
			form.exec_()
			
		else:
			msg = "Please select the row containing an expenditure item to be editted."
			QMessageBox.information( self, "Edit Expenditure", msg )
			
	def delHouseholdExpenses(self):
		numSelected = self.countRowsSelected(self.tblExpenditure)
		if  numSelected != 0:
			# confirm deletion
			if numSelected == 1:
				msg = "Are you sure you want to delete the selected household expenditure item?"
			else:
				msg = "Are you sure you want to delete the selected household expenditure items?"
				
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			# get the expenditure id of the selected expenses
			selectedRows = self.getSelectedRows(self.tblExpenditure)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tblExpenditure.model().item(row,0).text() )
			 
			# get household id and pid
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0] 
			pid = self.parent.projectid
			# delete selected expenses
			
			queries = []
			for expid in selectedIds:
				queries.append('''DELETE FROM expenditure WHERE hhid=%s AND pid=%s AND expid=%s ''' % (hhid, pid,  expid))

			self.executeMultipleUpdateQueries(queries)
			
			self.retrieveHouseholdExpenses()

		else:
			msg = "Please select the rows containing expenditure items to be deleted."
			QMessageBox.information( self, "Delete Expenditure", msg )
		
	def retrieveHouseholdExpenses(self):
		''' retrieves and shows a list of household expenses '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0] 
		pid = self.parent.projectid
		# select query to retrieve household expenses
		query = '''SELECT * FROM expenditure WHERE hhid=%i AND pid=%s''' % (hhid,  pid)
		
		rows = self.executeResultsQuery(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Exp. ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Exp. Type'))
		model.setHorizontalHeaderItem(2,QStandardItem('Unit'))
		model.setHorizontalHeaderItem(3,QStandardItem('Cost Per Unit'))
		model.setHorizontalHeaderItem(4,QStandardItem('KCal Per Unit'))
		model.setHorizontalHeaderItem(5,QStandardItem('Number of Units'))
		
		# add  data rows
		num = 0
		
		for row in rows:
			qtAssetID = QStandardItem( "%i" % row[0])
			qtAssetID.setTextAlignment( Qt.AlignCenter )
			qtAssetType = QStandardItem( row[2] )	
			qtUnitOfMeasure = QStandardItem( row[3] )
			qtCostPerUnit = QStandardItem( "%f" % row[4] )
			if ( row[5] != None ):
				qtKCalPerUnit = QStandardItem( "%f" % row[5] )
			else:
				qtKCalPerUnit = QStandardItem( "" )
			qtNumUnits = QStandardItem( "%f" % row[6] )
			
			model.setItem( num, 0, qtAssetID )
			model.setItem( num, 1, qtAssetType )
			model.setItem( num, 2, qtUnitOfMeasure )
			model.setItem( num, 3, qtCostPerUnit )
			model.setItem( num, 4, qtKCalPerUnit )
			model.setItem( num, 5, qtNumUnits )
			num = num + 1
		
		self.tblExpenditure.setModel(model)
		self.tblExpenditure.resizeColumnsToContents()
		self.tblExpenditure.hideColumn(0)
		self.tblExpenditure.show()
