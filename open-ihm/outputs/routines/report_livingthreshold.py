from data.database import Database
from report_adultequivalent import AdultEquivalent
from data.report_settingsmanager import ReportsSettingsManager
from report_disposable_income import DisposableHouseholdIncome


class LivingThreshhold:

    def getDisposableIncome(self,reporttype,projectid,houseids):
        '''Get Disposable income for selected households'''
        connector = DisposableHouseholdIncome()
        householdDI =householdDisposableIncome(reporttype,projectid,householdIDs)
        return householdDI
    
    def getHouseholdExpenditure(self,projectid,hhid):
        '''Calculate total household expenditure'''
        
        query = '''SELECT SUM(priceperunit * totalunits) AS houseexpenditure FROM expenditure WHERE pid=%s AND hhid=%s'''
        dbconnector = Database()
        dbconnector.open()
        recordset = dbconnector.execSelectQuery(query)
        dbconnector.close()
        hhExpenditure = 0
        for row in recordset:
            hhExpenditure = row[0]

        return hhExpenditure
    
    def determineLThresholdPosition(self,reporttype,projectid,houseids):
        
        householdDI = self.getDisposableIncome(reporttype,projectid,houseids)
        reporttable = []
        for household in householdDI:
            templist = []
            hhid = household[0]
            templist.append(hhid)
            hhExpenditure = self.getHouseholdExpenditure(projectid,hhid)
            livingThreshold = household[0] - hhExpenditure
            templist.append(livingThreshold)
            reporttable.append(tuple(templist))
        return reporttable
            
            
        
