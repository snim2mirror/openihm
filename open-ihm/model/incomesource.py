#-------------------------------------------------------------------	
#	Filename: incomesource.py
#-------------------------------------------------------------------

from database import Database
import common

class IncomeSource: 
     def __init__(self, pid, incomesourcename, incometype=None):
         ''' Creates an incomesource object by retrieving an object corresponding to the incomesourcename from databasee
            or creating a new object with the given incomesourcename and saving it to database '''
         # if only incomesourcename is specifed retrieve hotspot details         
         if ( incometype == None ):
            if ( not self.getIncomeSourceDetails( pid, incomesourcename ) ):
                self.name = ""
                return None
         # else save incomesource details
         else:
            self.addIncomeSource( pid,incomesourcename, incometype )
            
     def getIncomeSourceDetails(self,  pid, incomesourcename):
         ''' Retrieves a incomesource object corresponding to the given incomesourcename from database '''
         # connect to database
         db = Database()
         db.open()
         # query to retrieve incomesource details
         incomesourcename = common.getDbString( incomesourcename )
         query = "SELECT pid, incomesource, incometype FROM projectincomesources WHERE pid=%s AND incomesource='%s' " % (pid, incomesourcename)
             
         # get rows returned by query
         rows = db.execSelectQuery( query )
         
         # get incomesource details from record and assign to object attrbutes
         num = len(rows)
         if (num != 0):
             exists = True
             for row in rows:
                self.pid = pid
                self.name = common.getViewString( row[1] )
                self.type = common.getViewString( row[2] )
         else:
            exists = False
        
         # close database connection
         db.close()
         return exists
        
     def addIncomeSource( self,  pid, incomesourcename,  incometype ):
         ''' Adds a new incomesource object '''
         # connect to database
         db = Database()           
         db.open()
         
         # create INSERT INTO query
         incomesourcename = common.getDbString( incomesourcename )
         incometype = common.getDbString( incometype )
         query = '''INSERT INTO projectincomesources(pid,incomesource,incometype) VALUES(%s,'%s','%s')''' % (pid,incomesourcename,incometype)
        
         # execute query
         db.execUpdateQuery(query)
         
         # close database connection
         db.close()
        
         # set incomesource attributes to saved values
         self.name = common.getViewString( incomesourcename )
         self.type = common.getViewString( incometype )
         self.pid = pid
         
     def editIncomeSource( self,  incomesourcename,  incometype ):
         ''' edits the incomesourcename and category of the current incomesource object '''
         # connect to database
         db = Database()           
         db.open()
         
         # create INSERT INTO query
         incomesourcename = common.getDbString( incomesourcename )
         oldname = common.getDbString( self.name )
         incometype = common.getDbString( incometype )
         query = '''UPDATE projectincomesources SET incomesource='%s', incometype='%s',
         WHERE pid=%s AND incomesourcename='%s' ''' % (incomesourcename, incometype, self.pid, oldname)
        
         # execute query
         db.execUpdateQuery(query)
         
         # close database connection
         db.close()
        
         # set incomesource attributes to saved values
         self.name = common.getViewString( incomesourcename )
         self.type = common.getViewString( incometype )

