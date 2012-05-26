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

from model.database import Database
from model.currency import Currency

class CurrencyManager:
    '''Manages currencies.
    
    Allows adding, editing, deleting and retrieval of currencies.
    '''   
    def existsCurrency(self, name):
        currency = self.getCurrencyByName(name)
        if currency.name == "":
            return False
        else:
            return True
            
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
       
    def delCurrency(self, currencyid):
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
            curr_id = row[0]
            currency = Currency(curr_id)
            currencies.append( currency )
           
        return currencies   
