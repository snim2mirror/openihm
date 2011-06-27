from data.database import Database
from report_adultequivalent import AdultEquivalent
from data.report_settingsmanager import ReportsSettingsManager
from PyQt4 import QtGui
import datetime



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
            
        print householdAssets
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
                #print categoriesIncome

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

    def getHouseholdEnergyNeeds(self, householdids,pid):
        ''' get household food energy needs'''
        
        householdsENeed =[]
        for hhid in householdids:
            templist = []
            templist.append(hhid)
            connector = AdultEquivalent()
            houseENeed = connector.calculateHouseholdEnergyReq(hhid,pid)
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
            
    def householdDisposableIncome(self,reporttype,projectid,householdIDs):
        '''Calculate household disposable income'''
        
        houseids = ','.join(householdIDs)
        householdCashIncome = self.calculateHouseholdCashIncome(reporttype,projectid,houseids)
        householdFoodIncome = self.calculateHouseholdFoodIncome(reporttype,projectid,houseids)
        householdEnergyNeed = self.getHouseholdEnergyNeeds(householdIDs,projectid)
        #householdFoodPrice = self.checkHouseholdFoodNeeds(householdAE,householdFoodIncome)
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
                hhDisposableIncome = householdCashIncome[i][1] - householdFoodPrice
            else:
                excessFoodSales= self.calculateHouseholdFoodPrice(householdFoodNeed,projectid)
                hhDisposableIncome = householdCashIncome[i][1] + excessFoodSales
                
            #Standardise DI if reportype is DI/AE
            if (reporttype =='Disposable Income - Standardised')and householdEnergyNeed [i][1]!=0:
                houseAE = self.getHouseAE(householdEnergyNeed[i][1])
                hhDisposableIncome = hhDisposableIncome / houseAE

            templist.append(round(hhDisposableIncome,2))
            reporttable.append(tuple(templist))
            
        reporttable.sort(key=lambda x: x[1])


        return reporttable
            
