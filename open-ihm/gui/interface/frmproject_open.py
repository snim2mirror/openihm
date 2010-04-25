#-------------------------------------------------------------------	
#	Filename: frmproject_open.py
#
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from data.config import Config
import data.mysql.connector 

# import forms required to edit household
from gui.designs.ui_project_open import Ui_OpenProject

class FrmOpenProject(QtGui.QDialog, Ui_OpenProject):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.parent = parent
        self.config = Config.dbinfo().copy()
        
        # get projects
        self.getProjects()
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdOk, QtCore.SIGNAL("clicked()"), self.openProject)
        
    def getProjects(self):
        # connect to mysql database
        db = data.mysql.connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT pid, projectname FROM projects'''
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            projectid = row[0]
            projectname = row[1]
            self.cboProjectName.addItem(projectname, QtCore.QVariant(projectid))
    
    def openProject(self):
        ''' Show Household Details '''
        temp = self.cboProjectName.itemData(self.cboProjectName.currentIndex()).toInt()
        self.parent.projectid = temp[0]
        self.parent.projectname = self.cboProjectName.currentText()
        self.parent.setWindowTitle("Open IHM - " + self.cboProjectName.currentText())
        self.parent.mdi.closeActiveSubWindow()
