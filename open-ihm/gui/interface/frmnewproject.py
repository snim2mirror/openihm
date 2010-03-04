#-------------------------------------------------------------------	
#	Filename: frmnewproject.py
#
#	Class to create the Create Project form - FrmNewProject.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4 import QtGui, QtCore

# import the Create Project Dialog design class
from gui.designs.ui_newproject import Ui_NewProject

class FrmNewProject(QtGui.QDialog, Ui_NewProject):	
	''' Creates the Create (New) Project from. Uses the design class
		in gui.designs.ui_newproject. '''	
	def __init__(self, Mdi):
		''' Set up the dialog box interface '''
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		# connect relevant signals and slots
		self.connect(self.BtnProjectCancel, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
