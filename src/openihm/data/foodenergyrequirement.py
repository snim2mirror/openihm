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

class FoodEnergyRequirement:
    def __init__(self, age, malesenergyrequirement, femalesenergyrequirement):
        self.database = Database() 
        self.age = age
        self.malesenergyrequirement = malesenergyrequirement
        self.femalesenergyrequirement = femalesenergyrequirement
        if ( age == ""):
            return None
        else:
            self.setData()

    def setData(self):
        self.database.open()

	# check if record exists
	query = '''SELECT age, kCalNeedM, kCalNeedF FROM lookup_energy_needs WHERE age='%s' ''' % (self.age)    
		
#	p = GenericDBOP(query)
#        recordset = p.runSelectQuery()
        recordset = self.database.execSelectQuery( query )

	numrows = 0

	for row in recordset:
		numrows = numrows + 1
				      	
	if numrows == 0:
			
		query = '''INSERT INTO lookup_energy_needs(age, kCalNeedM, kCalNeedF) 
                    		VALUES(%s,%s,%s)''' % (self.age, self.malesenergyrequirement, self.femalesenergyrequirement)
	else:
		query = '''UPDATE lookup_energy_needs SET age='%s', kCalNeedM=%s, kCalNeedF='%s'
                     		WHERE age='%s' ''' % (self.age, self.malesenergyrequirement, self.femalesenergyrequirement, self.age)

        # execute query
        self.database.execUpdateQuery( query )
        self.database.close()

    #def deleteData(self):

 
