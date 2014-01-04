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
from PyQt4 import uic

from data.db import session_scope
import alchemy.household as household

Ui_Households_Edit, base_class = uic.loadUiType("gui/designs/ui_households_edit.ui")

from mixins import MDIDialogMixin

class FrmEditHousehold(QDialog, Ui_Households_Edit, MDIDialogMixin):	

    ''' Creates the Edit Household form. '''	
    def __init__(self, parent, projectid=None, projectname=None, hhid=None):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.projectid = projectid or parent.projectid
        self.hhid = hhid
        self.mdi = None
        
        # get current project details
        self.getHouseholdData()
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(projectname or parent.projectname)

    def getHouseholdData(self):
        ''' Retrieve and display household data '''

        with session_scope() as session:
            q = household.search(session, self.projectid, number=self.hhid)
            house = q.all()[0]
            hhid = house.hhid
            householdname = house.householdname
            dateofcollection = house.dateofcollection
        
            self.txtShortHouseHoldName.setText(str(hhid))
            self.dtpDateVisted.setDate(dateofcollection)
            self.txtHouseholdName.setText(householdname)
        
    def _saveHousehold(self):
        ''' Saves changes to household to database '''
        
        # get the data entered by user
        hhid              = self.txtShortHouseHoldName.text()
        householdname     = self.txtHouseholdName.text()
        dateofcollection  = self.dtpDateVisted.date().toPyDate()
        
        with session_scope() as session:
            q = household.search(session, self.projectid, number=self.hhid)
            house = q.all()[0]
            house.hhid = hhid
            house.householdname = householdname
            house.dateofcollection = dateofcollection
            # NOTE: the implicit commit here will cause the changes to be saved.

        return True
        
    def saveHousehold(self):
        # close new project window
        if self._saveHousehold():
            self.parent.getHouseholds()
            self.mdiClose()
