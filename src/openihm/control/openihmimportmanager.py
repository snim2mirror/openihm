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
from datetime import date

class OpenIhmImportManager:
     def logIhmTransfer(self, pid, pid_access, projectname, startdate, currency ):
         query = '''INSERT INTO transferlog(pid,pid_access,projectname,datecollected,currency) 
                      VALUES(%s,%s,'%s','%s','%s')''' % (pid, pid_access, projectname, startdate, currency)
                          
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
         
     def getProjectFromFile(self, filename):
         dbfile = file(filename, 'r')
         contents = dbfile.read()
         dbfile.close()
         
         lines = contents.split('<endl>\n')
         projectflds = lines[0].split('<d>')
         
         project = dict()
         project['projectname'] = projectflds[1]
         project['startdate'] = projectflds[2]
         project['enddate'] = projectflds[3]
         project['description'] = projectflds[4]
         project['currency'] = projectflds[5]
         
         return project
         
     def existsCorrespondingIhmProject(self, projectname, startdate,  currency):
         ''' Checks if the project was transfered before '''
         
         query = '''SELECT projects.pid FROM projects, transferlog WHERE projects.pid=transferlog.pid
                      AND transferlog.projectname='%s' AND transferlog.datecollected='%s' 
                      AND transferlog.currency='%s' ''' % (projectname,  startdate, currency)
                      
         db = Database()
         db.open() 
         records = db.execSelectQuery( query )
         
         exists = False
         if len(records) == 1:
             exists = True
        
         db.close()
         return exists
         
     def delCorrespondingIhmProject(self, projectname, startdate,  currency):
         ''' Delete if the project was transfered before '''
         
         query = '''SELECT projects.pid FROM projects, transferlog WHERE projects.pid=transferlog.pid  
                      AND transferlog.projectname='%s' AND transferlog.datecollected='%s' 
                      AND transferlog.currency='%s' ''' % (projectname,  startdate, currency)
                      
         db = Database()
         db.open() 
         records = db.execSelectQuery( query )
         for record in records:
             pid = record[0]
             query = '''DELETE FROM projects WHERE pid=%s''' % pid
             db.execUpdateQuery( query )
        
         db.close()
         
     def importIhmProject(self, filename):
         ''' transfers project data '''
         projectdata = self.getProjectFromFile( filename )
         
         if self.existsCorrespondingIhmProject(projectdata["projectname"], projectdata["startdate"], projectdata["currency"]):
             self.delCorrespondingIhmProject(projectdata["projectname"], projectdata["startdate"], projectdata["currency"])
             
         project = self.addProject(projectdata["projectname"], projectdata["startdate"], projectdata["enddate"], projectdata["description"], projectdata["currency"])
         
         self.importIhmProjectData(project,  filename)
         
         self.logTransfer(project.pid, project.pid, project.projectname, project.startdate, project.currency)
         
         if not self.existsCurrency(project.currency):
             self.addCurrency(project.currency, project.currency, project.currency)
             
     def importIhmProjectData(self, project, filename):
         dbfile = file(filename, 'r')
         contents = dbfile.read()
         dbfile.close()
         
         lines = contents.split('<endl>\n')
         for line in lines:
             fields = line.split('<d>')
             if fields[0] == "household":
                 self.importProjectHousehold(project, fields)
                 
     def importProjectHousehold(self, project, fields):
         project.addHousehold(fields[1], fields[2], fields[3])
    
