#-------------------------------------------------------------------	
#	Filename: frmhousehold_edit_getid.py
#
#	form that gets the ID of a household to be editted.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.controller import Controller

# import forms required to edit household
from gui.designs.ui_edithousehold_getid import Ui_EditHouseholdGetID
from frmhousehold_edit_details import FrmEditHouseholdDetails

class FrmEditHouseholdGetID(QDialog, Ui_EditHouseholdGetID):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        self.parent = parent
        QDialog.__init__(self)
        self.setupUi(self)
        
        # get projects
        self.getHouseholds()
        
    def mdiClose(self):
        self.parent.mdi.closeActiveSubWindow()
        
    def getHouseholds(self):
        controller = Controller()
        project = controller.getProject( self.parent.projectid )
        households = project.getHouseholds()
        
        for household in households:
            hhid = household.getHouseholdID()
            householdname = household.getHouseholdName()
            self.cboHouseholdName.addItem(householdname, QVariant(hhid))
    
    def showDetails(self):
        ''' Show Household Details '''
        temp = self.cboHouseholdName.itemData(self.cboHouseholdName.currentIndex()).toInt()
        hhid = temp[0]
        form = FrmEditHouseholdDetails(self.parent, hhid)
        subWin = self.parent.mdi.addSubWindow(form)
        self.parent.centerSubWindow(subWin)
        # close this form
        self.parent.mdi.closeActiveSubWindow()
        # show the details form
        form.show()
