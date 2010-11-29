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
         self.pid           = parent.parent.projectid
         self.assetid 	= assetid
         
         self.config = Config.dbinfo().copy()

         self.getAssetCategories()
         self.getAssetTypes()

         if ( assetid != 0 ):
             self.displayAssetDetails()
             self.setWindowTitle( "Edit Household Asset" )

         # display household name
         self.lblHouseholdName.setText(hhname)

         # connect relevant signals and slots
         self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
         self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveAsset)
         self.connect(self.cboAssetCategory, SIGNAL("currentIndexChanged(int)"), self.getAssetTypes)
         self.connect(self.cboAssetType, SIGNAL("currentIndexChanged(int)"), self.displayUnitOfMeasure)
    
     def getAssetCategories(self):
         ''' Retrieve Asset Categories and display them in a combobox '''
         # for now categories are hard coded (later will be moved to database)
         categories = ['Food Stock', 'Live Stock',  'Land',  'Trees', 'Tradable Goods']
         
         for category in categories:
             self.cboAssetCategory.addItem(category)
         
     def getAssetTypes(self):
         ''' Retrieve Asset Types and display them in a combobox '''
         category = self.cboAssetCategory.currentText()
         if ( category == "Food Stock" ):
             tblname = "setup_crops"
             assetfld = "foodtype"
             unitfld = "measuringunit"
         elif ( category == "Live Stock" ):
             tblname = "setup_livestock"
             assetfld = "incomesource"
             unitfld = "unitofmeasure"
         elif ( category == "Land" ):
             tblname = "setup_landtypes"
             assetfld = "landtype"
             unitfld = "unitofmeasure"
         elif ( category == "Trees" ):
             tblname = "setup_treetypes"
             assetfld = "treetype"
             unitfld = "measuringunit"
         elif ( category == "Tradable Goods" ):
             tblname = "setup_tradablegoods"
             assetfld = "tradablegoodtype"
             unitfld = "unitofmeasure"
             
         query = '''SELECT %s, %s FROM %s''' % (assetfld, unitfld, tblname)

         db = data.mysql.connector.Connect(**self.config)             
         cursor = db.cursor()

         cursor.execute(query)
         self.cboAssetType.clear()
         for row in cursor.fetchall():
             assettype = row[0]
             unitofmeasure = row[1]
             self.cboAssetType.addItem(assettype,  QVariant(unitofmeasure))
        
         unitofmeasure = self.cboAssetType.itemData( self.cboAssetType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )

         cursor.close()   
         db.close()
         
     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cboAssetType.itemData( self.cboAssetType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
        
     def displayAssetDetails(self):
         ''' Retrieve and display Household Asset details '''
         query = '''SELECT * FROM assets WHERE hhid=%s AND pid=%s AND assetid=%s ''' % ( self.hhid, self.pid,  self.assetid )
         
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
             query = '''INSERT INTO assets (hhid, assettype, unitofmeasure, unitcost, totalunits, pid )
                 VALUES(%s,'%s','%s',%s,%s,%s) ''' % ( self.hhid, assettype, unitofmeasure, costperunit, numunits, self.pid )
         else:
             query = ''' UPDATE assets SET assettype='%s', unitofmeasure='%s', unitcost=%s, totalunits=%s
                     WHERE hhid=%s AND pid=%s 
                     AND assetid=%s ''' % ( assettype, unitofmeasure, costperunit, numunits, self.hhid, self.pid,  self.assetid)

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
