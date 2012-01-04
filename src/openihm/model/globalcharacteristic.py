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

class GlobalCharacteristic:
     def __init__(self, characteristic, chartype="", datatype="", description=""):
         if (chartype == "" and datatype=="" and description=="" ):
             if ( not self.getCharacteristicDetails(characteristic) ):
                 self.name = ""
                 return None
         else:
             self.setData(characteristic, chartype, datatype, description)
            
     def getCharacteristicDetails(self, characteristic):
         database = Database()
         database.open()
         query = '''SELECT characteristic, chartype, datatype, description
                       FROM globalcharacteristics WHERE characteristic='%s' ''' % ( characteristic )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.name = characteristic
                 self.chartype = row[1]
                 self.datatype = row[2]
                 self.datatypestr = self.getStringDataType()
                 self.description = row[3]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, characteristic, chartype, datatype, description):
         database = Database()
         database.open()
        
         query = '''INSERT INTO globalcharacteristics (characteristic, chartype, datatype, description )
                 VALUES('%s','%s',%s,'%s') ''' % ( characteristic, chartype, datatype, description )
       
         # execute query
         database.execUpdateQuery( query )
            
         database.close()
         # update characteristic attributes
         self.name = characteristic
         self.chartype = chartype
         self.datatype = datatype
         self.datatypestr = self.getStringDataType()
         self.description = description
         
        
     def editData(self, characteristic, chartype, datatype, description):
         database = Database()
         database.open()
        
         query = ''' UPDATE globalcharacteristics SET characteristic='%s', chartype='%s', datatype=%s, description='%s'
                     WHERE characteristic='%s' ''' % ( characteristic, chartype, datatype, description,  self.name)
                     
         
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update characteristic attributes
         self.name = characteristic
         self.chartype = chartype
         self.datatype = datatype
         self.datatypestr = self.getStringDataType()
         self.description = description
         
     def getStringDataType(self):
         if self.datatype == 1:
             return "Boolean/Yes/No"
         elif self.datatype == 2:
             return "Integer"
         elif self.datatype == 3:
             return "String"
         elif self.datatype == 4:
             return "Double"
         else:
             return "Unknown"
