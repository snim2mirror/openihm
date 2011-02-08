from data.database import Database
from report_adultequivalent import AdultEquivalent

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

    def householdDisposableIncome(self):

        # get queries for household total cash income
        cropCashIncomeQuery = self.allCropsCashIncomeQuery(projectid,houseids)
        employmentCashIncomeQuery = self.totalEmploymentCashIncomeQuery(projectid,houseids)
        livestockCashIncomeQuery = self.totalLivestockCashIncomeQuery(projectid,houseids)
        transferCashIncomeQuery = self.totalTransferCashIncomeQuery(projectid,houseids)
        wildfoodCashIncomeQuery = self.totalWildFoodCashIncomeQuery(projectid,houseids)

        # get queries for household total food income
        cropFIncomeQuery = self.allCropsFIncomeQuery(projectid,houseids)
        employmentFIncomeQuery = self.totalEmploymentFIncomeQuery(projectid,houseids)
        livestockFIncomeQuery = self.totalLivestockFIncomeQuery(projectid,houseids)
        transferFIncomeQuery = self.totalTransferFIncomeQuery(projectid,houseids)
        wildfoodFIncomeQuery = self.totalWildFoodFIncomeQuery(projectid,houseids)

        cropIncomeCash = self.getCropCashIncome()
        employmentIncomeCash = self.getEmploymentCashIncome()
        livestockIncomeCash = self.getLivestockCashIncome()
        transferIncomeCash = self.getTransferCashIncome()
        wildFoodIcomeCash = getWildFoodCashIncome()

        cropIncomeFood = self.getCropFIncome()
        employmentIncomeFood = self.getEmploymentFIncome()
        livestockIncomeFood = self.getLivestockFIncome()
        transferIncomeFood = self.getTransferFIncome()
        wildFoodIcomeFood = getWildFoodFIncome()

        #calculate total household cash income
        listlength = len(cropIncomeCash)
        householdsCash = []
        for i in range(0,listlength):
            templist = []
            hhid = cropIncomeCash[i][0]
            householdCashIncome = cropIncomeCash[i][1] + employmentIncomeCash[i][1] + livestockIncomeCash[i][1] + transferIncomeCash[i][1] + wildFoodIcomeCash[i][1]
            templist.append(hhid,householdCashIncome)
            householdsCash.append(tuple(templist))
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
        databaseConnector.open()
        recordset = databaseConnector.execSelectQuery(query)
        databaseConnector.close()
        return recordset
        
        
            
        
            
        
        
        
        

    #get household cash income
    def getCropCashIncome(self):
        query = self.allCropsCashIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset
    
    def getEmploymentCashIncome(self):
        query = self.totalEmploymentCashIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset
    
    def getLivestockCashIncome(self):
        query = self.totalLivestockCashIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset

    def getTransferCashIncome(self):
        query = self.totalTransferCashIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset
    
    def getWildFoodCashIncome(self):
        query = self.totalWildFoodCashIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset

    #get household food income
    def getCropFIncome(self):
        query = self.buildCropFIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset
    
    def getEmploymentFIncome(self):
        query = self.buildEmploymentFIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset
    
    def getLivestockFIncome(self):
        query = self.buildLivestockFIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset

    def getTransferFIncome(self):
        query = self.buildTransferFIncomeQuery(projectid,houseids)
        recordset = self.executeQuery(query)
        return recordset
    
    def getWildFoodFIncome(self):
        query = self.totalWildFoodFIncomeQuery(projectid,houseids)
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
    

