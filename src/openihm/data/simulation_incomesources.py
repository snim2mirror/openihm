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

class EditIncomeSourcesModelPrice:
    def __init__(self, incomesourcecategory,incomesource,mpercentageprice, mpercentageproduction, projectid):
        self.database = Database()
        self.incomesourcecategory = incomesourcecategory
        self.incomesource = incomesource
        self.percentageprice = mpercentageprice
        self.percentageproduction = mpercentageproduction
        self.projectid = projectid
        
        if ( self.incomesource == "") or ( self.percentageprice == "")or ( self.percentageproduction == ""):
            return None
        else:
            self.setData()

    def setData(self):
        if self.incomesourcecategory =='Crops':
            incomesourcetable ='cropincome'
        elif (self.incomesourcecategory =='Formal Transfers') or (self.incomesourcecategory =='Informal Tansfers'):
            incomesourcetable ='transfers'
        elif self.incomesourcecategory =='Livestock':
            incomesourcetable ='livestockincome'
        elif self.incomesourcecategory =='WildFoods':
            incomesourcetable ='wildfoods'
            
        if incomesourcetable == 'cropincome' or incomesourcetable == 'livestockincome' or incomesourcetable == 'wildfoods':
            query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction=%s
                            WHERE incomesource='%s' AND pid=%s''' % (incomesourcetable,self.percentageprice, self.percentageproduction,self.incomesource, self.projectid)
        elif incomesourcetable == 'transfers':
            if self.incomesourcecategory =='Informal Tansfers':
                query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction=%s
                            WHERE sourceoftransfer='%s' AND sourcetype='Internal' AND pid=%s''' % (incomesourcetable,self.percentageprice, self.percentageproduction,self.incomesource, self.projectid)
            elif self.incomesourcecategory =='Formal Transfers':
                query = '''UPDATE %s SET preferenceprice=%s, preferenceproduction=%s
                            WHERE sourceoftransfer='%s' AND sourcetype='External' AND pid=%s''' % (incomesourcetable,self.percentageprice, self.percentageproduction,self.incomesource, self.projectid)

        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()

    #def deleteData(self):

 
