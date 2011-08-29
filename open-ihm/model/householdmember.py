#------------------------------------------------------------------------------------------------------------------------------------
# householdmember.py
# class corresponding to householdmember database entity
#------------------------------------------------------------------------------------------------------------------------------------
from datetime import date
from database import Database

class HouseholdMember:
     def __init__(self, pid, hhid, personid, yearofbirth="", headhousehold="",  sex="", education="", periodaway="", reason="", whereto=""):
         if (yearofbirth == "" ):
             if ( not self.getHouseholdMemberDetails(pid, hhid, personid) ):
                 self.pid = ""
                 self.hhid = ""
                 self.memberid = ""
                 return None
         else:
             self.setData(pid, hhid, personid, headhousehold, yearofbirth, sex, education, periodaway, reason, whereto)
            
     def getHouseholdMemberDetails(self, pid, hhid, memberid):
         database = Database()
         database.open()
         query = '''SELECT pid, hhid, personid, headofhousehold, yearofbirth, sex, education, periodaway, reason, whereto
                       FROM householdmembers WHERE hhid=%i and pid=%i and personid='%s' ''' % (hhid,  pid,  memberid)
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = row[0]
                 self.hhid = row[1]
                 self.memberid = row[2]
                 self.headofhousehold = row[3]
                 self.yearofbirth = row[4]
                 self.sex = row[5]
                 self.education = row[6]
                 self.periodaway = row[7]
                 self.reason = row[8]
                 self.whereto = row[9]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, personid, headofhousehold, yearofbirth, sex, education, periodaway, reason, whereto):
         database = Database()
         database.open()
        
         query = '''INSERT INTO householdmembers(pid, hhid, personid, headofhousehold, yearofbirth, sex, education, periodaway, reason, whereto) 
                     VALUES(%s,%s, '%s', '%s',%s,'%s','%s',%s,'%s','%s')''' % (pid, hhid, personid, headofhousehold, yearofbirth, sex, education, periodaway, reason, whereto)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         # update household attributes
         self.pid = pid
         self.hhid = hhid
         self.memberid = personid
         self.headofhousehold = headofhousehold
         self.yearofbirth = yearofbirth
         self.sex = sex
         self.education = education
         self.periodaway = periodaway
         self.reason = reason
         self.whereto = whereto
        
     def editData(self, personid,  headofhousehold, yearofbirth, sex, education, periodaway, reason, whereto):
         database = Database()
         database.open()
        
         query = '''UPDATE householdmembers
                     SET personid='%s', headofhousehold='%s', yearofbirth=%s, sex='%s', education='%s', periodaway=%s, reason='%s', whereto='%s'
                     WHERE pid=%s and hhid=%s and personid='%s' ''' 
                     
         query = query % (personid, headofhousehold, yearofbirth, sex, education, periodaway, reason, whereto,  self.pid,  self.hhid,  self.memberid)
       
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update household attributes
         self.headofhousehold = headofhousehold
         self.yearofbirth = yearofbirth
         self.sex = sex
         self.education = education
         self.periodaway = periodaway
         self.reason = reason
         self.whereto = whereto
         
     def updateIDfromAge(self):
         age = date.today().year - int( self.yearofbirth )
         
         if ( self.sex == "Male"):
             personid = "m%s" % age
         else:
             personid = "f%s" % age
             
         database = Database()
         database.open()
        
         query = '''UPDATE householdmembers
                     SET personid='%s' WHERE pid=%s and hhid=%s and personid='%s' '''  % (personid,  self.pid,  self.hhid,  self.memberid)
         
         # execute query
         database.execUpdateQuery( query )
         database.close()
         
         # update household attributes
         self.memberid = personid
        
     def getProjectID(self):
         return self.pid
        
     def getHouseholdID(self):
         return self.hhid
        
     def getPersonID(self):
         return self.memberid
