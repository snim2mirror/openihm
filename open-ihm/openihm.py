#-------------------------------------------------------------------	
#	Filename: openihm.py
#
#	The main module of Open IHM. PyQt4 is used to implement the GUI
#	of the system. Also used is the sys (system) package.
#-------------------------------------------------------------------

# imports from sys and PyQt4 packages
import sys
from PyQt4 import QtGui, QtCore

# import class that creates Open IHM Main Window
from gui.interface.frmmainwindow import FrmMainWindow

# import database initialisation classes
from gui.interface.frmdatabasemessage import FrmDatabaseMessage
from data.databaseinitialiser import *

dbInitialiser = DatabaseInitialiser()
dbstatus = dbInitialiser.initialiseDB()

# initiate application, main window and show main window
app = QtGui.QApplication(sys.argv)

if ( dbstatus['mysqlstarted'] == True and dbstatus['dbinstalled'] == True and dbstatus['dbuptodate']):
     window = FrmMainWindow()
     window.showMaximized()
elif ( dbstatus['mysqlstarted'] == False ):
     # inform user mysal not started
     msg = '''MySQL Server is currently not running. OpenIHM data is stored in a MySQL Database. \n\nPlease start MySQL before running Open-IHM.'''
     window = FrmDatabaseMessage(msg)
     window.show()
elif ( dbstatus['dbuptodate'] == False ):
     # inform user mysal not started
     msg = '''Failed to automatically update the database is not up to date.'''
     window = FrmDatabaseMessage(msg)
     window.show()
     window = FrmMainWindow()
     window.showMaximized()
elif ( dbstatus['dbinstalled'] == False ):
     # inform  the user that automatic installation of the database failed
     msg1 = '''Failed to install the database automatically. '''
     msg2 = '''The system requires the MySQL root password to be blank during database installation.'''
     msg3 =  '''Once the database is installed the root password can be reset to its original value.'''
     msg = "%s%s\n\n%s" % ( msg1,  msg2,  msg3)
     window = FrmDatabaseMessage(msg)
     window.show()

# enter the application event loop - accept and handle events until
# user exists the application.
sys.exit(app.exec_())
