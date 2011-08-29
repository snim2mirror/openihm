#---------------------------------------------------------------------------------------------------------------------------------------------------
# householdmembermanager.py
# inherited by household for adding, editing and deleting household members 
#---------------------------------------------------------------------------------------------------------------------------------------------------

from database import Database
from householdmember import HouseholdMember

class HouseholdMemberManager:
     '''
         Manages household members - inherited by Household. Allows adding, editing, deleting and retrieval of household members.
     '''   
     def existsMember(self, personid):
         member = self.getMember(personid)
         if member.memberid == "":
             return False
         else:
             return True
             
     def getMember(self,  personid):
         member = HouseholdMember(self.pid,  self.hhid,  personid)
         return member
        
     def addMember(self,  personid, yearofbirth, headhousehold,  sex, education, periodaway, reason, whereto ):
         num = 1
         # take care of twins
         oldpersonid = personid
         while self.existsMember(personid):
             personid = oldpersonid +"_%i" % num
             num = num + 1
             
         member = HouseholdMember(self.pid,  self.hhid,  personid, yearofbirth, headhousehold,  sex, education, periodaway, reason, whereto )
         return member
        
     def delMember(self,  personid):
         query = "DELETE FROM householdmembers WHERE pid=%s AND hhid=%s AND personid='%s' " % ( self.pid,  self.hhid,  personid )
         database = Database()
         database.open()
         database.execUpdateQuery( query )
         database.close()
        
     def getMembers(self):        
         query = "SELECT personid FROM householdmembers WHERE pid=%s AND hhid=%s" % ( self.pid,  self.hhid )
         database = Database()
         database.open()
         rows =database.execSelectQuery( query )
         database.close()
         members = []
        
         for row in rows:
             id = row[0]
             member = HouseholdMember(id)
             members.append( member )
            
         return members
