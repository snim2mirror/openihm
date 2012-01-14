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
         self.exportProjectCharacteristics(project, filename)
         self.exportHouseholds(project, filename)
         
     def exportProjectCharacteristics(self, project, filename):
         chars = project.getProjectCharacteristics()
         ihmFile = open(filename, 'a')
         for char in chars:
             charline = "projectcharacteristic<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (char.name, char.chartype, char.datatype)
             ihmFile.write(charline)
         ihmFile.close()
         
     def exportHouseholds(self, project,  filename):
         households = project.getHouseholds()
         ihmFile = open(filename, 'a')
         for household in households:
             householdline = "household<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (household.hhid, household.householdname, household.dateofcollection)
             ihmFile.write(householdline)
         ihmFile.close()
         
         for household in households:
             self.exportHouseholdCharacteristics(household, filename)
             self.exportHouseholdAssets(household, filename)
             self.exportHouseholdExpenditure(household, filename)
             self.exportHouseholdCropIncome(household, filename)
             self.exportHouseholdLivestockIncome(household, filename)
             self.exportHouseholdWildfoodsIncome(household, filename)
             self.exportHouseholdEmploymentIncome(household, filename)
             self.exportHouseholdTransfersIncome(household, filename)
             self.exportHouseholdMembers(household, filename)
             
     def exportHouseholdCharacteristics(self, household, filename):
         chars = household.getCharacteristicsWithValues()
         ihmFile = open(filename, 'a')
         for char in chars:
             charline = "householdcharacteristic<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (char.hhid, char.name, char.charvalue)
             ihmFile.write(charline)
         ihmFile.close()
         
     def exportHouseholdAssets(self, household, filename):
         assets = household.getAssets()
         ihmFile = open(filename, 'a')
         for asset in assets:
             assetline = "householdasset<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (asset.hhid, asset.category, asset.assettype, asset.unitofmeasure, asset.costperunit, asset.numunits)
             ihmFile.write(assetline)
         ihmFile.close()
         
     def exportHouseholdExpenditure(self, household, filename):
         pass
         
     def exportHouseholdCropIncome(self, household, filename):
         crops = household.getCropIncomes()
         ihmFile = open(filename, 'a')
         for crop in crops:
             cropline = "householdcropincome<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (crop.hhid,  crop.incomesource, crop.unitofmeasure, crop.unitsproduced, crop.unitssold, crop.unitprice,
                       crop.otheruses, crop.unitsconsumed)
             ihmFile.write(cropline)
         ihmFile.close()
         
     def exportHouseholdLivestockIncome(self, household, filename):
         items = household.getLivestockIncomes()
         ihmFile = open(filename, 'a')
         for item in items:
             livestockline = "householdlivestockincome<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (item.hhid,  item.incomesource, item.unitofmeasure, item.unitsproduced, item.unitssold, item.unitprice,
                       item.otheruses, item.unitsconsumed)
             ihmFile.write(livestockline)
         ihmFile.close()
         
     def exportHouseholdWildfoodsIncome(self, household, filename):
         items = household.getWildfoodsIncomes()
         ihmFile = open(filename, 'a')
         for item in items:
             wfline = "householdwildfoodsincome<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (item.hhid,  item.incomesource, item.unitofmeasure, item.unitsproduced, item.unitssold, item.unitprice,
                       item.otheruses, item.unitsconsumed)
             ihmFile.write(wfline)
         ihmFile.close()
         
     def exportHouseholdEmploymentIncome(self, household, filename):
         items = household.getEmploymentIncomes()
         ihmFile = open(filename, 'a')
         for item in items:
             empline = "householdemploymentincome<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (item.hhid,  item.incomesource, item.foodtypepaid, item.unitofmeasure, item.unitspaid, item.incomekcal,
                       item.cashincome)
             ihmFile.write(empline)
         ihmFile.close()
         
     def exportHouseholdTransfersIncome(self, household, filename):
         items = household.getTransferIncomes()
         ihmFile = open(filename, 'a')
         for item in items:
             transline = "householdtransferincome<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (item.hhid,  item.sourcetype, item.sourceoftransfer, item.cashperyear, item.foodtype, item.unitofmeasure,
                       item.unitsgiven, item.unitsconsumed, item.unitssold, item.priceperunit)
             ihmFile.write(transline)
         ihmFile.close()
         
     def exportHouseholdMembers(self, household, filename):
         members = household.getMembers()
         ihmFile = open(filename, 'a')
         for member in members:
             memberline = "householdmember<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (member.hhid,  member.memberid, member.yearofbirth, member.headofhousehold,  member.sex, member.education, 
                       member.periodaway, member.reason, member.whereto)
    
             ihmFile.write(memberline)
         ihmFile.close()
         
         for member in members:
             self.exportPersonalCharacteristics(member, filename)
             
     def exportPersonalCharacteristics(self, member, filename):
         chars = member.getCharacteristicsWithValues()
         ihmFile = open(filename, 'a')
         for char in chars:
             charline = "householdmembercharacteristic<d>%s<d>%s<d>%s<d>%s<d><endl>\n" \
                 % (char.hhid, char.personid,  char.name, char.charvalue)
             ihmFile.write(charline)
         ihmFile.close()
    
