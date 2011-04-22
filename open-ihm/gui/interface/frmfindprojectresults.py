#-------------------------------------------------------------------	
#	Filename: frmfindprojectresults.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.controller import Controller

# import the Create Project Dialog design class
from gui.designs.ui_findprojectresults import Ui_FindProjectResults

from mixins import MDIDialogMixin

class FrmFindProjectResults(QDialog, Ui_FindProjectResults, MDIDialogMixin):	
    ''' Creates the Find Project from, under the Project menu. Uses the design class
        in gui.designs.ui_findproject. '''	
    def __init__(self, parent, pid, ptitle):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        
        self.txtProjectID.setText( pid )
        self.txtProjectTitle.setText ( ptitle )
        
        self.tblResults.setSelectionMode( QAbstractItemView.SingleSelection )
        
        self.showResults()
        
    def showResults(self):
        ''' Find a project matching the criteria entered by user '''
        pid 			= self.txtProjectID.text()
        ptitle 			= self.txtProjectTitle.text()

        controller  = Controller()
        projects    = controller.getProjectsMatching(  pid, ptitle )
        count = len( projects )

        self.setWindowTitle("%i matching project(s) found." % (count) )

        model = QStandardItemModel(1,2)

        # set model headers
        model.setHorizontalHeaderItem(0,QStandardItem('Project ID.'))
        model.setHorizontalHeaderItem(1,QStandardItem('Project Title'))
        model.setHorizontalHeaderItem(2,QStandardItem('Start Date'))
        model.setHorizontalHeaderItem(3,QStandardItem('End Date'))

        # add  data rows
        num = 0

        for project in projects:
            qtProjectID = QStandardItem( "%i" % project.getProjectID() )
            qtProjectID.setTextAlignment( Qt.AlignCenter )
            
            qtProjectTitle = QStandardItem( project.getProjectName() )
            
            qtStartDate = QStandardItem( QDate( project.getStartDate() ).toString("dd/MM/yyyy") )
            qtStartDate.setTextAlignment( Qt.AlignCenter )
            
            qtEndDate = QStandardItem( QDate( project.getEndDate() ).toString("dd/MM/yyyy") )
            qtEndDate.setTextAlignment( Qt.AlignCenter )
            
            model.setItem( num, 0, qtProjectID )
            model.setItem( num, 1, qtProjectTitle )
            model.setItem( num, 2, qtStartDate )
            model.setItem( num, 3, qtEndDate )
            num = num + 1

        self.tblResults.setModel(model)
        self.tblResults.resizeColumnsToContents()
        self.tblResults.show()

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
        
            
