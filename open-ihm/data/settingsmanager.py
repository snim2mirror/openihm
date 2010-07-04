#-------------------------------------------------------------------	
#	Filename: settingsmanager.py
#-------------------------------------------------------------------

from database import Database
from globalhouseholdcharacteristic import GlobalHouseholdCharacteristic
from globalpersoncharacteristic import GlobalPersonCharacteristic

class SettingsManager:
    def __init__(self):
        self.database = Database()
        
    def getHouseholdCharacteristic(self,  charid=0, charname=""):
        char = GlobalHouseholdCharacteristic( charid, charname )
        return char
        
    def addHouseholdCharacteristic(self,  charname,  datatype ):
        char = GlobalHouseholdCharacteristic( 0 , charname,  datatype )
        return char
        
    def editHouseholdCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalHouseholdCharacteristic(charid)
        char.setData( charname, datatype )
        
    def delHouseholdCharacteristic(self,  charid="",  charname=""):        
        query = "DELETE FROM globalhouseholdcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
    
    def getHouseholdCharacteristics(self):
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
        
    def getPersonCharacteristic(self,  charid="",  charname=""):
        char = GlobalPersonCharacteristic( charid, charname )
        return char
        
    def addPersonCharacteristics(self,  charname,  datatype ):
        char = GlobalPersonCharacteristic( 0 , charname,  datatype )
        return char
        
    def editPersonCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalPersonCharacteristic(charid)
        char.setData( charname, datatype )
        
    def delPersonCharacteristic(self,  charid="",  charname=""):
        query = "DELETE FROM globalpersonalcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
        
    def getPersonCharacteristics(self):        
        query = "SELECT id FROM globalpersonalcharacteristics"
        self.database.open()
        rows = self.database.execSelectQuery( query )
        self.database.close()
        chars = []
        
        for row in rows:
            charid = row[0]
            char = GlobalPersonCharacteristic(charid)
            chars.append( char )
            
        return chars
