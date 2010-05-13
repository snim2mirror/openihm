from data.config import Config
import data.mysql.connector 

class GenericDBOP:
	def __init__(self,query):
		# connect to mysql database
		self.config = Config.dbinfo().copy()        	
		self.db = data.mysql.connector.Connect(**self.config)
        	self.cursor = self.db.cursor()		
		self.sqlquery = query
	
	def getdata(self):
		self.cursor.execute(self.sqlquery) 
		return self.cursor.fetchall()

        def runSelectQuery(self):	
        	#connect to mysql database
        	db = data.mysql.connector.Connect(**self.config)
        	cursor = db.cursor()
		
		cursor.execute(self.sqlquery)
		recset = cursor.fetchall()

		# close database connection
        	cursor.close()
        	db.close()

		return recset
	
	def runUpdateQuery(self):	
        	#connect to mysql database
        	db = data.mysql.connector.Connect(**self.config)
        	cursor = db.cursor()
        	
		# execute query and commit changes
		cursor.execute(self.sqlquery)
        	db.commit()
		
		# close database connection
        	cursor.close()
        	db.close()
