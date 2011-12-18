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
from householdincome_employment import HouseholdEmploymentIncome

class HouseholdEmploymentIncomeManager:
     '''
         Manages household employment income - inherited by Household. Allows adding, editing, deleting and retrieval of household employment income.
     '''   
     def existsEmploymentIncome(self, incomeid):
         empincome = self.getEmploymentIncome(incomeid)
         if empincome.incomeid == "":
             return False
         else:
             return True
             
     def getEmploymentIncome(self,  incomeid):
         empincome = HouseholdEmploymentIncome(incomeid, self.pid,  self.hhid)
         return empincome
        
     def addEmploymentIncome(self,  incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome ):             
         empincome = HouseholdEmploymentIncome(0, self.pid,  self.hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome )
         return empincome
        
     def delEmploymentIncome(self,  incomeid):
         query = "DELETE FROM employmentincome WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def delEmploymentIncomes(self, incomeids):
         database = Database()
         database.open()
         
         for incomeid in incomeids:
             query = "DELETE FROM employmentincome WHERE pid=%s AND hhid=%s AND id=%s " % ( self.pid,  self.hhid,  incomeid )
             database.execUpdateQuery( query )
             
         database.close()
        
     def getEmploymentIncomes(self):        
         query = "SELECT id FROM employmentincome WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         empincomes = []
        
         for row in rows:
             incomeid = row[0]
             empincome = HouseholdEmploymentIncome(incomeid, self.pid,  self.hhid)
             empincomes.append( empincome )
            
         return empincomes
