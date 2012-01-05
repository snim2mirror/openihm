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

class ProjectDietItem:
     def __init__(self, pid,  itemid=0, fooditem="", unitofmeasure="", percentage="", priceperunit=""):
         if (itemid != 0 ):
             if ( not self.getProjectDietItem(pid,  itemid) ):
                 self.itemid = ""
                 return None
         else:
             self.setData(pid, fooditem, unitofmeasure, percentage, priceperunit)
            
     def getProjectDietItem(self, pid,  itemid):
         database = Database()
         database.open()
         query = '''SELECT id, fooditem, unitofmeasure, percentage, priceperunit
                       FROM diet WHERE pid=%s AND id=%s ''' % ( pid,  itemid )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.itemid = itemid
                 self.fooditem = row[1]
                 self.unitofmeasure = row[2]
                 self.percentage = row[3]
                 self.priceperunit = row[4]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid,  fooditem, unitofmeasure, percentage, priceperunit):
         database = Database()
         database.open()
        
         query = '''INSERT INTO diet (pid, fooditem,unitofmeasure,percentage, priceperunit )
                         VALUES(%s,'%s','%s',%s,%s) ''' % ( pid, fooditem,unitofmeasure,percentage, priceperunit  )
       
         # execute query
         database.execUpdateQuery( query )
         
         # get the ID of the newly inserted project
         query = "SELECT LAST_INSERT_ID()"
         rows = database.execSelectQuery( query )
         for row in rows:
             itemid = row[0]
            
         database.close()
         # update characteristic attributes
         self.pid = pid
         self.itemid = itemid
         self.fooditem = fooditem
         self.unitofmeasure = unitofmeasure
         self.percentage = percentage
         self.priceperunit = priceperunit
        
     def editData(self, fooditem, unitofmeasure, percentage, priceperunit):
         database = Database()
         database.open()
        
         query = ''' UPDATE diet SET fooditem='%s', unitofmeasure='%s', percentage=%s, priceperunit=%s
                         WHERE id=%s AND pid=%s ''' % ( fooditem,unitofmeasure,percentage, priceperunit, self.itemid, self.pid)
                     
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update characteristic attributes
         self.fooditem = fooditem
         self.unitofmeasure = unitofmeasure
         self.percentage = percentage
         self.priceperunit = priceperunit
