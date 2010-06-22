#-------------------------------------------------------------------	
#	Filename: frmhousehold_data.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_data import Ui_HouseholdData
from frmhousehold_addmember import FrmAddHouseholdMember
from frmhousehold_editmember import FrmEditHouseholdMember
from frmhousehold_editcharacteristic import FrmEditHouseholdCharacteristic
from frmhousehold_addasset import FrmHouseholdAsset
from frmhousehold_addexpense import FrmHouseholdExpense
from frmhousehold_addincome_crop import FrmHouseholdCropIncome
from frmhousehold_addincome_livestock import FrmHouseholdLivestockIncome

class FrmHouseholdData(QDialog, Ui_HouseholdData):	
	''' Creates the household data (income, assets, expenditure, etc) form '''	
	def __init__(self, parent, hhid=0):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent = parent
		
		self.hhCharacteristicsTable = "p%iHouseholdCharacteristics" % (self.parent.projectid )
		# connect to database
		self.config = Config.dbinfo().copy()
		
		# get house holds
		self.getHouseholds()
		
		# set current house hold
		if hhid != 0:
			self.cboHouseholdNumber.setCurrentIndex(self.cboHouseholdNumber.findData(QVariant(hhid)))
		
		# retrieve members
		self.displayHouseholdData()
		# connect relevant signals and slots
		
		self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		self.connect(self.cmdAddMember, SIGNAL("clicked()"), self.addHouseholdMember)
		self.connect(self.cmdEditMember, SIGNAL("clicked()"), self.editHouseholdMember)	
		self.connect(self.cmdDelMember, SIGNAL("clicked()"), self.delHouseholdMembers)
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
			memberid = self.tblMembers.model().item(selectedRow,0).text()
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
				query = '''DELETE FROM householdmembers WHERE hhid=%s AND personid='%s' ''' % (hhid, memberid)	
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
		# select query to retrieve household members
		query = '''SELECT personid, headofhousehold, dateofbirth, sex, education 
		             FROM householdmembers WHERE hhid=%i''' % (hhid)
		
		# retrieve and display members
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Member ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Head of Household'))
		model.setHorizontalHeaderItem(2,QStandardItem('Date of Birth'))
		model.setHorizontalHeaderItem(3,QStandardItem('Sex'))
		model.setHorizontalHeaderItem(4,QStandardItem('Education'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			qtMemberID = QStandardItem(row[0])
			qtMemberID.setTextAlignment( Qt.AlignCenter )
			qtHouseholdHead = QStandardItem( row[1] )	
			qtDOB = QStandardItem( QDate(row[2]).toString("dd/MM/yyyy") )
			qtDOB.setTextAlignment( Qt.AlignCenter )
			
			qtSex = QStandardItem( row[3] )
			
			qtEducation = QStandardItem( row[4] )
			
			
			model.setItem( num, 0, qtMemberID )
			model.setItem( num, 1, qtHouseholdHead )
			model.setItem( num, 2, qtDOB )
			model.setItem( num, 3, qtSex )
			model.setItem( num, 4, qtEducation )
			num = num + 1
		
		cursor.close()   
		db.close()
		self.tblMembers.setModel(model)
		self.tblMembers.resizeColumnsToContents()
		self.tblMembers.show()
		
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
			if ( row[0] != "hhid" ):
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
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			# delete selected assets
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for assetid in selectedIds:
				query = '''DELETE FROM assets WHERE hhid=%s AND assetid='%s' ''' % (hhid, assetid)	
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
		# select query to retrieve household assets
		query = '''SELECT * FROM assets WHERE hhid=%i''' % (hhid)
		
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
			qtAssetID = QStandardItem( "%i" % row[1])
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
			# delete selected crops
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM cropincome WHERE hhid=%s AND id=%s ''' % (hhid, incomeid)	
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
		# select query to retrieve household expenses
		query = '''SELECT * FROM cropincome WHERE hhid=%i''' % (hhid)
		
		# retrieve and display assets
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
		model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(3,QStandardItem('Units Consumed'))
		model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
		model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			qtIncomeID = QStandardItem( "%i" % row[0])
			qtIncomeID.setTextAlignment( Qt.AlignCenter )
			qtIncomeType = QStandardItem( row[2] )	
			qtUnitOfMeasure = QStandardItem( row[3] )
			qtUnitsConsumed = QStandardItem( "%f" % row[4] )
			qtUnitsSold 	= QStandardItem( "%f" % row[5] )
			qtUnitPrice 	= QStandardItem( "%f" % row[6] )
			
			model.setItem( num, 0, qtIncomeID )
			model.setItem( num, 1, qtIncomeType )
			model.setItem( num, 2, qtUnitOfMeasure )
			model.setItem( num, 3, qtUnitsConsumed )
			model.setItem( num, 4, qtUnitsSold )
			model.setItem( num, 5, qtUnitPrice )
			num = num + 1
		
		cursor.close()   
		db.close()
		
		self.tblCropIncome.setModel(model)
		self.tblCropIncome.resizeColumnsToContents()
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
			# delete selected livestock items
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for incomeid in selectedIds:
				query = '''DELETE FROM livestockincome WHERE hhid=%s AND id=%s ''' % (hhid, incomeid)	
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
		# select query to retrieve household expenses
		query = '''SELECT * FROM livestockincome WHERE hhid=%i''' % (hhid)
		
		# retrieve and display assets
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Income ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Income Source'))
		model.setHorizontalHeaderItem(2,QStandardItem('Unit of Measure'))
		model.setHorizontalHeaderItem(3,QStandardItem('Units Consumed'))
		model.setHorizontalHeaderItem(4,QStandardItem('Units Sold'))
		model.setHorizontalHeaderItem(5,QStandardItem('Unit Price'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			qtIncomeID = QStandardItem( "%i" % row[0])
			qtIncomeID.setTextAlignment( Qt.AlignCenter )
			qtIncomeType = QStandardItem( row[2] )	
			qtUnitOfMeasure = QStandardItem( row[3] )
			qtUnitsConsumed = QStandardItem( "%f" % row[4] )
			qtUnitsSold 	= QStandardItem( "%f" % row[5] )
			qtUnitPrice 	= QStandardItem( "%f" % row[6] )
			
			model.setItem( num, 0, qtIncomeID )
			model.setItem( num, 1, qtIncomeType )
			model.setItem( num, 2, qtUnitOfMeasure )
			model.setItem( num, 3, qtUnitsConsumed )
			model.setItem( num, 4, qtUnitsSold )
			model.setItem( num, 5, qtUnitPrice )
			num = num + 1
		
		cursor.close()   
		db.close()
		
		self.tblLivestockIncome.setModel(model)
		self.tblLivestockIncome.resizeColumnsToContents()
		self.tblLivestockIncome.show()
	
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
			 
			# get household id
			temp = self.cboHouseholdNumber.itemData(self.cboHouseholdNumber.currentIndex()).toInt()
			hhid = temp[0]
			# delete selected expenses
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for expid in selectedIds:
				query = '''DELETE FROM expenditure WHERE hhid=%s AND expid=%s ''' % (hhid, expid)	
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
		# select query to retrieve household expenses
		query = '''SELECT * FROM expenditure WHERE hhid=%i''' % (hhid)
		
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
			qtAssetID = QStandardItem( "%i" % row[1])
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
