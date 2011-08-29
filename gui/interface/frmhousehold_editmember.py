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

from data.config import Config

from gui.designs.ui_household_editmember import Ui_EditHouseholdMember

from mixins import MDIDialogMixin, MySQLMixin

class FrmEditHouseholdMember(QDialog, Ui_EditHouseholdMember, MySQLMixin, MDIDialogMixin):	
     ''' Creates the Edit Household Member form. '''	
     def __init__(self, parent,  hhid, hhname, memberid):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent = parent
         self.hhid = hhid
         self.currentid = memberid
         
         # configure connect to database
         self.config = Config.dbinfo().copy()
        
         # add years to the year of birth combo box: current year to 150 years ago
         thisyear = date.today().year
         for year in range(thisyear, thisyear-151,  -1):
             self.cmbYearOfBirth.addItem("%i" % year)
        
         # display household name
         self.lblHouseholdName.setText(hhname)
        
         # get and display member details
         self.getMemberDetails()
        
     def updateYearOfBirth(self):
         ''' updates year of birth when the value of age is modified '''
         thisyear = date.today().year
         age = self.txtAge.text()
         yearOfBirth = thisyear - int(age)
         self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( "%i" % yearOfBirth ) )
        
     def updateAge(self):
         ''' updates age when year of birth is modified'''
         yearOfBirth = self.cmbYearOfBirth.currentText()
         thisyear = date.today().year
         age = thisyear - int(yearOfBirth)
         self.txtAge.setText( "%i" % age )
        
     def getMemberDetails(self):
         ''' retrieves and displays details of the member being editted '''
         pid = self.parent.parent.projectid
         # query to retrieve member details
         query = '''SELECT personid, headofhousehold, yearofbirth, sex, periodaway, reason, whereto 
                   FROM householdmembers WHERE hhid=%s AND personid='%s' AND pid=%s ''' % (self.hhid, self.currentid, pid)
         
         rows = self.executeResultsQuery(query)
         
         for row in rows:
             self.lblMemberID.setText( row[0] )			
             if row[1] == "Yes":
                 self.chkHeadHousehold.setChecked(True)	
             age = date.today().year - row[2]
             self.txtAge.setText( "%i" % age )
             self.cmbYearOfBirth.setCurrentIndex( self.cmbYearOfBirth.findText( "%i" % row[2] ) )
         
             self.cboSex.setCurrentIndex(self.cboSex.findText(row[3]))
             self.cmbMonthsAbsent.setCurrentIndex( self.cmbMonthsAbsent.findText( str( row[4]) ) )
             self.txtReason.setText( row[5] )
             self.txtWhere.setText( row[6] )
         
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
         query = '''UPDATE householdmembers SET personid='%s', headofhousehold='%s', yearofbirth=%s, sex='%s', 
             periodaway=%s, reason='%s', whereto='%s',education='%s' WHERE hhid=%s AND personid='%s' 
             AND pid=%s''' % (memberid, headhousehold, yearofbirth, sex, periodaway,  reason,  whereto, education, self.hhid, self.currentid, pid)
    
         self.executeUpdateQuery(query)
         
         # close new project window
         self.parent.retrieveHouseholdMembers()
         self.mdiClose()
