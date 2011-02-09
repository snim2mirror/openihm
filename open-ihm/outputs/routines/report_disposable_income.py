from data.database import Database
from report_adultequivalent import AdultEquivalent
from data.report_settingsmanager import ReportsSettingsManager


class DisposableHouseholdIncome:
    def getFinalIncomeReportTableQuery(self,projectid,householdIDs):
        
        #household cash income
        cropCashIncome = self.getCropCashIncome(projectid,householdIDs)
        employmentCashIncome = self.getEmploymentCashIncome(projectid,householdIDs)
        livestockCashIncome = self.getLivestockCashIncome(projectid,householdIDs)
        transferCashIncome = self.getTransferCashIncome(projectid,householdIDs)
        wildFoodCashIncome = self.getWildFoodCashIncome(projectid,householdIDs)

        #household cash income
        cropFIncome = self.getCropFIncome(projectid,householdIDs)
        employmentFIncome = self.getEmploymentFIncome(projectid,householdIDs)
        livestockFIncome = self.getLivestockFIncome(projectid,householdIDs)
        transferFIncome = self.getTransferFIncome(projectid,householdIDs)
        wildFoodFIncome = self.getWildFoodFIncome(projectid,householdIDs)

    def householdDisposableIncome(self,reporttype,projectid,householdIDs):
        houseids = ','.join(householdIDs)

        cropIncomeCash = self.getCropCashIncome(projectid,houseids)
        employmentIncomeCash = self.getEmploymentCashIncome(projectid,houseids)
        livestockIncomeCash = self.getLivestockCashIncome(projectid,houseids)
        transferIncomeCash = self.getTransferCashIncome(projectid,houseids)
        wildFoodIcomeCash = self.getWildFoodCashIncome(projectid,houseids)

        cropIncomeFood = self.getCropFIncome(projectid,houseids)
        employmentIncomeFood = self.getEmploymentFIncome(projectid,houseids)
        livestockIncomeFood = self.getLivestockFIncome(projectid,houseids)
        transferIncomeFood = self.getTransferFIncome(projectid,houseids)
        wildFoodIcomeFood = self.getWildFoodFIncome(projectid,houseids)

        #calculate total household cash income
        listlength = len(cropIncomeCash)
        print cropIncomeCash, '          ', employmentIncomeCash, '  ',livestockIncomeCash
        householdsCash = []
        for i in range(0,listlength):
            templist = []
            hhid = cropIncomeCash[i][0]
            templist.append(hhid)
            householdCashIncome = cropIncomeCash[i][1] + employmentIncomeCash[i][1] + livestockIncomeCash[i][1] + transferIncomeCash[i][1] + wildFoodIcomeCash[i][1]
            templist.append(householdCashIncome)
            householdsCash.append(tuple(templist))
            #householdsCash.append(hhid,householdCashIncome)
        print householdsCash

        listlength = len(cropIncomeFood)
        householdsFood = []
        for i in range(0,listlength):
            templist = []
            hhid = cropIncomeFood[i][0]
            householdFoodIncome = cropIncomeFood[i][1] + employmentIncomeFood[i][1] + livestockIncomeFood[i][1] + transferIncomeFood[i][1] + wildFoodIcomeFood[i][1]
            templist.append(hhid,householdFoodIncome)
            householdsFood.append(tuple(templist))
        print householdsFood

    def getHouseholdAE(self, householdids,pid):
        householdsAE =[]
        for hhid in householdids:
            connector = AdultEquivalent()
            houseAE = connector.calculateHouseholdEnergyReq(hhid,pid)
            householdsAE.append(hhid,houseAE)
        return householdsAE

    def calculateHouseholdFoodNeeds(self,householdsAE,householdsFood):

        houseFoodPrice = []
        for i in range (len(householdsAE)):
            foodPrice = 0
            hid = householdsAE[0]
            housefoodNeed = householdsAE[i] - householdsFood[i]
            if housefoodNeed < 0:
                foodPrice = self.calculateHouseholdFoodPrice(housefoodNeed,pid)
            houseFoodPrice.append(hid,foodPrice)
        print houseFoodPrice
        return houseFoodPrice
            

    def calculateHouseholdFoodPrice(self,housefoodNeed,pid):
        dietquery = '''SELECT pid, fooditem, unitofmeasure,percentage, priceperunit FROM diet WHERE pid=%s''' % pid
        householdDiet = self.executeQuery(dietquery)
        
        householdFoodPrices = []
        foodprice = 0
        for row in householdDiet:
            foodProportion = housefoodNeed * (household[3]/100)
            foodKcalQuery = '''SELECT  energyvalueperunit from setup_foods_crops WHERE name='%s' ''' % row[1]
            foodKcal = self.executeQuery(foodKcalQuery)
            foodprice = foodprice + ((foodProportion/foodKcal[0]) * household[4])
        return foodprice
        

    def executeQuery(self,query):
        dbconnector = Database()
        dbconnector.open()
        recordset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        return recordset
        

    #get household cash income
    def getCropCashIncome(self,projectid,householdIDs):
        query = self.totalCropCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset
    
    def getEmploymentCashIncome(self,projectid,householdIDs):
        query = self.totalEmploymentCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset
    
    def getLivestockCashIncome(self,projectid,householdIDs):
        query = self.totalLivestockCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset

    def getTransferCashIncome(self,projectid,householdIDs):
        query = self.totalTransferCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset
    
    def getWildFoodCashIncome(self,projectid,householdIDs):
        query = self.totalWildFoodCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset

    #get household food income
    def getCropFIncome(self,projectid,householdIDs):
        query = self.totalCropFIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset
    
    def getEmploymentFIncome(self,projectid,householdIDs):
        query = self.totalEmploymentCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset
    
    def getLivestockFIncome(self,projectid,householdIDs):
        query = self.totalLivestockCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset

    def getTransferFIncome(self,projectid,householdIDs):
        query = self.totalTransferCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset
    
    def getWildFoodFIncome(self,projectid,householdIDs):
        query = self.totalWildFoodCashIncomeQuery(projectid,householdIDs)
        recordset = self.executeQuery(query)
        return recordset

    #build queries for household total cash income
    def totalCropCashIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS cropincome FROM cropincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
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
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS cropincome FROM cropincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query
    
    def totalEmploymentFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(cashincome) AS employmentcashincome FROM employmentincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalLivestockFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS livestockincome FROM livestockincome
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalTransferFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(cashperyear) AS transferincome FROM transfers
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query

    def totalWildFoodFIncomeQuery(self,projectid,houseids):
        query = '''SELECT hhid,SUM(unitssold * unitprice) AS wildfoodsincome FROM wildfoods
                        WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
        return query
    
    def getFinalIncomeReportTableQuery(self,reporttype,projectid,householdIDs):

        if reporttype =='Cash Income - Raw' or reporttype =='Cash Income - Standardised':
            cropsQuery = self.buildCropIncomeQuery(projectid,cropdetails,householdIDs)
            employmentQuery = self.buildEmploymentIncomeQuery(projectid,employmentdetails,householdIDs)
            livestockQuery = self.buildLivestockIncomeQuery(projectid,livestockdetails,householdIDs)
            loansQuery =''
            #loansQuery = self.buildLoanIncomeQuery(projectid,loandetails,householdIDs)
            transfersQuery = self.buildTransferIncomeQuery(projectid,transferdetails,householdIDs)
            wildfoodsQuery = self.buildWildFoodsIncomeQuery(projectid,wildfoodsdetails,householdIDs)

        elif reporttype =='Food Income - Raw' or reporttype =='Food Income - Standardised':
            cropsQuery = self.buildCropFIncomeQuery(projectid,cropdetails,householdIDs)
            employmentQuery = self.buildEmploymentFIncomeQuery(projectid,employmentdetails,householdIDs)
            livestockQuery = self.buildLivestockFIncomeQuery(projectid,livestockdetails,householdIDs)
            transfersQuery = self.buildTransferFIncomeQuery(projectid,transferdetails,householdIDs)
            wildfoodsQuery = self.buildWildFoodsFIncomeQuery(projectid,wildfoodsdetails,householdIDs)
            loansQuery =''


        queryconnector = HouseholdIncomeQuery()
        query = queryconnector.buildFinalReportQuery (projectid,householdIDs)

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
                basequery = basequery + " and '%s' IS NOT NULL" % (currentcolumn)
        return basequery
        
    def buildHCharacteristicsQuery(self,hcharacteristics, tablename):
        ''' build query for selecting households that meet selected household characteristics from the report interface'''
        houseid = tablename + '.hhid'
        basequery = ''
        
        if len(hcharacteristics)!=0:
            basequery = '''SELECT households.hhid, households.pid FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
            for coulumnname in hcharacteristics:
                currentcolumn =  tablename + '.' + coulumnname
                basequery = basequery + " and '%s' IS NOT NULL" % (currentcolumn)
        return basequery

