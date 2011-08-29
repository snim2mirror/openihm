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


from data.config import Config
import includes.mysql.connector as connector

class GenericDBOP:
	def __init__(self,query):
		# connect to mysql database
		self.config = Config.dbinfo().copy()        	
		self.db = connector.Connect(**self.config)
        	self.cursor = self.db.cursor()		
		self.sqlquery = query
	
	def getdata(self):
		self.cursor.execute(self.sqlquery) 
		return self.cursor.fetchall()

        def runSelectQuery(self):	
        	#connect to mysql database
        	db = connector.Connect(**self.config)
        	cursor = db.cursor()
		
		cursor.execute(self.sqlquery)
		recset = cursor.fetchall()

		# close database connection
        	cursor.close()
        	db.close()

		return recset
	
	def runUpdateQuery(self):	
        	#connect to mysql database
        	db = connector.Connect(**self.config)
        	cursor = db.cursor()
        	
		# execute query and commit changes
		cursor.execute(self.sqlquery)
        	db.commit()
		
		# close database connection
        	cursor.close()
        	db.close()
