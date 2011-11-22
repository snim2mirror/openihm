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
from householdincome_crop import HouseholdCropIncome

class HouseholdCropIncomeManager:
     '''
         Manages household crop income - inherited by Household. Allows adding, editing, deleting and retrieval of household crop income.
     '''   
     def existsCropIncome(self, incomeid):
         cropincome = self.getCropIncome(incomeid)
         if cropincome.incomeid == "":
             return False
         else:
             return True
             
     def getCropIncome(self,  incomeid):
         cropincome = HouseholdCropIncome(incomeid, self.pid,  self.hhid)
         return cropincome
        
     def addCropIncome(self,  incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed ):             
         cropincome = HouseholdCropIncome(0, self.pid,  self.hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed )
         return cropincome
        
     def delCropIncome(self,  incomeid):
         query = "DELETE FROM cropincome WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delCropIncomes(self, incomeids):
         database = Database()
         database.open()
         
         for incomeid in incomeids:
             query = "DELETE FROM cropincome WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getCropIncomes(self):        
         query = "SELECT id FROM cropincome WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         cropincomes = []
        
         for row in rows:
             incomeid = row[0]
             cropincome = HouseholdCropIncome(incomeid, self.pid,  self.hhid)
             cropincomes.append( cropincome )
            
         return cropincomes
