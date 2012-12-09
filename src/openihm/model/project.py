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
from household import Household
from projecthouseholdcharacteristic import ProjectHouseholdCharacteristic
from projectpersoncharacteristic import ProjectPersonCharacteristic
from incomesourcemanager import IncomeSourceManager
from projectcharacteristicsmanager import ProjectCharacteristicsManager
from standardoflivingentrymanager import StandardOfLivingEntryManager
from projectdietitemmanager import ProjectDietItemManager
from projectassetsmanager import ProjectAssetsManager

class Project(IncomeSourceManager, ProjectAssetsManager,  ProjectCharacteristicsManager, StandardOfLivingEntryManager, ProjectDietItemManager):
    def __init__(self, pid=0, projectname="", startdate="", enddate="", description="", currency=""):
        if ( pid != 0 ):
            if ( not self.getProjectDetails( pid ) ):
                return None
        else:
            self.addProject(projectname, startdate, enddate, description, currency)
            
    def getProjectDetails(self,  pid):
        database = Database()
        database.open()
        query = "SELECT pid, projectname, startdate, enddate, description, currency FROM projects WHERE pid=%i " % (pid)
        rows = database.execSelectQuery( query )
        database.close()
        num = len(rows)
        if (num != 0):
            exists = True
            for row in rows:
                self.pid = row[0]
                self.projectname = row[1]
                self.startdate = row[2]
                self.enddate = row[3]
                self.description = row[4]
                self.currency = row[5]
        else:
            exists = False
       
        return exists
        
    def addProject(self, projectname, startdate, enddate, description, currency):
        # create INSERT INTO query
        query = '''INSERT INTO projects(projectname,startdate,enddate,description,currency) 
                     VALUES('%s','%s', '%s', '%s', '%s')''' % (projectname, startdate, enddate, description, currency)
        
        # execute query and commit changes
        database = Database()
        database.open()
        database.execUpdateQuery( query )
        
        # get the ID of the newly inserted project
        query = "SELECT LAST_INSERT_ID()"
        rows = database.execSelectQuery( query )
        for row in rows:
            projectid = row[0]
        
        database.close()
        
        # set project attributes to saved values
        self.pid = projectid
        self.projectname = projectname
        self.startdate = startdate
        self.enddate = enddate
        self.description = description
        self.currency = currency
        
    def getProjectID(self):
        return self.pid
    
    def getProjectName(self):
        return self.projectname
        
    def getStartDate(self):
        return self.startdate
    
    def getEndDate(self):
        return self.enddate
        
    def getDescription(self):
        return self.description
        
    def getCurrency(self):
        return self.currency
        
    def setData(self, projectname, startdate, enddate, description, currency):
        # create UPDATE query to update project
        query = '''UPDATE projects SET projectname='%s', startdate = '%s',enddate = '%s',description = '%s',currency = '%s'
                     WHERE pid=%i''' % (projectname, startdate, enddate, description, currency, self.pid)
    
        # execute query
        database = Database()
        database.open()
        database.execUpdateQuery( query )
        database.close()
        
        # set project attributes to saved values
        self.projectname = projectname
        self.startdate = startdate
        self.enddate = enddate
        self.description = description
        self.currency = currency
        
    #-------------------------------------------------------------------------------------------------------
    #  Project Households
    #-------------------------------------------------------------------------------------------------------
        
    def getHousehold(self,  hhid):
        household = Household( self.pid,  hhid )
        return household
        
    def addHousehold(self, hhid, householdname, dateofcollection):
        household = Household( self.pid,  hhid,  householdname, dateofcollection )
        return household
            
    def editHousehold(self, hhid, newhhid,  householdname, dateofcollection):
        household = Household( self.pid,  hhid )
        household.setData( householdname, dateofcollection,  newhhid )
        return household
        
    def delHousehold(self,  hhid):
        query = "DELETE FROM households WHERE pid=%s AND hhid=%s " % ( self.pid, hhid )
        database = Database()
        database.open()
        database.execUpdateQuery( query )
        database.close()
        
    def getHouseholds(self):
        query = '''SELECT hhid FROM households WHERE pid=%s ''' % (self.pid)
        
        database = Database()
        database.open()
        rows = database.execSelectQuery(query)
        database.close()
        
        households = []
        for row in rows:
            household = Household( self.pid,  row[0] )
            households.append( household )
                
        return households
