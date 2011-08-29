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

class GlobalHouseholdCharacteristic:
    def __init__(self,  id=0,  charname="",  datatype="" ):
        self.database = Database()
        if ( ( id != 0 ) or ( datatype == "" ) ):
            if ( not self.getCharDetails(id, charname) ):
                return None
        else:
            self.addCharacteristic(charname, datatype)
            
    def getCharDetails(self,  id=0,  charname=""):
        self.database.open()
        if ( id != 0 ):
            query = "SELECT * FROM globalhouseholdcharacteristics WHERE id=%i " % (id)
        else:
            query = "SELECT * FROM globalhouseholdcharacteristics WHERE characteristic='%s' " % (charname)
        rows = self.database.execSelectQuery( query )
        self.database.close()
        num = len(rows)
        if (num != 0):
            exists = True
            for row in rows:
                self.id = row[0]
                self.charname = row[1]
                self.datatype = row[2]
        else:
            exists = False
        self.database.close()
        return exists
    
    def addCharacteristic(self, charname, datatype):
        # create INSERT INTO query
        query = '''INSERT INTO globalhouseholdcharacteristics(characteristic, datatype) 
                     VALUES('%s',%s)''' % (charname, datatype)
        
        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        
        # get the ID of the newly inserted project
        query = "SELECT LAST_INSERT_ID()"
        rows = self.database.execSelectQuery( query )
        for row in rows:
            id = row[0]
        
        self.database.close()
        
        # set attributes to saved values
        self.id = id
        self.charname = charname
        self.datatype = datatype
    
    def getID(self):
        return self.id
        
    def getName(self):
        return self.charname
        
    def getDataType(self ):
        return self.datatype
        
    def setData(self,  charname,  datatype):
        self.database.open()
        
        # create UPDATE query to update project
        query = '''UPDATE globalhouseholdcharacteristics SET characteristic='%s', datatype = %s
                     WHERE id=%i''' % (charname, datatype, self.id)
    
        # execute query
        self.database.execUpdateQuery( query )
        self.database.close()
        
        # set attributes to saved values
        self.charname = charname
        self.datatype = datatype

