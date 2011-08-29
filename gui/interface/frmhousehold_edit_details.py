#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""

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
