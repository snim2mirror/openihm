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

from gui.designs.ui_household_editcharacteristic import Ui_EditHouseholdCharacteristic

from mixins import MDIDialogMixin, MySQLMixin

class FrmEditHouseholdCharacteristic(QDialog, Ui_EditHouseholdCharacteristic, MySQLMixin, MDIDialogMixin):	
    ''' Creates the Edit Household Characteristic form. '''	
    def __init__(self, parent, pid, hhid, charName, charVal):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
        self.pid = pid
        self.charName = charName
        self.hhCharacteristicsTable = "p%iHouseholdCharacteristics" % (pid )
        # connect to database
        self.config = Config.dbinfo().copy()       
        
        # display characteristic name
        self.lblCharName.setText(charName)
        if ( self.parent.getCharacteristicDataType( charName ) == 1 ):
        	self.cboYesNoVal.setVisible( True )
        	self.txtValue.setVisible( False )
        	if ( charVal != "Not Set" ):
        		self.cboYesNoVal.setCurrentIndex( self.cboYesNoVal.findText( charVal ) )
        else:
        	self.cboYesNoVal.setVisible( False )
        	self.txtValue.setVisible( True )
        	if ( charVal != "Not Set" ):
        		self.txtValue.setText( charVal )
        	
    def saveCharacteristic(self):
		''' Saves characteristic '''
		
		tbl = self.hhCharacteristicsTable
		if self.cboYesNoVal.isVisible():
			charVal = self.cboYesNoVal.currentText() 
		else:
			charVal = self.txtValue.text()
			
		if ( self.parent.getCharacteristicDataType( self.charName ) == 2 ):
			queryInsert = '''INSERT INTO %s (hhid, pid,`%s`) VALUES (%s, %s, %s )''' % (tbl, self.charName, self.hhid, self.pid,  charVal )
			queryUpdate	= '''UPDATE %s SET `%s`=%s WHERE hhid=%s and pid=%s''' % (tbl, self.charName, charVal, self.hhid,  self.pid )
		else:
		 	queryInsert = '''INSERT INTO %s (hhid, pid,`%s`) VALUES (%s, %s, '%s' )''' % (tbl, self.charName, self.hhid, self.pid,  charVal )
		 	queryUpdate	= '''UPDATE %s SET `%s`='%s' WHERE hhid=%s and pid=%s''' % (tbl, self.charName, charVal, self.hhid,  self.pid )
		 	
		try:
			self.executeUpdateQuery(queryInsert)
		except:
			self.executeUpdateQuery(queryUpdate)
			
		# close window and refresh characteristics
		self.parent.retrieveHouseholdCharacteristics()
		self.mdiClose()
