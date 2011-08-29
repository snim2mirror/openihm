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

from gui.designs.ui_household_addasset import Ui_AddHouseholdAsset

from mixins import MDIDialogMixin

class FrmHouseholdAsset(QDialog, Ui_AddHouseholdAsset, MDIDialogMixin):	
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

         rows = self.executeResultsQuery(query)
         self.cboAssetType.clear()
         for row in rows:
             assettype = row[0]
             unitofmeasure = row[1]
             self.cboAssetType.addItem(assettype,  QVariant(unitofmeasure))
        
         unitofmeasure = self.cboAssetType.itemData( self.cboAssetType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
         
     def displayUnitOfMeasure(self):
         ''' displays the unit of measure of the selected income source '''
         unitofmeasure = self.cboAssetType.itemData( self.cboAssetType.currentIndex() ).toString()
         self.txtUnitOfMeasure.setText( unitofmeasure )
        
     def displayAssetDetails(self):
         ''' Retrieve and display Household Asset details '''
         query = '''SELECT assetid, assetcategory, assettype, unitofmeasure, unitcost, totalunits 
                       FROM assets WHERE hhid=%s AND pid=%s AND assetid=%s ''' % ( self.hhid, self.pid,  self.assetid )
         
         rows = self.executeResultsQuery(query)

         for row in rows:
             assetcategory = row[1]
             self.cboAssetCategory.setCurrentIndex( self.cboAssetCategory.findText( assetcategory ) )
             
             # force pulling of asset types in the selected category; for some strange reason it is not happening automatically
             self.getAssetTypes()
             
             # now show the assettype
             assettype = row[2]
             self.cboAssetType.setCurrentIndex( self.cboAssetType.findText( assettype ) )
        
             unitofmeasure = row[3]
             self.txtUnitOfMeasure.setText( unitofmeasure )
             costperunit = row[4]
             self.txtCostPerUnit.setText( str(costperunit) )
             numunits = row[5]
             self.txtNumberOfUnits.setText( str(numunits) )

     def saveAsset(self):
         ''' Saves asset to database '''    	

         # get the data entered by user
         category        = self.cboAssetCategory.currentText()
         assettype       = self.cboAssetType.currentText()
         unitofmeasure	= self.txtUnitOfMeasure.text()
         costperunit     = self.txtCostPerUnit.text()
         numunits        = self.txtNumberOfUnits.text()

         # create UPDATE query
         if (self.assetid == 0):
             query = '''INSERT INTO assets (hhid, assetcategory, assettype, unitofmeasure, unitcost, totalunits, pid )
                 VALUES(%s,'%s','%s','%s',%s,%s,%s) ''' % ( self.hhid, category,  assettype, unitofmeasure, costperunit, numunits, self.pid )
         else:
             query = ''' UPDATE assets SET assetcategory='%s', assettype='%s', unitofmeasure='%s', unitcost=%s, totalunits=%s
                     WHERE hhid=%s AND pid=%s 
                     AND assetid=%s ''' % ( category,  assettype, unitofmeasure, costperunit, numunits, self.hhid, self.pid,  self.assetid)

         self.executeUpdateQuery(query)

         # close new project window
         self.parent.retrieveHouseholdAssets()
         self.mdiClose()
