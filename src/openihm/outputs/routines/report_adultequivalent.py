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

import includes.mysql.connector as connector # FIXME: Do we need this?
from data.config import Config
from data.database import Database
import datetime

class AdultEquivalent:

    def getHouseholdMembers (self,hhid,pid):
        query = '''SELECT personid, yearofbirth, sex, periodaway FROM householdmembers WHERE hhid=%s AND pid=%s''' %(hhid,pid)
        memberstable= self.executeQuery(query)
        return memberstable

    def calculateHouseholdEnergyReq(self,hid,pid):
        '''Calculate a household's energy requirements by age and sex, for the current year'''
        
        householdenergyreq = 0

        today = datetime.date.today()
        currentyear = today.year
        memberlist = self.getHouseholdMembers(hid,pid)
        for member in memberlist:
            currentage = currentyear - member[1]
            gender = member[2]
            periodaway = member[3]
            energyreq = self.calculateEnergyReqByAgeSex(currentage,gender)

            # adjust member's yearly energy requirement according to absence from household
            adjustedenergyreq = self.adjustMemberEnergyReq(energyreq,periodaway)
            householdenergyreq = householdenergyreq + adjustedenergyreq
        return householdenergyreq

    def calculateEnergyReqByAgeSex(self,age,gender):
        '''Return energy requirement by age and sex'''
        
        energyreq = 0
        if gender=='Male':
            query = '''SELECT kCalNeedM FROM lookup_energy_needs WHERE age =%s''' %(age)
            resulttable = self.executeQuery(query)
            for row in resulttable:
		energyreq = row[0] *365
		
        elif gender=='Female':
            query = '''SELECT kCalNeedF FROM lookup_energy_needs WHERE age =%s''' %(age)
            resulttable = self.executeQuery(query)
            for row in resulttable:
		energyreq = row[0] * 365

        return energyreq

    def executeQuery(self,query):
        '''Execute queries under adult equivalent calculations '''
        databaseConnector = Database()
        databaseConnector.open()
        result = databaseConnector.execSelectQuery( query )
        databaseConnector.close()
        return result
        
    def adjustMemberEnergyReq(self,energyreq,periodaway):
        '''Adjust member's yearly energy requirement according to absence from household'''
        absence = periodaway
        adjustedenergyreq = energyreq
        if absence <> 0:
            adjustedenergyreq = adjustedenergyreq - (adjustedenergyreq *(absence/12))
        return adjustedenergyreq

    def calculateAdultEnergyEquivalent(self):
        '''Calculate avarage daily food need for adults'''
        energyreqAdultMale = self.getEnergyReqAdultMale()
        energyreqAdultFemale = self.getEnergyReqAdultFemale()
        averageAdultRequirement = (energyreqAdultMale + energyreqAdultFemale)/2
        adultRequirement = averageAdultRequirement * 365
        return adultRequirement
        
    def getEnergyReqAdultMale(self):
        query = '''SELECT kCalNeedM FROM lookup_energy_needs WHERE age =25 ''' 
        resulttable = self.executeQuery(query)
        for row in resulttable:
	    energyreq = row[0]
	return energyreq

    def getEnergyReqAdultFemale(self):
        query = '''SELECT kCalNeedF FROM lookup_energy_needs WHERE age =25 ''' 
        resulttable = self.executeQuery(query)
        for row in resulttable:
	    energyreq = row[0]
	return energyreq
    
    def caclulateHouseholdAE(self,householdenergyreq):
        adultRequirement = self.calculateAdultEnergyEquivalent()
        adultEquivalent = round((float(householdenergyreq) / adultRequirement ),2)
        return adultEquivalent

	    
