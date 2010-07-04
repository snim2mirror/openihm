#-------------------------------------------------------------------	
#	Filename: project.py
#-------------------------------------------------------------------

from database import Database
from household import Household
from projecthouseholdcharacteristic import ProjectHouseholdCharacteristic
from projectpersoncharacteristic import ProjectPersonCharacteristic

class Project:
    def __init__(self, pid=0, projectname="", startdate="", enddate="", description="", currency=""):
        self.database = Database() 
        if ( pid != 0 ):
            if ( not self.getProjectDetails( pid ) ):
                return None
        else:
            self.addProject(projectname, startdate, enddate, description, currency)
            
    def getProjectDetails(self,  pid):
        self.database.open()
        query = "SELECT pid, projectname, startdate, enddate, description, currency FROM projects WHERE pid=%i " % (pid)
        rows = self.database.execSelectQuery( query )
        self.database.close()
        num = len(rows)
        if (num != 0):
            exists = True
            for row in rows:
                self.pid = row[0]
                self.projectname = row[1]
                self.startdate = row[2]
                self.enddate = row[3]
                self.description = row[4]
                self.currency = row[5]
        else:
            exists = False
        self.database.close()
        return exists
        
    def addProject(self, projectname, startdate, enddate, description, currency):
        # create INSERT INTO query
        query = '''INSERT INTO projects(projectname,startdate,enddate,description,currency) 
                     VALUES('%s','%s', '%s', '%s', '%s')''' % (projectname, startdate, enddate, description, currency)
        
        # execute query and commit changes
        self.database.open()
        self.database.execUpdateQuery( query )
        
        # get the ID of the newly inserted project
        query = "SELECT LAST_INSERT_ID()"
        rows = self.database.execSelectQuery( query )
        for row in rows:
            projectid = row[0]
            
        # create project specific tables (e.g. householdcharacteristics & personalcharacteristics)
        HouseholdCharacteristicsTableName 	= '''p%iHouseholdCharacteristics''' % (projectid)
        PersonalCharactericticsTableName	= '''p%iPersonalCharacteristics''' % (projectid)
        
        queryCreate = '''CREATE  TABLE IF NOT EXISTS `openihmdb`.`%s` 
                        (
                            `hhid` INT NOT NULL ,
                            PRIMARY KEY (`hhid`) ,
                            INDEX `fk_p%i_householdcharacteristics_households` (`hhid` ASC) ,
                            CONSTRAINT `fk_p%i_householdcharacteristics_households`
                            FOREIGN KEY (`hhid` )
                            REFERENCES `openihmdb`.`households` (`hhid` )
                            ON DELETE CASCADE
                            ON UPDATE CASCADE)
                        ENGINE = InnoDB;''' % (HouseholdCharacteristicsTableName, projectid, projectid)
                        
        self.database.execDefinitionQuery( queryCreate )
        
        queryCreate = '''CREATE  TABLE IF NOT EXISTS `openihmdb`.`%s` (
                          `hhid` INT NOT NULL ,
                          `personid` VARCHAR(20) NOT NULL ,
                          PRIMARY KEY (`personid`, `hhid`) ,
                          INDEX `fk_p%i_personalcharacteristics_householdmembers` (`personid` ASC, `hhid` ASC) ,
                          CONSTRAINT `fk_p%i_personalcharacteristics_householdmembers`
                            FOREIGN KEY (`personid` , `hhid` )
                            REFERENCES `openihmdb`.`householdmembers` (`personid` , `hhid` )
                            ON DELETE CASCADE
                            ON UPDATE CASCADE)
                        ENGINE = InnoDB;''' % (PersonalCharactericticsTableName, projectid, projectid)
        
        self.database.execDefinitionQuery( queryCreate )
        self.database.close()
        
        # set project attributes to saved values
        self.pid = projectid
        self.projectname = projectname
        self.startdate = startdate
        self.enddate = enddate
        self.description = description
        self.currency = currency
        
    def getProjectID(self):
        return self.pid
    
    def getProjectName(self):
        return self.projectname
        
    def getStartDate(self):
        return self.startdate
    
    def getEndDate(self):
        return self.enddate
        
    def getDescription(self):
        return self.description
        
    def getCurrency(self):
        return self.currency
        
    def setData(self, projectname, startdate, enddate, description, currency):
        # create UPDATE query to update project
        query = '''UPDATE projects SET projectname='%s', startdate = '%s',enddate = '%s',description = '%s',currency = '%s'
                     WHERE pid=%i''' % (projectname, startdate, enddate, description, currency, self.pid)
    
        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
        
        # set project attributes to saved values
        self.projectname = projectname
        self.startdate = startdate
        self.enddate = enddate
        self.description = description
        self.currency = currency
        
    #-------------------------------------------------------------------------------------------------------
    #  Project Household Characteristics
    #-------------------------------------------------------------------------------------------------------
        
    def addHouseholdCharacteristic(self, char, datatype):
        char = ProjectHouseholdCharacteristic( self.pid,  char, datatype )
            
    def removeHouseholdCharacteristic(self, char):
         #get target table
        tbl = '''p%iHouseholdCharacteristics''' % (self.pid)
        #delete the characteristic field
        self.database.open()
            
        queryAlter = '''ALTER TABLE `%s` DROP `%s` ''' % (tbl, char)
        
        self.database.execDefinitionQuery(queryAlter)
        self.database.close()
        
    def getHouseholdCharacteristics(self):
        #get target table
        tbl = '''p%iHouseholdCharacteristics''' % (self.pid)
        
        query = '''SHOW COLUMNS FROM %s ''' % (tbl)
        
        self.database.open()
        rows = self.database.execSelectQuery(query)
        self.database.close()
        
        chars = []
        for row in rows:
            if "hhid" != row[0]:
                char = ProjectHouseholdCharacteristic( self.pid,  row[0] )
                chars.append( char )
                
        return chars
        
    #-------------------------------------------------------------------------------------------------------
    #  Project Person Characteristics
    #-------------------------------------------------------------------------------------------------------
        
    def addPersonCharacteristic(self, char, datatype):
        char = ProjectPersonCharacteristic( self.pid,  char, datatype )
            
    def removePersonCharacteristic(self, char):
         #get target table
        tbl = '''p%iPersonalCharacteristics''' % (self.pid)
        #delete the characteristic field
        self.database.open()
            
        queryAlter = '''ALTER TABLE `%s` DROP `%s` ''' % (tbl, char)
        
        self.database.execDefinitionQuery(queryAlter)
        self.database.close()
        
    def getPersonCharacteristics(self):
        #get target table
        tbl = '''p%iPersonalCharacteristics''' % (self.pid)
        
        query = '''SHOW COLUMNS FROM %s ''' % (tbl)
        
        self.database.open()
        rows = self.database.execSelectQuery(query)
        self.database.close()
        
        chars = []
        for row in rows:
            if "hhid" != row[0] and "personid" != row[0]:
                char = ProjectPersonCharacteristic( self.pid,  row[0] )
                chars.append( char )
                
        return chars
        
    #-------------------------------------------------------------------------------------------------------
    #  Project Households
    #-------------------------------------------------------------------------------------------------------
        
    def getHousehold(self,  hhid):
        household = Household( self.pid,  hhid )
        return household
        
    def addHousehold(self, hhid, householdname, dateofcollection):
        household = Household( self.pid,  hhid,  householdname, dateofcollection )
            
    def editHousehold(self, hhid, newhhid,  householdname, dateofcollection):
        household = Household( self.pid,  hhid )
        household.setData( householdname, dateofcollection,  newhhid )
        
    def delHousehold(self,  hhid):
        query = "DELETE FROM households WHERE pid=%s AND hhid=%s " % ( self.pid, hhid )
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()
        
    def getHouseholds(self):
        query = '''SELECT hhid FROM households WHERE pid=%s ''' % (self.pid)
        
        self.database.open()
        rows = self.database.execSelectQuery(query)
        self.database.close()
        
        households = []
        for row in rows:
            household = Household( self.pid,  row[0] )
            households.append( household )
                
        return households
        

