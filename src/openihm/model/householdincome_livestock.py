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

class HouseholdLivestockIncome:
     def __init__(self, incomeid=0, pid="", hhid="",  incomesource="", unitofmeasure="", unitsproduced="", unitssold="", unitprice="", otheruses="", unitsconsumed=""):
         if (incomeid != 0 ):
             if ( not self.getIncomeDetails(pid, hhid, incomeid) ):
                 self.pid = ""
                 self.hhid = ""
                 self.incomeid = ""
                 return None
         else:
             self.setData(pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed)
            
     def getIncomeDetails(self, pid, hhid, incomeid):
         database = Database()
         database.open()
         query = '''SELECT id, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed
                       FROM livestockincome WHERE hhid=%s AND pid=%s AND id=%s ''' % ( hhid, pid,  incomeid )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.hhid = hhid
                 self.incomeid = incomeid
                 self.incomesource = row[1]
                 self.unitofmeasure = row[2]
                 self.unitsproduced = row[3]
                 self.unitssold = row[4]
                 self.unitprice = row[5]
                 self.otheruses = row[6]
                 self.unitsconsumed = row[7]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed):
         database = Database()
         database.open()
        
         query = '''INSERT INTO livestockincome(pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed)
                 VALUES(%s,%s,'%s','%s',%s,%s,%s,%s,%s) ''' % ( pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed )
       
         print query
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
         self.unitofmeasure = unitofmeasure
         self.unitsproduced = unitsproduced
         self.unitssold = unitssold
         self.unitprice = unitprice
         self.otheruses = otheruses
         self.unitsconsumed = unitsconsumed
        
     def editData(self, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed):
         database = Database()
         database.open()
        
         query = ''' UPDATE livestockincome SET incomesource='%s', unitofmeasure='%s', unitsproduced=%s, unitssold=%s, unitprice=%s,
                     otheruses=%s, unitsconsumed=%s
                     WHERE hhid=%s AND pid=%s 
                     AND id=%s ''' % ( incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed, self.hhid, self.pid,  self.incomeid)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update asset attributes
         self.incomesource = incomesource
         self.unitofmeasure = unitofmeasure
         self.unitsproduced = unitsproduced
         self.unitssold = unitssold
         self.unitprice = unitprice
         self.otheruses = otheruses
         self.unitsconsumed = unitsconsumed

