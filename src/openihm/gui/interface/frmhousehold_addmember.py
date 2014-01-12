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

Ui_AddHouseholdMember, base_class = uic.loadUiType("gui/designs/ui_household_addmember.ui")

from mixins import MDIDialogMixin
from gui.interface.db_errors import QErrorMessage
from data.db import ErrorHandler
from household_addmember import AddHouseHoldMemberLogic
from datetime import date


class FrmAddHouseholdMember(QDialog, Ui_AddHouseholdMember, MDIDialogMixin):
    ''' Creates the Add Household Member form. '''
    def __init__(self, parent,  hhid, hhname):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.logic = AddHouseHoldMemberLogic(hhid, parent.parent.projectid)

        # add years to the year of birth combo box: current year to 150 years ago
        thisyear = date.today().year
        for year in range(thisyear, thisyear-151,  -1):
            self.cmbYearOfBirth.addItem("%i" % year)

        # display household name
        self.lblHouseholdName.setText(hhname)

    def updateYearOfBirth(self):
        ''' updates year of birth when the value of age is modified '''
        age = self.txtAge.text()
        yearOfBirth = self.logic.yearOfBirth(age)
        if yearOfBirth:
            self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( yearOfBirth ) )

    def updateAge(self):
        ''' updates age when year of birth is modified'''
        yearOfBirth = self.cmbYearOfBirth.currentText()
        age = self.logic.age(yearOfBirth)
        self.txtAge.setText( age )

    def saveMember(self):
        ''' Saves changes to household to database '''

        # get the data entered by user
        sex = self.cboSex.currentText()
        age = self.txtAge.text()
        yearofbirth = self.cmbYearOfBirth.currentText()
        periodaway = self.cmbMonthsAbsent.currentText()
        reason = self.txtReason.text()
        whereto = self.txtWhere.text()

        headofhousehold = self.chkHeadHousehold.isChecked()
        eh = ErrorHandler(QErrorMessage(self))
        with eh.error_wrapper():
            if self.logic.saveMember(sex, age, yearofbirth, headofhousehold,
                                     periodaway, reason, whereto):
                # close new project window
                self.parent.retrieveHouseholdMembers()
                self.mdiClose()
