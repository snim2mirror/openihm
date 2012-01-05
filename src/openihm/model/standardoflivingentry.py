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

class StandardOfLivingEntry:
     def __init__(self, pid,  summary, scope="", gender="", agebottom="", agetop="", item="", costperyear=""):
         if (item == "" and costperyear=="" ):
             if ( not self.getStandardOfLivingEntry(pid,  summary) ):
                 self.summary = ""
                 return None
         else:
             self.setData(pid,  summary, scope, gender, agebottom, agetop, item, costperyear)
            
     def getStandardOfLivingEntry(self, pid,  summary):
         database = Database()
         database.open()
         query = '''SELECT summary, scope, gender, agebottom, agetop, item, costperyear
                       FROM standardofliving WHERE pid=%s AND summary='%s' ''' % ( pid,  summary )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.summary = summary
                 self.scope = row[1]
                 self.gender = row[2]
                 self.agebottom = row[3]
                 self.agetop = row[4]
                 self.item = row[5]
                 self.costperyear = row[6]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid,  summary, scope, gender, agebottom, agetop, item, costperyear):
         database = Database()
         database.open()
        
         query = '''INSERT INTO standardofliving (pid, summary, scope, gender, agebottom, agetop, item, costperyear )
                 VALUES(%s,'%s','%s','%s',%s,%s,'%s',%s) ''' % ( pid,  summary, scope, gender, agebottom, agetop, item, costperyear )
       
         # execute query
         database.execUpdateQuery( query )
            
         database.close()
         # update characteristic attributes
         self.pid = pid
         self.summary = summary
         self.scope = scope
         self.gender = gender
         self.agebottom = agebottom
         self.agetop = agetop
         self.item = item
         self.costperyear = costperyear
        
     def editData(self, summary, scope, gender, agebottom, agetop, item, costperyear):
         database = Database()
         database.open()
        
         query = ''' UPDATE standardofliving SET summary='%s', scope='%s', gender='%s', agebottom=%s, agetop=%s, 
                     item='%s', costperyear=%s WHERE pid=%s AND 
                     summary='%s' ''' % ( summary, scope, gender, agebottom, agetop, item, costperyear,  self.pid,  self.summary)
                     
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update characteristic attributes
         self.summary = summary
         self.scope = scope
         self.gender = gender
         self.agebottom = agebottom
         self.agetop = agetop
         self.item = item
         self.costperyear = costperyear
