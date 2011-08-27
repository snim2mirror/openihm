#-------------------------------------------------------------------	
#	Filename: personacharacteristics.py
#-------------------------------------------------------------------

from model.database import Database
from model.globalpersoncharacteristic import GlobalPersonCharacteristic

class GlobalPersonCharacteristicManager:
     ''' 
        Manages global Person Characteristics from which project person characteristics can be chosen.
        Allows adding, editing, deleting and retrieval of global person characteristic.
     '''   
     def getGlobalPersonCharacteristic(self,  charid="",  charname=""):
        char = GlobalPersonCharacteristic( charid, charname )
        return char
        
     def addGlobalPersonCharacteristics(self,  charname,  datatype ):
        char = GlobalPersonCharacteristic( 0 , charname,  datatype )
        return char
        
     def editGlobalPersonCharacteristic(self,  charid,  charname,  datatype):
        char = GlobalPersonCharacteristic(charid)
        char.setData( charname, datatype )
        
     def delGlobalPersonCharacteristic(self,  charid="",  charname=""):
        query = "DELETE FROM globalpersonalcharacteristics WHERE id=%i OR characteristic='%s' " % ( charid, charname )
        database = Database()
        database.open()
        database.execUpdateQuery( query )
        database.close()
        
     def getGlobalPersonCharacteristics(self):        
        query = "SELECT id FROM globalpersonalcharacteristics"
        database = Database()
        atabase.open()
        rows = database.execSelectQuery( query )
        database.close()
        chars = []
        
        for row in rows:
            charid = row[0]
            char = GlobalPersonCharacteristic(charid)
            chars.append( char )
            
        return chars
