#-------------------------------------------------------------------	
#	Filename: frmproject_edit.py
#
#	Class to create the Edit Project form - FrmEditProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from data.config import Config
import data.mysql.connector 

# import the Edit Project Dialog design class
from gui.designs.ui_editproject_details import Ui_EditProject

class FrmEditProject(QtGui.QDialog, Ui_EditProject):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.config = Config.dbinfo().copy()
        
        # get current project details
        self.getProjectData()
        
        # allow the calendar widget to pop up
        self.dtpStartDate.setCalendarPopup(True)
        self.dtpEndDate.setCalendarPopup(True)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), self.saveProject)
        
    def getProjectData(self):
        ''' Retrieves project data from the database '''
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT projectname, startdate, enddate, description, currency 
                     FROM projects WHERE pid=%i''' % (self.parent.projectid)
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            projectname = row[0]
            startdate = row[1]
            enddate = row[2]
            description = row[3]
            currency = row[4]
        
        self.lblProjectID.setText(str(self.parent.projectid))
        self.txtProjectName.setText(projectname)
        self.dtpStartDate.setDate(startdate)
        self.dtpEndDate.setDate(enddate)
        self.txtDescription.setText(description)
        self.cmbCurrency.setCurrentIndex(self.cmbCurrency.findText(currency))
        
    def saveProject(self):
        ''' Saves changes database '''
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # get the data entered by user
        projectname = self.txtProjectName.text()
        startdate     = self.dtpStartDate.date().toString("yyyy-MM-dd")
        enddate       = self.dtpEndDate.date().toString("yyyy-MM-dd")
        description   = self.txtDescription.toPlainText()
        currency      = self.cmbCurrency.currentText()
        pid              = self.parent.projectid
        
        # create INSERT INTO query
        query = '''UPDATE projects SET projectname='%s', startdate = '%s',enddate = '%s',description = '%s',currency = '%s'
                     WHERE pid=%i''' % (projectname, startdate, enddate, description, currency, pid)
    
        # execute query and commit changes
        cursor.execute(query)
        db.commit()
        
        # set the newly inserted project as the current project
        self.parent.projectname = projectname
        self.parent.setWindowTitle("Open IHM - " + projectname)
        
        # close database connection
        cursor.close()
        db.close()
        
        # close new project window
        self.parent.mdi.closeActiveSubWindow()
