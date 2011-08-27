from includes.mysql.connector import Connect
from includes.mysql.connector import errors

class DbConfig(object):
     """ Configures the mysql database connector which is then called as below:
    
        mysql.connector.Connect(**Config.dbinfo())
     """
     def __init__(self,  host='localhost', database='', user='', password='', port=3306, charset='utf8', unicode = True,  warnings=True):
         self.host = host
         self.database = database
         self.user = user
         self.password = password
         self.port = port
    
         self.charset = charset
         self.unicode = unicode
         self.warnings = warnings
    
     def dbinfo(self):
         return {
            'host'          : self.host,
            'database'      : self.database,
            'user'          : self.user,
            'password'      : self.password,
            'charset'       : self.charset,
            'use_unicode'   : self.unicode,
            'get_warnings'  : self.warnings,
            }

class DatabaseInitialiser:
     def __init__(self, host='localhost', rootpwd=''):
         self.host = host
         self.rootpwd = rootpwd
         
     def initialiseDB(self):
         config = DbConfig(self.host, 'openihmdb', 'openihm', 'ihm2010')
         dbinfo = config.dbinfo().copy()
         # assume that mysql server is running and database is installed already
         mysqlstarted = True
         dbinstalled = True
         # try connecting to database
         try:
             db = Connect( **dbinfo )
             db.close()
         # interfaceError occurs if MySQL server is not running
         except errors.InterfaceError:
             mysqlstarted = False
         # OperationalError or ProgrammingError happen if the db does not exist
         except ( errors.OperationalError,  errors.ProgrammingError) as e:
             dbinstalled = self.createDatabase()
             
         if ( dbinstalled ):
                 dbuptodate = self.updateDatabase()
                 self.insertStartupCrops()

         dbstatus = dict()
         dbstatus['mysqlstarted'] = mysqlstarted
         dbstatus['dbinstalled'] = dbinstalled
         dbstatus['dbuptodate'] = dbuptodate
     
         return dbstatus
     
     def createDatabase(self):
         sqlfile = file('data/scripts/openihmdb_mysql.sql', 'r')
         commands = sqlfile.read()
         commandlist = commands.split(';')
         sqlfile.close()
         try:
             config = DbConfig(self.host, '', 'root', self.rootpwd)
             dbinfo = config.dbinfo().copy()
             db = Connect(**dbinfo)             
             cursor = db.cursor()

             for command in commandlist:
                 if ( not command.isspace() ):
                     cursor.execute(command)
             
             cursor.close()
             db.close()
         
             return True
         
         except errors.InterfaceError,  e:
             return False
         
         except ( errors.OperationalError,  errors.ProgrammingError) as e:
             return False
             
     def databaseUpToDate(self):
         # check if the database is already up to date: i.e. there is "summary" in standardofliving
         #   checks in assets
         
         config = DbConfig(self.host, 'openihmdb', 'openihm', 'ihm2010')
         dbinfo = config.dbinfo().copy()
         db = Connect(**dbinfo)             
         cursor = db.cursor()
         
         query = "SHOW TABLES"
         
         cursor.execute(query)
         rows = cursor.fetchall()
         
         cursor.close()
         db.close()
         
         upToDate = False
         for row in rows:
             if row[0] == "transferlog":
                     upToDate = True
         
         return upToDate
        
     def updateDatabase(self):
         # if database is already up to date return
         if self.databaseUpToDate():
             return True
         # else update the database    
         else:
             sqlfile = file('data/scripts/openihmdb_mysql_update.sql', 'r')
             commands = sqlfile.read()
             commandlist = commands.split(';')
             sqlfile.close()
             try:
                 config = DbConfig(self.host, '', 'root', self.rootpwd)
                 dbinfo = config.dbinfo().copy()
                 db = Connect(**dbinfo)             
                 cursor = db.cursor()

                 for command in commandlist:
                     if ( not command.isspace() ):
                         cursor.execute(command)
             
                 cursor.close()
                 db.close()
         
                 return True
         
             except errors.InterfaceError,  e:
                 print e
                 return False
         
             except ( errors.OperationalError,  errors.ProgrammingError) as e:
                 print e
                 return False
                 
     def cropsExist(self):
         # check if the database is already up to date: i.e. there is "summary" in standardofliving
         #   checks in assets
         
         config = DbConfig(self.host, 'openihmdb', 'openihm', 'ihm2010')
         dbinfo = config.dbinfo().copy()
         db = Connect(**dbinfo)             
         cursor = db.cursor()
         
         query = "SHOW COLUMNS FROM standardofliving"
         ## will change to:
         ## query = "SELECT * FROM setup_foods_crops"
         ## if it returns some rows then returns otherwise returns false
         
         cursor.execute(query)
         rows = cursor.fetchall()
         
         cursor.close()
         db.close()
         
         upToDate = False
         for row in rows:
             for field in row:
                 if field == "null":
                     upToDate = True
         
         return upToDate
                 
     def insertStartupCrops(self):
         # if database is already up to date return
         if self.cropsExist():
             return True
         # else update the database    
         else:
             sqlfile = file('data/scripts/openihmdb_mysql_fix59.sql', 'r')
             commands = sqlfile.read()
             commandlist = commands.split(';')
             sqlfile.close()
             try:
                 config = DbConfig(self.host, '', 'root', self.rootpwd)
                 dbinfo = config.dbinfo().copy()
                 db = Connect(**dbinfo)             
                 cursor = db.cursor()

                 for command in commandlist:
                     if ( not command.isspace() ):
                         cursor.execute(command)
             
                 cursor.close()
                 db.close()
         
                 return True
         
             except errors.InterfaceError,  e:
                 print e
                 return False
         
             except ( errors.OperationalError,  errors.ProgrammingError) as e:
                 print e
                 return False
