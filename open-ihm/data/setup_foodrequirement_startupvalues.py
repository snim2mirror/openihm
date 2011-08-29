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

from data.database import Database

class FoodRequirementValues:
    def __init__(self):
        self.query =''

    def insertSartUpValues(self):
        '''Insert food energy requirements by age and sex into table lookup_energy_needs'''
        
        database = Database()
        database.open()
        deleteQuery = '''DELETE FROM lookup_energy_needs'''
        database.execUpdateQuery(deleteQuery)
        
        insertQuery = '''INSERT INTO lookup_energy_needs (age,kCalNeedM,kCalNeedF) VALUES
                            (0,820,820),
                            (1,820,820),
                            (2,1150,1150),
                            (3,1350,1350),
                            (4,1550,1550),
                            (5,1550,1550),
                            (6,1850,1750),
                            (7,1850,1750),
                            (8,1850,1750),
                            (9,1850,1750),
                            (10,2100,1800),
                            (11,2100,1800),
                            (12,2200,1950),
                            (13,2200,1950),
                            (14,2400,2100),
                            (15,2400,2100),
                            (16,2650,2150),
                            (17,2650,2150)'''
                            
        database.execUpdateQuery(insertQuery)
        
        insertQuery = "INSERT INTO lookup_energy_needs (age,kCalNeedM,kCalNeedF) VALUES (18,2600,2600)"
        
        for i in range(19,30):
            insertQuery = insertQuery + ",(%s,2600,2600) " % i 
        database.execUpdateQuery(insertQuery)

        insertQuery = "INSERT INTO lookup_energy_needs (age,kCalNeedM,kCalNeedF) VALUES (30,2500,2050)"
        
        for i in range(31,60):
            insertQuery = insertQuery + ",(%s,2500,2050) " % i 
        database.execUpdateQuery(insertQuery)

        insertQuery = "INSERT INTO lookup_energy_needs (age,kCalNeedM,kCalNeedF) VALUES (60,2100,1850)"
        
        for i in range(61,100):
            insertQuery = insertQuery + ",(%s,2100,1850) " % i 
        database.execUpdateQuery(insertQuery)

        database.close()
                            
                            
