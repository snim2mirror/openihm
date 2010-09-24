#-------------------------------------------------------------------	
#	Filename: foodenergyrequirement.py
#-------------------------------------------------------------------

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

 
