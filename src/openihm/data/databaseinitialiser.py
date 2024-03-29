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


from includes.mysql.connector import Connect
from includes.mysql.connector import errors
from datetime import date

class DbConfig(object):
    """ Configures the mysql database connector which is then called as below:
    
       mysql.connector.Connect(**Config.dbinfo())
    """
    def __init__(self,  host='localhost', database='', user='', password='',
                 port=3306, superuser='root', superuser_password='',
                 charset='utf8', unicode=True,  warnings=True):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.superuser_password = superuser_password
        self.superuser = superuser
        self.charset = charset
        self.unicode = unicode
        self.warnings = warnings

    def superuser_dbinfo(self):
        return {
          'host': self.host,
          'database': self.database,
          'user': self.superuser,
          'password': self.superuser_password,
          'charset': self.charset,
          'use_unicode': self.unicode,
          'get_warnings': self.warnings,
          }

    def dbinfo(self):
        return {
          'host': self.host,
          'database': self.database,
          'user': self.user,
          'password': self.password,
          'charset': self.charset,
          'use_unicode': self.unicode,
          'get_warnings': self.warnings,
          }

class DatabaseInitialiser:
    def __init__(self, config):
        self.config = config

        #date of latest DB update: must be reset to latest date when DB changes are being pushed - format yyyy-mm-dd
        self.latestupdatestring = "latest update on 2012-12-09" 

    def initialiseDB(self):
        config = self.config
        dbinfo = config.dbinfo().copy()
        # assume that mysql server is running and database is installed already
        mysqlstarted = True
        dbinstalled = False
        # try connecting to database
        try:
            db = Connect( **dbinfo )
            db.close()
            dbinstalled = True
        # interfaceError occurs if MySQL server is not running
        except errors.InterfaceError:
            mysqlstarted = False
        # OperationalError or ProgrammingError happen if the db does not exist
        except ( errors.OperationalError,  errors.ProgrammingError) as e:
            dbinstalled = self.createDatabase()
            self.setupStartupCrops() # initialise setup_foods_crops table
           
        dbuptodate = False
        if ( mysqlstarted==True and dbinstalled==True ):
            dbuptodate = self.updateDatabase()
            #self.insertStartupCrops()

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
            dbinfo = self.config.superuser_dbinfo().copy()
            database = dbinfo['database']
            del dbinfo['database']
            db = Connect(**dbinfo)
            cursor = db.cursor()
            # FIXME: long term we should look at changing the character set.
            cursor.execute("CREATE SCHEMA IF NOT EXISTS `%s` DEFAULT CHARACTER SET latin1 ;" % database)
            cursor.execute("USE `%s`;" % database)

            for command in commandlist:
                if ( not command.isspace() ):
                    cursor.execute(command)
            try:
                if self.config.user != self.config.superuser:
                    cursor.execute("GRANT ALL ON %s.* TO %s@localhost IDENTIFIED BY '%s';" % 
                                    (database, self.config.user, self.config.password)) 
            except ( errors.OperationalError,  errors.ProgrammingError) as e:
                print e.msg
                
            updatestr = "latest update on %s" % (date.today().isoformat())      
            query = "INSERT INTO dbupdate VALUES('%s')" % updatestr
            cursor.execute(query)
            db.commit()
            
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

        config = self.config
        dbinfo = config.dbinfo().copy()
        db = Connect(**dbinfo)
        cursor = db.cursor()

        query = "SHOW TABLES"

        cursor.execute(query)
        rows = cursor.fetchall()

        upToDate = False
        for row in rows:
            if row[0] == "dbupdate":
                query = "SELECT lastupdate FROM dbupdate"
                cursor.execute(query)
                rows = cursor.fetchall()

                if len(rows) != 0:
                    for row in rows:
                        if row[0] > self.latestupdatestring:
                            upToDate = True
                else:
                    updatestr = "latest update on %s" % (date.today().isoformat())
                    query = "INSERT INTO dbupdate VALUES('%s')" % updatestr
                    cursor.execute(query)
                    db.commit()
                    upToDate = True

        cursor.close()
        db.close()

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
                dbinfo = self.config.superuser_dbinfo().copy()
                db = Connect(**dbinfo)
                cursor = db.cursor()

                for command in commandlist:
                    if ( not command.isspace() ):
                        cursor.execute(command)

                updatestr = "latest update on %s" % (date.today().isoformat())

                query = "UPDATE dbupdate SET lastupdate='%s'" % updatestr
                cursor.execute(query)
                db.commit()

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

        config = self.config
        dbinfo = config.dbinfo().copy()
        db = Connect(**dbinfo)
        cursor = db.cursor()

        query = "SHOW COLUMNS FROM standardofliving"
        ## will change to:
        #query = "SELECT * FROM setup_foods_crops"
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
                dbinfo = self.config.superuser_dbinfo().copy()
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

    def setupStartupCrops(self):
        """ Initialise table setup_foods_crops at database creation time"""
        sqlfile = file('data/scripts/openihmdb_mysql_fix59.sql', 'r')
        commands = sqlfile.read()
        commandlist = commands.split(';')
        sqlfile.close()
        try:
            dbinfo = self.config.superuser_dbinfo().copy()
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
