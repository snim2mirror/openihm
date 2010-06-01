#-------------------------------------------------------------------	
#	Filename: frmhouseholds.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_households_all import Ui_AllHouseholds
from frmhouseholds_add import FrmAddHousehold
from frmhouseholds_edit import FrmEditHousehold
from frmhousehold_data import FrmHouseholdData

class FrmHouseholds(QDialog, Ui_AllHouseholds):	
	''' Creates the view households form '''	
	def __init__(self, parent):
	    ''' Set up the dialog box interface '''
	    self.parent = parent
	    QDialog.__init__(self)
	    self.setupUi(self)
	    self.parent = parent
	    self.config = Config.dbinfo().copy()
	    
	    self.lblProjectName.setText( self.parent.projectname ) 
	    # get current project details
	    self.getHouseholds()
	    
	    # connect relevant signals and slots
	    self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
	    self.connect(self.cmdAdd, SIGNAL("clicked()"), self.addHousehold)
	    self.connect(self.cmdEdit, SIGNAL("clicked()"), self.editHousehold)
	    self.connect(self.cmdDel, SIGNAL("clicked()"), self.delHouseholds)
	    self.connect(self.cmdData, SIGNAL("clicked()"), self.viewHouseholdData)
	    
	def getHouseholds(self):
		# connect to mysql database
		db = data.mysql.connector.Connect(**self.config)
		cursor = db.cursor()
		
		# select query to retrieve project households
		query = '''SELECT hhid, householdname, totalassetvalue, totalincomevalue, totalexpenditure, dateofcollection 
		             FROM households WHERE pid=%i''' % (self.parent.projectid)
		
		cursor.execute(query)
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Household No.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Household Name'))
		model.setHorizontalHeaderItem(2,QStandardItem('Total Asset Value'))
		model.setHorizontalHeaderItem(3,QStandardItem('Total Income Value'))
		model.setHorizontalHeaderItem(4,QStandardItem('Total Expenditure'))
		model.setHorizontalHeaderItem(5,QStandardItem('Date Visited'))
		
		# add  data rows
		num = 0
	    
		for row in cursor.fetchall():
		    qtHouseholdNo = QStandardItem( "%i" % row[0])
		    qtHouseholdNo.setTextAlignment( Qt.AlignCenter )
		    
		    qtHouseholdName = QStandardItem( row[1] )
		    
		    qtAssetValue = QStandardItem( "%i" % row[2] )
		    qtAssetValue.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    qtIncomeValue = QStandardItem( "%i" % row[3] )
		    qtIncomeValue.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    qtExpenditure = QStandardItem( "%i" % row[4] )
		    qtExpenditure.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
		    qtDateCollected = QStandardItem( QDate(row[5]).toString("dd/MM/yyyy") )
		    qtDateCollected.setTextAlignment( Qt.AlignCenter )
		    
		    model.setItem( num, 0, qtHouseholdNo )
		    model.setItem( num, 1,  qtHouseholdName )
		    model.setItem( num, 2, qtAssetValue )
		    model.setItem( num, 3, qtIncomeValue )
		    model.setItem( num, 4, qtExpenditure )
		    model.setItem( num, 5, qtDateCollected )
		    num = num + 1
	    
		self.tableView.setModel(model)
		self.tableView.show()
		
		cursor.close()
		db.close()
		
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
		if self.countRowsSelected(self.tableView) != 0:
			# get the hhid of the selected household
			selectedRow = self.getCurrentRow(self.tableView)
			hhid = self.tableView.model().item(selectedRow,0).text()
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
		numSelected = self.countRowsSelected(self.tableView)
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
			selectedRows = self.getSelectedRows(self.tableView)
			selectedIds = []
			for row in selectedRows:
				selectedIds.append( self.tableView.model().item(row,0).text() )
			 
			# delete selected households
			
			db = data.mysql.connector.Connect(**self.config)
			cursor =  db.cursor()
			
			for hhid in selectedIds:
				query = '''DELETE FROM households WHERE hhid=%s ''' % (hhid)	
				cursor.execute(query)
				db.commit()
    
			# close database connection
			cursor.close()
			db.close()
			
			self.getHouseholds()

		else:
			QMessageBox.information(self,"Delete Households","Please select the rows containing households to be deleted.")
			
	def viewHouseholdData(self):
		if self.countRowsSelected(self.tableView) != 0:
			# get the hhid of the selected household
			selectedRow = self.getCurrentRow(self.tableView)
			hhid = self.tableView.model().item(selectedRow,0).text()
		
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
        

