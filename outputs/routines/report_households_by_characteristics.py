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
            currentcolumn =  tablename + '.' + '%s' % coulumnname
            basequery = basequery + " and '%s' IS NOT NULL" % (currentcolumn)
        print basequery
        return basequery
        
    def buildHCharacteristicsQuery(self,hcharacteristics, tablename):
        ''' build query for selecting households that meet selected household characteristics from the report interface'''
        
        #settingsmanager = ReportsSettingsManager()
        houseid = tablename + '.hhid'
        
        basequery = '''SELECT households.hhid, households.householdname FROM households JOIN %s ON households.hhid = %s''' % (tablename,houseid)
        for coulumnname in hcharacteristics:
            currentcolumn =  tablename + '.' + '%s' % coulumnname
            basequery = basequery + " and '%s' IS NOT NULL" % (currentcolumn)
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
        
