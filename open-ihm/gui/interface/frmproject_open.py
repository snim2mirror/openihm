#-------------------------------------------------------------------	
#	Filename: frmproject_open.py
#
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

from data.controller import Controller

# import forms required to edit household
from gui.designs.ui_project_open import Ui_OpenProject

class FrmOpenProject(QtGui.QDialog, Ui_OpenProject):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # get projects
        self.getProjects()
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdOk, QtCore.SIGNAL("clicked()"), self.openProject)
        
    def getProjects(self):
        # connect to mysql database
        controller = Controller()
        
        for project in controller.getProjects():
            projectid = project.getProjectID()
            projectname = project.getProjectName()
            self.cboProjectName.addItem(projectname, QtCore.QVariant(projectid))
    
    def openProject(self):
        ''' Show Household Details '''
        temp = self.cboProjectName.itemData(self.cboProjectName.currentIndex()).toInt()
        self.parent.projectid = temp[0]
        self.parent.projectname = self.cboProjectName.currentText()
        self.parent.setWindowTitle("Open IHM - " + self.cboProjectName.currentText())
        self.parent.actionClose_Project.setDisabled(False)
        self.parent.mdi.closeActiveSubWindow()
