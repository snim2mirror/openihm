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
from householdincome_transfers import HouseholdTransfersIncome

class HouseholdTransfersIncomeManager:
     '''
         Manages household transfers income - inherited by Household. Allows adding, editing, deleting and retrieval of household transfers income.
     '''   
     def existsTransferIncome(self, incomeid):
         transincome = self.getTransfersIncome(incomeid)
         if transincome.incomeid == "":
             return False
         else:
             return True
             
     def getTransferIncome(self,  incomeid):
         transincome = HouseholdTransfersIncome(incomeid, self.pid,  self.hhid)
         return transincome
        
     def addTransferIncome(self, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit ):             
         transincome = HouseholdTransfersIncome(0, self.pid,  self.hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit )
         return transincome
        
     def delTransferIncome(self,  incomeid):
         query = "DELETE FROM transfers WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delTransferIncomes(self, incomeids):
         database = Database()
         database.open()
         
         for incomeid in incomeids:
             query = "DELETE FROM transfers WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getTransferIncomes(self):        
         query = "SELECT id FROM transfers WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         transincomes = []
        
         for row in rows:
             incomeid = row[0]
             transincome = HouseholdTransfersIncome(incomeid, self.pid,  self.hhid)
             transincomes.append( transincome )
            
         return transincomes
