#-------------------------------------------------------------------	
#	Filename: frmmainwindow.py
#
#	Inherits from Ui_MainWindow in gui.designs.ui_mainwindow module
#	to create a class FrmMainWindow which creates the main window
#	of the application.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the main window design class
from gui.designs.ui_mainwindow import Ui_MainWindow

# import the Create Project dialog class
from frmnewproject import FrmNewProject

class FrmMainWindow(Ui_MainWindow):
	''' Creates the Main Window of the application using the main 
	    window design in the gui.designs.ui_mainwindow module '''
	    
	def __init__(self, parent=None):
		''' Initialises Main Window. Adds the MdiArea (QMdiArea) '''
		self.mdi = QtGui.QMdiArea()
		
	def newProject(self):
		''' Creates and Shows the New Project form '''
		self.form = QtGui.QDialog()
		self.ui = FrmNewProject()
		self.ui.setupUi(self.form, self.mdi)
		self.mdi.addSubWindow(self.form)
		self.form.show()
		
	def setupUi(self, MainWindow):
		''' Sets up the main window adding signal and slot connections
			where necessary. '''
		Ui_MainWindow.setupUi(self, MainWindow) 		
		MainWindow.setCentralWidget(self.mdi)
		
		# connect relevant signals and slots
		QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
		QtCore.QObject.connect(self.actionNew_Project, QtCore.SIGNAL("triggered()"), self.newProject)