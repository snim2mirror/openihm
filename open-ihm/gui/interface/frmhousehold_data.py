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

class FrmHouseholdData(QDialog, Ui_HouseholdData):	
	''' Creates the household data (income, assets, expenditure, etc) form '''	
	def __init__(self, parent, hhid=0):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent = parent
		
		# connect to database
		self.config = Config.dbinfo().copy()
		
		self.tabHouseHold.setCurrentIndex(0)
		
		# get house holds
		self.getHouseholds()
		
		# set current house hold
		if hhid != 0:
			self.cboHouseholdNumber.setCurrentIndex(self.cboHouseholdNumber.findData(QVariant(hhid)))
		
		# retrieve members
		self.retrieveHouseholdMembers()
		# connect relevant signals and slots
		
		self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		self.connect(self.cmdAddMember, SIGNAL("clicked()"), self.addHouseholdMember)
		self.connect(self.cmdEditMember, SIGNAL("clicked()"), self.editHouseholdMember)	
		self.connect(self.cmdDelMember, SIGNAL("clicked()"), self.delHouseholdMembers)					
		self.connect(self.cboHouseholdNumber, SIGNAL("currentIndexChanged(int)"), self.displayHouseholdMembers)
		
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
		
	def displayHouseholdMembers(self):
		self.tabHouseHold.setCurrentIndex(0)
		self.retrieveHouseholdMembers()
		
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
		self.tblMembers.show()
		
		
		