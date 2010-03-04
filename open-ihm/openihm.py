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

# initiate application, main window and show main window
app = QtGui.QApplication(sys.argv)
window = FrmMainWindow()
window.showMaximized()

# enter the application event loop - accept and handle events until
# user exists the application.
sys.exit(app.exec_())
