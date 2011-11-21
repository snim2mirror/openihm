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

from datetime import date
from database import Database

class HouseholdAsset:
     def __init__(self, assetid=0, pid="", hhid="",  category="", assettype="", unitofmeasure="", costperunit="", numunits=""):
         if (assetid != 0 ):
             if ( not self.getAssetDetails(pid, hhid, assetid) ):
                 self.pid = ""
                 self.hhid = ""
                 self.assetid = ""
                 return None
         else:
             self.setData(pid, hhid, category,  assettype, unitofmeasure, costperunit, numunits)
            
     def getAssetDetails(self, pid, hhid, assetid):
         database = Database()
         database.open()
         query = '''SELECT assetid, assetcategory, assettype, unitofmeasure, unitcost, totalunits 
                       FROM assets WHERE hhid=%s AND pid=%s AND assetid=%s ''' % ( hhid, pid,  assetid )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.hhid = hhid
                 self.assetid = assetid
                 self.category = row[1]
                 self.assettype = row[2]
                 self.unitofmeasure = row[3]
                 self.costperunit = row[4]
                 self.numunits = row[5]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, category,  assettype, unitofmeasure, costperunit, numunits):
         database = Database()
         database.open()
        
         query = '''INSERT INTO assets (hhid, assetcategory, assettype, unitofmeasure, unitcost, totalunits, pid )
                 VALUES(%s,'%s','%s','%s',%s,%s,%s) ''' % ( hhid, category,  assettype, unitofmeasure, costperunit, numunits, pid )
       
         # execute query
         database.execUpdateQuery( query )
         
         query = "SELECT LAST_INSERT_ID()"
         rows = database.execSelectQuery( query )
         for row in rows:
            assetid = row[0]
            
         database.close()
         # update asset attributes
         self.pid = pid
         self.hhid = hhid
         self.assetid = assetid
         self.category = category
         self.assettype = assettype
         self.unitofmeasure = unitofmeasure
         self.costperunit = costperunit
         self.numunits = numunits
        
     def editData(self, category,  assettype, unitofmeasure, costperunit, numunits):
         database = Database()
         database.open()
        
         query = ''' UPDATE assets SET assetcategory='%s', assettype='%s', unitofmeasure='%s', unitcost=%s, totalunits=%s
                     WHERE hhid=%s AND pid=%s 
                     AND assetid=%s ''' % ( category,  assettype, unitofmeasure, costperunit, numunits, self.hhid, self.pid,  self.assetid)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update asset attributes
         self.category = category
         self.assettype = assettype
         self.unitofmeasure = unitofmeasure
         self.costperunit = costperunit
         self.numunits = numunits
