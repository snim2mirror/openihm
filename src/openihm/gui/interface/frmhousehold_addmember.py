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
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

from data.config import Config

Ui_AddHouseholdMember, base_class = uic.loadUiType("gui/designs/ui_household_addmember.ui")


from mixins import MDIDialogMixin, MySQLMixin

class FrmAddHouseholdMember(QDialog, Ui_AddHouseholdMember, MySQLMixin, MDIDialogMixin):	
    ''' Creates the Add Household Member form. '''	
    def __init__(self, parent,  hhid, hhname):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        
        # connect to database
        config = Config.dbinfo().copy()
        self.db = connector.Connect(**config)
        
        # add years to the year of birth combo box: current year to 150 years ago
        thisyear = date.today().year
        for year in range(thisyear, thisyear-151,  -1):
             self.cmbYearOfBirth.addItem("%i" % year)
        
        # display household name
        self.lblHouseholdName.setText(hhname)
        
    def updateYearOfBirth(self):
        ''' updates year of birth when the value of age is modified '''
        thisyear = date.today().year
        age = self.txtAge.text()
        if age != None and age != "":
            yearOfBirth = thisyear - int(age)
            self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( "%i" % yearOfBirth ) )
        
    def updateAge(self):
        ''' updates age when year of birth is modified'''
        yearOfBirth = self.cmbYearOfBirth.currentText()
        thisyear = date.today().year
        age = thisyear - int(yearOfBirth)
        self.txtAge.setText( "%i" % age )
        
    def saveMember(self):
        ''' Saves changes to household to database '''    	
        
        # get the data entered by user
        sex   			= self.cboSex.currentText()
        age = self.txtAge.text()
        
        if ( sex == "Male"):
             memberid = "m%s" % age
        else:
             memberid = "f%s" % age
             
        education       = ""
        yearofbirth = self.cmbYearOfBirth.currentText()
        if self.chkHeadHousehold.isChecked():
        	headhousehold = "Yes"
        else:
        	headhousehold = "No"
        
        pid = self.parent.parent.projectid
        periodaway = self.cmbMonthsAbsent.currentText()
        reason = self.txtReason.text()
        whereto = self.txtWhere.text()
        # create UPDATE query
        query = '''INSERT INTO householdmembers 
        	    VALUES('%s',%s,'%s',%s,'%s','%s',%s,%s,'%s','%s')''' % (memberid, self.hhid, headhousehold, yearofbirth, sex, education, pid, periodaway, reason, whereto)
    
        self.executeUpdateQuery(query)
        
        # close new project window
        self.parent.retrieveHouseholdMembers()
        self.mdiClose()
