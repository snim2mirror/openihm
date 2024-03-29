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

from data.database import Database
from report_adultequivalent import AdultEquivalent
from data.report_settingsmanager import ReportsSettingsManager
from PyQt4 import QtGui
import datetime
from outputs.routines.report_livingthreshold import LivingThreshhold 

class HouseholdBudget:
    def getHouseholdMembership(self,projectid,selectedHouseholds):
        householdMembership =[]
        t = datetime.datetime.now()
        currentYear = t.year

        for hid in selectedHouseholds:
            currentHouseMembership =[]
            housememberlist = []
            query = ''' SELECT hhid,sex,yearofbirth FROM householdmembers WHERE hhid =%s AND pid =%s''' %(hid,projectid)
            currentHouseMembership = self.executeQuery(query)
            members = len(currentHouseMembership)
            for row in currentHouseMembership:
                
                templist = list(row)
                templist[2]= currentYear - templist[2]
                housememberlist.append(tuple(templist))
            householdMembership.append(tuple(housememberlist))
        return householdMembership

    def getAssets(self,projectid,selectedHouseholds):
        householdAssets =[]
        for hid in selectedHouseholds:
            currentHouseholdAssets =[]
            query = ''' SELECT  hhid,assetcategory,assettype,unitofmeasure,(unitcost * totalunits) AS assetvalue FROM assets WHERE hhid =%s AND pid =%s
                            ORDER BY assetcategory,assettype''' %(hid,projectid)
            currentHouseholdAssets = self.executeQuery(query)
            householdAssets.append(tuple(currentHouseholdAssets))

        return householdAssets

    def getCashIncome(self,projectid,selectedHouseholds):
        allHouseholdsCashIncome =[]
        incomeSourceCategories = ['cropincome','employmentincome','livestockincome','transfers','wildfoods']
        for hid in selectedHouseholds:
            currentHouseholdIncome = []
            categoriesIncome = []
            householdCashIncome = 0
            currentHouseholdIncome.append(hid)
            
            for incomeSourceCategory in incomeSourceCategories:
                categoryIncome =[]
                sourcename = incomeSourceCategory + 'income'
                if incomeSourceCategory=='employmentincome':
                    query = '''SELECT SUM(cashincome) AS '%s' FROM %s
                            WHERE pid = %s AND hhid = %s ''' % (sourcename,incomeSourceCategory,projectid,hid)
                
                elif incomeSourceCategory=='transfers':
                    query = '''SELECT SUM(cashperyear) AS '%s' FROM %s
                            WHERE pid = %s AND hhid = %s ''' % (sourcename,incomeSourceCategory,projectid,hid)
                else:
                    query = '''SELECT SUM(unitssold * unitprice) AS '%s' FROM %s
                            WHERE pid = %s AND hhid = %s ''' % (sourcename,incomeSourceCategory,projectid,hid)

                categoryIncome = self.executeQuery(query)
                for row in categoryIncome:
                    if row[0]:
                        categoriesIncome.append(row[0])
                        householdCashIncome = householdCashIncome + row[0]
                    else:
                        categoriesIncome.append(0)

            currentHouseholdIncome.extend(categoriesIncome)
            currentHouseholdIncome.append(householdCashIncome)
            allHouseholdsCashIncome.append(tuple(currentHouseholdIncome))
        return allHouseholdsCashIncome

    def getFoodIncome(self,projectid,selectedHouseholds):
        allHouseholdsFoodIncome =[]
        incomeSourceCategories = ['cropincome','employmentincome','livestockincome','transfers','wildfoods']
        for hid in selectedHouseholds:
            currentHouseholdIncome = []
            categoriesIncome = []
            householdFoodIncome = 0
            currentHouseholdIncome.append(hid)

            for incomeSourceCategory in incomeSourceCategories:
                categoryIncome =[]
                sourcename = incomeSourceCategory + 'income'
                if incomeSourceCategory == 'transfers':
                    fieldname = incomeSourceCategory + '.foodtype'
                else:
                    fieldname = incomeSourceCategory + '.incomesource'
                    
                if incomeSourceCategory == 'employmentincome':
                    query = '''SELECT SUM(incomekcal) AS employmentfoodincome FROM employmentincome WHERE pid = %s AND hhid=%s ''' % (projectid,hid)
                else:
                    query = '''SELECT SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=%s))
                            AS '%s' FROM %s WHERE pid = %s AND hhid = %s''' % (fieldname,sourcename,incomeSourceCategory,projectid,hid)
                    
                categoryIncome = self.executeQuery(query)
                for row in categoryIncome:
                    if row[0]:
                        categoriesIncome.append(row[0])
                        householdFoodIncome = householdFoodIncome + row[0]
                    else:
                        categoriesIncome.append(0)

            currentHouseholdIncome.extend(categoriesIncome)    
            currentHouseholdIncome.append(householdFoodIncome)
            allHouseholdsFoodIncome.append(tuple(currentHouseholdIncome))
            
        return allHouseholdsFoodIncome
        
            
    def executeQuery(self,query):
        '''run various select queries'''
        
        dbconnector = Database()
        dbconnector.open()
        recordset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        return recordset

    def getHouseholdEnergyNeeds(self, projectid,selectedHouseholds):
        ''' get household food energy needs'''
        
        householdsENeed =[]
        for hhid in selectedHouseholds:
            templist = []
            templist.append(hhid)
            connector = AdultEquivalent()
            houseENeed = connector.calculateHouseholdEnergyReq(hhid,projectid)
            templist.append(houseENeed)
            householdsENeed.append(tuple(templist))
        return householdsENeed

    def getHouseAE(self,houseEnergyNeed):
        connector = AdultEquivalent()
        hholdAE = connector.caclulateHouseholdAE(houseEnergyNeed)
        return hholdAE

    def checkHouseholdFoodNeeds(self,householdsAE,householdsFood):

        houseFoodPrice = []
        for i in range (len(householdsAE)):
            templist = []
            foodPrice = 0
            hhid = householdsAE[0]
            templist.append(hhid)
            housefoodNeed = householdsAE[i] - householdsFood[i]
            if housefoodNeed < 0:
                foodPrice = self.calculateHouseholdFoodPrice(housefoodNeed,pid)
            templist.append(foodPrice)
            houseFoodPrice.append(tuple(templist))
        return houseFoodPrice

    def calculateHouseholdFoodPrice(self,housefoodNeed,projectid):
        ''' calculate the cost of food a houshold has to buy, to meet household food energy needs'''
        
        dietquery = '''SELECT pid, fooditem, unitofmeasure,percentage, priceperunit FROM diet WHERE pid=%s''' % projectid
        householdDiet = self.executeQuery(dietquery)
        
        householdFoodPrices = []
        foodprice = 0
        for row in householdDiet:
            foodKcalQuery = '''SELECT  energyvalueperunit from setup_foods_crops WHERE name='%s' ''' % row[1]
            foodKcal = self.executeQuery(foodKcalQuery)

            for item in foodKcal:
                kCal=item[0]

            if kCal!=0:
                foodprice = foodprice + (row[3] * (row[4]/kCal))

        totalCost = foodprice/100
        return totalCost

            
    def householdDisposableIncome(self,reporttype,projectid,householdIDs):
        '''Calculate household disposable income'''
        
        houseids = ','.join(householdIDs)
        householdCashIncome = self.calculateHouseholdCashIncome(reporttype,projectid,houseids)
        householdFoodIncome = self.calculateHouseholdFoodIncome(reporttype,projectid,houseids)
        householdEnergyNeed = self.getHouseholdEnergyNeeds(householdIDs,projectid)
        householdFoodPrice = 0
        reporttable = []
        listlen = len(householdIDs)
        for i in range(0,listlen):
            templist = []
            templist.append(householdIDs[i])
            householdFoodPrice = 0
            householdFoodNeed = householdEnergyNeed [i][1] - householdFoodIncome[i][1]

            if householdFoodNeed > 0:
                householdFoodPrice = self.calculateHouseholdFoodPrice(householdFoodNeed,projectid)
                hhDisposableIncome = householdCashIncome[i][1] - (householdFoodPrice * householdFoodNeed)
            else:
                householdExcess = householdFoodNeed
                excessFoodSales= self.calculateHouseholdFoodPrice(householdExcess,projectid)
                hhDisposableIncome = householdCashIncome[i][1] + (excessFoodSales * abs(householdFoodNeed))
                
            #Standardise DI if reportype is DI/AE
            if (reporttype =='Disposable Income - Standardised')and householdEnergyNeed [i][1]!=0:
                houseAE = self.getHouseAE(householdEnergyNeed[i][1])
                hhDisposableIncome = hhDisposableIncome / houseAE

            templist.append(round(hhDisposableIncome,2))
            reporttable.append(tuple(templist))
            
        reporttable.sort(key=lambda x: x[1])

        return reporttable

    def getnonFoodExepenses(self,projectid,hid):
        '''Get household non-food expenses'''
        expenses = 0
        connector = LivingThreshhold()
        expenses = connector.getHouseholdExpenditure(projectid,hid)
        return expenses
            
    def householdBudgetSummaries(self,projectid,selectedHouseholds):
        '''Calculate household disposable income'''
        
        householdCashIncome = self.getCashIncome(projectid,selectedHouseholds)
        householdFoodIncome = self.getFoodIncome(projectid,selectedHouseholds)
        householdEnergyNeed = self.getHouseholdEnergyNeeds(projectid,selectedHouseholds)
        householdFoodPrice = 0
        reporttable = []
        listlen = len(selectedHouseholds)
        for i in range(0,listlen):
            templist = []
            householdFoodPrice = 0
            percentageFoodCostMet = 0
            nonFoodPercentageMet = 0
            percentageFoodNeedMet = 0
            
            templist.append(selectedHouseholds[i])
            templist.append(householdEnergyNeed [i][1])
            
            householdExpenses = self.getnonFoodExepenses(projectid,selectedHouseholds[i])
            
            householdFoodNeed = householdEnergyNeed [i][1] - householdFoodIncome[i][6]
            
            if householdEnergyNeed [i][1]!=0:
                percentageFoodNeedMet = (householdFoodIncome[i][6] / householdEnergyNeed [i][1]) * 100
            if percentageFoodNeedMet > 100:
                percentageFoodNeedMet = 100

            templist.append(round(percentageFoodNeedMet,2))

            if householdFoodNeed > 0:
                householdFoodPrice = self.calculateHouseholdFoodPrice(householdFoodNeed,projectid)
                hhDisposableIncome = householdCashIncome[i][6] - (householdFoodPrice * householdFoodNeed)
                print 'Inde ',hhDisposableIncome
                householdFoodPrice = abs(householdFoodPrice * householdFoodNeed)
                
                if householdFoodPrice!=0 and hhDisposableIncome > 0:
                    percentageFoodCostMet = (householdCashIncome[i][6]/householdFoodPrice)* 100
                    if percentageFoodCostMet > 100:
                        percentageFoodCostMet =100
                else:
                    if hhDisposableIncome > 0:
                        percentageFoodCostMet =100
                print '%age ',percentageFoodCostMet
            else:
                householdExcess = householdFoodNeed
                excessFoodSales= self.calculateHouseholdFoodPrice(householdExcess,projectid)
                hhDisposableIncome = householdCashIncome[i][6] + (excessFoodSales * abs(householdFoodNeed))
                householdFoodPrice = abs(householdFoodPrice * householdFoodNeed)
                
            templist.append(householdFoodPrice)          
            hhDisposableIncome = round(hhDisposableIncome,2)
            templist.append(round(percentageFoodCostMet,2))
            templist.append(hhDisposableIncome)
            
            if householdExpenses!=0 and hhDisposableIncome > 0:
                nonFoodPercentageMet = (hhDisposableIncome/householdExpenses)*100
                if nonFoodPercentageMet > 100:
                    nonFoodPercentageMet = 100
            else:
                if hhDisposableIncome > 0:
                    nonFoodPercentageMet = 100
                

            templist.append(householdExpenses)
            templist.append(round(nonFoodPercentageMet,2))

            finalIncome = hhDisposableIncome - householdExpenses
            templist.append(finalIncome)
            
            reporttable.append(tuple(templist))
            
        #reporttable.sort(key=lambda x: x[1])
        return reporttable
