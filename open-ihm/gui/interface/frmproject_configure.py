#---------------------------------------------------------------------------------	
#	Filename: frmproject_configure.py
#
#	Class to create the Configure Project form - FrmConfigureProject.
#---------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

# import the Create Project Dialog design class
from gui.designs.ui_projectconfiguration import Ui_ProjectConfiguration

class FrmConfigureProject(QDialog, Ui_ProjectConfiguration):	
	''' Creates the Edit Project form. '''	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.parent = parent
		self.setupUi(self)
		
		# connect to database
		self.config = Config.dbinfo().copy()
		
		self.tabProject.setCurrentIndex(0)
		
		# display project name
		self.lblProjectName.setText(self.parent.projectname)
		
		# display Available and Selected Household Characteristics
		self.hhCharacteristicsTable = "p%iHouseholdCharacteristics" % (self.parent.projectid )
		self.psCharacteristicsTable = "p%iPersonalCharacteristics" % (self.parent.projectid )
		self.displayAvailableChars("globalhouseholdcharacteristics", self.lstHouseholdAvailableChars)
		self.displayAvailableChars("globalpersonalcharacteristics", self.lstPersonalAvailableChars)
		self.displaySelectedChars(self.hhCharacteristicsTable, self.lstHouseholdSelectedChars)
		self.displaySelectedChars(self.psCharacteristicsTable, self.lstPersonalSelectedChars)
		
		# connect relevant signals and slots
		self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		self.connect(self.cmdHouseholdMoveAll, SIGNAL("clicked()"), self.moveAllHouseholdChars)
		self.connect(self.cmdHouseholdRemoveAll, SIGNAL("clicked()"), self.removeAllHouseholdChars)
		self.connect(self.cmdHouseholdMoveSelected, SIGNAL("clicked()"), self.moveSelectedHouseholdChars)
		self.connect(self.cmdHouseholdRemoveSelected, SIGNAL("clicked()"), self.removeSelectedHouseholdChars)
		self.connect(self.cmdPersonalMoveAll, SIGNAL("clicked()"), self.moveAllPersonalChars)
		self.connect(self.cmdPersonalRemoveAll, SIGNAL("clicked()"), self.removeAllPersonalChars)
		self.connect(self.cmdPersonalMoveSelected, SIGNAL("clicked()"), self.moveSelectedPersonalChars)
		self.connect(self.cmdPersonalRemoveSelected, SIGNAL("clicked()"), self.removeSelectedPersonalChars)
		
	def countRowsSelected(self, lstVw):
		selectedRows = self.getSelectedRows(lstVw)
		return len(selectedRows)
		
	def getSelectedRows(self, lstVw):
		
		selectedRows = []
		selectedIndexes = lstVw.selectedIndexes()
		
		for indexVal in selectedIndexes:
			if indexVal.row() not in selectedRows:
				selectedRows.append(indexVal.row())
				
		return selectedRows
		
	def getProjectCharacteristics(self, lstVw):
		chars = []
		row = 0
		while (lstVw.model().item(row,0)):
			val = lstVw.model().item(row,0).text()
			chars.append(val)
			row = row + 1
			
		return chars
		
	def displayAvailableChars(self, tbl, lstAvailable):
		''' Retrieve and display available Household Characteristics ''' 
		
		# select query to retrieve global characteristics
		query = '''SELECT characteristic, datatype FROM %s ORDER BY id ASC''' % (tbl)
		
		# retrieve and display members
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
		model.setHorizontalHeaderItem(1,QStandardItem('Data Type'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			qtCharacteristic = QStandardItem(row[0])
			qtDataType = QStandardItem( "%i" % row[1] )		
			
			model.setItem( num, 0, qtCharacteristic )
			model.setItem( num, 1, qtDataType )
			
			num = num + 1
		
		cursor.close()   
		db.close()
		lstAvailable.setModel(model)
		lstAvailable.setSelectionMode(QAbstractItemView.ExtendedSelection)
		
	def displaySelectedChars(self, tbl, lstSelected):
		''' Retrieve and display Project Characteristics (Household or Personal)'''
				
		# select query to retrieve global characteristics
		query = '''SHOW COLUMNS FROM %s''' % (tbl)
		
		# retrieve and display members
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,1)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Characteristic'))
		
		# add  data rows
		num = 0
		
		for row in cursor.fetchall():
			if "hhid" != row[0] and "personid" != row[0]:
				qtCharacteristic = QStandardItem(row[0])	
			
				model.setItem( num, 0, qtCharacteristic )
			
				num = num + 1
		
		cursor.close()   
		db.close()
		lstSelected.setModel(model)
		lstSelected.setSelectionMode(QAbstractItemView.ExtendedSelection)
		
	def removeCharacteristic(self, tbl, characteristic):
		''' removes a characteristic from a project'''
							
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
			
		queryAlter = '''ALTER TABLE `%s` DROP `%s` ''' % (tbl, characteristic)
		
		cursor.execute(queryAlter)
		
		cursor.close()   
		db.close()
		
	
	def addCharacteristic(self, tbl, characteristic, datatype):
		''' adds a characteristic from a project'''
		
		if datatype == "1":
			vartype = "ENUM('Yes','No')"
		elif datatype == "2":
			vartype = "BIGINT"
		elif datatype == "3":
			vartype = "VARCHAR(250)"
			
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
			
		queryAlter = '''ALTER TABLE `%s` ADD COLUMN `%s` %s ''' % (tbl, characteristic, vartype)
		
		cursor.execute(queryAlter)
		cursor.close()   
		db.close()
		 
		
	def moveAllChars(self, tbl, lstAvailable, lstSelected):
		''' Add all available household characteristics to Project'''
		row = 0
		while(lstAvailable.model().item(row,0)):
			characteristic 		= lstAvailable.model().item(row,0).text()
			datatype 			= lstAvailable.model().item(row,1).text()
			currentProjectChars = self.getProjectCharacteristics(lstSelected)
			if characteristic not in currentProjectChars:
				self.addCharacteristic(tbl, characteristic, datatype)
			else:
			    msg = "The characteristic labelled, %s, has already been selected" % (characteristic)
			    QMessageBox.information(self,"Project Configuration",msg)
			row = row + 1
		
	def removeAllChars(self, tbl, lstSelected):
		''' remove all listed household characteristics from Project'''
		msg = "Are you sure you want to remove all household characteristics from this project?"
		ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
		# if deletion is rejected return without deleting
		if ret == QMessageBox.No:
			return
			
		row = 0
		while(lstSelected.model().item(row,0)):
			characteristic = lstSelected.model().item(row,0).text()
			self.removeCharacteristic(tbl,characteristic)
			row = row + 1
		
	def moveSelectedChars(self, tbl, lstAvailable, lstSelected):
		''' Add selected available household characteristics to Project'''
		numSelected = self.countRowsSelected(lstAvailable)
		if  numSelected != 0:
			selectedRows = self.getSelectedRows(lstAvailable)
			for row in selectedRows:
				characteristic 		= lstAvailable.model().item(row,0).text()
				datatype 			= lstAvailable.model().item(row,1).text()
				currentProjectChars = self.getProjectCharacteristics(lstSelected)
				if characteristic not in currentProjectChars:
					self.addCharacteristic(tbl, characteristic, datatype)
				else:
				    msg = "The characteristic labelled, %s, has already been selected" % (characteristic)
				    QMessageBox.information(self,"Project Configuration",msg)
		else:
			msg = "Please select the characteristics you want to add."
			QMessageBox.information(self,"Project Configuration",msg) 
		
	def removeSelectedChars(self, tbl, lstSelected):
		''' remove selected household characteristics from Project'''
		numSelected = self.countRowsSelected(lstSelected)
		if  numSelected != 0:
			msg = "Are you sure you want to remove the selected household characteristic(s) from this project?"
			ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
			# if deletion is rejected return without deleting
			if ret == QMessageBox.No:
				return
			selectedRows = self.getSelectedRows(lstSelected)
			for row in selectedRows:
				characteristic = lstSelected.model().item(row,0).text()
				self.removeCharacteristic(tbl, characteristic)
		else:
			msg = "Please select the characteristics you want to remove."
			QMessageBox.information(self,"Project Configuration",msg) 
			
			
	#-----------------------------------------------------------------------------------------------------------
	# Household Characteristics methods
	#-----------------------------------------------------------------------------------------------------------
	
	def moveAllHouseholdChars(self):
		''' Add all available personal characteristics to Project'''
		self.moveAllChars(self.hhCharacteristicsTable, self.lstHouseholdAvailableChars, self.lstHouseholdSelectedChars)
		self.displaySelectedChars( self.hhCharacteristicsTable, self.lstHouseholdSelectedChars )
		
	def removeAllHouseholdChars(self):
		''' remove all listed personal characteristics from Project'''
		self.removeAllChars(self.hhCharacteristicsTable, self.lstHouseholdSelectedChars)
		self.displaySelectedChars( self.hhCharacteristicsTable, self.lstHouseholdSelectedChars )
		
	def moveSelectedHouseholdChars(self):
		''' Add selected available household characteristics to Project'''
		self.moveSelectedChars(self.hhCharacteristicsTable, self.lstHouseholdAvailableChars, self.lstHouseholdSelectedChars)
		self.displaySelectedChars( self.hhCharacteristicsTable, self.lstHouseholdSelectedChars ) 
		
	def removeSelectedHouseholdChars(self):
		''' remove selected household characteristics from Project'''
		self.removeSelectedChars(self.hhCharacteristicsTable, self.lstHouseholdSelectedChars)
		self.displaySelectedChars( self.hhCharacteristicsTable, self.lstHouseholdSelectedChars )
			
	#-----------------------------------------------------------------------------------------------------------
	# Personal Characteristics methods
	#-----------------------------------------------------------------------------------------------------------
	
	def moveAllPersonalChars(self):
		''' Add all available personal characteristics to Project'''
		self.moveAllChars(self.psCharacteristicsTable, self.lstPersonalAvailableChars, self.lstPersonalSelectedChars)
		self.displaySelectedChars( self.psCharacteristicsTable, self.lstPersonalSelectedChars )
		
	def removeAllPersonalChars(self):
		''' remove all listed personal characteristics from Project'''
		self.removeAllChars(self.psCharacteristicsTable, self.lstPersonalSelectedChars)
		self.displaySelectedChars( self.psCharacteristicsTable, self.lstPersonalSelectedChars )
		
	def moveSelectedPersonalChars(self):
		''' Add selected available household characteristics to Project'''
		self.moveSelectedChars(self.psCharacteristicsTable, self.lstPersonalAvailableChars, self.lstPersonalSelectedChars)
		self.displaySelectedChars( self.psCharacteristicsTable, self.lstPersonalSelectedChars ) 
		
	def removeSelectedPersonalChars(self):
		''' remove selected household characteristics from Project'''
		self.removeSelectedChars(self.psCharacteristicsTable, self.lstPersonalSelectedChars)
		self.displaySelectedChars( self.psCharacteristicsTable, self.lstPersonalSelectedChars )
