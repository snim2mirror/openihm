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

class EditStandardOfLivingModelPrice:
    def __init__(self, modelprice, item,pid):
        self.database = Database() 
        self.item = item
        self.modelprice = modelprice
        self.projectid = pid
        
        if ( self.item == "") or ( self.modelprice == ""):
            return None
        else:
            self.setData()

    def setData(self):
        self.database.open()
	query = '''UPDATE standardofliving SET modelprice=%s WHERE summary='%s' AND pid=%s''' % (self.modelprice, self.item, self.projectid)

        # execute query
        self.database.execUpdateQuery( query )
        self.database.close()

    #def deleteData(self):

 
