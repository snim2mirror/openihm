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
from model.globalcharacteristic import GlobalCharacteristic

class GlobalCharacteristicsManager:
     def existsGlobalCharacteristic(self, charname):
         char = self.getGlobalCharacteristic(charname)
         if char.name == "":
             return False
         else:
             return True
     
     def getGlobalCharacteristic(self,  charname=""):
        char = GlobalCharacteristic( charname )
        return char
        
     def addGlobalCharacteristic(self,  charname,  chartype,  datatype,  description  = "" ):
        char = GlobalCharacteristic( charname,  chartype,  datatype,  description )
        return char
        
     def delGlobalCharacteristic(self,  charname=""):  
         database = Database()      
         query = "DELETE FROM globalcharacteristics WHERE characteristic='%s' " % ( charname )
         database.open()
         database.execUpdateQuery( query )
         database.close()
    
     def getGlobalCharacteristics(self,  chartype="Any"):
         
         if (chartype != "Any"):
             strcondition = "WHERE chartype='%s' " % chartype
         else:
             strcondition = ""
         
         query = "SELECT characteristic FROM globalcharacteristics %s" % strcondition
         self.database.open()
         rows = self.database.execSelectQuery( query )
         self.database.close()
         chars = []
        
         for row in rows:
             charname = row[0]
             char = GlobalCharacteristic(charname)
             chars.append( char )
            
         return chars
