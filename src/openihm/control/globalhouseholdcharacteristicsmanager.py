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


from model.database import Database
from model.globalhouseholdcharacteristic import GlobalHouseholdCharacteristic

class GlobalHouseholdCharacteristicsManager:
     def __init__(self):
        self.database = Database()
     
     def getGlobalHouseholdCharacteristic(self,  charid=0, charname=""):
        char = GlobalHouseholdCharacteristic( charid, charname )
        return char
        
     def addGlobalHouseholdCharacteristic(self,  charname,  datatype ):
        char = GlobalHouseholdCharacteristic( 0 , charname,  datatype )
        return char
        
     def editGlobalHouseholdCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalHouseholdCharacteristic(charid)
        char.setData( charname, datatype )
        
     def delGlobalHouseholdCharacteristic(self,  charid="",  charname=""):        
        query = "DELETE FROM globalhouseholdcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
    
     def getGlobalHouseholdCharacteristics(self):
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
