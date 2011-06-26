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
            query = ''' SELECT hhid,sex,yearofbirth FROM householdmembers WHERE hhid =%s AND pid =%s''' %(hid,projectid)
            currentHouseMembership = self.executeQuery(query)
            currentHouseMembership[2]= currentYear - currentHouseMembership[2]
            householdMembership.append(tuple(currentHouseMembership))
        return householdMembership

    def getAssets(self,projectid,selectedHouseholds):
        householdAssets =[]
        for hid in selectedHouseholds:
            currentHouseholdAssets =[]
            query = ''' SELECT  hhid,assetcategory,assettype,unitofmeasure,(unitcost * totalunitshhid) AS assetvalue FROM assets WHERE hhid =%s AND pid =%s
                            ORDER BY assetcategory,assettype''' %(hid,projectid)
            currentHouseholdAssets = self.executeQuery(query)
            householdAssets.append(tuple(currentHouseholdAssets))
        return householdAssets

    def getCashIncome(self,projectid,selectedHouseholds):
        householdCashIncome =[]
        incomesources = ['cropincome','employmentincome','livestockincome','transfers','wildfoods']
        for hid in selectedHouseholds:
            currentHouseholdIncome = []
            categoriesIncome = []
            householdCashIncome = 0
            currentHouseholdIncome.append(hid)
            
            for incomesource in incomesources:
                categoryIncome =[]
                sourcename = incomesource + 'income'
                query = '''SELECT SUM(unitssold * unitprice) AS '%s' FROM '%s'
                        WHERE pid = %s AND hhid = %s ''' % (incomesource,sourcename,projectid,hid)
                categoryIncome = self.executeQuery(query)
                categoriesIncome.append(categoryIncome[0])
                householdCashIncome = householdCashIncome + categoryIncome[0]
                
            currentHouseholdIncome.extend(categoriesIncome)
            currentHouseholdIncome.append(householdCashIncome)
            householdCashIncome.append(tuple(currentHouseholdIncome))
        return householdCashIncome

    def getFoodIncome(self,projectid,selectedHouseholds):
        allHouseholds =[]
        incomesources = ['cropincome','employmentincome','livestockincome','transfers','wildfoods']
        for hid in selectedHouseholds:
            currentHouseholdIncome = []
            categoriesIncome = []
            householdFoodIncome = 0
            currentHouseholdIncome.append(hid)

            for incomesource in incomesources:
                categoryIncome =[]
                sourcename = incomesource + 'income'
                fieldname = incomesource + '.incomesource'
                if incomesource == 'employmentincome':
                    query = '''SELECT hhid,SUM(incomekcal) AS employmentfoodincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,hid)
                else:
                    query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name='%s'))
                            AS '%s' FROM '%s' WHERE pid = %s AND hhid = %s''' % (fieldname,sourcename,incomesource,projectid,hid)
                categoryIncome = self.executeQuery(query)
                categoriesIncome.append(categoryIncome[0])
                householdFoodIncome = householdFoodIncome + categoryIncome[0]

            currentHouseholdIncome.extend(categoriesIncome)    
            currentHouseholdIncome.append(householdFoodIncome)
            allHouseholds.append(tuple(currentHouseholdIncome))
        return allHouseholds
        
            
    def executeQuery(self,query):
        '''run various select queries'''
        
        dbconnector = Database()
        recordset = dbconnector.execSelectQuery(query)
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
            
