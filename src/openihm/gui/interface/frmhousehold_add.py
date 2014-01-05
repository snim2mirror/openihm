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

# import the Create Project Dialog design class
Ui_AddHousehold, base_class = uic.loadUiType("gui/designs/ui_addhousehold.ui")

from mixins import MDIDialogMixin
from data.db import session_scope, error_wrapper
from gui.interface.db_errors import QErrorMessage
from model.alchemy_schema import Household


class FrmAddHousehold(QDialog, Ui_AddHousehold, MDIDialogMixin):
    ''' Creates the add household form '''

    def __init__(self, parent, projectid=None, projectname=None):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)

        self.setupUi(self)
        self.parent = parent
        self.projectid = projectid or parent.projectid
        self.mdi = None

        # set the dates to the date of today
        now = QDate.currentDate()
        self.dtpDateVisted.setDate(now)

        # allow the calendar widget to pop up
        self.dtpDateVisted.setCalendarPopup(True)

        # display project name
        self.lblProjectName.setText(projectname or parent.projectname)

    def _saveHousehold(self):
        ''' Saves newly created household data to database '''

        # get the data entered by user
        hhid = self.txtShortHouseHoldName.text()
        householdname = self.txtHouseholdName.text()
        dateofcollection = self.dtpDateVisted.date().toPyDate()
        pid = self.projectid

        # save household
        with error_wrapper(QErrorMessage(self, custom_duplicate_message="Household No already recorded")):
            with session_scope() as session:
                h = Household(hhid=hhid, householdname=householdname,
                              pid=pid, dateofcollection=dateofcollection)
                session.add(h)
        return True

    def saveHousehold(self):
        if self._saveHousehold():
            self.parent.mdi.closeActiveSubWindow()
