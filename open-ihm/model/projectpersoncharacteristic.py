#-------------------------------------------------------------------	
#	Filename: projectpersoncharacteristic.py
#-------------------------------------------------------------------

from database import Database
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ProjectPersonCharacteristic:
    def __init__(self,  pid,  charname,  datatype="" ):
        self.pid = pid
        self.charname = charname
        self.database = Database()
        #if characteristic is new add it to database
        if ( datatype != "" ):
            self.addCharacteristic( charname,  datatype )
            
    def addCharacteristic(self,  charname, datatype):
        # get the target table
        tbl = '''p%iPersonalCharacteristics''' % (self.pid)
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
        
