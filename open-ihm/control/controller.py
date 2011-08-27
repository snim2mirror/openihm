#------------------------------------------------------------------------------------------------------------------	
#	Filename: controller.py
#
#  The main controller module for openihm. Based on earlier work on controller.py 
#  in the data sub-package.
#------------------------------------------------------------------------------------------------------------------

from model.database import Database 
from model.project import Project
from currencymanager import CurrencyManager
from globalhouseholdcharacteristicsmanager import GlobalHouseholdCharacteristicsManager
from globalpersoncharacteristicsmanager import GlobalPersonCharacteristicsManager
from transfermanager import TransferManager

class Controller(CurrencyManager, GlobalHouseholdCharacteristicsManager, GlobalPersonCharacteristicsManager, TransferManager):
    def __init__(self):
        self.database = Database()
        
    def getProject(self, pid):
        project = Project(pid)
        return project
        
    def getProjectName(self, pid):
        project = Project(pid)
        return project.getProjectName()
        
    def addProject(self, projectname, startdate, enddate, description, currency):
        project = Project(0, projectname, startdate, enddate, description, currency)
        return project
        
    def saveProject(self, pid, projectname, startdate, enddate, description, currency):
        project = Project(pid)
        project.setData(projectname, startdate, enddate, description, currency)
        
    def addProjectCharacteristic(self, pid, characteristic, characteristictype, datatype):
        project = Project(pid)
        project.addCharacteristic(characteristic, characteristictype, datatype)
        
    def removeProjectCharacteristic(self, pid, characteristic, characteristictype):
        project = Project(pid)
        project.addCharacteristic(characteristic, characteristictype)
        
    def getProjects(self):       
        query = "SELECT pid FROM projects"
        self.database.open()
        rows = self.database.execSelectQuery( query )
        self.database.close()
        projects = []
        
        for row in rows:
            pid = row[0]
            project = Project(pid)
            projects.append( project )
            
        return projects
        
    def getProjectsMatching(self,  pid="",  ptitle=""):
        SQLcondition 	= ""
        if ( pid != "" ):
            SQLcondition = " WHERE pid=%s" % pid
        
        if ( ptitle != "" ):
            if ( SQLcondition == "" ):
                SQLcondition = " WHERE projectname LIKE '%" + "%s" % ( ptitle ) + "%'" 
            else:
                SQLcondition = SQLcondition + " OR projectname LIKE '%" + "%s" % ( ptitle ) + "%'" 
                
        query = ''' SELECT pid FROM projects%s''' % ( SQLcondition )
        
        self.database.open()
        rows = self.database.execSelectQuery(  query )
        self.database.close()
        
        projects = []
        for row in rows:
            pid = row[0]
            project = Project(pid)
            projects.append( project )
        
        return projects

    def existsProjectMatching(self,  pid="",  ptitle=""):
        projects    = self.getProjectsMatching( pid,  ptitle )
        exists       = True if len(projects) != 0 else False
        return exists

