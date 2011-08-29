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
from globalhouseholdcharacteristic import GlobalHouseholdCharacteristic
from globalpersoncharacteristic import GlobalPersonCharacteristic
from currency import Currency

class SettingsManager:
     def __init__(self):
        self.database = Database()
     
     #----------------------------------------------------------------------------------------------------------
     # household characteristics
     #----------------------------------------------------------------------------------------------------------   
     def getHouseholdCharacteristic(self,  charid=0, charname=""):
        char = GlobalHouseholdCharacteristic( charid, charname )
        return char
        
     def addHouseholdCharacteristic(self,  charname,  datatype ):
        char = GlobalHouseholdCharacteristic( 0 , charname,  datatype )
        return char
        
     def editHouseholdCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalHouseholdCharacteristic(charid)
        char.setData( charname, datatype )
        
     def delHouseholdCharacteristic(self,  charid="",  charname=""):        
        query = "DELETE FROM globalhouseholdcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
    
     def getHouseholdCharacteristics(self):
        query = "SELECT id FROM globalhouseholdcharacteristics"
        self.database.open()
        rows = self.database.execSelectQuery( query )
        self.database.close()
        chars = []
        
        for row in rows:
            charid = row[0]
            char = GlobalHouseholdCharacteristic(charid)
            chars.append( char )
            
        return chars
      
     #----------------------------------------------------------------------------------------------------------
     # personal characteristics
     #----------------------------------------------------------------------------------------------------------     
     def getPersonCharacteristic(self,  charid="",  charname=""):
        char = GlobalPersonCharacteristic( charid, charname )
        return char
        
     def addPersonCharacteristics(self,  charname,  datatype ):
        char = GlobalPersonCharacteristic( 0 , charname,  datatype )
        return char
        
     def editPersonCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalPersonCharacteristic(charid)
        char.setData( charname, datatype )
        
     def delPersonCharacteristic(self,  charid="",  charname=""):
        query = "DELETE FROM globalpersonalcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
        
     def getPersonCharacteristics(self):        
        query = "SELECT id FROM globalpersonalcharacteristics"
        self.database.open()
        rows = self.database.execSelectQuery( query )
        self.database.close()
        chars = []
        
        for row in rows:
            charid = row[0]
            char = GlobalPersonCharacteristic(charid)
            chars.append( char )
            
        return chars
        
     #----------------------------------------------------------------------------------------------------------
     # currencies
     #----------------------------------------------------------------------------------------------------------
     def getCurrencies(self):        
         query = "SELECT id FROM currencies"
         self.database.open()
         rows = self.database.execSelectQuery( query )
         self.database.close()
         currencies = []
        
         for row in rows:
             id = row[0]
             currency = Currency(id)
             currencies.append( currency )
            
         return currencies   
