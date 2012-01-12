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
from householdcharacteristic import HouseholdCharacteristic

class UnsetCharacteristic:
    def __init__(self, pid, hhid, charname):
         self.pid = pid
         self.hhid = hhid
         self.name = charname
         self.charvalue = "Not Set"

class HouseholdCharacteristicManager:
     '''
         Manages household characteristic- inherited by Household. Allows adding, editing, deleting and retrieval of household characteristics.
     '''   
     def existsCharacteristic(self, charname):
         char = self.getCharacteristic(charname)
         if char.name == "":
             return False
         else:
             return True
             
     def getCharacteristic(self,  charname):
         char = HouseholdCharacteristic(self.pid,  self.hhid, charname)
         return char
        
     def addCharacteristic(self,  charname,  charvalue ):             
         char = HouseholdCharacteristic(self.pid,  self.hhid, charname,  charvalue )
         return char
        
     def delCharacteristic(self,  charname):
         query = '''DELETE FROM householdcharacteristics WHERE pid=%s 
                      AND hhid=%s AND characteristic='%s' ''' % ( self.pid,  self.hhid,  charname )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delCharacteristics(self, chars):
         database = Database()
         database.open()
         
         for charname in chars:
             query = '''DELETE FROM householdcharacteristics WHERE pid=%s 
                           AND hhid=%s AND characteristic='%s' ''' % ( self.pid,  self.hhid,  charname )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getCharacteristicsWithValues(self):        
         query = "SELECT characteristic FROM householdcharacteristics WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         chars = []
        
         for row in rows:
             charname = row[0]
             char = HouseholdCharacteristic(self.pid,  self.hhid, charname)
             chars.append( char )
            
         return chars
         
     def getAllCharacteristics(self):
         query = "SELECT characteristic FROM projectcharacteristics WHERE pid=%s AND chartype='Household'" % ( self.pid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         chars = []
        
         for row in rows:
             charname = row[0]
             if self.existsCharacteristic(charname):
                 char = HouseholdCharacteristic(self.pid,  self.hhid, charname)
             else:
                 char = UnsetCharacteristic(self.pid, self.hhid, charname)
             
             chars.append( char )
            
         return chars
