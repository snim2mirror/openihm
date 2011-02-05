# -*- coding: cp1252 -*-
#-------------------------------------------------------------------	
#	Filename: report_householdsincome.py
#-------------------------------------------------------------------
import data.mysql.connector
from data.config import Config


from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager
from report_householdsincome_query import HouseholdIncomeQuery
from report_adultequivalent import AdultEquivalent

class HouseholdIncome:
    def __init__(self):
        self.database = Database()
        self.config = Config.dbinfo().copy() 

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

    def getReportHouseholdIDs(self,query):
        
        reporthouseholdIDs=[]
        databaseConnector = Database()
        if query !='':
            databaseConnector.open()
            reporthouseholdIDs = databaseConnector.execSelectQuery( query )
            databaseConnector.close()
        return reporthouseholdIDs

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

    def getFinalIncomeReportTableQuery(self,reporttype,projectid,householdIDs,cropdetails,employmentdetails, livestockdetails,loandetails,transferdetails,wildfoodsdetails):

        if reporttype =='Cash Income - Raw':
            cropsQuery = self.buildCropIncomeQuery(projectid,cropdetails,householdIDs)
            employmentQuery = self.buildEmploymentIncomeQuery(projectid,employmentdetails,householdIDs)
            livestockQuery = self.buildLivestockIncomeQuery(projectid,livestockdetails,householdIDs)
            loansQuery =''
            #loansQuery = self.buildLoanIncomeQuery(projectid,loandetails,householdIDs)
            transfersQuery = self.buildTransferIncomeQuery(projectid,transferdetails,householdIDs)
            wildfoodsQuery = self.buildWildFoodsIncomeQuery(projectid,wildfoodsdetails,householdIDs)

        elif reporttype =='Food Income - Raw':
            cropsQuery = self.buildCropFIncomeQuery(projectid,cropdetails,householdIDs)
            employmentQuery = self.buildEmploymentFIncomeQuery(projectid,employmentdetails,householdIDs)
            livestockQuery = self.buildLivestockFIncomeQuery(projectid,livestockdetails,householdIDs)
            transfersQuery = self.buildTransferFIncomeQuery(projectid,transferdetails,householdIDs)
            wildfoodsQuery = self.buildWildFoodsFIncomeQuery(projectid,wildfoodsdetails,householdIDs)
            loansQuery =''


        queryconnector = HouseholdIncomeQuery()
        query = queryconnector.buildFinalReportQuery (projectid,householdIDs,cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)

        return query
                
    def buildCropIncomeQuery(self,projectid,cropdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in cropdetails)
        allincomesources = 'All'
        query =''

        if len(cropdetails)!=0:
            if allincomesources in cropdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS cropincome FROM cropincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in cropdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitssold * unitprice,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM cropincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        print query

        return query            

    def buildEmploymentIncomeQuery(self,projectid,employmentdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in employmentdetails)
        allincomesources = 'All'
        query =''
        if len(employmentdetails)!=0:
            if allincomesources in employmentdetails:
                query = '''SELECT hhid,SUM(cashincome) AS employmentcashincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in employmentdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', cashincome,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM employmentincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            

    def buildLivestockIncomeQuery(self,projectid,livestockdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in livestockdetails)
        allincomesources = 'All'
        query =''
        if len(livestockdetails)!=0:
            if allincomesources in livestockdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS livestockincome FROM livestockincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in livestockdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitssold * unitprice,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM livestockincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            

    def buildLoanIncomeQuery(self,projectid,loandetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in loandetails)
        allincomesources = 'All'
        query =''
        if len(loandetails)!=0:
            if allincomesources in loandetails:
                query = '''SELECT hhid,SUM(creditvalue) AS loanincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in loandetails:
                    query = query + ", GROUP_CONCAT(IF (creditsource = '%s', creditvalue,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM creditandloans WHERE pid=%s AND hhid IN (%s) AND creditsource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            

    def buildTransferIncomeQuery(self,projectid,transferdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in transferdetails)

        allincomesources = 'All'
        query =''
        if len(transferdetails)!=0:
            if allincomesources in transferdetails:
                query = '''SELECT hhid,SUM(cashperyear) AS transferincome FROM transfers WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in transferdetails:
                    query = query + ", GROUP_CONCAT(IF (sourceoftransfer = '%s', cashperyear,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM transfers WHERE pid=%s AND hhid IN (%s)" % (projectid,houseids)
                query = query + " GROUP BY hhid"
                
        return query            

    def buildWildFoodsIncomeQuery(self,projectid,wildfoodsdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in wildfoodsdetails)
        allincomesources = 'All'
        query =''
        if len(wildfoodsdetails)!=0:
            if allincomesources in wildfoodsdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS wildfoodsincome FROM wildfoods WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in wildfoodsdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitssold * unitprice,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM wildfoods WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            

    def getReportTable(self,query):
        result = []
        databaseConnector = Database()
        if query !='':
            db = data.mysql.connector.Connect(**self.config)
            cursor = db.cursor()
	    cursor.execute(query)
            columns = tuple( [d[0].decode('utf8') for d in cursor.description] )
            rows = cursor.fetchall()
            for row in rows:
                print row
                result.append(dict(zip(columns, row)))
                
	    # close database connection
            cursor.close()
            db.close()
        return result



    #Build Queries for Raw Income
    def buildCropFIncomeQuery(self,projectid,cropdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in cropdetails)
        allincomesources = 'All'
        query =''

        if len(cropdetails)!=0:
            if allincomesources in cropdetails:
                query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=cropincome.incomesource)) AS cropincome
                            FROM cropincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in cropdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitsconsumed * ( SELECT energyvalueperunit FROM setup_foods_crops WHERE name ='%s'),NULL)) AS '%s'" %(myincomesource,myincomesource,myincomesource)
                query = query + " FROM cropincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            


    def buildEmploymentFIncomeQuery(self,projectid,employmentdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in employmentdetails)
        allincomesources = 'All'
        query =''
        if len(employmentdetails)!=0:
            if allincomesources in employmentdetails:
                query = '''SELECT hhid,SUM(incomekcal) AS employmentcashincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in employmentdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', incomekcal,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM employmentincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            

    def buildLivestockFIncomeQuery(self,projectid,livestockdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in livestockdetails)
        allincomesources = 'All'
        query =''
        if len(livestockdetails)!=0:
            if allincomesources in livestockdetails:
                query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=livestockincome.incomesource))
                            AS livestockincome FROM livestockincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in livestockdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitsconsumed * unitsconsumed * ( SELECT energyvalueperunit FROM setup_foods_crops WHERE name='%s'),NULL)) AS '%s'" %(myincomesource,myincomesource,myincomesource)
                query = query + " FROM livestockincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            


    def buildTransferFIncomeQuery(self,projectid,transferdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in transferdetails)

        allincomesources = 'All'
        query =''
        if len(transferdetails)!=0:
            if allincomesources in transferdetails:
                query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=transfers.foodtype)) AS transferincome
                            FROM transfers WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in transferdetails:
                    query = query + ", GROUP_CONCAT(IF (sourceoftransfer = '%s', unitsconsumed *(SELECT energyvalueperunit FROM setup_foods_crops WHERE name='%s' ),NULL)) AS '%s'" %(myincomesource,myincomesource,myincomesource)
                query = query + " FROM transfers WHERE pid=%s AND hhid IN (%s)" % (projectid,houseids)
                query = query + " GROUP BY hhid"
                
        return query
    

    def buildWildFoodsFIncomeQuery(self,projectid,wildfoodsdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in wildfoodsdetails)
        allincomesources = 'All'
        query =''
        if len(wildfoodsdetails)!=0:
            if allincomesources in wildfoodsdetails:
                query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=wildfoods.incomesource))
                            AS wildfoodsincome FROM wildfoods WHERE pid = %s AND hhid IN (%s) AND GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in wildfoodsdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitsconsumed * ( SELECT energyvalueperunit FROM setup_foods_crops WHERE name ='%s'),NULL)) AS '%s'" %(myincomesource,myincomesource,myincomesource)
                query = query + " FROM wildfoods WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query

    #Standardised income - Cash Income

    def buildStandardisedCropIncomeQuery(self,projectid,cropdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in cropdetails)
        allincomesources = 'All'
        query =''

        if len(cropdetails)!=0:
            if allincomesources in cropdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS cropincome
                                FROM cropincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in cropdetails:
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitssold * unitprice,NULL)) AS '%s'" %(myincomesource,myincomesource)
                query = query + " FROM cropincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN (%s)" % (projectid,houseids,incomesources)
                query = query + " GROUP BY hhid"
        return query            

    def getHouseholdAdultEquivalent(self,projectid,householdids):
        adultEquivalentCalculator = AdultEquivalent()
        householdAdultEquivalent = adultEquivalentCalculator.calculateHouseholdEnergyReq(householdids,projectid)
        return householdAdultEquivalent
