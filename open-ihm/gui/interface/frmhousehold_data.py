#-------------------------------------------------------------------	
#	Filename: frmhousehold_data.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_data import Ui_HouseholdData
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

class FrmHouseholdData(QDialog, Ui_HouseholdData):	
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
			
		# temporarily disable editing of transfers and transfers from orgs
		self.cmdEditGifts.setEnabled( False )
		self.cmdEditTransfer.setEnabled( False )
		
		# retrieve members
		self.displayHouseholdData()
		# connect relevant signals and slots
		self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		self.connect(self.cmdAddMember, SIGNAL("clicked()"), self.addHouseholdMember)
		self.connect(self.cmdEditMember, SIGNAL("clicked()"), self.editHouseholdMember)	
		self.connect(self.cmdDelMember, SIGNAL("clicked()"), self.delHouseholdMembers)
		self.connect(self.cmdEditPersonalCharacteristic, SIGNAL("clicked()"), self.editPersonalCharacteristic)
		self.connect(self.tblMembers, SIGNAL("clicked(QModelIndex)"), self.showMemberPersonalCharacteristics)
		self.connect(self.cmdEditCharacteristic, SIGNAL("clicked()"), self.editCharacteristic)						
		self.connect(self.cboHouseholdNumber, SIGNAL("currentIndexChanged(int)"), self.displayHouseholdData)
		self.connect(self.cmdAddAsset, SIGNAL("clicked()"), self.addHouseholdAsset)
		self.connect(self.cmdEditAsset, SIGNAL("clicked()"), self.editHouseholdAsset)
		self.connect(self.cmdDelAsset, SIGNAL("clicked()"), self.delHouseholdAssets)
		self.connect(self.cmdAddExpenditure, SIGNAL("clicked()"), self.addHouseholdExpenditure)
		self.connect(self.cmdEditExpenditure, SIGNAL("clicked()"), self.editHouseholdExpenditure)
		self.connect(self.cmdDelExpenditure, SIGNAL("clicked()"), self.delHouseholdExpenses)
		self.connect(self.cmdAddCrop, SIGNAL("clicked()"), self.addHouseholdCropIncome)
		self.connect(self.cmdEditCrop, SIGNAL("clicked()"), self.editHouseholdCropIncome)
		self.connect(self.cmdDelCrop, SIGNAL("clicked()"), self.delHouseholdCropIncome)
		self.connect(self.cmdAddLivestock, SIGNAL("clicked()"), self.addHouseholdLivestockIncome)
		self.connect(self.cmdEditLivestock, SIGNAL("clicked()"), self.editHouseholdLivestockIncome)
		self.connect(self.cmdDelLivestock, SIGNAL("clicked()"), self.delHouseholdLivestockIncome)
		self.connect(self.cmdAddWildfoods, SIGNAL("clicked()"), self.addHouseholdWildfoodsIncome)
		self.connect(self.cmdEditWildfoods, SIGNAL("clicked()"), self.editHouseholdWildfoodsIncome)
		self.connect(self.cmdDelWildfoods, SIGNAL("clicked()"), self.delHouseholdWildfoodsIncome)
		self.connect(self.cmdAddGifts, SIGNAL("clicked()"), self.addHouseholdGiftsIncome)
		self.connect(self.cmdEditGifts, SIGNAL("clicked()"), self.editHouseholdGiftsIncome)
		self.connect(self.cmdDelGifts, SIGNAL("clicked()"), self.delHouseholdGiftsIncome)
		self.connect(self.cmdAddTransfer, SIGNAL("clicked()"), self.addHouseholdTransferIncome)
		self.connect(self.cmdEditTransfer, SIGNAL("clicked()"), self.editHouseholdTransferIncome)
		self.connect(self.cmdDelTransfer, SIGNAL("clicked()"), self.delHouseholdTransferIncome)
		self.connect(self.cmdAddEmployment, SIGNAL("clicked()"), self.addHouseholdEmploymentIncome)
		self.connect(self.cmdEditEmployment, SIGNAL("clicked()"), self.editHouseholdEmploymentIncome)
		self.connect(self.cmdDelEmployment, SIGNAL("clicked()"), self.delHouseholdEmploymentIncome)			
		
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
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    hhid = row[0]
		    householdname = row[1]
		    self.cboHouseholdNumber.addItem(householdname, QVariant(hhid))
		 
		cursor.close()   
		db.close()
		
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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for memberid in selectedIds:
				query = '''DELETE FROM householdmembers WHERE pid=%i and hhid=%s AND personid='%s' ''' % (self.parent.projectid, hhid, memberid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
			self.retrieveHouseholdMembers()

		else:
			QMessageBox.information(self,"Delete Members","Please select the rows containing members to be deleted.")
		
	def retrieveHouseholdMembers(self):
		''' retrieves and shows a list of household members '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0] 
		pid = self.parent.projectid
		# select query to retrieve household members
		query = '''SELECT personid, headofhousehold, yearofbirth, sex 
		             FROM householdmembers WHERE hhid=%i and pid=%i ORDER BY yearofbirth ''' % (hhid,  pid)
		
		# retrieve and display members
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Member ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Head of Household'))
		model.setHorizontalHeaderItem(2,QStandardItem('Age'))
		model.setHorizontalHeaderItem(3,QStandardItem('Sex'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			qtMemberID = QStandardItem(row[0])
			qtMemberID.setTextAlignment( Qt.AlignCenter )
			qtHouseholdHead = QStandardItem( row[1] )
			age = date.today().year - row[2]
			qtAge = QStandardItem( "%i" % age )
			
			qtSex = QStandardItem( row[3] )
			
			
			model.setItem( num, 0, qtMemberID )
			model.setItem( num, 1, qtHouseholdHead )
			model.setItem( num, 2, qtAge )
			model.setItem( num, 3, qtSex )
			num = num + 1
		
		cursor.close()   
		db.close()
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
		     
		self.retrievePersonalCharacteristics(personid)
		
	def showMemberPersonalCharacteristics(self):
         ''' show personal characteristics of selected household member '''
         selectedRow = self.getCurrentRow(self.tblMembers)
         if ( self.tblMembers.model().item(selectedRow, 0) != None ):
             personid = self.tblMembers.model().item(selectedRow,0).text()
         else:
             personid = "0"
         self.retrievePersonalCharacteristics(personid)
         
	#-----------------------------------------------------------------------------------
	#	Personal Characteristics
	#-----------------------------------------------------------------------------------
	
	def getPersonalCharacteristicDataType(self, charName):
		tbl = "globalpersonalcharacteristics"
		query = '''SELECT datatype FROM %s WHERE characteristic='%s' ''' % (tbl, charName)
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
			return row[0]
	
	def retrievePersonalCharacteristics( self,  personid ):
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		tbl = self.psCharacteristicsTable
		# select query to retrieve project household characteristics
		query = '''SHOW COLUMNS FROM %s''' % (tbl)
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		fields = []
		for row in cursor.fetchall():
			if ( (row[0] != "hhid")  and (row[0]!= "pid" )  and (row[0]!= "personid" ) ):
				fields.append( row[0] )
		
		model = QStandardItemModel(1,1)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
		model.setHorizontalHeaderItem(1,QStandardItem('Value'))
		
		# add  data rows
		num = 0
		
		for field in fields:
			query = '''SELECT `%s` FROM %s WHERE hhid=%i AND personid='%s' ''' % ( field, tbl, hhid,  personid )	
			cursor.execute(query)
			val = "Not Set"
			for row in cursor.fetchall():
				if ( row[0] != None ):
					val = row[0]
					
			qtChar 	= QStandardItem( field )
			if ( ( self.getPersonalCharacteristicDataType( field ) == 2 ) and (val != "Not Set") ):
				qtVal	= QStandardItem( "%i" % val )
			else:
				qtVal	= QStandardItem( "%s" % val )
				
			model.setItem( num, 0, qtChar )
			model.setItem( num, 1, qtVal )
				
			num = num + 1
		
		cursor.close()   
		db.close()
		
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
		tbl = "globalhouseholdcharacteristics"
		query = '''SELECT datatype FROM %s WHERE characteristic='%s' ''' % (tbl, charName)
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
			return row[0]
	
	def retrieveHouseholdCharacteristics( self ):
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		tbl = self.hhCharacteristicsTable
		# select query to retrieve project household characteristics
		query = '''SHOW COLUMNS FROM %s''' % (tbl)
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		fields = []
		for row in cursor.fetchall():
			if ( (row[0] != "hhid")  and (row[0]!= "pid" ) ):
				fields.append( row[0] )
		
		model = QStandardItemModel(1,1)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
		model.setHorizontalHeaderItem(1,QStandardItem('Value'))
		
		# add  data rows
		num = 0
		
		for field in fields:
			query = '''SELECT `%s` FROM %s WHERE hhid=%i ''' % ( field, tbl, hhid )	
			cursor.execute(query)
			val = "Not Set"
			for row in cursor.fetchall():
				if ( row[0] != None ):
					val = row[0]
					
			qtChar 	= QStandardItem( field )
			if ( ( self.getCharacteristicDataType( field ) == 2 ) and (val != "Not Set") ):
				qtVal	= QStandardItem( "%i" % val )
			else:
				qtVal	= QStandardItem( "%s" % val )
				
			model.setItem( num, 0, qtChar )
			model.setItem( num, 1, qtVal )
				
			num = num + 1
		
		cursor.close()   
		db.close()
		
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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for assetid in selectedIds:
				query = '''DELETE FROM assets WHERE hhid=%s AND pid=%s AND assetid='%s' ''' % (hhid, pid,  assetid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
			self.retrieveHouseholdAssets()

		else:
			QMessageBox.information(self,"Delete Assets","Please select the rows containing assets to be deleted.")
		
	def retrieveHouseholdAssets(self):
		''' retrieves and shows a list of household asset '''
		temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
		hhid = temp[0]
		pid = self.parent.projectid
		# select query to retrieve household assets
		query = '''SELECT * FROM assets WHERE hhid=%i AND pid=%s''' % (hhid, pid)
		
		# retrieve and display assets
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Asset ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Asset Type'))
		model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(3,QStandardItem('Cost Per Unit'))
		model.setHorizontalHeaderItem(4,QStandardItem('Number of Units'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			qtAssetID = QStandardItem( "%i" % row[0])
			qtAssetID.setTextAlignment( Qt.AlignCenter )
			qtAssetType = QStandardItem( row[2] )	
			qtUnitOfMeasure = QStandardItem( row[3] )
			qtCostPerUnit = QStandardItem( "%f" % row[4] )
			qtNumUnits = QStandardItem( "%f" % row[5] )
			
			model.setItem( num, 0, qtAssetID )
			model.setItem( num, 1, qtAssetType )
			model.setItem( num, 2, qtUnitOfMeasure )
			model.setItem( num, 3, qtCostPerUnit )
			model.setItem( num, 4, qtNumUnits )
			num = num + 1
		
		cursor.close()   
		db.close()
		
		self.tblAssets.setModel(model)
		self.tblAssets.resizeColumnsToContents()
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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM cropincome WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
			self.retrieveHouseholdCropIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Crop Income", msg )
		
	def retrieveHouseholdCropIncome(self):
         ''' retrieves and shows a list of household crop income items '''
         temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
         hhid = temp[0]
         pid = self.parent.projectid 
         # select query to retrieve household crop income
         query = '''SELECT id, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed 
                 FROM cropincome WHERE hhid=%i AND pid=%s ''' % (hhid, pid)

         # run query
         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Income Produced'))
         model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
         model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
         model.setHorizontalHeaderItem(6,QStandardItem('Other Uses'))
         model.setHorizontalHeaderItem(7,QStandardItem('Units Consumed'))
         
         # add  data rows
         num = 0
         
         for row in cursor.fetchall():
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

         cursor.close()   
         db.close()

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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM livestockincome WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
			self.retrieveHouseholdLivestockIncome()

		else:
			msg = "Please select the rows containing income items to be deleted."
			QMessageBox.information( self, "Delete Livestock Income", msg )
		
	def retrieveHouseholdLivestockIncome(self):
         ''' retrieves and shows a list of household livestock income items '''
         temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
         hhid = temp[0]
         pid = self.parent.projectid 
         # select query to retrieve household crop income
         query = '''SELECT id, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed 
                 FROM livestockincome WHERE hhid=%i AND pid=%s ''' % (hhid, pid)

         # run query
         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Income Produced'))
         model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
         model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
         model.setHorizontalHeaderItem(6,QStandardItem('Other Uses'))
         model.setHorizontalHeaderItem(7,QStandardItem('Units Consumed'))
         
         # add  data rows
         num = 0
         
         for row in cursor.fetchall():
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

         cursor.close()   
         db.close()

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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
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
		
		# retrieve and display items
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Source of Transfer'))
		model.setHorizontalHeaderItem(2,QStandardItem('Cash Per Year'))
		model.setHorizontalHeaderItem(3,QStandardItem('Food Type'))
		model.setHorizontalHeaderItem(4,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(5,QStandardItem('Units Consumed'))
		model.setHorizontalHeaderItem(6,QStandardItem('Units Sold'))
		model.setHorizontalHeaderItem(7,QStandardItem('Price per Unit'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
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
		
		cursor.close()   
		db.close()
		
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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM employmentincome WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
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
		
		# retrieve and display items
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
		model.setHorizontalHeaderItem(2,QStandardItem('Type of Food Paid'))
		model.setHorizontalHeaderItem(3,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(4,QStandardItem('Units Paid'))
		model.setHorizontalHeaderItem(5,QStandardItem('Energy Value (KCals)'))
		model.setHorizontalHeaderItem(6,QStandardItem('Cash Income'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
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
		
		cursor.close()   
		db.close()
		
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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid, incomeid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
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
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Source of Transfer'))
		model.setHorizontalHeaderItem(2,QStandardItem('Cash Per Year'))
		model.setHorizontalHeaderItem(3,QStandardItem('Food Type'))
		model.setHorizontalHeaderItem(4,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(5,QStandardItem('Units Consumed'))
		model.setHorizontalHeaderItem(6,QStandardItem('Units Sold'))
		model.setHorizontalHeaderItem(7,QStandardItem('Price per Unit'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
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
		
		cursor.close()   
		db.close()
		
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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM wildfoods WHERE hhid=%s AND pid=%s AND id=%s ''' % (hhid, pid,  incomeid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
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
         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)

         model = QStandardItemModel(1,2)
         
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
         model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
         model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
         model.setHorizontalHeaderItem(3,QStandardItem('Income Produced'))
         model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
         model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
         model.setHorizontalHeaderItem(6,QStandardItem('Other Uses'))
         model.setHorizontalHeaderItem(7,QStandardItem('Units Consumed'))
         
         # add  data rows
         num = 0
         
         for row in cursor.fetchall():
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

         cursor.close()   
         db.close()

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
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for expid in selectedIds:
				query = '''DELETE FROM expenditure WHERE hhid=%s AND pid=%s AND expid=%s ''' % (hhid, pid,  expid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
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
		
		# retrieve and display assets
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Exp. ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Exp. Type'))
		model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(3,QStandardItem('Cost Per Unit'))
		model.setHorizontalHeaderItem(4,QStandardItem('KCal Per Unit'))
		model.setHorizontalHeaderItem(5,QStandardItem('Number of Units'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
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
		
		cursor.close()   
		db.close()
		
		self.tblExpenditure.setModel(model)
		self.tblExpenditure.resizeColumnsToContents()
		self.tblExpenditure.show()
