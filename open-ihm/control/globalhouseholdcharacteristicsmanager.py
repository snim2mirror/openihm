#---------------------------------------------------------------------------------------------------------------------------------------	
#	filename: householdcharacteristicsmanager.py
#
#  Manages global household characteristics
#---------------------------------------------------------------------------------------------------------------------------------------

from model.database import Database
from model.globalhouseholdcharacteristic import GlobalHouseholdCharacteristic

class GlobalHouseholdCharacteristicsManager:
     def __init__(self):
        self.database = Database()
     
     def getGlobalHouseholdCharacteristic(self,  charid=0, charname=""):
        char = GlobalHouseholdCharacteristic( charid, charname )
        return char
        
     def addGlobalHouseholdCharacteristic(self,  charname,  datatype ):
        char = GlobalHouseholdCharacteristic( 0 , charname,  datatype )
        return char
        
     def editGlobalHouseholdCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalHouseholdCharacteristic(charid)
        char.setData( charname, datatype )
        
     def delGlobalHouseholdCharacteristic(self,  charid="",  charname=""):        
        query = "DELETE FROM globalhouseholdcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
    
     def getGlobalHouseholdCharacteristics(self):
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
