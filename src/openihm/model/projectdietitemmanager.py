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
from projectdietitem import ProjectDietItem

class ProjectDietItemManager:
     def existsProjectDietItem(self, itemid):
         item = self.getProjectDietItem(itemid)
         if item.itemid == "":
             return False
         else:
             return True
     
     def getProjectDietItem(self,  itemid):
        item = ProjectDietItem( self.pid,  itemid )
        return item
        
     def addProjectDietItem(self,  fooditem, unitofmeasure, percentage, priceperunit ):
        item = ProjectDietItem( self.pid,  0, fooditem, unitofmeasure, percentage, priceperunit )
        return item
        
     def delProjectDietItem(self,  itemid):  
         database = Database()      
         query = "DELETE FROM diet WHERE pid=%s AND id=%s " % ( self.pid,  itemid )
         database.open()
         database.execUpdateQuery( query )
         database.close()
    
     def getProjectDietItems(self):
         strcondition = "WHERE pid=%s" % (self.pid)
         
         query = "SELECT id FROM diet %s" % strcondition
         
         database = Database()
         database.open()
         rows = database.execSelectQuery( query )
         database.close()
         items = []
        
         for row in rows:
             itemid = row[0]
             item = ProjectDietItem(self.pid,  itemid)
             items.append( item )
            
         return items
