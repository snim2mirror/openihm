#-------------------------------------------------------------------	
#	Filename: frmhousehold_editcharacteristic.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import includes.mysql.connector as connector

from gui.designs.ui_household_editcharacteristic import Ui_EditHouseholdCharacteristic

from mixins import MDIDialogMixin

class FrmEditHouseholdCharacteristic(QDialog, Ui_EditHouseholdCharacteristic, MDIDialogMixin):	
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
		
		db 		= connector.Connect(**self.config)
		cursor 	=  db.cursor()
		
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
			cursor.execute(queryInsert)
		except:
			cursor.execute(queryUpdate)
			
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
			
		# close window and refresh characteristics
		self.parent.retrieveHouseholdCharacteristics()
		self.mdiClose()
