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
from model.globalpersoncharacteristic import GlobalPersonCharacteristic

class GlobalPersonCharacteristicsManager:
     ''' 
        Manages global Person Characteristics from which project person characteristics can be chosen.
        Allows adding, editing, deleting and retrieval of global person characteristic.
     '''   
     def getGlobalPersonCharacteristic(self,  charid="",  charname=""):
        char = GlobalPersonCharacteristic( charid, charname )
        return char
        
     def addGlobalPersonCharacteristics(self,  charname,  datatype ):
        char = GlobalPersonCharacteristic( 0 , charname,  datatype )
        return char
        
     def editGlobalPersonCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalPersonCharacteristic(charid)
        char.setData( charname, datatype )
        
     def delGlobalPersonCharacteristic(self,  charid="",  charname=""):
        query = "DELETE FROM globalpersonalcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        database = Database()
        database.open()
        database.execUpdateQuery( query )
        database.close()
        
     def getGlobalPersonCharacteristics(self):        
        query = "SELECT id FROM globalpersonalcharacteristics"
        database = Database()
        database.open()
        rows = database.execSelectQuery( query )
        database.close()
        chars = []
        
        for row in rows:
            charid = row[0]
            char = GlobalPersonCharacteristic(charid)
            chars.append( char )
            
        return chars
