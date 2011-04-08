#-------------------------------------------------------------------	
#	Filename: report_adultequivalent.py
#-------------------------------------------------------------------
import data.mysql.connector
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
