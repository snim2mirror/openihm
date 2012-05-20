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
    def __init__(self, incomesource,mpercentageincome, projectid):
        self.database = Database()
        self.incomesource = incomesource
        self.percentageincome = mpercentageincome
        self.projectid = projectid
        
        if ( self.incomesource == "") or ( self.percentageincome == ""):
            return None
        else:
            self.setData()

    def setData(self):
        query = '''UPDATE employmentincome SET preferenceincome=%s
                        WHERE incomesource='%s' AND pid=%s''' % (self.percentageincome, self.incomesource, self.projectid)

        # execute query
        self.database.open()
        self.database.execUpdateQuery( query )
        self.database.close()

    #def deleteData(self):

 
