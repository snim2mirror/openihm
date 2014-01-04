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

# import form design
Ui_DeleteHousehold, base_class = uic.loadUiType("gui/designs/ui_household_delete.ui")

from mixins import MDIDialogMixin


class FrmDelHousehold(QDialog, Ui_DeleteHousehold, MDIDialogMixin):    
    ''' Creates the Edit Project form. '''    
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        
        # get projects
        self.getHouseholds()

    def getHouseholds(self):
        
        # select query to retrieve project data
        with session_scope() as session:
            query = household.search(session, self.parent.projectid)
        
            for row in query:
                hhid = row.hhid
                householdname = row.householdname
                self.cboHouseholdName.addItem(householdname, QVariant(hhid))
    
    def delHousehold(self):
        ''' Delete Selected Household '''
        temp = self.cboHouseholdName.itemData(self.cboHouseholdName.currentIndex()).toInt()
        hhid = temp[0]

        # select query to retrieve project data
        
        count = 0
        with session_scope() as session:
            query = household.search(session, self.parent.projectid, number=hhid)
            count = query.count()
        
        if count:
            msg = "Are sure sure you want to delete this household?"
            ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
            if ret == QMessageBox.Yes:
                with session_scope() as session:
                    household.remove_house(session, self.parent.projectid, [hhid])
                QMessageBox.information(self,"Notice","Household has been deleted")
                self.close()
        else:
            QMessageBox.information(self, "Notice", "Household Not found")

        
        
        
        
