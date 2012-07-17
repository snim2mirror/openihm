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
         enddate = row.DateOfDataCollection
             
         project = self.addProject(projectname, startdate, enddate, description, currency)
             
         self.logTransfer(project.pid, row.ProjectID, projectname, startdate, currency)
         
         #transfer standard of living
         self.transferStandardOfLiving(filename, row.ProjectID,  project.pid)
         
         #transfer diet
         self.transferProjectDiet(filename, row.ProjectID,  project.pid)
         
         if not self.existsCurrency(row.Currency):
             self.addCurrency(row.Currency, row.Currency, row.Currency)
             
         self.transferHouseholds(filename, row.ProjectID, project.pid,  startdate)
         
     def transferStandardOfLiving(self, accessfilename, sourcepid, targetpid):
         query = '''SELECT tblLkUpExpenses.ExpenseType, tblLkUpExpenses.Price, tblExpenses.Category, tblExpenses.LowerAgeM,
                       tblExpenses.UpperAgeM, tblExpenses.LowerAgeF, tblExpenses.UpperAgeF
                       FROM tblLkUpExpenses, tblExpenses
                       WHERE tblExpenses.ExpenseID = tblLkUpExpenses.ExpenseID AND tblExpenses.ProjectID=%s''' % sourcepid
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         project = self.getProject( targetpid )
         
         for row in rows:
             if (row.Category == "HH"):
                 scope = "Household"
                 gender = "All"
                 agetop = 0
                 agebottom = 0
             else:
                 scope = "Person"
                 gender = "Male" if row.Category == "M" else "Female"
                 agetop = row.UpperAgeM if gender=="Male" else row.UpperAgeF
                 agebottom = row.LowerAgeM if gender=="Male" else row.LowerAgeF
             item = row.ExpenseType
             costperyear = row.Price
             
             summary = "%s - %s - [%s to %s years]" % (item,  gender,  agebottom,  agetop) if scope == "Person" else "%s - %s" % (item, scope)
             project.addStandardOfLivingEntry(summary, scope, gender, agebottom, agetop, item, costperyear)
             
     def transferProjectDiet(self, accessfilename, sourcepid, targetpid):
         query = '''SELECT tblLkUpFoodVals.FoodName, tblFoodPurchase.PercentInDiet, tblFoodPurchase.PurchasePrice
                       FROM tblLkUpFoodVals, tblFoodPurchase
                       WHERE tblFoodPurchase.FoodUnitID = tblLkUpFoodVals.FoodUnitID AND tblFoodPurchase.ProjectID=%s''' % sourcepid
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         project = self.getProject( targetpid )
         
         for row in rows:
             fooditem = row.FoodName
             percentage = row.PercentInDiet
             priceperunit = row.PurchasePrice
             unitofmeasure = "Kg"
             project.addProjectDietItem(fooditem, unitofmeasure, percentage, priceperunit)
         
     def transferHouseholds(self, accessfilename, sourcepid, targetpid, startdate):
         query = "SELECT HHID, HHName, HHRealName FROM TblHouseholds WHERE ProjectID=%s" % sourcepid
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         project = self.getProject( targetpid )
         
         for row in rows:
             household = project.addHousehold(row.HHName, row.HHRealName, startdate)
             self.transferHouseholdChars( accessfilename, sourcepid,  row.HHID,  household ,  project)
             self.transferHouseholdMembers( accessfilename, sourcepid,  row.HHID,  household,  project )
             self.transferHouseholdAssets( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdCropIncome( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdLivestockIncome( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdWildfoodsIncome( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdGiftsIncome( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdAIDIncome( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdEmploymentIncome( accessfilename, sourcepid,  row.HHID,  household )
             self.transferHouseholdExpenditure( accessfilename, sourcepid,  row.HHID,  household )
             
         db.close()
         
     def transferHouseholdChars(self, accessfilename, sourcepid,  sourcehhid,  household,  project ):
          
         query = '''SELECT tblLkUpHHItem.ItemName, tblLkUpHHItem.Unit, tblHHItemValues.Value, tblHHItemValues.TrueFalse
                       FROM tblLkUpHHItem, tblHHItemValues
                       WHERE tblHHItemValues.ItemID = tblLkUpHHItem.ItemID AND tblHHItemValues.ProjectID=%s 
                       AND tblHHItemValues.HHID=%s''' % (sourcepid, sourcehhid)
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             chartype = "Household"
             charname = row.ItemName
             val = row.Value
             valyesno = row.TrueFalse
             if row.Unit != "Yes/No":
                 datatype = 3
                 charvalue = val
             else:
                 datatype = 1
                 charvalue = "Yes" if str(valyesno) == "True" else "No"
                 
             if not self.existsGlobalCharacteristic(charname):
                 self.addGlobalCharacteristic(charname,  chartype,  datatype)
                 
             if not project.existsProjectCharacteristic(charname):
                 project.addProjectCharacteristic(charname, chartype, datatype)
                 
             household.addCharacteristic(charname, charvalue)  
             
         db.close()
         
     def transferHouseholdMembers(self, accessfilename, sourcepid,  sourcehhid,  household,  project ):
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
             member = household.addMember(row.PersonID, yearofbirth, headhousehold,  sex, education, periodaway, reason, whereto)
             self.transferHouseholdMemberChars(accessfilename, sourcepid, sourcehhid,  row.PersonID,  member,  project)
             
         db.close()
         
     def transferHouseholdMemberChars(self, accessfilename, sourcepid,  sourcehhid,  personid,  member,  project):
         query = '''SELECT tblLkUpPersonalChars.CharType, tblPersonValsNew.DataValue, tblPersonValsNew.TrueFalse,
                      tblPersonValsNew.PercentTimeAway
                       FROM tblLkUpPersonalChars, tblPersonValsNew
                       WHERE tblPersonValsNew.CharID = tblLkUpPersonalChars.CharID AND tblPersonValsNew.ProjectID=%s 
                       AND tblPersonValsNew.HHID=%s AND tblPersonValsNew.PersonID=%s  ''' % (sourcepid, sourcehhid, personid)
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             chartype = "Personal"
             charname = row.CharType
             valdata = row.DataValue
             valpercent = row.PercentTimeAway
             valyesno = row.TrueFalse
             if valdata != None and str(valyesno) != "True":
                 datatype = 3
                 charvalue = valdata
             elif valpercent != None and str(valyesno) != "True":
                 datatype = 3
                 charvalue = valpercent
             else:
                 datatype = 1
                 charvalue = "Yes" if str(valyesno) == "True" else "No"
                 
             if not self.existsGlobalCharacteristic(charname):
                 self.addGlobalCharacteristic(charname,  chartype,  datatype)
                 
             if not project.existsProjectCharacteristic(charname):
                 project.addProjectCharacteristic(charname, chartype, datatype)
                 
             member.addCharacteristic(charname, charvalue)
             
         db.close()
         
     def transferHouseholdAssets(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT tblLkUpAssets.AssetCategory, tblLkUpAssets.AssetName, tblLkUpAssets.Unit, tblLkUpAssets.PriceUnit, TblAssetVals.Value
                       FROM TblAssetVals, tblLkUpAssets
                       WHERE TblAssetVals.AssetID = tblLkUpAssets.AssetID AND TblAssetVals.ProjectID=%s 
                       AND TblAssetVals.HHID=%s''' % (sourcepid, sourcehhid)
         
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
         
     def transferHouseholdCropIncome(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT TblLkUpIncomeSources.IncomeSource, TblIncomeSourcesCrops.Unit, 
                                 TblIncomeValsCrops.UnitsSold + TblIncomeValsCrops.UnitsConsumed AS UnitsProduced, 
                                 TblIncomeValsCrops.UnitsSold, TblIncomeValsCrops.PriceUnit, 0 AS OtherUses, 
                                 TblIncomeValsCrops.UnitsConsumed
                       FROM TblLkUpIncomeSources, TblIncomeSourcesCrops, TblIncomeValsCrops
                       WHERE TblLkUpIncomeSources.IncomeSourceID=TblIncomeSourcesCrops.IncomeSourceIDCrops 
                       AND TblIncomeSourcesCrops.IncomeSourceIDCrops=TblIncomeValsCrops.IncomeSourceIDCrops 
                       AND TblIncomeValsCrops.ProjectID=%s AND TblIncomeValsCrops.HHID=%s ''' % (sourcepid, sourcehhid)
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             incomesource = row.IncomeSource
             unitofmeasure = row.Unit
             unitsproduced = row.UnitsProduced if row.UnitsProduced != None else 0
             unitssold = row.UnitsSold if row.UnitsSold != None else 0
             unitprice = row.PriceUnit if row.PriceUnit != None else 0
             otheruses = row.OtherUses if row.OtherUses != None else 0
             unitsconsumed = row.UnitsConsumed if row.UnitsConsumed != None else 0
             unitsproduced = unitsconsumed if unitsproduced==0 and unitsconsumed != 0 else unitsproduced
             household.addCropIncome(incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed )    
             
         db.close()
         
     def transferHouseholdLivestockIncome(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT TblLkUpIncomeSources.IncomeSource, TblIncomeSourcesLS.Unit, 
                                 TblIncomeValsLS.UnitsSold + TblIncomeValsLS.UnitsConsumed AS UnitsProduced, 
                                 TblIncomeValsLS.UnitsSold, TblIncomeValsLS.PriceUnit, 0 AS OtherUses, 
                                 TblIncomeValsLS.UnitsConsumed
                       FROM TblLkUpIncomeSources, TblIncomeSourcesLS, TblIncomeValsLS
                       WHERE TblLkUpIncomeSources.IncomeSourceID=TblIncomeSourcesLS.IncomeSourceIDLS 
                       AND TblIncomeSourcesLS.IncomeSourceIDLS=TblIncomeValsLS.IncomeSourceIDLS 
                       AND TblIncomeValsLS.ProjectID=%s AND TblIncomeValsLS.HHID=%s ''' % (sourcepid, sourcehhid)
                       
         print query
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             incomesource = row.IncomeSource
             unitofmeasure = row.Unit
             unitsproduced = row.UnitsProduced if row.UnitsProduced != None else 0
             unitssold = row.UnitsSold if row.UnitsSold != None else 0
             unitprice = row.PriceUnit if row.PriceUnit != None else 0
             otheruses = row.OtherUses if row.OtherUses != None else 0
             unitsconsumed = row.UnitsConsumed if row.UnitsConsumed != None else 0
             unitsproduced = unitsconsumed if unitsproduced==0 and unitsconsumed != 0 else unitsproduced
             household.addLivestockIncome(incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed )    
             
         db.close()
         
     def transferHouseholdWildfoodsIncome(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT TblLkUpIncomeSources.IncomeSource, TblIncomeSourcesWF.Unit, 
                                 TblIncomeValsWF.UnitsSold + TblIncomeValsWF.UnitsConsumed AS UnitsProduced, 
                                 TblIncomeValsWF.UnitsSold, 0 AS PriceUnit, 0 AS OtherUses, 
                                 TblIncomeValsWF.UnitsConsumed
                       FROM TblLkUpIncomeSources, TblIncomeSourcesWF, TblIncomeValsWF
                       WHERE TblLkUpIncomeSources.IncomeSourceID=TblIncomeSourcesWF.IncomeSourceIDWF 
                       AND TblIncomeSourcesWF.IncomeSourceIDWF=TblIncomeValsWF.IncomeSourceIDWF 
                       AND TblIncomeValsWF.ProjectID=%s AND TblIncomeValsWF.HHID=%s ''' % (sourcepid, sourcehhid)
                       
         print query
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             incomesource = row.IncomeSource
             unitofmeasure = row.Unit
             unitsproduced = row.UnitsProduced if row.UnitsProduced != None else 0
             unitssold = row.UnitsSold if row.UnitsSold != None else 0
             unitprice = row.PriceUnit if row.PriceUnit != None else 0
             otheruses = row.OtherUses if row.OtherUses != None else 0
             unitsconsumed = row.UnitsConsumed if row.UnitsConsumed != None else 0
             unitsproduced = unitsconsumed if unitsproduced==0 and unitsconsumed != 0 else unitsproduced
             household.addWildfoodsIncome(incomesource, unitofmeasure, unitsproduced, unitssold, unitprice, otheruses, unitsconsumed )    
             
         db.close()
         
     def transferHouseholdGiftsIncome(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT TblLkUpIncomeSources.IncomeSource AS sourceoftransfer, 'Internal' AS sourcetype, 
                                 TblIncomeValsGift.CashYr AS cashperyear, '' AS foodtype,TblIncomeSourcesGift.Unit AS unitofmeasure,
                                 TblIncomeValsGift.UnitsConsumed AS unitsgiven,
                                 TblIncomeValsGift.UnitsConsumed AS unitsconsumed,
                                 0 AS unitssold, 0 AS priceperunit
                       FROM TblLkUpIncomeSources, TblIncomeSourcesGift, TblIncomeValsGift
                       WHERE TblLkUpIncomeSources.IncomeSourceID=TblIncomeSourcesGift.IncomeSourceIDGift 
                       AND TblIncomeSourcesGift.IncomeSourceIDGift=TblIncomeValsGift.IncomeSourceIDGift 
                       AND TblIncomeValsGift.ProjectID=%s AND TblIncomeValsGift.HHID=%s ''' % (sourcepid, sourcehhid)
                       
         print query
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             sourcetype = row.sourcetype
             sourceoftransfer = row.sourceoftransfer
             cashperyear = row.cashperyear if row.cashperyear != None else 0
             foodtype = row.foodtype if row.foodtype != None else ""
             unitofmeasure = row.unitofmeasure if row.unitofmeasure != None else ""
             unitsgiven = row.unitsgiven if row.unitsgiven != None else 0
             unitsconsumed = row.unitsconsumed if row.unitsconsumed != None else 0
             unitssold = row.unitssold if row.unitssold != None else 0
             priceperunit = row.priceperunit if row.priceperunit != None else 0
             household.addTransferIncome(sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit )    
             
         db.close()
         
     def transferHouseholdAIDIncome(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT TblLkUpIncomeSources.IncomeSource AS sourceoftransfer, 'External' AS sourcetype, 
                                 TblIncomeValsAID.UnitValueCash * TblIncomeValsAID.TimesItemsReceived AS cashperyear,
                                 '' AS foodtype,
                                 TblIncomeSourcesAID.Unit AS unitofmeasure,
                                 TblIncomeValsAID.UnitValueFood * TblIncomeValsAID.TimesItemsReceived AS unitsgiven,
                                 0 AS unitsconsumed,
                                 0 AS unitssold, 0 AS priceperunit
                       FROM TblLkUpIncomeSources, TblIncomeSourcesAID, TblIncomeValsAID
                       WHERE TblLkUpIncomeSources.IncomeSourceID=TblIncomeSourcesAID.IncomeSourceID 
                       AND TblIncomeSourcesAID.IncomeSourceID=TblIncomeValsAID.IncomeSourceID 
                       AND TblIncomeValsAID.ProjectID=%s AND TblIncomeValsAID.HHID=%s ''' % (sourcepid, sourcehhid)
                       
         print query
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             sourcetype = row.sourcetype
             sourceoftransfer = row.sourceoftransfer
             cashperyear = row.cashperyear if row.cashperyear != None else 0
             foodtype = row.foodtype if row.foodtype != None else ""
             unitofmeasure = row.unitofmeasure if row.unitofmeasure != None else ""
             unitsgiven = row.unitsgiven if row.unitsgiven != None else 0
             unitsconsumed = row.unitsconsumed if row.unitsconsumed != None else 0
             unitssold = row.unitssold if row.unitssold != None else 0
             priceperunit = row.priceperunit if row.priceperunit != None else 0
             household.addTransferIncome(sourcetype, sourceoftransfer, cashperyear, foodtype, unitofmeasure, unitsgiven, unitsconsumed, unitssold, priceperunit )    
             
         db.close()
         
     def transferHouseholdEmploymentIncome(self, accessfilename, sourcepid,  sourcehhid,  household ):
         query = '''SELECT TblLkUpIncomeSources.IncomeSource AS incomesource, TblIncomeSourcesEmp.FoodTypePaid as foodtypepaid, 
                                 TblIncomeSourcesEmp.FoodUnit as unitofmeasure,
                                 TblIncomeValsEmp.NFoodUnits AS unitspaid, 
                                 TblIncomeValsEmp.IncomeKcals AS incomekcal, 
                                 TblIncomeValsEmp.IncomeCash AS cashincome
                       FROM TblLkUpIncomeSources, TblIncomeSourcesEmp, TblIncomeValsEmp
                       WHERE TblLkUpIncomeSources.IncomeSourceID=TblIncomeSourcesEmp.IncomeSourceIDEmp 
                       AND TblIncomeSourcesEmp.IncomeSourceIDEmp=TblIncomeValsEmp.IncomeSourceIDEmp 
                       AND TblIncomeValsEmp.ProjectID=%s AND TblIncomeValsEmp.HHID=%s ''' % (sourcepid, sourcehhid)
                       
         print query
         
         db = AccessDB(accessfilename)
         db.open()
         rows = db.execSelectQuery( query )
         
         for row in rows:
             incomesource = row.incomesource
             foodtypepaid = row.foodtypepaid
             unitofmeasure = row.unitofmeasure if row.unitofmeasure != None else ''
             unitspaid= row.unitspaid if row.unitspaid != None else 0
             incomekcal = row.incomekcal if row.incomekcal != None else 0
             cashincome= row.cashincome if row.cashincome != None else 0
             household.addEmploymentIncome(incomesource, foodtypepaid, unitofmeasure, unitspaid, incomekcal, cashincome  )    
             
         db.close()
         
     def transferHouseholdExpenditure( self,  accessfilename, sourcepid,  sourcehhid,  household ):
         pass
    
