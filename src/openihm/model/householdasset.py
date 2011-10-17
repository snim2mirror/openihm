#------------------------------------------------------------------------------------------------------------------------------
# householdasset.py
# class corresponding to household asset entity
#-----------------------------------------------------------------------------------------------------------------------------

from datetime import date
from database import Database

class HouseholdAsset:
     def __init__(self, assetid=0, pid="", hhid="",  category="", assettype="", unitofmeasure="", costperunit="", numunits=""):
         if (assetid != 0 ):
             if ( not self.getAssetDetails(pid, hhid, assetid) ):
                 self.pid = ""
                 self.hhid = ""
                 self.assetid = ""
                 return None
         else:
             self.setData(pid, hhid, category,  assettype, unitofmeasure, costperunit, numunits)
            
     def getAssetDetails(self, pid, hhid, assetid):
         database = Database()
         database.open()
         query = '''SELECT assetid, assetcategory, assettype, unitofmeasure, unitcost, totalunits 
                       FROM assets WHERE hhid=%s AND pid=%s AND assetid=%s ''' % ( hhid, pid,  assetid )
                     
         rows = database.execSelectQuery( query )
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                 self.pid = pid
                 self.hhid = hhid
                 self.assetid = assetid
                 self.category = row[1]
                 self.assettype = row[2]
                 self.unitofmeasure = row[3]
                 self.costperunit = row[4]
                 self.numunits = row[5]
                 
         else:
             exists = False
         database.close()
         return exists
        
     def setData(self, pid, hhid, category,  assettype, unitofmeasure, costperunit, numunits):
         database = Database()
         database.open()
        
         query = '''INSERT INTO assets (hhid, assetcategory, assettype, unitofmeasure, unitcost, totalunits, pid )
                 VALUES(%s,'%s','%s','%s',%s,%s,%s) ''' % ( hhid, category,  assettype, unitofmeasure, costperunit, numunits, pid )
       
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
