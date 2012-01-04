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
from projectcharacteristic import ProjectCharacteristic

class ProjectCharacteristicsManager:
     def existsProjectCharacteristic(self, charname):
         char = self.getCharacteristic(charname)
         if char.name == "":
             return False
         else:
             return True
     
     def getProjectCharacteristic(self,  charname=""):
        char = ProjectCharacteristic( self.pid,  charname )
        return char
        
     def addProjectCharacteristic(self,  charname,  chartype,  datatype ):
        char = ProjectCharacteristic( self.pid,  charname,  chartype,  datatype )
        return char
        
     def delProjectCharacteristic(self,  charname=""):  
         database = Database()      
         query = "DELETE FROM projectcharacteristics WHERE pid=%s AND characteristic='%s' " % ( self.pid,  charname )
         database.open()
         database.execUpdateQuery( query )
         database.close()
    
     def getProjectCharacteristics(self,  chartype="Any"):
         
         if (chartype != "Any"):
             strcondition = "WHERE pid=%s AND chartype='%s' " % (self.pid,  chartype)
         else:
             strcondition = "WHERE pid=%s" % (self.pid)
         
         query = "SELECT characteristic FROM projectcharacteristics %s" % strcondition
         
         database = Database()
         database.open()
         rows = database.execSelectQuery( query )
         database.close()
         chars = []
        
         for row in rows:
             charname = row[0]
             char = ProjectCharacteristic(self.pid,  charname)
             chars.append( char )
            
         return chars
