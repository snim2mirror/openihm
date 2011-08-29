#-------------------------------------------------------------------	
#	Filename: household.py
#-------------------------------------------------------------------

from database import Database
from householdmember_manager import HouseholdMemberManager

class Household(HouseholdMemberManager):
    def __init__(self, pid, hhid=0, householdname="", dateofcollection=""):
        self.database = Database() 
        self.pid = pid
        self.hhid = hhid
        if ( householdname == "" and dateofcollection== "" ):
            if ( not self.getHouseholdDetails() ):
                return None
        else:
            self.setData(householdname,  dateofcollection)
            
    def getHouseholdDetails(self):
        self.database.open()
        query = "SELECT householdname, dateofcollection FROM households WHERE pid=%s AND hhid=%s " % ( self.pid,  self.hhid )
        rows = self.database.execSelectQuery( query )
        num = len(rows)
        if (num != 0):
            exists = True
            for row in rows:
                self.householdname = row[0]
                self.dateofcollection = row[1]
        else:
            exists = False
        self.database.close()
        return exists
        
    def setData(self, householdname,  dateofcollection,  newhhid=""):
        self.database.open()
        # create query to update or insert new household
        if ( newhhid == "" ):  # newhhid defaults to "" when inserting a new household
            query = '''INSERT INTO households(hhid,pid,dateofcollection,householdname) 
                     VALUES(%s,%s, '%s', '%s')''' % (self.hhid, self.pid, dateofcollection, householdname)
        else:                       
            query = '''UPDATE households SET hhid=%s, dateofcollection='%s', householdname='%s'
                     WHERE hhid=%s AND pid=%s''' % (newhhid, dateofcollection, householdname,  self.hhid,  self.pid)
            self.hhid = newhhid
            
        # execute query
        self.database.execUpdateQuery( query )
        self.database.close()
        # update household attributes
        self.householdname = householdname
        self.dateofcollection = dateofcollection
        
    def getProjectID(self):
        return self.pid
        
    def getHouseholdID(self):
        return self.hhid
        
    def getHouseholdName(self):
        return self.householdname
        
    def getDateOfCollection(self):
        return self.dateofcollection

