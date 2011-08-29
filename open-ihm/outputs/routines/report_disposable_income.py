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



class DisposableHouseholdIncome:

    def calculateHouseholdCashIncome(self,reporttype,projectid,houseids):
        '''Calculate total cash income for selected households'''
        
        cropIncomeCash = self.getCropCashIncome(projectid,houseids)
        employmentIncomeCash = self.getEmploymentCashIncome(projectid,houseids)
        livestockIncomeCash = self.getLivestockCashIncome(projectid,houseids)
        transferIncomeCash = self.getTransferCashIncome(projectid,houseids)
        wildFoodIcomeCash = self.getWildFoodCashIncome(projectid,houseids)

        listlength = len(cropIncomeCash)
        householdsCash = []

        for i in range(0,listlength):
            templist = []
            hhid = cropIncomeCash[i][0]
            templist.append(hhid)
            if cropIncomeCash[i][1]:
                cropsCashIncome = cropIncomeCash[i][1]
            else:
                cropsCashIncome = 0
                
            if employmentIncomeCash[i][1]:
                employmentCashIncome = employmentIncomeCash[i][1]
            else:
                employmentCashIncome = 0
                
            if livestockIncomeCash[i][1]:
                livestockCashIncome = livestockIncomeCash[i][1]
            else:
                livestockCashIncome = 0
                
            if transferIncomeCash[i][1] :
                transfersCashIncome = transferIncomeCash[i][1]
            else:
                transfersCashIncome = 0
                
            if wildFoodIcomeCash[i][1]:
                wildfoodCashIncome  = wildFoodIcomeCash[i][1]
            else:
                wildfoodCashIncome = 0

            householdCashIncome = cropsCashIncome + employmentCashIncome + livestockCashIncome + transfersCashIncome + wildfoodCashIncome
            templist.append(householdCashIncome)
            householdsCash.append(tuple(templist))
        return householdsCash

    def calculateHouseholdFoodIncome(self,reporttype,projectid,houseids):
        '''Calculate total food income for selected households'''

        cropIncomeFood = self.getCropFIncome(projectid,houseids)
        employmentIncomeFood = self.getEmploymentFIncome(projectid,houseids)
        livestockIncomeFood = self.getLivestockFIncome(projectid,houseids)
        transferIncomeFood = self.getTransferFIncome(projectid,houseids)
        wildFoodIcomeFood = self.getWildFoodFIncome(projectid,houseids)

        listlength = len(cropIncomeFood)
        householdsFoodIncome = []
        
        for i in range(0,listlength):
            templist = []
            hhid = cropIncomeFood[i][0]
            templist.append(hhid)
            if cropIncomeFood[i][1]:
                cropsFoodIncome = cropIncomeFood[i][1]
            else:
                cropsFoodIncome = 0
                
            if employmentIncomeFood[i][1]:
                employmentFoodIncome = employmentIncomeFood[i][1]
            else:
                employmentFoodIncome = 0
                
            if livestockIncomeFood[i][1]:
                livestockFoodIncome = livestockIncomeFood[i][1]
            else:
                livestockFoodIncome = 0
                
            if transferIncomeFood[i][1] :
                transfersFoodIncome = transferIncomeFood[i][1]
            else:
                transfersFoodIncome = 0
                
            if wildFoodIcomeFood[i][1]:
                wildfoodFIncome  = wildFoodIcomeFood[i][1]
            else:
                wildfoodFIncome = 0

            householdFoodIncome = cropsFoodIncome + employmentFoodIncome + livestockFoodIncome + transfersFoodIncome + wildfoodFIncome
            templist.append(householdFoodIncome)
            householdsFoodIncome.append(tuple(templist))
            
        return householdsFoodIncome
            

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

    def calculateHouseholdFoodPrice(self,housefoodNeed,pid):
        ''' calculate the cost of food a houshold has to buy, to meet household food energy needs'''
        
        dietquery = '''SELECT pid, fooditem, unitofmeasure,percentage, priceperunit FROM diet WHERE pid=%s''' % pid
        householdDiet = self.executeQuery(dietquery)
        
        householdFoodPrices = []
        foodprice = 0
        for row in householdDiet:
            foodProportion = abs(housefoodNeed) * (row[3]/100)
            foodKcalQuery = '''SELECT  energyvalueperunit from setup_foods_crops WHERE name='%s' ''' % row[1]
            foodKcal = self.executeQuery(foodKcalQuery)

            for item in foodKcal:
                kCal=item[0]

            if kCal!=0:
                foodprice = foodprice + ((foodProportion/kCal) * row[4])
                
            foodprice = round(foodprice,2)
        return foodprice
        
    def executeQuery(self,query):
        '''run various select queries'''
        
        dbconnector = Database()
        dbconnector.open()
        recordset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        return recordset

    #get household cash income
    def getCropCashIncome(self,projectid,householdIDs):
        '''get total houshold crop cash income'''
        
        basicQuery = self.totalCropCashIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset
    
    def getEmploymentCashIncome(self,projectid,householdIDs):
        '''get total houshold employment cash income'''
        
        basicQuery = self.totalEmploymentCashIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset
    
    def getLivestockCashIncome(self,projectid,householdIDs):
        '''get total houshold livestock cash income'''
        
        basicQuery = self.totalLivestockCashIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset

    def getTransferCashIncome(self,projectid,householdIDs):
        '''get total houshold transfer cash income'''
        
        basicQuery = self.totalTransferCashIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset
    
    def getWildFoodCashIncome(self,projectid,householdIDs):
        '''get total houshold wildfood cash income'''
        
        basicQuery = self.totalWildFoodCashIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        
        return recordset

    #get household food income
    def getCropFIncome(self,projectid,householdIDs):
        '''get total houshold crop food income'''
        
        basicQuery = self.totalCropFIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset
    
    def getEmploymentFIncome(self,projectid,householdIDs):
        '''get total houshold employment food income'''
        
        basicQuery = self.totalEmploymentFIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset
    
    def getLivestockFIncome(self,projectid,householdIDs):
        '''get total houshold livestock food income'''
        
        basicQuery = self.totalLivestockFIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset

    def getTransferFIncome(self,projectid,householdIDs):
        '''get total houshold transfer food income'''
        
        basicQuery = self.totalTransferFIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset
    
    def getWildFoodFIncome(self,projectid,householdIDs):
        '''get total houshold food income from wildfoods'''
        
        basicQuery = self.totalWildFoodFIncomeQuery(projectid,householdIDs)
        finalQuery = self.buildFinalIncomeCategoryQuery(basicQuery,projectid,householdIDs)
        recordset = self.executeQuery(finalQuery)
        return recordset

    def buildFinalIncomeCategoryQuery(self,query,projectid,householdids):
        ''' build a final query for getting total household incomes'''
        
        baseQuery  = '''SELECT hhid from households WHERE hhid IN (%s) and pid =%s''' % (householdids,projectid)
        baseQuery = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (baseQuery,query)
        return baseQuery

    #build queries for household total cash income
    def totalCropCashIncomeQuery(self,projectid,houseids):
        print 'houses ', houseids
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS cropincome FROM cropincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        print query
        return query
    
    def totalEmploymentCashIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(cashincome) AS employmentcashincome FROM employmentincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalLivestockCashIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS livestockincome FROM livestockincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalTransferCashIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(cashperyear) AS transferincome FROM transfers
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalWildFoodCashIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS wildfoodsincome FROM wildfoods
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    #build queries for household total food income
    def totalCropFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=cropincome.incomesource)) AS cropincome
                            FROM cropincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query
    
    def totalEmploymentFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(incomekcal) AS employmentcashincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalLivestockFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=livestockincome.incomesource))
                            AS livestockincome FROM livestockincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalTransferFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=transfers.foodtype)) AS transferincome
                            FROM transfers WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalWildFoodFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=wildfoods.incomesource))
                            AS wildfoodsincome FROM wildfoods WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def buildReportHouseholdIDsQuery(self,projectid,selectedhouseholds,pcharselected,hcharselected):
        ''' generate report household ids'''
        selectedpchars =[]
        selectedhchars = []
        selectedpchars = pcharselected
        selectedhchars = hcharselected
        
        hcharssetting = ReportsSettingsManager()
        hcharsTable= hcharssetting.setHCharacteristicsTableName(projectid)
        pcharssetting = ReportsSettingsManager()
        pharsTable = pcharssetting.setPCharacteristicsTableName(projectid)
        householdsquery = self.buildHouseholdsQuery(selectedhouseholds,projectid)
        
        query = ''

        if len(selectedhouseholds)!=0:
            if len(selectedpchars) ==0 and len(selectedhchars) ==0:
                query = householdsquery
                householdids = self.getReportHouseholdIDs(query)
                
            elif len(selectedpchars) !=0 and len(selectedhchars) !=0:
                pcharsQuery =self.buildPCharacteristicsQuery(pcharselected, pharsTable)
                hcharsQuery = self.buildHCharacteristicsQuery(hcharselected, hcharsTable)
                query = '''SELECT * FROM (%s UNION ALL %s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 3 ''' % (householdsquery,pcharsQuery,hcharsQuery)
                
            elif len(selectedhchars) !=0:
                hcharsQuery = self.buildHCharacteristicsQuery(hcharselected, hcharsTable)
                query = '''SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2 ''' % (householdsquery,hcharsQuery)
            elif len(selectedpchars) !=0:
                pcharsQuery =self.buildPCharacteristicsQuery(pcharselected, pharsTable)
                query = '''SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2 ''' % (householdsquery,pcharsQuery)
        return query

    def buildHouseholdsQuery(self,selectedhouseholds,projectid):
        households = tuple(selectedhouseholds)
        if len(households)==1:
            query = ''' SELECT hhid, pid FROM households WHERE householdname ='%s' AND pid=%s ''' % (households[0],projectid)
        else:
            query = ''' SELECT hhid, pid FROM households WHERE householdname IN %s AND pid=%s ''' % (households,projectid)
        return query

    def getReportHouseholdIDs(self,query):
        
        reporthouseholdIDs=[]
        databaseConnector = Database()
        if query !='':
            databaseConnector.open()
            reporthouseholdIDs = databaseConnector.execSelectQuery( query )
            databaseConnector.close()
        return reporthouseholdIDs

    def buildPCharacteristicsQuery(self,pcharacteristics, tablename):
        ''' build query for selecting households that meet selected personal characteristics from the report interface'''
        
        houseid = tablename + '.hhid'
        basequery = ''
        
        if len(pcharacteristics)!=0:
            basequery = '''SELECT households.hhid, households.pid FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
            for coulumnname in pcharacteristics:
                currentcolumn =  tablename + '.' + coulumnname
                basequery = basequery + " and '%s'='Yes'" % (currentcolumn)
        print 'pchars Query ', basequery
        return basequery
        
    def buildHCharacteristicsQuery(self,hcharacteristics, tablename):
        ''' build query for selecting households that meet selected household characteristics from the report interface'''
        houseid = tablename + '.hhid'
        basequery = ''
        
        if len(hcharacteristics)!=0:
            basequery = '''SELECT households.hhid, households.pid FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
            for coulumnname in hcharacteristics:
                currentcolumn =  tablename + '.' + coulumnname
                basequery = basequery + " and '%s'='Yes'" % (currentcolumn)
        return basequery

