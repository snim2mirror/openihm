#-------------------------------------------------------------------	
#	Filename: frmnewproject.py
#
#	Class to create the Create Project form - FrmNewProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_newproject import Ui_NewProject

from data.config import Config
import data.mysql.connector 

class FrmNewProject(QtGui.QDialog, Ui_NewProject):	
    ''' Creates the Create Project from. Uses the design class
        in gui.designs.ui_newproject. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.config = Config.dbinfo().copy()
        
        # set the dates to the date of today
        now = QtCore.QDate.currentDate()
        self.dtpStartDate.setDate(now)
        self.dtpEndDate.setDate(now)
        
        # allow the calendar widget to pop up
        self.dtpStartDate.setCalendarPopup(True)
        self.dtpEndDate.setCalendarPopup(True)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), self.saveProject)
        
    def saveProject(self):
        ''' Saves newly created data to database '''
        
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # get the data entered by user
        projectname = self.txtProjectName.text()
        startdate     = self.dtpStartDate.date().toString("yyyy-MM-dd")
        enddate       = self.dtpEndDate.date().toString("yyyy-MM-dd")
        description   = self.txtDescription.toPlainText()
        currency      = self.cmbCurrency.currentText()
        
        # create INSERT INTO query
        query = '''INSERT INTO projects(projectname,startdate,enddate,description,currency) 
                     VALUES('%s','%s', '%s', '%s', '%s')''' % (projectname, startdate, enddate, description, currency)
    
        # execute query and commit changes
        cursor.execute(query)
        db.commit()
        
        # get the ID of the newly inserted project
        query = "SELECT LAST_INSERT_ID()"
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            projectid = row[0]
            
        # create project specific tables (e.g. householdcharacteristics & personalcharacteristics)
         
        # set the newly inserted project as the current project
        self.parent.projectid = projectid
        self.parent.projectname = projectname
        self.parent.setWindowTitle("Open IHM - " + projectname)
        self.parent.actionClose_Project.setDisabled(False)
        
        # close database connection
        cursor.close()
        db.close()
        
        # close new project window
        self.parent.mdi.closeActiveSubWindow()
