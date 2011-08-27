#-------------------------------------------------------------------	
#	Filename: database.py
#
#  A convinience wrapper around mysql connector
#-------------------------------------------------------------------

import includes.mysql.connector as connector

class Database:
    def __init__(self,  host="localhost", database="openihmdb",  user="openihm",  password="ihm2010", port=3306):
         ''' 
            Initialise database connection with settings from Config class
         '''
         self.host = host
         self.db = database
         self.user = user
         self.pwd = password
         self.port = port
        
    def databaseServerRunning(self):
         '''
            Checks if the database server (mysql) is running
         '''
         pass
        
    def databaseExists(self):
         ''' 
            checks if database exists 
         '''
         pass
        
    def open(self):
         ''' Open a connection to the database'''
         self.db = connector.Connect(host=self.host, database=self.db, user=self.user, password=self.pwd, port=self.port)             
         self.cursor = self.db.cursor()
        
    def close(self):
         ''' close connection to the database'''
         self.cursor.close()
         self.db.close()       
        
    def execDefinitionQuery( self, query ):
         ''' 
            Execute a data definition query (e.g. CREATE TABLE) on the database
         '''
         self.cursor.execute(query)
        
    def execSelectQuery( self, query ):
         ''' 
            Execute a SELECT (data retrieval) query on the database and return the
            rows retrieved 
         '''
         self.cursor.execute(query)
         rows = self.cursor.fetchall()
         return rows
        
    def execUpdateQuery( self, query ):
         ''' 
            Execute an update query (INSERT INTO, UPDATE and DELETE FROM)on the database 
            and commit the change 
         '''
         self.cursor.execute(query)
         self.db.commit()
        
