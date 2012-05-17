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
             if fields[0] == "projectcharacteristic":
                 self.importProjectCharacteristic(project, fields)
                 
             if fields[0] == "projectdiet":
                 self.importProjectDiet(project, fields)
                 
             if fields[0] == "projectstandardofliving":
                 self.importProjectStandardOfLiving(project, fields)
             
             if fields[0] == "household":
                 self.importProjectHousehold(project, fields)
                 
             if fields[0] == "householdcharacteristic":
                 self.importHouseholdCharacteristic(project, fields)
                 
             if fields[0] == "householdasset":
                 self.importHouseholdAsset(project, fields)
                 
             if fields[0] == "householdcropincome":
                 self.importHouseholdCropIncome(project, fields)
                 
             if fields[0] == "householdlivestockincome":
                 self.importHouseholdLivestockIncome(project, fields)
                 
             if fields[0] == "householdwildfoodsincome":
                 self.importHouseholdWildfoodsIncome(project, fields)
                 
             if fields[0] == "householdemploymentincome":
                 self.importHouseholdEmploymentIncome(project, fields)
                 
             if fields[0] == "householdtransferincome":
                 self.importHouseholdTransferIncome(project, fields)
                 
             if fields[0] == "householdmember":
                 self.importHouseholdMember(project, fields)
                 
             if fields[0] == "householdmembercharacteristic":
                 self.importHouseholdMemberCharacteristic(project, fields)
     
     def importProjectCharacteristic(self, project, fields):
         if not self.existsGlobalCharacteristic(fields[1]):
             self.addGlobalCharacteristic(fields[1], fields[2], fields[3]) 
             
         project.addProjectCharacteristic(fields[1], fields[2], fields[3]) 
         
     def importProjectDiet(self, project, fields):
         project.addProjectDietItem(fields[1], fields[2], fields[3], fields[4]) 
         
     def importProjectStandardOfLiving(self, project, fields):
         project.addStandardOfLivingEntry(fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7]) 
      
     def importProjectHousehold(self, project, fields):
         project.addHousehold(fields[1], fields[2], fields[3])
         
     def importHouseholdCharacteristic(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addCharacteristic(fields[2], fields[3])
         
     def importHouseholdAsset(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addAsset(fields[2], fields[3], fields[4], fields[5], fields[6])
         
     def importHouseholdCropIncome(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addCropIncome(fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8])
         
     def importHouseholdLivestockIncome(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addLivestockIncome(fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8])
         
     def importHouseholdWildfoodsIncome(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addWildfoodsIncome(fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8])
         
     def importHouseholdEmploymentIncome(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addEmploymentIncome(fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])
         
     def importHouseholdTransferIncome(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addTransferIncome(fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10])
    
     def importHouseholdMember(self, project, fields):
         household = project.getHousehold(fields[1])
         household.addMember(fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9])
         
     def importHouseholdMemberCharacteristic(self, project, fields):
         member = project.getHousehold(fields[1]).getMember(fields[2])
         member.addCharacteristic(fields[3], fields[4])
