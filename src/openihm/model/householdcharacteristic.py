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

class HouseholdCharacteristic:
     def __init__(self, pid="", hhid="",  charname="", charvalue=""):
         if (charvalue == "" ):
             if ( not self.getCharDetails(pid, hhid, charname) ):
                 self.pid = ""
                 self.hhid = ""
                 self.name = ""
                 return None
         else:
             self.setData(pid, hhid, charname, charvalue)
            
     def getCharDetails(self, pid, hhid, charname):
         database = Database()
         database.open()
         query = '''SELECT characteristic, charvalue 
                       FROM householdcharacteristics WHERE hhid=%s AND pid=%s 
                       AND characteristic='%s' ''' % ( hhid, pid,  charname )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.hhid = hhid
                 self.name = charname
                 self.charvalue = row[1]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, charname,  charvalue):
         database = Database()
         database.open()
        
         query = '''INSERT INTO householdcharacteristics (pid,hhid, characteristic, charvalue )
                 VALUES(%s,%s,'%s','%s') ''' % ( pid, hhid, charname,  charvalue )
       
         # execute query
         database.execUpdateQuery( query )
            
         database.close()
         # update attributes
         self.pid = pid
         self.hhid = hhid
         self.name = charname
         self.charvalue = charvalue
        
     def editData(self, charname, charvalue):
         database = Database()
         database.open()
        
         query = ''' UPDATE householdcharacteristics SET characteristic='%s', charvalue='%s'
                     WHERE hhid=%s AND pid=%s 
                     AND characteristic='%s' ''' % ( charname,  charvalue, self.hhid, self.pid,  self.name)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update asset attributes
         self.name = charname
         self.charvalue = charvalue
