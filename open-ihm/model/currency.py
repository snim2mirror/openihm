#-------------------------------------------------------------------	
#	Filename: currency.py
#-------------------------------------------------------------------

from database import Database

class Currency:
     def __init__(self,  id=0,  currencyname="",  abbreviation="",  symbol="" ):
        self.database = Database()
        if ( ( ( id != 0 ) or ( currencyname != "" ) )  and ( ( abbreviation == "" ) or ( symbol == "" ) ) ):
            if ( not self.getCurrencyDetails( id ,  currencyname ) ):
                return None
        else:
            self.setData(currencyname,  abbreviation,  symbol )
            
     def getCurrencyDetails(self,  id = 0,  currencyname="" ):
         self.database.open()
         if ( id != 0 ):
             query = "SELECT * FROM currencies WHERE id=%s " % (id)
         else:
             query = "SELECT * FROM currencies WHERE currencyname='%s' " % (currencyname)
         rows = self.database.execSelectQuery( query )
         self.database.close()
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.id = row[0]
                 self.name = row[1]
                 self.abbreviation = row[2]
                 self.symbol = row[3]
         else:
             exists = False
         self.database.close()
         return exists
    
     def getID(self):
         return self.id
        
     def getName(self):
         return self.name
        
     def getAbbreviation(self ):
         return self.abbreviation
        
     def getSymbol(self ):
         return self.symbol
        
     def setData(self,  currencyname,  abbreviation,  symbol):
         self.database.open()
        
         query = '''INSERT INTO currencies (currencyname,abbreviation,symbol )
                         VALUES('%s','%s','%s') ''' % ( currencyname, abbreviation, symbol )
         
         # execute query
         self.database.execUpdateQuery( query )
         
         query = "SELECT LAST_INSERT_ID()"
         rows = self.database.execSelectQuery( query )
         for row in rows:
             id = row[0]
                 
         self.database.close()
        
         # set attributes to saved values
         self.id = id
         self.name = currencyname
         self.abbreviation = abbreviation
         self.symbol = symbol
         
     def editData(self,  currencyname,  abbreviation,  symbol):
         self.database.open()
        
         query = ''' UPDATE currencies SET currencyname='%s', abbreviation='%s', symbol='%s'
                         WHERE id=%s ''' % ( currencyname, abbreviation, symbol, self.id)
    
         # execute query
         self.database.execUpdateQuery( query )
         self.database.close()
        
         # set attributes to saved values
         self.id = id
         self.name = currencyname
         self.abbreviation = abbreviation
         self.symbol = symbol
