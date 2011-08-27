#----------------------------------------------------------------------------------------------------------------------------------------------
# currencymanager.py
#----------------------------------------------------------------------------------------------------------------------------------------------

from model.database import Database
from model.currency import Currency

class SettingsManager:
     '''
         Manages currencies. Allows adding, editing, deleting and retrieval of currencies.
     '''   
     def getCurrencyByID(self,  currencyid):
         currency = Currency(currencyid)
         return currency
         
     def getCurrencyByName(self,  name):
         currency = Currency(currencyname=name)
         return currency
        
     def addCurrency(self,  currencyname,  abbreviation,  symbol ):
         currency = Currency( 0 , currencyname,  abbreviation,  symbol )
         return currency
        
     def editCurrency(self,  currencyid,  currencyname,  abbreviation,  symbol ):
         currency = Currency(currencyid)
         currency.editData( currencyname,  abbreviation,  symbol )
        
     def delCurrency(self,  currencyid):
         query = "DELETE FROM currencies WHERE id=%i " % ( currencyid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
        
     def getCurrencies(self):        
         query = "SELECT id FROM currencies"
         self.database.open()
         rows = self.database.execSelectQuery( query )
         self.database.close()
         currencies = []
        
         for row in rows:
             id = row[0]
             currency = Currency(id)
             currencies.append( currency )
            
         return currencies   
