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
from standardoflivingentry import StandardOfLivingEntry

class StandardOfLivingEntryManager:
     def existsStandardOfLivingEntry(self, summary):
         entry = self.getStandardOfLivingEntry(summary)
         if entry.summary == "":
             return False
         else:
             return True
     
     def getStandardOfLivingEntry(self,  summary=""):
        entry = StandardOfLivingEntry( self.pid,  summary )
        return entry
        
     def addStandardOfLivingEntry(self,  summary, scope, gender, agebottom, agetop, item, costperyear ):
        entry = StandardOfLivingEntry( self.pid,  summary, scope, gender, agebottom, agetop, item, costperyear )
        return entry
        
     def delStandardOfLivingEntry(self,  summary=""):  
         database = Database()      
         query = "DELETE FROM standardofliving WHERE pid=%s AND summary='%s' " % ( self.pid,  summary )
         database.open()
         database.execUpdateQuery( query )
         database.close()
    
     def getStandardOfLivingEntries(self,  scope="Any",  gender="Any"):
         
         if (scope != "Any"):
             strcondition = "WHERE pid=%s AND scope='%s' " % (self.pid,  scope)
         else:
             strcondition = "WHERE pid=%s" % (self.pid)
         
         query = "SELECT summary FROM standardofliving %s" % strcondition
         
         database = Database()
         database.open()
         rows = database.execSelectQuery( query )
         database.close()
         entries = []
        
         for row in rows:
             summary = row[0]
             entry = StandardOfLivingEntry(self.pid,  summary)
             entries.append( entry )
            
         return entries
