#!/usr/bin/env python

"""
This file is part of open-ihm.

-*- coding: utf-8 -*-

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
from settingsmanager import SettingsManager
from project import Project

class Controller:
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
        
    def getGlobalHouseholdCharacteristic(self, charid=0, charname=""):
        settingsmgr = SettingsManager()
        char = settingsmgr.getHouseholdCharacteristic(charid, charname)
        return char
        
    def getGlobalHouseholdCharacteristics(self):
        settingsmgr = SettingsManager()
        chars = settingsmgr.getHouseholdCharacteristics()
        return chars
        
    def getGlobalPersonCharacteristic(self, charid=0, charname=""):
        settingsmgr = SettingsManager()
        char = settingsmgr.getPersonCharacteristic(charid, charname)
        return char
        
    def getGlobalPersonCharacteristics(self):
        settingsmgr = SettingsManager()
        chars = settingsmgr.getPersonCharacteristics()
        return chars
        
    def getCurrencies(self):
        settingsmgr = SettingsManager()
        currencies = settingsmgr.getCurrencies()
        return currencies

