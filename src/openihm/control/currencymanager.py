#!/usr/bin/env python
"""currency.py.

The Open-IHM currency manager.
'Currencies' are entries in a database, each consisting of:

ID
Name
Abbreviation
Currency symbol


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

class CurrencyError( Exception ) :
    """Our own exception handling"""
    pass


class CurrencyManager( object ):
    """Manages currencies.
    
    Allows adding, editing, deleting and retrieval of currencies.
    """   

    def __init__( self ) :
        self.database = Database()
        self.currencies = None
        self.currency_names = None
        self.getCurrencies()

    def existsCurrency(self, name):
        """Check if currency 'name' exists
        """
        currency = Currency(currencyname=name)
        if not currency.name :
            return False
        else:
            return True
            
    def getCurrencyByID(self, currencyid):
        """return currency currencyid from the database
        (returns by currency id)
        """
        currency = Currency(currencyid)
        if not currency.name :
            raise CurrencyError(
                "Can't get Currency id %r which does not exist" % currencyid )
        return currency
        
    def getCurrencyByName(self,  name):
        """return currency currencyname from the database
        (returns by currency name)
        """
        currency = Currency(currencyname=name)
        if not currency.name :
            raise CurrencyError(
                "Can't get Currency '%r' which does not exist" % name )
        return currency
       
    def addCurrency(self,  currencyname,  abbreviation,  symbol ):
        """Adds currency 'currencyname' to the currencies database.
        """
        currency = Currency( 0 , currencyname,  abbreviation,  symbol )
        self.getCurrencies()    # update currency list
        return currency
       
    def editCurrency(self,  currencyid,  currencyname,  abbreviation,  symbol ):
        """Edit currency 'currencyid' providing new name, abbreviation, symbol.
        """
        currency = Currency(currencyid)
        if not currency.name :
            raise CurrencyError(
                "Can't find Currency id %r which does not exist" % currencyid )
        currency.editData( currencyname,  abbreviation,  symbol )
        self.getCurrencies()    # update currency list
        return
       
    def delCurrency(self, currencyid):
        """Delete currency 'currencyid' from the database.
        """
        currency = Currency(currencyid)
        if not currency.name :
            raise CurrencyError(
                "Can't delete Currency id %r which does not exist" %currencyid )
        query = "DELETE FROM currencies WHERE id=%i " % ( currencyid )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
        self.getCurrencies()    # update currency list
        return
       
    def getCurrencies(self):        
        """Return a list of currencies stored in the database

        At same time set self.currencies to this list.
        """
        query = "SELECT id FROM currencies"
        self.database.open()
        rows = self.database.execSelectQuery( query )
        self.database.close()
        self.currencies = list()
       
        for row in rows:
            curr_id = row[0]
            currency = Currency(curr_id)
            self.currencies.append( currency )
           
        self.currency_names = [ x.name for x in self.currencies ]
        return self.currencies   

if __name__ == '__main__' :
    # our test code will go here
    CURRMAN = CurrencyManager()
    print CURRMAN.currency_names
