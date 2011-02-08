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
                            
                            
