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

from data.controller import Controller

# import the Create Project Dialog design class
Ui_AddHousehold, base_class = uic.loadUiType("gui/designs/ui_addhousehold.ui")

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
