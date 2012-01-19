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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from control.controller import Controller

from mixins import TableViewMixin

class ProjectAssetsManager(TableViewMixin):
     def getProjectAssets(self):
         chars = []
         row = 0
         while (self.tblSelectedAssets.model().item(row,0)):
             val = self.tblSelectedAssets.model().item(row,0).text()
             chars.append(val)
             row = row + 1
            
         return chars
        
     def displayAvailableAssets(self):
         ''' Retrieve and display available assets ''' 
         assettype = self.cboAssetType.currentText()
         assets = self.project.getAvailableAssets(assettype)
        
         model = QStandardItemModel(1,2)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Asset Name'))
         model.setHorizontalHeaderItem(1,QStandardItem('Asset Type'))
        
         # add  data rows
         num = 0
        
         for asset in assets:
             qtAsset = QStandardItem( asset.name )
             qtAssetType = QStandardItem( asset.type )		
             model.setItem( num, 0, qtAsset )
             model.setItem( num, 1, qtAssetType )
             num = num + 1
        
         self.tblAvailableAssets.setModel(model)
         self.tblAvailableAssets.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblAvailableAssets.resizeColumnsToContents()
        
     def displaySelectedAssets(self):
         ''' Retrieve and display Project Assets '''
         assettype = self.cboAssetType.currentText()
         assets = self.project.getProjectAssets(assettype)
        
         model = QStandardItemModel(1,2)
        
         # set model headers
         model.setHorizontalHeaderItem(0,QStandardItem('Asset Name'))
         model.setHorizontalHeaderItem(1,QStandardItem('Asset Type'))
        
         # add  data rows
         num = 0
        
         for asset in assets:
             qtAsset = QStandardItem( asset.name )
             qtAssetType = QStandardItem( asset.type )		
             model.setItem( num, 0, qtAsset )
             model.setItem( num, 1, qtAssetType )
             num = num + 1
        
         self.tblSelectedAssets.setModel(model)
         self.tblSelectedAssets.setSelectionMode(QAbstractItemView.ExtendedSelection)
         self.tblSelectedAssets.resizeColumnsToContents()
        
     def moveAllAssets(self):
         ''' Add all available assets to Project '''
         row = 0
         assettype = self.cboAssetType.currentText()
         assets = self.project.getAvailableAssets(assettype)
         for asset in assets:
             if self.project.existsProjectAsset(asset.name):
                 msg = "The asset labelled, %s, has already been added to project" % (asset.name)
                 QMessageBox.information(self,"Project Configuration",msg)
             else:
                 self.project.addProjectAsset(asset.name, asset.type)
         self.displaySelectedAssets()   
        
     def removeAllAssets(self):
         ''' remove all listed assets from Project'''
         msg = "Are you sure you want to remove all these assets from this project?"
         ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
         # if deletion is rejected return without deleting
         if ret == QMessageBox.No:
             return
            
         assettype = self.cboAssetType.currentText()
         assets = self.project.getAvailableAssets(assettype)
         for asset in assets:
             self.project.deleteProjectAsset(asset.name)
             
         self.displaySelectedAssets() 
        
     def moveSelectedAssets(self):
        ''' Add selected available assets to Project'''
        numSelected = self.countRowsSelected(self.tblAvailableAssets)
        if  numSelected != 0:
             selectedRows = self.getSelectedRows(self.tblAvailableAssets)
             for row in selectedRows:
                 assetname = self.tblAvailableAssets.model().item(row,0).text()
                 assettype = self.tblAvailableAssets.model().item(row,1).text()
                 
                 if not self.project.existsProjectAsset(assetname):
                     self.project.addProjectAsset(assetname, assettype)
                 else:
                     msg = "The asset labelled, %s, has already been added to project" % (assetname)
                     QMessageBox.information(self,"Project Configuration",msg)
                     
             self.displaySelectedAssets()
        else:
            msg = "Please select the assets you want to add."
            QMessageBox.information(self,"Project Configuration",msg) 
        
     def removeSelectedAssets(self):
         ''' remove selected assets from Project'''
         numSelected = self.countRowsSelected(self.tblSelectedAssets)
         
         if  numSelected != 0:
             msg = "Are you sure you want to remove the selected assets from this project?"
             ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
             
             # if deletion is rejected return without deleting
             if ret == QMessageBox.No:
                 return
                 
             selectedRows = self.getSelectedRows(self.tblSelectedAssets)
             
             for row in selectedRows:
                 assetname = self.tblSelectedAssets.model().item(row,0).text()
                 self.project.deleteProjectAsset( assetname )
                 
             self.displaySelectedAssets()
             
         else:
             msg = "Please select the assets you want to remove."
             QMessageBox.information(self,"Project Configuration",msg) 
             
     def refreshAssetLists(self):
         self.displayAvailableAssets()
         self.displaySelectedAssets()
