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

from projectasset import ProjectAsset
import common

class GlobalAsset:
    def __init__(self, assetname, assettype):
        self.name = assetname
        self.type = assettype

class ProjectAssetsManager:
     def existsProjectAsset(self, assetname):
         asset = self.getProjectAsset(assetname)
         if asset.name == "":
             return False
         else:
             return True
             
     def getProjectAsset(self, assetname):
         ''' Retrieve an asset identified by assetname '''
         projectasset = ProjectAsset(self.pid, assetname)
         return projectasset
    
     def addProjectAsset(self, assetname, assettype):
         ''' Adds (saves) a new project asset to the database '''
         projectasset = ProjectAsset(self.pid, assetname, assettype)
         return projectasset
         
     def deleteProjectAsset(self,  assetname):
         ''' Remove an asset from project '''
         db = Database()
         db.open() 
         
         assetname = common.getDbString( assetname )
         query = "DELETE FROM projectassets WHERE pid=%s AND assetname='%s'" % (self.pid, assetname)
         db.execUpdateQuery( query )
             
         db.close()
         
     def getProjectAssets(self, assettype=""):
         ''' Retrieves all project assets from the database and returns an array of project asset objects '''
         
         # create filtering condition		 
         assettype = common.getDbString( assettype )
         condition = "AND assettype LIKE '%"+assettype+"%' " if assettype != "" and assettype != "All" else ""
             
         query = "SELECT assetname, assettype FROM projectassets WHERE pid=%s %s ORDER BY assettype, assetname" % (self.pid, condition)
         
         db = Database()
         db.open() 
         records = db.execSelectQuery( query )
         
         assets = []
         for rec in records:
            assetname = rec[0]
            projectasset = ProjectAsset(self.pid, assetname)
            assets.append( projectasset )
            
         db.close()
         return assets
         
     def getCropAssets(self, assets):
         ''' Retrieves crop assets '''
         query = '''SELECT foodtype FROM setup_crops'''

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         for rec in records:
             assetname = rec[0]
             asset = GlobalAsset(assetname, "Crops")
             assets.append( asset )
        
         db.close()
         return assets
         
     def getLivestockAssets(self, assets):
         ''' Retrieve livestock assets '''
         
         query = '''SELECT incomesource FROM setup_livestock'''

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         for rec in records:
             assetname = rec[0]
             asset = GlobalAsset(assetname, "Livestock")
             assets.append( asset )
        
         db.close()
         return assets
         
     def getLandAssets(self, assets):
         ''' Retrieves landed assets '''
         
         query = '''SELECT landtype FROM setup_landtypes'''

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         for rec in records:
             assetname = rec[0]
             asset = GlobalAsset(assetname, "Land")
             assets.append( asset )
        
         db.close()
         return assets
         
     def getTreeAssets(self, assets):
         ''' Retrieve trees '''
         
         query = '''SELECT treetype FROM setup_treetypes'''

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         for rec in records:
             assetname = rec[0]
             asset = GlobalAsset(assetname, "Trees")
             assets.append( asset )
        
         db.close()
         return assets

     def getTradableGoods(self, assets):
         ''' Retrieve tradable goods '''
         
         query = '''SELECT tradablegoodtype FROM setup_tradablegoods'''

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         for rec in records:
             assetname = rec[0]
             asset = GlobalAsset(assetname, "Tradable Goods")
             assets.append( asset )
        
         db.close()
         return assets
         
     def getAvailableAssets(self, assettype="All"):
         assets = []
         if assettype == "Crops" or assettype == "All":
             assets = self.getCropAssets(assets)
             
         if assettype == "Livestock" or assettype == "All":
             assets = self.getLivestockAssets(assets) 
          
         if assettype == "Land" or assettype == "All":
             assets = self.getLandAssets(assets)
         
         if assettype == "Trees" or assettype == "All":
             assets = self.getTreeAssets(assets)  
             
         if assettype == "Tradable Goods" or assettype == "All":
             assets = self.getTradableGoods(assets)  
             
         return assets
         
