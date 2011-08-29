#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# accesstransfermanager.py
#
# this module controls the transferring of data from Access DB to Open-IHM
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pyodbc
from model.database import Database
from model.accessdb import AccessDB

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
             project.addHousehold(row.HHID, row.HHRealName, startdate)
             
         db.close()
         
    
