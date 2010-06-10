#-------------------------------------------------------------------	
#	Filename: frmhousehold_editcharacteristic.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_editcharacteristic import Ui_EditHouseholdCharacteristic

class FrmEditHouseholdCharacteristic(QDialog, Ui_EditHouseholdCharacteristic):	
    ''' Creates the Edit Household Characteristic form. '''	
    def __init__(self, parent, pid, hhid, charName, charVal):
        ''' Set up the dialog box interface '''
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.hhid = hhid
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
        	
        # connect relevant signals and slots
        self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
        self.connect(self.cmdOk, SIGNAL("clicked()"), self.saveCharacteristic)
        
    def saveCharacteristic(self):
		''' Saves characteristic '''
		
		db 		= data.mysql.connector.Connect(**self.config)
		cursor 	=  db.cursor()
		
		tbl = self.hhCharacteristicsTable
		if self.cboYesNoVal.isVisible():
			charVal = self.cboYesNoVal.currentText() 
		else:
			charVal = self.txtValue.text()
			
		if ( self.parent.getCharacteristicDataType( self.charName ) == 2 ):
			queryInsert = '''INSERT INTO %s (hhid,`%s`) VALUES (%s, %s )''' % (tbl, self.charName, self.hhid, charVal )
			queryUpdate	= '''UPDATE %s SET `%s`=%s WHERE hhid=%s''' % (tbl, self.charName, charVal, self.hhid )
		else:
		 	queryInsert = '''INSERT INTO %s (hhid,`%s`) VALUES (%s, '%s' )''' % (tbl, self.charName, self.hhid, charVal )
			queryUpdate	= '''UPDATE %s SET `%s`='%s' WHERE hhid=%s''' % (tbl, self.charName, charVal, self.hhid )
			
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
		self.close()
