#-------------------------------------------------------------------	
#	Filename: frmfindprojectresults.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector

# import the Create Project Dialog design class
from gui.designs.ui_findprojectresults import Ui_FindProjectResults

class FrmFindProjectResults(QDialog, Ui_FindProjectResults):	
	''' Creates the Find Project from, under the Project menu. Uses the design class
		in gui.designs.ui_findproject. '''	
	def __init__(self, parent, pid, ptitle):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent = parent
		self.config = Config.dbinfo().copy()
		
		self.txtProjectID.setText( pid )
		self.txtProjectTitle.setText ( ptitle )
		
		self.tblResults.setSelectionMode( QAbstractItemView.SingleSelection )
		
		self.showResults()
		
		# connect relevant signals and slots
		self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
		self.connect(self.cmdSearch, SIGNAL("clicked()"), self.showResults)
		self.connect(self.cmdOpen, SIGNAL("clicked()"), self.openProject)

	def showResults(self):
		''' Find a project matching the criteria entered by user '''
		pid 			= self.txtProjectID.text()
		ptitle 			= self.txtProjectTitle.text()
	
		SQLcondition 	= ""
		if ( pid != "" ):
			SQLcondition = " WHERE pid=%s" % pid
		
		if ( ptitle != "" ):
			if ( SQLcondition == "" ):
				SQLcondition = " WHERE projectname LIKE '%" + "%s" % ( ptitle ) + "%'" 
			else:
				SQLcondition = SQLcondition + " OR projectname LIKE '%" + "%s" % ( ptitle ) + "%'" 
				
		query = ''' SELECT * FROM projects%s''' % ( SQLcondition )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		count = len( rows )
		
		self.setWindowTitle("%i matching project(s) found." % (count) )
		
		model = QStandardItemModel(1,2)
		
		# set model headers
		model.setHorizontalHeaderItem(0,QStandardItem('Project ID.'))
		model.setHorizontalHeaderItem(1,QStandardItem('Project Title'))
		model.setHorizontalHeaderItem(2,QStandardItem('Start Date'))
		model.setHorizontalHeaderItem(3,QStandardItem('End Date'))
		
		# add  data rows
		num = 0
	    
		for row in rows:
		    qtProjectID = QStandardItem( "%i" % row[0])
		    qtProjectID.setTextAlignment( Qt.AlignCenter )
		    
		    qtProjectTitle = QStandardItem( row[1] )
		    
		    qtStartDate = QStandardItem( QDate(row[2]).toString("dd/MM/yyyy") )
		    qtStartDate.setTextAlignment( Qt.AlignCenter )
		    
		    qtEndDate = QStandardItem( QDate(row[3]).toString("dd/MM/yyyy") )
		    qtEndDate.setTextAlignment( Qt.AlignCenter )
		    
		    model.setItem( num, 0, qtProjectID )
		    model.setItem( num, 1, qtProjectTitle )
		    model.setItem( num, 2, qtStartDate )
		    model.setItem( num, 3, qtEndDate )
		    num = num + 1
	    
		self.tblResults.setModel(model)
		self.tblResults.resizeColumnsToContents()
		self.tblResults.show()
		
		cursor.close()
		db.close()
		
	def openProject(self):
		''' Open Selected Project '''
		
		msg = "Opening the selected project will close all active sub windows. Are you sure you want to open the project?"
		
		ret = QMessageBox.question(self,"Confirm Opening", msg, QMessageBox.Yes|QMessageBox.No)
		# if opening is rejected return
		if ( ret == QMessageBox.No ):
			return
		
		selectedRow = self.tblResults.currentIndex().row()
		pid 		= self.tblResults.model().item(selectedRow,0).text()
		ptitle 		= self.tblResults.model().item(selectedRow,1).text()
		
		self.parent.projectid = int( pid )
		self.parent.projectname = ptitle
		self.parent.setWindowTitle( "Open IHM - " + ptitle )
		self.parent.actionClose_Project.setDisabled(False)
		self.parent.mdi.closeAllSubWindows()
		
			