#-------------------------------------------------------------------	
#	Filename: openihm.pyw
#
#	The main module of Open IHM. PyQt4 is used to implement the GUI
#	of the system. Also used is the sys (system) package.
#-------------------------------------------------------------------

# imports from sys and PyQt4 packages
import sys
from PyQt4 import QtGui, QtCore

import logging
import logging.handlers
import traceback

LOGFILE = 'openihmlog.txt'

if __name__ == '__main__':
     
     log = logging.getLogger(__name__)
     log.setLevel(logging.DEBUG)
     handler = logging.handlers.RotatingFileHandler(LOGFILE, backupCount=5)
     log.addHandler(handler)

     #
     # Check for updates to open-ihm.
     #
     try:
          log.info('Checking for updates.')
          
     except:
          log.debug('Exception raised in __main__.')
          ty, value, tback = sys.exc_info()
          log.debug('Exception raised on updating software. Debug info follows:')
          log.debug(''.join(traceback.format_exception(ty, value, tback)))

     

     #
     # Start open-ihm.
     #
     try:

          # import class that creates Open IHM Main Window
          from gui.interface.frmmainwindow import FrmMainWindow

          # import database initialisation classes
          from gui.interface.frmdatabasemessage import FrmDatabaseMessage
          from data.databaseinitialiser import *
          
          log.info('Initialising database.')
          
          dbInitialiser = DatabaseInitialiser()
          dbstatus = dbInitialiser.initialiseDB()

          # initiate application, main window and show main window
          log.info('Creating GUI.')
          app = QtGui.QApplication(sys.argv)

          if ( dbstatus['mysqlstarted'] == True and dbstatus['dbinstalled'] == True and dbstatus['dbuptodate'] ):
               log.info('Started MySQL, DB up to date and DB installed.')
               window = FrmMainWindow()
               window.showMaximized()

          elif ( dbstatus['mysqlstarted'] == False ):
               log.info('Not started MySQL.')
               # inform user mysal not started
               msg = '''MySQL Server is currently not running. OpenIHM data is stored in a MySQL Database. \n\nPlease start MySQL before running Open-IHM.'''
               window = FrmDatabaseMessage(msg)
               window.show()
               
          elif ( dbstatus['dbuptodate'] == False ):
               log.info('DB not up to date.')
               # inform user mysal not started
               msg = '''Failed to automatically update the database.'''
               window = FrmDatabaseMessage(msg)
               window.show()
               window = FrmMainWindow()
               window.showMaximized()
               
          elif ( dbstatus['dbinstalled'] == False ):
               log.info('DB not installed.')
               # inform  the user that automatic installation of the database failed
               msg1 = '''Failed to install the database automatically. '''
               msg2 = '''The system requires the MySQL root password to be blank during database installation.'''
               msg3 =  '''Once the database is installed the root password can be reset to its original value.'''
               msg = "%s%s\n\n%s" % ( msg1,  msg2,  msg3)
               window = FrmDatabaseMessage(msg)
               window.show()
          
          # enter the application event loop - accept and handle events until
          # user exists the application.
          log.info('Starting main loop of GUI.')
          sys.exit(app.exec_())

     except Exception, e:
          log.debug('Exception raised in __main__.')
          ty, value, tback = sys.exc_info()
          log.debug('Exception raised in start script. Debug info follows:')
          log.debug(''.join(traceback.format_exception(ty, value, tback)))

