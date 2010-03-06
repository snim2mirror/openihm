#-------------------------------------------------------------------	
#	Filename: frmproject_open.py
#
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import forms required to edit household
from gui.designs.ui_project_open import Ui_OpenProject

class FrmOpenProject(QtGui.QDialog, Ui_OpenProject):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # connect relevant signals and slots
        self.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmdOk, QtCore.SIGNAL("clicked()"), self.openProject)
    
    def openProject(self):
        ''' Show Household Details '''
        self.parent.setWindowTitle("Open IHM - " + self.cboProjectName.currentText())
        self.parent.mdi.closeActiveSubWindow()
