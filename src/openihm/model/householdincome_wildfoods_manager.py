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
from householdincome_wildfoods import HouseholdWildfoodsIncome

class HouseholdWildfoodsIncomeManager:
     '''
         Manages household wildfoods income - inherited by Household. Allows adding, editing, deleting and retrieval of household wildfoods income.
     '''   
     def existsLivestockIncome(self, incomeid):
         wsincome = self.getWildfoodsIncome(incomeid)
         if wsincome.incomeid == "":
             return False
         else:
             return True
             
     def getWildfoodsIncome(self,  incomeid):
         wsincome = HouseholdWildfoodsIncome(incomeid, self.pid,  self.hhid)
         return wsincome
        
     def addWildfoodsIncome(self,  incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed ):             
         wsincome = HouseholdWildfoodsIncome(0, self.pid,  self.hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed )
         return wsincome
        
     def delWildfoodsIncome(self,  incomeid):
         query = "DELETE FROM wildfoods WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delWildfoodsIncomes(self, incomeids):
         database = Database()
         database.open()
         
         for incomeid in incomeids:
             query = "DELETE FROM wildfoods WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getWildfoodsIncomes(self):        
         query = "SELECT id FROM wildfoods WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         wsincomes = []
        
         for row in rows:
             incomeid = row[0]
             wsincome = HouseholdWildfoodsIncome(incomeid, self.pid,  self.hhid)
             wsincomes.append( wsincome )
            
         return wsincomes
