#-------------------------------------------------------------------	
#	Filename: frmhousehold_addasset.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_addasset import Ui_AddHouseholdAsset

class FrmHouseholdAsset(QDialog, Ui_AddHouseholdAsset):	
    ''' Form to add or edit a Household Asset  '''	
    def __init__(self, parent,  hhid, hhname, assetid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.hhid 		= hhid
		self.assetid 	= assetid
		
		self.config = Config.dbinfo().copy()
		
		self.getAssetTypes()
		
		if ( assetid != 0 ):
			self.displayAssetDetails()
			self.setWindowTitle( "Edit Household Asset" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveAsset)
        
    def getAssetTypes(self):
		''' Retrieve Asset Types and display them in a combobox '''
		# select query to Asset Types
		query = '''SELECT assettype FROM assettypes'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    assettype = row[0]
		    self.cboAssetType.addItem(assettype)
		 
		cursor.close()   
		db.close()
        
    def displayAssetDetails(self):
		''' Retrieve and display Household Asset details '''
		query = '''SELECT * FROM assets WHERE hhid=%s AND assetid=%s ''' % ( self.hhid, self.assetid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    assettype = row[2]
		    self.cboAssetType.setCurrentIndex( self.cboAssetType.findText( assettype ) )
		    unitofmeasure = row[3]
		    self.txtUnitOfMeasure.setText( unitofmeasure )
		    costperunit = row[4]
		    self.txtCostPerUnit.setText( str(costperunit) )
		    numunits = row[5]
		    self.txtNumberOfUnits.setText( str(numunits) )
		 
		cursor.close()   
		db.close()
        
    def saveAsset(self):
		''' Saves asset to database '''    	
		
		# get the data entered by user
		assettype       = self.cboAssetType.currentText()
		unitofmeasure	= self.txtUnitOfMeasure.text()
		costperunit     = self.txtCostPerUnit.text()
		numunits        = self.txtNumberOfUnits.text()
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.assetid == 0):
			query = '''INSERT INTO assets (hhid, assettype, unitofmeasure, unitcost, totalunits )
			    VALUES(%s,'%s','%s',%s,%s) ''' % ( self.hhid, assettype, unitofmeasure, costperunit, numunits )
		else:
			query = ''' UPDATE assets SET assettype='%s', unitofmeasure='%s', unitcost=%s, totalunits=%s
						WHERE hhid=%s 
						AND assetid=%s ''' % ( assettype, unitofmeasure, costperunit, numunits, self.hhid, self.assetid)
		
		# execute query and commit changes
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdAssets()
		self.close()
