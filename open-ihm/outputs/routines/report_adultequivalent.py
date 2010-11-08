#-------------------------------------------------------------------	
#	Filename: report_adultequivalent.py
#-------------------------------------------------------------------
import data.mysql.connector
from data.config import Config
from data.database import Database

class AdultEquivalent:

    def getHouseholdMembers (self,hhid,pid):
        query = '''SELECT personid, dateofbirth, sex FROM householdmembers WHERE hhid=%s AND pid=%s''' %(hhid,pid)
        memberstable= self.fireQuery(query)
        return memberstable

    def calculateHouseholdEnergyReq(self,hid,pid):
        '''Calculate a household's energy requirements by age and sex, for the current year'''
        
        householdenergyreq = 0
        today = datetime.date.today()
        currentyear = today.year
        memberlist = self.getHouseholdMembers(hid,pid)
        for member in memberlist:
            currentage = currentyear - memberlist[1]
            gender = memberlist[2]
            energyreq = self.calculateEnergyReqByAgeSex(currentage,gender)

            # adjust member's yearly energy requirement according to absence from household
            adjustedenergyreq = self.adjustMemberEnergyReq(memberid,hid,pid,energyreq)

        householdenergyreq = householdenergyreq + adjustedenergyreq
        return householdenergyreq

    def calculateEnergyReqByAgeSex(self,age,gender):
        '''Return energy requirement by age and sex'''
        
        energyreq = 0
        if gender=='Male':
            query = '''SELECT kCalNeedM WHERE age =%s''' %(age)
            resulttable = self.fireQuery(query)
            for row in resulttable:
		energyreq = row[0]
        elif gender=='Female':
            query = '''SELECT kCalNeedF WHERE age =%s''' %(age)
            resulttable = self.fireQuery(query)
            for row in resulttable:
		energyreq = row[0]

        return energyreq

    def fireQuery(self,query):
        '''Execute queries under adult equivalent calculations '''
        databaseConnector = Database()
        databaseConnector.open()
        result = databaseConnector.execSelectQuery( query )
        databaseConnector.close()
        return result
        
    def adjustMemberEnergyReq(self,memberid,hid,pid,energyreq):
        '''Adjust member's yearly energy requirement according to absence from household'''
        absence = 0
        adjustedenergyreq = energyreq
        absencequery = '''SELECT percentageaway FROM absencefromhousehold WHERE hhid=%s AND pid =%s AND personid=%s''' % (memberid,hid,pid)
        resulttable = self.fireQuery(query)
        for row in resulttable:
	    absence = row[0]

        if absence >= 25 and absence < 50:
            adjustedenergyreq = adjustedenergyreq * 0.75

        elif absence >= 50 and absence < 75:
            adjustedenergyreq = adjustedenergyreq * 0.5
        elif absence >= 75 and absence < 100:
            adjustedenergyreq = adjustedenergyreq * 0.25
        elif absence >= 100:
            adjustedenergyreq =0
        return adjustedenergyreq
