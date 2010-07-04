#-------------------------------------------------------------------	
#	Filename: frmnewproject.py
#
#	Class to create the Create Project form - FrmNewProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_newproject import Ui_NewProject

from data.controller import Controller

class FrmNewProject(QtGui.QDialog, Ui_NewProject):	
    ''' Creates the Create Project from. Uses the design class
        in gui.designs.ui_newproject. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        
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
        # get the data entered by user
        projectname = self.txtProjectName.text()
        startdate     = self.dtpStartDate.date().toString("yyyy-MM-dd")
        enddate       = self.dtpEndDate.date().toString("yyyy-MM-dd")
        description   = self.txtDescription.toPlainText()
        currency      = self.cmbCurrency.currentText()
        # create project
        controller      = Controller()
        project         = controller.addProject(projectname, startdate, enddate, description, currency)
        
        # set the newly inserted project as the current project
        self.parent.projectid = project.getProjectID()
        self.parent.projectname = project.getProjectName()
        self.parent.setWindowTitle("Open IHM - " + projectname)
        self.parent.actionClose_Project.setDisabled(False)
        
        # close new project window
        self.parent.mdi.closeActiveSubWindow()
