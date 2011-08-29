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

from data.config import Config
import includes.mysql.connector as connector

Ui_Households_Edit, base_class = uic.loadUiType("gui/designs/ui_households_edit.ui")


from mixins import MDIDialogMixin

class FrmEditHousehold(QDialog, Ui_Households_Edit, MDIDialogMixin):	
    ''' Creates the Edit Household form. '''	
    def __init__(self, parent, projectid, projectname, hhid):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.projectid = projectid
        self.hhid = hhid
        self.config = Config.dbinfo().copy()
        self.mdi = None
        
        # get current project details
        self.getHouseholdData()
        
        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)
        
        # display project name
        self.lblProjectName.setText(projectname)

    def getHouseholdData(self):
        ''' Retrieve and display household data '''
        # select query to retrieve project data
        query = '''SELECT hhid, householdname, dateofcollection 
                     FROM households WHERE hhid=%s''' % (self.hhid)
        
        rows = self.executeResultsQuery(query)
        
        for row in rows:
            hhid = row[0]
            householdname = row[1]
            dateofcollection = row[2]
        
        self.txtShortHouseHoldName.setText(str(hhid))
        self.dtpDateVisted.setDate(dateofcollection)
        self.txtHouseholdName.setText(householdname)
        
    def saveHousehold(self):
        ''' Saves changes to household to database '''
        
        # get the data entered by user
        hhid              = self.txtShortHouseHoldName.text()
        householdname     = self.txtHouseholdName.text()
        dateofcollection  = self.dtpDateVisted.date().toString("yyyy-MM-dd")
        pid               = self.projectid
        
        # create UPDATE query
        query = '''UPDATE households SET hhid=%s, dateofcollection='%s', householdname='%s'
                     WHERE hhid=%s AND pid=%s''' % (hhid, dateofcollection, householdname,  self.hhid,  pid)
    
        self.executeUpdateQuery(query)
        # close new project window
        self.parent.getHouseholds()
        self.mdiClose()
