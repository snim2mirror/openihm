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

from PyQt4 import QtGui

class HouseholdIncomeQuery:
    def __init__(self):
        self.query = ''

    def buildFinalReportQuery (self,projectid,householdIDs,cropsQuery,employmentQuery,livestockQuery,loansQuery,transfersQuery,wildfoodsQuery):
        
        householdids = ','.join(householdIDs)
        temphouseidsortorder = ['hhid']
        for i in range (0, len(householdIDs)):
                    temphouseidsortorder.append(householdIDs[i])
        householdidsorder = ','.join(temphouseidsortorder)
                        
        if len(householdIDs)!=0:
            
            if cropsQuery !='' or employmentQuery!='' or livestockQuery !='' or loansQuery !='' or transfersQuery !='' or wildfoodsQuery !='':
                self.query  = '''SELECT hhid from households WHERE hhid IN (%s) and pid =%s ORDER BY FIELD (%s) ''' % (householdids,projectid,householdidsorder)
                if cropsQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,cropsQuery)
                if employmentQuery!='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,employmentQuery)
                if livestockQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,livestockQuery)
                #if loansQuery !='':
                #self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,loansQuery)
                if transfersQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,transfersQuery)
                if wildfoodsQuery !='':
                    self.query  = '''SELECT * FROM ((%s) table1 LEFT JOIN (%s) table2 USING (hhid) )''' % (self.query,wildfoodsQuery)
            else:
                QtGui.QMessageBox.information(None,"Households By Income Source","No Income sources Selected")
        return self.query 
