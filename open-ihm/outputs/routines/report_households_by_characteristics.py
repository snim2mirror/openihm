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
        
        #settingsmanager = ReportsSettingsManager()
        houseid = tablename + '.hhid'
        
        basequery = '''SELECT households.hhid, households.householdname FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
        for coulumnname in pcharacteristics:
            currentcolumn =  tablename + '.' + coulumnname
            basequery = basequery + ' and %s IS NOT NULL' % (currentcolumn)
        print basequery
        return basequery
        
    def buildHCharacteristicsQuery(self,hcharacteristics, tablename):
        ''' build query for selecting households that meet selected household characteristics from the report interface'''
        
        #settingsmanager = ReportsSettingsManager()
        houseid = tablename + '.hhid'
        
        basequery = '''SELECT households.hhid, households.householdname FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
        for coulumnname in hcharacteristics:
            currentcolumn =  tablename + '.' + coulumnname
            basequery = basequery + ' and %s IS NOT NULL' % (currentcolumn)
        print basequery
        return basequery

    def getReportTable(self,projectid,pquery,hquery):
        ''' generate report tables'''
        
        pcharstable =self.getPcharacteristicsTable(pquery)
        hcharstable = self.getHcharacteristicsTable(hquery)
        x = len(pcharstable)
        y = len(hcharstable)

        #if x != 0 and y !=0: this line has been commented out bcoz the interface currently provides no way to add pchars so the pcharstable is always empty
        #if y !=0:
        #query = '''SELECT households.hhid, households.householdname FROM households WHERE households.hhid IN (%s) ''' % htuple
        query = ''' SELECT * FROM (%s UNION ALL %s) AS tbl GROUP BY tbl.hhid HAVING COUNT(*) = 2''' % (pquery,hquery)
        #query = ''' %s  UNION %s''' % (pquery,hquery)
        print query
        self.database.open()
        reporttable = self.database.execSelectQuery( query )
        
        self.database.close()
        #else: reporttable = []
        print reporttable
        return reporttable

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
    
        
