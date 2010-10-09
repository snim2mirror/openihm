# -*- coding: cp1252 -*-
#-------------------------------------------------------------------	
#	Filename: report_households_by_characteristics.py
#-------------------------------------------------------------------

from data.database import Database
from data.report_settingsmanager import ReportsSettingsManager

class HouseholdsByCharacteristics:
    def __init__(self):
        self.database = Database()

    def buildPCharacteristicsQuery(self,pcharacteristics, tablename):
        ''' build query for selecting households that meet selected personal characteristics from the report interface'''
        
        houseid = tablename + '.hhid'
        
        basequery = '''SELECT households.hhid, households.householdname FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
        for coulumnname in pcharacteristics:
            currentcolumn =  tablename + '.' + coulumnname
            basequery = basequery + ' and %s IS NOT NULL' % (currentcolumn)
        return basequery
        
    def buildHCharacteristicsQuery(self,hcharacteristics, tablename):
        ''' build query for selecting households that meet selected household characteristics from the report interface'''
        
        #settingsmanager = ReportsSettingsManager()
        houseid = tablename + '.hhid'
        
        basequery = '''SELECT households.hhid, households.householdname FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
        for coulumnname in hcharacteristics:
            currentcolumn =  tablename + '.' + coulumnname
            basequery = basequery + ' and %s IS NOT NULL' % (currentcolumn)
        return basequery

    def getReportTable(self,projectid,pcharselected,hcharselected,pquery,hquery):
        ''' generate report tables'''
        
        pcharstable =self.getPcharacteristicsTable(pquery)
        hcharstable = self.getHcharacteristicsTable(hquery)
        x = len(pcharstable)
        y = len(hcharstable)
        reporttable = []

        if (x ==0 and y== 0)or (x == 0 and pcharselected !=0)or (y == 0 and hcharselected !=0):
            return reporttable
        elif (x !=0 and y != 0):
            query = ''' SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2''' % (pquery,hquery)
            reporttable = self.getFinalReportTableData(query)
            return reporttable
        elif (x == 0 and pcharselected ==0):
            return hcharstable
        elif (y == 0 and hcharselected ==0):
            return pcharstable

    def getPcharacteristicsTable(self,pquery):
        ''' get households where selected personal characteristics from the interface are met'''
        self.database.open()
        ptable = self.database.execSelectQuery( pquery )
        self.database.close()
        return ptable

    def getHcharacteristicsTable(self,hquery):
        ''' get households where selected household characteristics from the interface are met'''
        self.database.open()
        htable = self.database.execSelectQuery( hquery )
        self.database.close()
        return htable
    
    def getFinalReportTableData(self, query):
        '''get reporttable where user has selected both household and personal characteristics as output criteria'''
        self.database.open()
        reporttable = self.database.execSelectQuery( query )
        self.database.close()
        return reporttable
    def getHouseholdsForReport(self):
        pass
        
