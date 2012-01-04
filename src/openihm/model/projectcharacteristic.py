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

class ProjectCharacteristic:
     def __init__(self, pid,  characteristic, chartype="", datatype=""):
         if (chartype == "" and datatype=="" ):
             if ( not self.getCharacteristicDetails(pid,  characteristic) ):
                 self.name = ""
                 return None
         else:
             self.setData(pid,  characteristic, chartype, datatype)
            
     def getCharacteristicDetails(self, pid,  characteristic):
         database = Database()
         database.open()
         query = '''SELECT pid, characteristic, chartype, datatype
                       FROM projectcharacteristics WHERE pid=%s AND characteristic='%s' ''' % ( pid,  characteristic )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.name = characteristic
                 self.chartype = row[2]
                 self.datatype = row[3]
                 self.datatypestr = self.getStringDataType()
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid,  characteristic, chartype, datatype):
         database = Database()
         database.open()
        
         query = '''INSERT INTO projectcharacteristics (pid, characteristic, chartype, datatype )
                 VALUES(%s,'%s','%s',%s) ''' % ( pid,  characteristic, chartype, datatype )
       
         # execute query
         database.execUpdateQuery( query )
            
         database.close()
         # update characteristic attributes
         self.pid = pid
         self.name = characteristic
         self.chartype = chartype
         self.datatype = datatype
         self.datatypestr = self.getStringDataType()
         
        
     def editData(self, characteristic, chartype, datatype):
         database = Database()
         database.open()
        
         query = ''' UPDATE projectcharacteristics SET characteristic='%s', chartype='%s', datatype=%s
                     WHERE pid=%s AND characteristic='%s' ''' % ( characteristic, chartype, datatype,  self.pid,  self.name)
                     
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update characteristic attributes
         self.name = characteristic
         self.chartype = chartype
         self.datatype = datatype
         self.datatypestr = self.getStringDataType()
         
     def getStringDataType(self):
         print self.datatype
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
