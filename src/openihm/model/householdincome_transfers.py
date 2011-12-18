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

class HouseholdTransfersIncome:
     def __init__(self, incomeid=0, pid="", hhid="",  sourcetype="", sourceoftransfer="", cashperyear=0, foodtype="", unitofmeasure="", unitsgiven=0, unitsconsumed=0, unitssold=0, priceperunit=0):
         if (incomeid != 0 ):
             if ( not self.getIncomeDetails(pid, hhid, incomeid) ):
                 self.pid = ""
                 self.hhid = ""
                 self.incomeid = ""
                 return None
         else:
             self.setData(pid, hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit)
            
     def getIncomeDetails(self, pid, hhid, incomeid):
         database = Database()
         database.open()
         query = '''SELECT id, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit
                       FROM transfers WHERE hhid=%s AND pid=%s AND id=%s ''' % ( hhid, pid,  incomeid )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.hhid = hhid
                 self.incomeid = incomeid
                 self.sourcetype = row[1]
                 self.sourceoftransfer = row[2]
                 self.cashperyear = row[3]
                 self.foodtype = row[4]
                 self.unitofmeasure = row[5]
                 self.unitsgiven = row[6]
                 self.unitsconsumed = row[7]
                 self.unitssold = row[8]
                 self.priceperunit = row[9]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit):
         database = Database()
         database.open()
        
         query = '''INSERT INTO transfers(pid, hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven,
                      unitsconsumed, unitssold, priceperunit) VALUES(%s,%s,'%s','%s',%s,'%s','%s',%s,
                      %s,%s,%s) ''' % ( pid, hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit )
       
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
         self.sourcetype = sourcetype
         self.sourceoftransfer = sourceoftransfer
         self.cashperyear = cashperyear
         self.foodtype = foodtype
         self.unitofmeasure = unitofmeasure
         self.unitsgiven = unitsgiven
         self.unitsconsumed = unitsconsumed
         self.unitssold = unitssold
         self.priceperunit = priceperunit
        
     def editData(self, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit):
         database = Database()
         database.open()
        
         query = ''' UPDATE transfers SET sourcetype='%s', sourceoftransfer='%s', cashperyear=%s, foodtype='%s', unitofmeasure='%s', 
                     unitsgiven=%s, unitsconsumed=%s, unitssold=%s, priceperunit=%s
                     WHERE hhid=%s AND pid=%s 
                     AND id=%s ''' % ( sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit, self.hhid, self.pid,  self.incomeid)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update income attributes
         self.sourcetype = sourcetype
         self.sourceoftransfer = sourceoftransfer
         self.cashperyear = cashperyear
         self.foodtype = foodtype
         self.unitofmeasure = unitofmeasure
         self.unitsgiven = unitsgiven
         self.unitsconsumed = unitsconsumed
         self.unitssold = unitssold
         self.priceperunit = priceperunit
