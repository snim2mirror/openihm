#!/usr/bin/env python

"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
from datetime import date
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

from model.database import Database          # connector to mysql database
from model.accessdb import AccessDB         #  connector to access database
from datetime import date

class TransferManager:
     def logTransfer(self, pid, pid_access, projectname, startdate, currency ):
         query = '''INSERT INTO transferlog(pid,pid_access,projectname,datecollected,currency) 
                      VALUES(%s,%s,'%s','%s','%s')''' % (pid, pid_access, projectname, startdate, currency)
                          
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def getProjectsFromAccess(self, filename):
         query = 'SELECT ProjectID, ProjectName, DateOfDataCollection FROM TblProject'
         db = AccessDB(filename)
         db.open()
         rows = db.execSelectQuery( query )
         db.close()
         return rows
         
     def existsCorrespondingProject(self, projectid, projectname, dateofcollection,  currency):
         ''' Checks if the project was transfered before '''
         
         query = '''SELECT projects.pid FROM projects, transferlog WHERE projects.pid=transferlog.pid AND transferlog.pid_access=%s 
                      AND transferlog.projectname='%s' AND transferlog.datecollected='%s' 
                      AND transferlog.currency='%s' ''' % (projectid,  projectname,  dateofcollection, currency)
                      
         db = Database()
         db.open() 
         records = db.execSelectQuery( query )
         
         exists = False
         if len(records) == 1:
             exists = True
        
         db.close()
         return exists
         
     def delCorrespondingProject(self, projectid, projectname, dateofcollection,  currency):
         ''' Checks if the project was transfered before '''
         
         query = '''SELECT projects.pid FROM projects, transferlog WHERE projects.pid=transferlog.pid AND transferlog.pid_access=%s 
                      AND transferlog.projectname='%s' AND transferlog.datecollected='%s' 
                      AND transferlog.currency='%s' ''' % (projectid,  projectname,  dateofcollection, currency)
                      
         db = Database()
         db.open() 
         records = db.execSelectQuery( query )
         for record in records:
             pid = record[0]
             query = '''DELETE FROM projects WHERE pid=%s''' % pid
             db.execUpdateQuery( query )
        
         db.close()
         
         
     def importProjects(self, filename, selectedProjects=""):
         ''' Imports all or selected projects from Access DB to OpenIHM '''
         for projectid in selectedProjects:
             self.importProject(filename, projectid)
         
     def importProject(self, filename, projectid):
         ''' transfers project data '''
         query = "SELECT ProjectID, ProjectName, DateOfDataCollection, Currency FROM TblProject WHERE ProjectID=%s" % projectid
         
         db = AccessDB(filename)
         db.open()
         row = db.execSelectOneQuery( query )
         
         if self.existsCorrespondingProject(row.ProjectID, row.ProjectName, row.DateOfDataCollection,  row.Currency):
             self.delCorrespondingProject(row.ProjectID, row.ProjectName, row.DateOfDataCollection,  row.Currency)
             
         projectname = row.ProjectName
         startdate = row.DateOfDataCollection
         currency = row.Currency
             
         # old IHM does not have these
         description = ""
         enddate = "0000-00-00"
             
         project = self.addProject(projectname, startdate, enddate, description, currency)
             
         self.logTransfer(project.pid, row.ProjectID, projectname, startdate, currency)
         
         if not self.existsCurrency(row.Currency):
             self.addCurrency(row.Currency, row.Currency, row.Currency)
             
         self.transferHouseholds(filename, row.ProjectID, project.pid,  startdate)
         
     def transferHouseholds(self, accessfilename, sourcepid, targetpid, startdate):
         query = "SELECT HHID, HHRealName FROM TblHouseholds WHERE ProjectID=%s" % sourcepid
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         project = self.getProject( targetpid )
         
         for row in rows:
             household = project.addHousehold(row.HHID, row.HHRealName, startdate)
             self.transferHouseholdMembers( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdAssets( accessfilename, sourcepid,  row.HHID,  household )
             
         db.close()
         
     def transferHouseholdMembers(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = "SELECT PersonID, Sex, Age FROM TblDemog WHERE ProjectID=%s AND HHID=%s " % (sourcepid, sourcehhid)
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         # old IHM does not have these fields
         headhousehold = "No"
         education = "" 
         periodaway = 0
         reason = ""
         whereto = ""
         
         # this year
         thisyear = date.today().year
         for row in rows:
             yearofbirth = thisyear - int(row.Age)
             sex = "Male" if row.Sex == "M" else "Female"
             household.addMember(row.PersonID, yearofbirth, headhousehold,  sex, education, periodaway, reason, whereto)
             
         db.close()
         
     def transferHouseholdAssets(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT tblLkUpAssets.AssetCategory, tblLkUpAssets.AssetName, tblLkUpAssets.Unit, tblLkUpAssets.PriceUnit, TblAssetVals.Value
                       FROM TblAssetVals, tblLkUpAssets
                       WHERE TblAssetVals.AssetID = tblLkUpAssets.AssetID AND TblAssetVals.ProjectID=%s 
                       AND TblAssetVals.HHID=%s''' % (sourcepid, sourcehhid)
         print query
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             category = row.AssetCategory
             assettype = row.AssetName
             unitofmeasure = row.Unit
             costperunit = row.PriceUnit
             numunits = row.Value
             household.addAsset(category,  assettype, unitofmeasure, costperunit, numunits )    
             
         db.close()
    
