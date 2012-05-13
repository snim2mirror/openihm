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

from incomesource import IncomeSource
import common

class IncomeSourceManager:
     def addIncomeSource(self, incomesourcename, incometype):
         ''' Adds (saves) a new incomesource to the database '''
         incomesource = IncomeSource(self.pid, incomesourcename, incometype)
         return incomesource
         
     def editIncomeSource(self, incomesourcename, incometype, newincomesourcename="" ):
         ''' Edits an existing incomesource '''
         newincomesourcename = incomesourcename if newincomesourcename == "" else newincomesourcename
         # get incomesource
         incomesource = IncomeSource(self.pid, incomesourcename)
         # modify the data
         incomesource.editIncomeSource(newincomesourcename, incometype)
         return incomesource
         
     def deleteIncomeSources(self,  incomesources):
         ''' Deletes incomesources matching names in the array incomesources from database '''
         db = Database()
         db.open() 
         
         for incomesourcename in incomesources:
             incomesourcename = common.getDbString( incomesourcename )
             query = "DELETE FROM projectincomesources WHERE pid=%s AND incomesource='%s'" % (self.pid, incomesourcename)
             db.execUpdateQuery( query )
             
         db.close()
         
     def getIncomeSource(self, incomesourcename):
         ''' Retrieve a incomesource identified by incomesourcename '''
         incomesource = IncomeSource(self.pid, incomesourcename)
         return incomesource
         
     def getIncomeSources(self, incometype=""):
         ''' Retrieves all incomesources from the database and returns an array of incomesource objects '''
         
         # create filtering condition		 
         incometype = common.getDbString( incometype )
         condition = "AND incometype LIKE '%"+incometype+"%' " if incometype != "" else ""
             
         query = "SELECT incomesource FROM projectincomesources WHERE pid=%s %s ORDER BY incomesource" % (self.pid, condition)
         
         db = Database()
         db.open() 
         records = db.execSelectQuery( query )
         
         incomesources = []
         for rec in records:
            incomesourcename = rec[0]
            incomesource = IncomeSource(self.pid, incomesourcename)
            incomesources.append( incomesource )
            
         db.close()
         return incomesources
         
     def getCropIncomes(self):
         ''' Retrieves crop incomes '''
         pass
         
     def getLivestockIncomes(self):
         ''' Retrieves livestock incomes '''
         pass
         
     def getWildfoodIncomes(self):
         ''' Retrieves wildfood incomes '''
         pass
         
     def getFoodIncomes(self,incometype=None):
         ''' Retrieve food (crop, livestock or wildfood incomes) '''
         # select query to get matchng food incomes
         query = '''SELECT name FROM setup_foods_crops WHERE category='%s' ''' % ( incometype )

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         incomesources = []
         for rec in records:
             incomesource = rec[0]
             incomesources.append( incomesource )
        
         db.close()
         return incomesources

     def getEmploymentIncomes(self):
         ''' Retrieve employment incomes '''
         # select query to get matchng food incomes
         query = '''SELECT incomesource FROM setup_employment'''

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         incomesources = []
         for rec in records:
             incomesource = rec[0]
             incomesources.append( incomesource )
        
         db.close()
         return incomesources

     def getTransferIncomes(self, transfertype="All"):
         ''' Retrieve transfer incomes '''
         # select query to get matchng food incomes
         if transfertype == "Official":
             condstr = "WHERE assistancetype='Official' OR assistancetype='External' "
         elif transfertype == "Unofficial":
             condstr = "WHERE assistancetype='UnOfficial' OR assistancetype='Internal' "
         else:
             condstr = ""
             
         query = '''SELECT sourceoftransfer FROM setup_transfers %s ''' % condstr

         db = Database()            
         db.open()
         records = db.execSelectQuery( query )

         incomesources = []
         for rec in records:
             incomesource = rec[0]
             incomesources.append( incomesource )
        
         db.close()
         return incomesources

