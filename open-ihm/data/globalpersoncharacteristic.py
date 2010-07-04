#-------------------------------------------------------------------	
#	Filename: globalpersoncharacteristic.py
#-------------------------------------------------------------------

from database import Database

class GlobalPersonCharacteristic:
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
            query = "SELECT * FROM globalpersonalcharacteristics WHERE id=%i " % (id)
        else:
            query = "SELECT * FROM globalpersonalcharacteristics WHERE characteristic='%s' " % (charname)
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
        query = '''INSERT INTO globalpersonalcharacteristics(characteristic, datatype) 
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
        query = '''UPDATE globalpersonalcharacteristics SET characteristic='%s', datatype = %s
                     WHERE id=%i''' % (charname, datatype, self.id)
    
        # execute query
        self.database.execUpdateQuery( query )
        self.database.close()
        
        # set attributes to saved values
        self.charname = charname
        self.datatype = datatype
        
