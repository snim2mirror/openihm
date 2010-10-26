#-------------------------------------------------------------------	
#	Filename: report_settingsmanager.py
#-------------------------------------------------------------------

from database import Database

class ReportsSettingsManager:
    def __init__(self):
        self.database = Database()

    def getProjectNames(self):
        query = ''' select projectname from projects'''
        self.database.open()
        rows = self.database.execSelectQuery( query )
        self.database.close()
        return rows

    def getSelectedProjectID(self,projectname):
        if (projectname != ""):
            query = '''SELECT pid FROM projects WHERE projectname ='%s' ''' % (projectname)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
            pid = 0

            for row in rows:
                pid = row[0]
            return pid
            
    def getHouseholdCharacteristics(self,projectid):
        rows =[]
        
        if projectid != 0: 
            tablename = self.setHCharacteristicsTableName(projectid)
            query = '''SELECT column_name FROM information_schema.columns WHERE table_name='%s' ''' % (tablename)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getPersonalCharacteristics(self,projectid):
        
        rows =[]
        if projectid != 0:
            
            tablename = self.setPCharacteristicsTableName(projectid)
            query = '''SELECT column_name FROM information_schema.columns WHERE table_name='%s' ''' % (tablename)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows
       
        
    def buildReportQuery(self,projectid):
        
        rows =[]
        if projectid != 0:
            tablename = 'p' + '%s' %(projectid) + 'personalcharacteristics'
            query = '''SELECT column_name FROM information_schema.columns WHERE table_name='%s' ''' % (tablename)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows
       
    def setPCharacteristicsTableName(self, projectid):
        tablename = 'p' + '%s' %(projectid) + 'personalcharacteristics'
        return tablename
         
    def setHCharacteristicsTableName(self, projectid):
        tablename = 'p' + '%s' %(projectid) + 'householdcharacteristics'
        return tablename

    def getProjectHouseholds(self, projectid):
        rows =[]
        if projectid != 0:
            query = '''SELECT householdname FROM households WHERE pid='%s' ''' % (projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getCropIncomeSources(self,projectid):
        rows =[]
        if projectid != 0:
            query = ''' SELECT DISTINCT incomesource FROM cropincome WHERE pid='%s' ''' %(projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getEmploymentIncomeSources(self,projectid):
        rows =[]
        if projectid != 0:
            query = ''' SELECT DISTINCT incomesource FROM employmentincome WHERE pid='%s' ''' %(projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getLivestockIncomeSources(self,projectid):
        rows =[]
        if projectid != 0:
            query = ''' SELECT DISTINCT incomesource FROM livestockincome WHERE pid='%s' ''' %(projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getWildfoodsIncomeSources(self,projectid):
        rows =[]
        if projectid != 0:
            query = ''' SELECT DISTINCT incomesource FROM wildfoods WHERE pid='%s' ''' %(projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getTransferIncomeSources(self,projectid):
        rows =[]
        if projectid != 0:
            query = ''' SELECT DISTINCT assistancetype FROM transfers WHERE pid='%s' ''' %(projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows

    def getLoanIncomeSources(self,projectid):
        rows =[]
        if projectid != 0:
            query = ''' SELECT DISTINCT creditsource FROM creditandloans WHERE pid='%s' ''' %(projectid)
            self.database.open()
            rows = self.database.execSelectQuery( query )
            self.database.close()
        return rows
