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

from datetime import date
from database import Database

class HouseholdEmploymentIncome:
     def __init__(self, incomeid=0, pid="", hhid="",  incomesource="", foodtypepaid="", unitofmeasure="", unitspaid=0, incomekcal=0, cashincome=0):
         if (incomeid != 0 ):
             if ( not self.getIncomeDetails(pid, hhid, incomeid) ):
                 self.pid = ""
                 self.hhid = ""
                 self.incomeid = ""
                 return None
         else:
             self.setData(pid, hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome)
            
     def getIncomeDetails(self, pid, hhid, incomeid):
         database = Database()
         database.open()
         query = '''SELECT id, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome
                       FROM employmentincome WHERE hhid=%s AND pid=%s AND id=%s ''' % ( hhid, pid,  incomeid )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.hhid = hhid
                 self.incomeid = incomeid
                 self.incomesource = row[1]
                 self.foodtypepaid = row[2]
                 self.unitofmeasure = row[3]
                 self.unitspaid = row[4]
                 self.incomekcal = row[5]
                 self.cashincome = row[6]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome):
         database = Database()
         database.open()
        
         query = '''INSERT INTO employmentincome(pid, hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome)
                 VALUES(%s,%s,'%s','%s','%s',%s,%s,%s) ''' % ( pid, hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome )
       
         # execute query
         database.execUpdateQuery( query )
         
         query = "SELECT LAST_INSERT_ID()"
         rows = database.execSelectQuery( query )
         for row in rows:
            incomeid = row[0]
            
         database.close()
         # update income attributes
         self.pid = pid
         self.hhid = hhid
         self.incomeid = incomeid
         self.incomesource = incomesource
         self.foodtypepaid = foodtypepaid
         self.unitofmeasure = unitofmeasure
         self.unitspaid = unitspaid
         self.incomekcal = incomekcal
         self.cashincome = cashincome
        
     def editData(self, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome):
         database = Database()
         database.open()
        
         query = ''' UPDATE employmentincome SET incomesource='%s', foodtypepaid='%s', unitofmeasure='%s', unitspaid=%s, incomekcal=%s,
                     cashincome=%s
                     WHERE hhid=%s AND pid=%s 
                     AND id=%s ''' % ( incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome, self.hhid, self.pid,  self.incomeid)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update income attributes
         self.incomesource = incomesource
         self.foodtypepaid = foodtypepaid
         self.unitofmeasure = unitofmeasure
         self.unitspaid = unitspaid
         self.incomekcal = incomekcal
         self.cashincome = cashincome

