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
import common

class ProjectAsset: 
     def __init__(self, pid, assetname, assettype=None):
         ''' constructor: retrieves or creates a new project asset object '''
         # if only assetname is specifed retrieve asset details        
         if ( assettype == None ):
            if ( not self.getAssetDetails( pid, assetname ) ):
                self.name = ""
                return None
         # else save asset details
         else:
            self.createAsset( pid,assetname, assettype )
            
     def getAssetDetails(self,  pid, assetname):
         ''' Retrieves an asset matching assetname '''
         # connect to database
         db = Database()
         db.open()
         # query to retrieve asset details
         assetname = common.getDbString( assetname )
         query = "SELECT pid, assetname, assettype FROM projectassets WHERE pid=%s AND assetname='%s' " % (pid, assetname)
             
         # get rows returned by query
         rows = db.execSelectQuery( query )
         
         # get asset details from record and assign to object attrbutes
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                self.pid = pid
                self.name = common.getViewString( row[1] )
                self.type = common.getViewString( row[2] )
         else:
            exists = False
        
         # close database connection
         db.close()
         return exists
        
     def createAsset( self,  pid, assetname,  assettype ):
         ''' Adds a new incomesource object '''
         # connect to database
         db = Database()           
         db.open()
         
         # create INSERT INTO query
         assetname = common.getDbString( assetname )
         assettype = common.getDbString( assettype )
         query = '''INSERT INTO projectassets(pid,assetname,assettype) VALUES(%s,'%s','%s')''' % (pid,assetname,assettype)
        
         # execute query
         db.execUpdateQuery(query)
         
         # close database connection
         db.close()
        
         # set asset attributes to saved values
         self.name = common.getViewString( assetname )
         self.type = common.getViewString( assettype )
         self.pid = pid
         
     def editData( self,  assetname,  assettype ):
         ''' edits the assetname and assettype of the asset object '''
         # connect to database
         db = Database()           
         db.open()
         
         # create INSERT INTO query
         assetname = common.getDbString( assetname )
         oldname = common.getDbString( self.name )
         assettype = common.getDbString( assettype )
         query = '''UPDATE projectassets SET assetname='%s', assettype='%s',
         WHERE pid=%s AND assetname='%s' ''' % (assetname, assettype, self.pid, oldname)
        
         # execute query
         db.execUpdateQuery(query)
         
         # close database connection
         db.close()
        
         # set asset attributes to saved values
         self.name = common.getViewString( assetname )
         self.type = common.getViewString( assettype )

