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

class OpenIhmExportManager:
     def exportIhmProject(self, projectid,  filename):
         project = self.getProject(projectid)                  # self refers to controller which inherits OpenIhmExportManager
         projectline = "project<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                           % (project.projectname + " [imported]", project.startdate, project.enddate,  project.description,  project.currency)
         ihmFile = open(filename, 'w')
         ihmFile.write(projectline)
         ihmFile.close()
         
         # export project data
         self.exportProjectCharacteristics(project, filename)
         self.exportProjectDiet(project, filename)
         self.exportProjectStandardOfLiving(project, filename)
         self.exportProjectAssets(project, filename)
         self.exportProjectIncomeSources(project, filename)
         self.exportHouseholds(project, filename)
         
     def exportProjectCharacteristics(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT characteristic, chartype, datatype FROM projectcharacteristics
                       WHERE pid=%s''' % project.pid
                       
         chars = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for char in chars:
             charline = '''INSERT INTO projectcharacteristics (pid, characteristic, chartype, datatype )
                 VALUES({pid},'%s','%s',%s)<endl>\n''' % (char[0], char[1], char[2])
             ihmFile.write(charline)
             
         ihmFile.close()
         
     def exportProjectIncomeSources(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT incomesource, incometype FROM projectincomesources
                       WHERE pid=%s''' % project.pid
                       
         incomes = database.execSelectQuery( query )
         
         database.close()
         ihmFile = open(filename, 'a')
         for inc in incomes:
             incomeline = '''INSERT INTO projectincomesources(pid,incomesource,incometype) 
             VALUES({pid},'%s','%s')<endl>\n''' % (inc[0], inc[1])
             ihmFile.write(incomeline)
         ihmFile.close()
         
     def exportProjectDiet(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT fooditem, unitofmeasure, percentage, priceperunit FROM diet
                       WHERE pid=%s''' % project.pid
                       
         diets = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for diet in diets:
             dietline = '''INSERT INTO diet (pid, fooditem,unitofmeasure,percentage, priceperunit )
                         VALUES({pid},'%s','%s',%s,%s)<endl>\n''' % (diet[0], diet[1], diet[2], diet[3])
             ihmFile.write(dietline)
         ihmFile.close()
         
     def exportProjectAssets(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT assetname, assettype FROM projectassets
                       WHERE pid=%s''' % project.pid
                       
         assets = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for asset in assets:
             assetline = '''INSERT INTO projectassets(pid,assetname,assettype) 
             VALUES({pid},'%s','%s')<endl>\n''' % (asset[0], asset[1])
             ihmFile.write(assetline)
         ihmFile.close()
         
     def exportProjectStandardOfLiving(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT summary, scope, gender, agebottom, agetop, item, costperyear FROM standardofliving
                       WHERE pid=%s''' % project.pid
                       
         stdLvs = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for stdLv in stdLvs:
             stdLvline = '''INSERT INTO standardofliving (pid, summary, scope, gender, agebottom, agetop, item, costperyear )
                 VALUES({pid},'%s','%s','%s',%s,%s,'%s',%s)<endl>\n''' % (stdLv[0], stdLv[1], stdLv[2], stdLv[3], stdLv[4], stdLv[5], stdLv[6])
             ihmFile.write(stdLvline)
         ihmFile.close()
         
     def exportHouseholds(self, project,  filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, householdname, dateofcollection FROM households
                       WHERE pid=%s''' % project.pid
                       
         households = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for household in households:
             householdline = '''INSERT INTO households(pid,hhid,householdname,dateofcollection) 
                     VALUES({pid},%s, '%s', '%s')<endl>\n''' % (household[0], household[1], household[2])
             ihmFile.write(householdline)
         ihmFile.close()
         
         self.exportHouseholdCharacteristics(project, filename)
         self.exportHouseholdAssets(project, filename)
         self.exportHouseholdExpenditure(project, filename)
         self.exportHouseholdCropIncome(project, filename)
         self.exportHouseholdLivestockIncome(project, filename)
         self.exportHouseholdWildfoodsIncome(project, filename)
         self.exportHouseholdEmploymentIncome(project, filename)
         self.exportHouseholdTransfersIncome(project, filename)
         self.exportHouseholdMembers(project, filename)
             
     def exportHouseholdCharacteristics(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, characteristic, charvalue FROM householdcharacteristics
                       WHERE pid=%s''' % project.pid
                       
         chars = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for char in chars:
             charline = '''INSERT INTO householdcharacteristics (pid,hhid, characteristic, charvalue )
                 VALUES({pid},%s,'%s','%s')<endl>\n'''  % (char[0], char[1], char[2])
             ihmFile.write(charline)
         ihmFile.close()
         
     def exportHouseholdAssets(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, assetcategory, assettype, unitofmeasure, unitcost, totalunits FROM assets
                       WHERE pid=%s''' % project.pid
                       
         assets = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for asset in assets:
             assetline = '''INSERT INTO assets (pid, hhid, assetcategory, assettype, unitofmeasure, unitcost, totalunits )
                 VALUES({pid},%s,'%s','%s','%s',%s,%s)<endl>\n''' % (asset[0], asset[1], asset[2], asset[3], asset[4], asset[5])
             ihmFile.write(assetline)
         ihmFile.close()
         
     def exportHouseholdExpenditure(self, project, filename):
         pass
         
     def exportHouseholdCropIncome(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed FROM cropincome
                       WHERE pid=%s''' % project.pid
                       
         crops = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for crop in crops:
             cropline = '''INSERT INTO cropincome(pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed)
                 VALUES({pid},%s,'%s','%s',%s,%s,%s,%s,%s)<endl>\n''' % (crop[0],  crop[1], crop[2], crop[3], crop[4], crop[5], crop[6], crop[7])
             ihmFile.write(cropline)
         ihmFile.close()
         
     def exportHouseholdLivestockIncome(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed FROM livestockincome
                       WHERE pid=%s''' % project.pid
                       
         items = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for item in items:
             livestockline = '''INSERT INTO livestockincome(pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed)
                 VALUES({pid},%s,'%s','%s',%s,%s,%s,%s,%s)<endl>\n''' % (item[0],  item[1], item[2], item[3], item[4], item[5], item[6], item[7])
             ihmFile.write(livestockline)
         ihmFile.close()
         
     def exportHouseholdWildfoodsIncome(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed FROM wildfoods
                       WHERE pid=%s''' % project.pid
                       
         items = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for item in items:
             wfline = '''INSERT INTO wildfoods(pid, hhid, incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed)
                 VALUES({pid},%s,'%s','%s',%s,%s,%s,%s,%s)<endl>\n''' % (item[0],  item[1], item[2], item[3], item[4], item[5], item[6], item[7])
             ihmFile.write(wfline)
         ihmFile.close()
         
     def exportHouseholdEmploymentIncome(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome FROM employmentincome
                       WHERE pid=%s''' % project.pid
                       
         items = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for item in items:
             empline = '''INSERT INTO employmentincome(pid, hhid, incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome)
                 VALUES({pid},%s,'%s','%s','%s',%s,%s,%s)<endl>\n''' % (item[0],  item[1], item[2], item[3], item[4], item[5], item[6])
             ihmFile.write(empline)
         ihmFile.close()
         
     def exportHouseholdTransfersIncome(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven,
                      unitsconsumed, unitssold, priceperunit FROM transfers
                      WHERE pid=%s''' % project.pid
                       
         items = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for item in items:
             transline = '''INSERT INTO transfers(pid, hhid, sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven,
                      unitsconsumed, unitssold, priceperunit) VALUES({pid},%s,'%s','%s',%s,'%s','%s',%s,
                      %s,%s,%s)<endl>\n''' % (item[0],  item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9])
             ihmFile.write(transline)
         ihmFile.close()
         
     def exportHouseholdMembers(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, personid, yearofbirth, headofhousehold, sex, education, periodaway, reason, whereto 
                      FROM householdmembers
                      WHERE pid=%s''' % project.pid
                       
         members = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for member in members:
             memberline = '''INSERT INTO householdmembers(pid, hhid, personid, yearofbirth, headofhousehold, sex, education, periodaway, reason, whereto) 
                     VALUES({pid},%s, '%s', %s,'%s','%s','%s',%s,'%s','%s')<endl>\n''' % (member[0],  member[1], member[2], member[3], 
                     member[4], member[5], member[6], member[7], member[8])
    
             ihmFile.write(memberline)
         ihmFile.close()
         
         self.exportPersonalCharacteristics(project, filename)
             
     def exportPersonalCharacteristics(self, project, filename):
         database = Database()
         database.open()
         
         query = '''SELECT hhid, personid, characteristic, charvalue 
                      FROM personalcharacteristics
                      WHERE pid=%s''' % project.pid
                       
         chars = database.execSelectQuery( query )
         
         database.close()
         
         ihmFile = open(filename, 'a')
         for char in chars:
             charline = '''INSERT INTO personalcharacteristics (pid,hhid, personid, characteristic, charvalue )
                 VALUES({pid},%s,'%s','%s','%s')<endl>\n''' % (char[0], char[1],  char[2], char[3])
             ihmFile.write(charline)
         ihmFile.close()
    
