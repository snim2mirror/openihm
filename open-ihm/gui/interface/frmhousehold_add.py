#------------------------------------------------------------------------------------------------	
#	Filename: frmhousehold_add.py
#
#	Class to create the Add Household form - FrmAddHousehold.
#------------------------------------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.controller import Controller

# import the Create Project Dialog design class
from gui.designs.ui_addhousehold import Ui_AddHousehold

from mixins import MDIDialogMixin

class FrmAddHousehold(QDialog, Ui_AddHousehold, MDIDialogMixin):	
    ''' Creates the add household form '''	

    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        
        self.setupUi(self)
        self.parent = parent
        self.mdi = None
        
        # set the dates to the date of today
        now = QDate.currentDate()
        self.dtpDateVisted.setDate(now)
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(self.parent.projectname)


    def saveHousehold(self):
        ''' Saves newly created household data to database '''
    
        # get the data entered by user
        hhid                = self.txtShortHouseHoldName.text()
        householdname = self.txtHouseholdName.text()
        dateofcollection       = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        pid              = self.parent.projectid
        
        # save household
        controller = Controller()
        project = controller.getProject( pid )
        project.addHousehold( hhid,  householdname,  dateofcollection)
        
        # close new project window
        self.parent.mdi.closeActiveSubWindow()
