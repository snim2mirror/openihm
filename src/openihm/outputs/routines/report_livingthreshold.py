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
from report_disposable_income import DisposableHouseholdIncome
from datetime import date


class LivingThreshhold:

    def getDisposableIncome(self,reporttype,projectid,houseids):
        '''Get Disposable income for selected households'''
        connector = DisposableHouseholdIncome()
        householdDI = connector.householdDisposableIncome(reporttype,projectid,houseids)
        return householdDI

    def executeSelectQuery(self,query):
        '''Run Select Query'''
        dbconnector = Database()
        dbconnector.open()
        recset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        return recset
    
    def determineLThresholdPosition(self,reporttype,projectid,houseids):
        '''Check whether a household is above or below the living threshold for a particular project'''
        
        
        householdDI = self.getDisposableIncome(reporttype,projectid,houseids)
        reporttype = 'raw DI' #get raw DI for determining SOLT position
        rawhouseholdDI = self.getDisposableIncome(reporttype,projectid,houseids)
        reporttable = []
        
        for household in householdDI:
            temphouseid= []
            positionmarker = 0
            templist = []
            hhid = household[0]
            templist.append(hhid)
            hholdDi = household[1]
            templist.append(hholdDi)
            hhCosts = self.getHouseholdExpenditure(projectid,hhid)
            temphouseid.append(hhid)
            
            rawhouseholdDI = self.getDisposableIncome(reporttype,projectid,temphouseid)
            rawDI = rawhouseholdDI[0][1]
            #print 'hhid ', hhid,' expenditure ',hhCosts, ' nyumba ', rawhouseholdDI[0][0],' raw ',rawDI
            #if (float(household[1]) - hhCosts)< 0:
            if (float(rawDI) - hhCosts)< 0:
                positionmarker = -1 #this is a marker just to indicate hholds below STOL, when producing output
            templist.append(positionmarker)
            reporttable.append(tuple(templist))
        return reporttable
            
    def getHouseholdExpenditure(self,projectid,hhid):
        '''Calculate total household expenditure'''
        
        query = '''SELECT scope,gender, agebottom,agetop,costperyear FROM standardofliving WHERE pid=%s''' %(projectid)
        stolList = self.executeSelectQuery(query)

        householdcosts=0

        for item in stolList:
            scope =  item[0]
            itemcost = item[4]
	
            if scope=='Household':
		householdcosts = householdcosts + itemcost
		
            else:
		gender = item[1]
		currentyear = date.today().year 
		startyear = currentyear - item[3]
		endyear = currentyear - item[2]
		countvalue = 0
		
		if gender=='All':
		    query ='''SELECT COUNT(*) FROM householdmembers WHERE pid=%s AND hhid=%s AND yearofbirth BETWEEN %s  AND %s''' % (projectid,hhid,startyear,endyear)
		    temprecset = self.executeSelectQuery(query)
		    for row in temprecset:
			countvalue = row[0]

		elif gender=='Female':
		    query ='''SELECT COUNT(*) FROM householdmembers WHERE pid=%s AND hhid=%s AND sex='Female' AND yearofbirth BETWEEN %s  AND %s''' % (projectid,hhid,startyear,endyear)
		    temprecset = self.executeSelectQuery(query)
		    for row in temprecset:
			countvalue = row[0]
		
		elif gender=='Male':
                    
		    query ='''SELECT COUNT(*) FROM householdmembers WHERE pid=%s AND hhid=%s AND sex='Male' AND yearofbirth BETWEEN %s  AND %s''' % (projectid,hhid,startyear,endyear)
		    temprecset = self.executeSelectQuery(query)
		    for row in temprecset:
			countvalue = row[0]
		
		householdcosts = householdcosts + (itemcost * countvalue )
        return householdcosts
            
        
