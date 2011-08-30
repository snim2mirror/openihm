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

class ProjectHouseholdCharacteristic:
    def __init__(self,  pid,  charname,  datatype="" ):
        self.pid = pid
        self.charname = charname
        self.database = Database()
        #if characteristic is new add it to database
        if ( datatype != "" ):
            self.addCharacteristic( charname,  datatype )
            
    def addCharacteristic(self,  charname, datatype):
        # get the target table
        tbl = '''p%iHouseholdCharacteristics''' % (self.pid)
        # determine the data type
        if datatype == "1":
            vartype = "ENUM('Yes','No')"
        elif datatype == "2":
            vartype = "BIGINT"
        elif datatype == "3":
            vartype = "VARCHAR(250)"
        elif datatype == "4":
            vartype = "DOUBLE"
            
        # check if characteristic already exists
        query = '''SHOW COLUMNS FROM %s ''' % (tbl)
        
        self.database.open()
        rows = self.database.execSelectQuery(query)
        
        exists = False
        for row in rows:
            if ( row[0]  == charname ):
                exists = True
        
        # add or (if characteristic exists) modify characteristic 
        if ( exists ):
            queryAlter = '''ALTER TABLE `%s` CHANGE COLUMN `%s` %s ''' % (tbl, charname, vartype)
        else:
            queryAlter = '''ALTER TABLE `%s` ADD COLUMN `%s` %s ''' % (tbl, charname, vartype)
            
        self.database.execDefinitionQuery( queryAlter )
        self.database.close()
        
    def getName(self):
        return self.charname
        
