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

# -*- coding: cp1252 -*-

import includes.mysql.connector as connector
from data.config import Config


from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager
from report_householdsincome_query import HouseholdIncomeQuery
from report_adultequivalent import AdultEquivalent

class HouseholdIncome:
    def __init__(self):
        self.database = Database()
        self.config = Config.dbinfo().copy() 

    def buildPCharacteristicsQuery(self,pcharacteristics, projectid):
        ''' build query for selecting households that meet selected personal characteristics from the report interface'''
        
        basequery = ''
        
        if len(pcharacteristics)!=0:
            basequery = '''SELECT personalcharacteristics.hhid, personalcharacteristics.pid FROM personalcharacteristics WHERE
                            personalcharacteristics.pid=%s''' % (projectid)
            for pcharacteristic in pcharacteristics:
                basequery = basequery + " AND personalcharacteristics.characteristic='%s' AND personalcharacteristics.charvalue='Yes'" % (pcharacteristic)
        return basequery
        
    def buildHCharacteristicsQuery(self,hcharacteristics, projectid):
        ''' build query for selecting households that meet selected household characteristics from the report interface'''
        basequery = ''
        
        if len(hcharacteristics)!=0:
            basequery = '''SELECT householdcharacteristics.hhid, householdcharacteristics.pid FROM householdcharacteristics WHERE
                            householdcharacteristics.pid=%s''' % (projectid)
            for hcharacteristic in hcharacteristics:
                basequery = basequery + " AND householdcharacteristics.characteristic='%s' AND householdcharacteristics.charvalue='Yes'" % (hcharacteristic)
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
                pcharsQuery =self.buildPCharacteristicsQuery(pcharselected, projectid)
                hcharsQuery = self.buildHCharacteristicsQuery(hcharselected, projectid)
                query = '''SELECT * FROM (%s UNION ALL %s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 3 ''' % (householdsquery,pcharsQuery,hcharsQuery)
                
            elif len(selectedhchars) !=0:
                hcharsQuery = self.buildHCharacteristicsQuery(hcharselected, projectid)
                query = '''SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2 ''' % (householdsquery,hcharsQuery)
            elif len(selectedpchars) !=0:
                pcharsQuery =self.buildPCharacteristicsQuery(pcharselected, projectid)
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

    def getReportTable(self,query,pid,reporttype):
        result = []
        databaseConnector = Database()
        if query !='':
            db = connector.Connect(**self.config)
            cursor = db.cursor()
	    cursor.execute(query)
            columns = tuple( [d[0].decode('utf8') for d in cursor.description] ) #get column headers
            rows = cursor.fetchall()
            for row in rows:
                if reporttype == 'Cash Income - Standardised' or reporttype == 'Food Income - Standardised':
                    hhid = row[0]
                    householdAE = self.getAdultEquivalent(hhid,pid)
                    standardisedList = tuple(self.standardiseIncome(row,householdAE))
                    result.append(dict(zip(columns, standardisedList)))
                else:
                    result.append(dict(zip(columns, row)))
                
	    # close database connection
            cursor.close()
            db.close()
        return result

    def getAdultEquivalent(self, hhid,pid):
        connector = AdultEquivalent()
        householdEnergyNeed = connector.calculateHouseholdEnergyReq(hhid,pid)
        houseAE = connector.caclulateHouseholdAE(householdEnergyNeed)
        return houseAE
        
    def standardiseIncome(self,row,householdAE):
        standardisedList =[]
        standardisedList.append(row[0])
        listlength = len(row)
        houseAE = householdAE
        for i in range(1,listlength):
            stardisedincome = row[i]
            if row[i]:
                income = float(row[i])/householdAE
                stardisedincome= round(income,2)
            standardisedList.append(stardisedincome)
        return standardisedList


    #Build Queries for Raw Food Income
    def buildCropFIncomeQuery(self,projectid,cropdetails,householdids):
        houseids = ','.join(householdids)
        incomesources = ','.join("'" + p + "'" for p in cropdetails)
        allincomesources = 'All'
        query =''

        if len(cropdetails)!=0:
            if allincomesources in cropdetails:
                query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=cropincome.incomesource)) AS 'CropFoodIncome (KCals)'
                            FROM cropincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in cropdetails:
                    outputname = myincomesource + '(KCal)'
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitsconsumed * ( SELECT energyvalueperunit FROM setup_foods_crops WHERE name ='%s'),NULL)) AS '%s'" %(myincomesource,myincomesource,outputname)
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
                query = '''SELECT hhid,SUM(incomekcal) AS 'EmploymentFoodIncome (KCals)' FROM employmentincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in employmentdetails:
                    outputname = myincomesource + '(KCal)'
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', incomekcal,NULL)) AS '%s'" %(myincomesource,outputname)
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
                            AS 'LivestockFoodIncome (KCals)' FROM livestockincome WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in livestockdetails:
                    outputname = myincomesource + '(KCal)'
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitsconsumed * unitsconsumed * ( SELECT energyvalueperunit FROM setup_foods_crops WHERE name='%s'),NULL)) AS '%s'" %(myincomesource,myincomesource,outputname)
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
                query = '''SELECT hhid,SUM(unitsconsumed * (SELECT energyvalueperunit FROM setup_foods_crops WHERE setup_foods_crops.name=transfers.foodtype)) AS 'TransferFoodIncome (KCals)'
                            FROM transfers WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in transferdetails:
                    outputname = myincomesource + '(KCal)'
                    query = query + ", GROUP_CONCAT(IF (sourceoftransfer = '%s', unitsconsumed *(SELECT energyvalueperunit FROM setup_foods_crops WHERE name='%s' ),NULL)) AS '%s'" %(myincomesource,myincomesource,outputname)
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
                            AS 'WildFoodsIncome (KCals)' FROM wildfoods WHERE pid = %s AND hhid IN (%s) GROUP BY hhid''' % (projectid,houseids)
            else:
                query = "SELECT hhid"
                for myincomesource in wildfoodsdetails:
                    outputname = myincomesource + '(KCal)'
                    query = query + ", GROUP_CONCAT(IF (incomesource = '%s', unitsconsumed * ( SELECT energyvalueperunit FROM setup_foods_crops WHERE name ='%s'),NULL)) AS '%s'" %(myincomesource,myincomesource,outputname)
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
