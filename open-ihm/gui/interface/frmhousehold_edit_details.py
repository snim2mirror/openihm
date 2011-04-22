#-------------------------------------------------------------------	
#	Filename: frmhousehold_edit_details.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.controller import Controller

from gui.designs.ui_edithousehold_details import Ui_EditHousehold

from mixins import MDIDialogMixin

class FrmEditHouseholdDetails(QDialog, Ui_EditHousehold, MDIDialogMixin):	
    ''' Creates the Edit Household form. '''	
    def __init__(self, parent,  hhid):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        
        # get current project details
        controller = Controller()
        project  = controller.getProject( self.parent.projectid )
        self.household = project.getHousehold( self.hhid )
        self.showHouseholdDetails()
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(self.parent.projectname)
        
    def showHouseholdDetails(self):
        ''' Retrieve and display household data '''
        self.txtShortHouseHoldName.setText(str( self.household.getHouseholdID() ))
        self.dtpDateVisted.setDate( self.household.getDateOfCollection() )
        self.txtHouseholdName.setText( self.household.getHouseholdName() )
        
    def saveHousehold(self):
        ''' Saves changes to household to database '''
        
        # get the data entered by user
        newhhid                    = self.txtShortHouseHoldName.text()
        householdname     = self.txtHouseholdName.text()
        dateofcollection    = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        
        # save household
        self.household.setData( householdname,  dateofcollection,  newhhid )
        
        # close new project window
        self.mdiClose()
