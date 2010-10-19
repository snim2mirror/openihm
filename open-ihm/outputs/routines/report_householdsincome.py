#-------------------------------------------------------------------	
#	Filename: report_householdsincome.py
#-------------------------------------------------------------------

from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager
from report_householdsincome_query import HouseholdIncomeQuery

class HouseholdIncome:
    def __init__(self):
        self.database = Database()

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
        
        #settingsmanager = ReportsSettingsManager()
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
        print reporthouseholdIDs
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
                print householdsquery
                householdids = self.getReportHouseholdIDs(query)
                
            elif len(selectedpchars) !=0 and len(selectedhchars) !=0:
                pcharsQuery =self.buildPCharacteristicsQuery(pcharselected, pharsTable)
                hcharsQuery = self.buildHCharacteristicsQuery(hcharselected, hcharsTable)
                print householdsquery
                query = '''SELECT * FROM (%s UNION ALL %s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 3 ''' % (householdsquery,pcharsQuery,hcharsQuery)
                
            elif len(selectedhchars) !=0:
                hcharsQuery = self.buildHCharacteristicsQuery(hcharselected, hcharsTable)
                print householdsquery
                query = '''SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2 ''' % (householdsquery,hcharsQuery)
                print query
            elif len(selectedpchars) !=0:
                pcharsQuery =self.buildPCharacteristicsQuery(pcharselected, pharsTable)
                print householdsquery
                query = '''SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2 ''' % (householdsquery,pcharsQuery)
                print query
            
                print query
        return query

    def buildHouseholdsQuery(self,selectedhouseholds,projectid):
        print selectedhouseholds
        households = tuple(selectedhouseholds)
        if len(households)==1:
            query = ''' SELECT hhid, pid FROM households WHERE householdname ='%s' AND pid=%s ''' % (households[0],projectid)
        else:
            query = ''' SELECT hhid, pid FROM households WHERE householdname IN %s AND pid=%s ''' % (households,projectid)
        print query
        return query

    def getFinalIncomeReportTableQuery(self,projectid,householdIDs,cropdetails,employmentdetails, livestockdetails,loandetails,transferdetails,wildfoodsdetails):

        cropsQuery = self.buildCropIncomeQuery(projectid,cropdetails,householdIDs)
        employmentQuery = self.buildEmploymentIncomeQuery(projectid,employmentdetails,householdIDs)
        livestockQuery = self.buildLivestockIncomeQuery(projectid,livestockdetails,householdIDs)
        loansQuery = self.buildLoanIncomeQuery(projectid,loandetails,householdIDs)
        transfersQuery = self.buildTransferIncomeQuery(projectid,transferdetails,householdIDs)
        wildfoodsQuery = self.buildWildFoodsIncomeQuery(projectid,wildfoodsdetails,householdIDs)

        queryconnector = HouseholdIncomeQuery()
        query = queryconnector.buildFinalReportQuery (projectid,householdIDs,cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery)

        print query
        return query
                
    def buildCropIncomeQuery(self,projectid,cropdetails,householdids):
        houseids = ','.join(householdids)
        print 'nawa ma details a mbewu', cropdetails
        incomesources = tuple(cropdetails)
        print 'zinazo',incomesources
        allincomesources = 'All'
        query =''
        if len(cropdetails)!=0:
            if allincomesources in cropdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS cropincome FROM cropincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                if len(incomesources)==1:
                    query = '''SELECT hhid,incomesource,(unitssold * unitprice) AS cropincome FROM cropincome WHERE pid=%s AND hhid IN (%s) AND incomesource ='%s' GROUP BY hhid''' % (projectid,houseids,incomesources[0])
                else:
                    query = '''SELECT hhid,incomesource,(unitssold * unitprice) AS cropincome FROM cropincome WHERE pid=%s AND hhid IN (%s) AND incomesource IN %s''' % (projectid,houseids,incomesources)
        return query            

    def buildEmploymentIncomeQuery(self,projectid,employmentdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = tuple(employmentdetails)
        allincomesources = 'All'
        query =''
        if len(employmentdetails)!=0:
            if allincomesources in employmentdetails:
                query = '''SELECT hhid,SUM(cashincome) AS employmentcashincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                if len(incomesources)==1:
                    query = '''SELECT hhid,incomesource,cashincome AS employmentcashincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) AND incomesource ='%s' ''' % (projectid,houseids,incomesources[0])
                else:
                    query = '''SELECT hhid,incomesource,cashincome AS employmentcashincome FROM employmentincome WHERE pid = %s AND hhid IN (%s) AND incomesource IN %s''' % (projectid,houseids,incomesources)
        return query            

    def buildLivestockIncomeQuery(self,projectid,livestockdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = tuple(livestockdetails)
        allincomesources = 'All'
        query =''
        if len(livestockdetails)!=0:
            if allincomesources in livestockdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS livestockincome FROM livestockincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                if len(incomesources)==1:
                    query = '''SELECT hhid,incomesource,unitssold * unitprice AS livestockincome FROM livestockincome WHERE pid = %s AND hhid IN (%s) AND incomesource='%s' ''' % (projectid,houseids,incomesources[0])
                else:
                    query = '''SELECT hhid,incomesource,unitssold * unitprice AS livestockincome FROM livestockincome WHERE pid = %s AND hhid IN (%s) AND incomesource IN %s''' % (projectid,houseids,incomesources)
        return query            

    def buildLoanIncomeQuery(self,projectid,loandetails,householdids):
        houseids = ','.join(householdids)
        incomesources = tuple(loandetails)
        allincomesources = 'All'
        query =''
        if len(loandetails)!=0:
            if allincomesources in loandetails:
                query = '''SELECT hhid,SUM(creditvalue) AS loanincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                if len(incomesources)==1:
                    query = '''SELECT hhid,creditsource,creditvalue AS loanincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) AND creditsource='%s' ''' % (projectid,houseids,incomesources[0])
                else:
                    query = '''SELECT hhid,creditsource,creditvalue AS loanincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) AND creditsource IN %s''' % (projectid,houseids,incomesources)
        return query            

    def buildTransferIncomeQuery(self,projectid,transferdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = tuple(transferdetails)

        allincomesources = 'All'
        query =''
        if len(transferdetails)!=0:
            if allincomesources in transferdetails:
                query = '''SELECT hhid,SUM(cashperyear) AS transferincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                if len(incomesources)==1:
                    query = '''SELECT hhid,sourcetype,cashperyear AS transferincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) AND sourcetype='%s' ''' % (projectid,houseids,incomesources[0])
                else:
                    query = '''SELECT hhid,sourcetype,cashperyear AS transferincome FROM creditandloans WHERE pid = %s AND hhid IN (%s) AND sourcetype IN %s''' % (projectid,houseids,incomesources)
        return query            

    def buildWildFoodsIncomeQuery(self,projectid,wildfoodsdetails,householdids):
        houseids = ','.join(householdids)
        print houseids
        incomesources = tuple(wildfoodsdetails)
        allincomesources = 'All'
        query =''
        if len(wildfoodsdetails)!=0:
            if allincomesources in wildfoodsdetails:
                query = '''SELECT hhid,SUM(unitssold * unitprice) AS wildfoodsincome FROM wildfoods WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                if len(incomesources)==1:
                    query = '''SELECT hhid,incomesource,unitssold * unitprice AS wildfoodsincome FROM wildfoods WHERE pid = %s AND hhid IN (%s) AND incomesource='%s' ''' % (projectid,houseids,incomesources[0])
                else:
                    query = '''SELECT hhid,incomesource,unitssold * unitprice AS wildfoodsincome FROM wildfoods WHERE pid = %s AND hhid IN (%s) AND incomesource IN (%s)''' % (projectid,houseids,incomesources)
        return query            

    def getReportTable(self,query):
        reportTable=[]
        databaseConnector = Database()
        if query !='':
            databaseConnector.open()
            reportTable = databaseConnector.execSelectQuery( query )
            databaseConnector.close()
        print reportTable
        return reportTable
