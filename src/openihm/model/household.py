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


from database import Database
from householdmember_manager import HouseholdMemberManager
from householdasset_manager import HouseholdAssetManager
from householdincome_crop_manager import HouseholdCropIncomeManager

class Household(HouseholdMemberManager, HouseholdAssetManager, HouseholdCropIncomeManager):
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

