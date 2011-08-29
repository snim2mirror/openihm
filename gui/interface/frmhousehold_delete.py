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

from data.config import Config
import includes.mysql.connector as connector

# import form design
from gui.designs.ui_household_delete import Ui_DeleteHousehold

from mixins import MDIDialogMixin

class FrmDelHousehold(QDialog, Ui_DeleteHousehold, MDIDialogMixin):	
    ''' Creates the Edit Project form. '''	
    def __init__(self, parent):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        
        self.config = Config.dbinfo().copy()
        
        # get projects
        self.getHouseholds()

    def getHouseholds(self):
        # connect to mysql database
        db = connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT hhid, householdname 
                     FROM households WHERE pid=%i''' % (self.parent.projectid)
        
        cursor.execute(query)
        
        for row in cursor.fetchall():
            hhid = row[0]
            householdname = row[1]
            self.cboHouseholdName.addItem(householdname, QVariant(hhid))
            
        cursor.close()
        db.close()
    
    def delHousehold(self):
        ''' Delete Selected Household '''
        temp = self.cboHouseholdName.itemData(self.cboHouseholdName.currentIndex()).toInt()
        hhid = temp[0]
        
        # connect to mysql database
        db = connector.Connect(**self.config)
        cursor = db.cursor()
        
        # select query to retrieve project data
        query = '''SELECT * FROM households WHERE pid=%i AND hhid=%s''' % (self.parent.projectid, hhid)
        
        cursor.execute(query)
        
        numresult = len(cursor.fetchall())
        
        if numresult:
        	msg = "Are sure sure you want to delete this household?"
        	ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
        	if ret == QMessageBox.Yes:
        		query = '''DELETE FROM households WHERE pid=%i AND hhid=%s''' % (self.parent.projectid, hhid)
        		cursor.execute(query)
        		db.commit()
        		QMessageBox.information(self,"Notice","Household has been deleted")
        else:
        	QMessageBox.information(self, "Notice", "Household Not found")
        	
        cursor.close()
        db.close()
        
        self.mdiClose()
        
        
        
        
