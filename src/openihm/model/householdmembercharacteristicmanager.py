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
from householdmembercharacteristic import HouseholdMemberCharacteristic

class UnsetCharacteristic:
    def __init__(self, pid, hhid, personid,  charname):
         self.pid = pid
         self.hhid = hhid
         self.personid = personid
         self.name = charname
         self.charvalue = "Not Set"

class HouseholdMemberCharacteristicManager:
     '''
         Manages personal characteristic- inherited by HouseholdMember. Allows adding, editing, deleting and retrieval of household characteristics.
     '''   
     def existsCharacteristic(self, charname):
         char = self.getCharacteristic(charname)
         if char.name == "":
             return False
         else:
             return True
             
     def getCharacteristic(self,  charname):
         char = HouseholdMemberCharacteristic(self.pid,  self.hhid, self.memberid,  charname)
         return char
        
     def addCharacteristic(self,  charname,  charvalue ):             
         char = HouseholdMemberCharacteristic(self.pid,  self.hhid, self.memberid,  charname,  charvalue )
         return char
        
     def delCharacteristic(self,  charname):
         query = '''DELETE FROM personalcharacteristics WHERE pid=%s 
                      AND hhid=%s AND personid='%s' AND characteristic='%s' ''' % ( self.pid,  self.hhid,  self.memberid,  charname )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delCharacteristics(self, chars):
         database = Database()
         database.open()
         
         for charname in chars:
             query = '''DELETE FROM personalcharacteristics WHERE pid=%s 
                          AND hhid=%s AND personid='%s' AND characteristic='%s' ''' % ( self.pid,  self.hhid,  self.memberid,  charname )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getCharacteristicsWithValues(self):        
         query = '''SELECT characteristic FROM personalcharacteristics WHERE pid=%s 
                      AND hhid=%s AND personid='%s' ''' % ( self.pid,  self.hhid,  self.memberid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         chars = []
        
         for row in rows:
             charname = row[0]
             char = HouseholdMemberCharacteristic(self.pid,  self.hhid, self.memberid,  charname)
             chars.append( char )
            
         return chars
         
     def getAllCharacteristics(self):
         query = "SELECT characteristic FROM projectcharacteristics WHERE pid=%s AND chartype='Personal' " % ( self.pid )
         print query
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         chars = []
        
         for row in rows:
             charname = row[0]
             if self.existsCharacteristic(charname):
                 char = HouseholdMemberCharacteristic(self.pid,  self.hhid, self.memberid,  charname)
             else:
                 char = UnsetCharacteristic(self.pid, self.hhid, self.memberid,  charname)
             
             chars.append( char )
            
         return chars
