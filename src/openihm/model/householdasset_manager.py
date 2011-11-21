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
from database import Database
from householdasset import HouseholdAsset

class HouseholdAssetManager:
     '''
         Manages household asset - inherited by Household. Allows adding, editing, deleting and retrieval of household assets.
     '''   
     def existsAsset(self, assetid):
         asset = self.getAsset(assetid)
         if asset.assetid == "":
             return False
         else:
             return True
             
     def getAsset(self,  assetid):
         asset = HouseholdAsset(assetid, self.pid,  self.hhid)
         return asset
        
     def addAsset(self,  category,  assettype, unitofmeasure, costperunit, numunits ):             
         asset = HouseholdAsset(0, self.pid,  self.hhid, category,  assettype, unitofmeasure, costperunit, numunits )
         return asset
        
     def delAsset(self,  assetid):
         query = "DELETE FROM assets WHERE pid=%s AND hhid=%s AND assetid=%s " % ( self.pid,  self.hhid,  assetid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delAssets(self, assetids):
         database = Database()
         database.open()
         
         for assetid in assetids:
             query = "DELETE FROM assets WHERE pid=%s AND hhid=%s AND assetid=%s " % ( self.pid,  self.hhid,  assetid )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getAssets(self):        
         query = "SELECT assetid FROM assets WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         assets = []
        
         for row in rows:
             assetid = row[0]
             asset = HouseholdAsset(assetid, self.pid,  self.hhid)
             assets.append( asset )
            
         return assets
